from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication

from gui.reference_list_widget import Ui_Form
from wizard.tools import log
from wizard.vars import defaults
import ref_list_asset_widget
from wizard.prefs.main import prefs
from wizard.asset.reference import references
import reference_list_item_widget
from wizard.asset import main as asset_core
import pickle
import editable_list_widget
import options_widget
from wizard.clipboard import clipboard
from gui import build

logger = log.pipe_log(__name__)

prefs = prefs()

class Main(QtWidgets.QWidget):

    def __init__(self, main_window):
        super(Main, self).__init__()
        # Build the ui from ui converted file
        self.setAcceptDrops(True)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.connect_functions()
        self.init_scene()

    def init_scene(self):
        self.scene_references = []
        self.asset=None
        self.ui.reference_list_listWidget.clear()

    def refresh_scene(self, asset=None):
        self.init_scene()
        self.asset = asset
        self.refresh_references()

    def refresh_references(self):
        if self.asset:
            if self.asset.stage and self.asset.variant:
                self.get_references()
            else:
                self.scene_references = []
        else:
            self.scene_references = []

    def get_references(self):
        self.scene_references = []
        ref_assets_list = references(self.asset).references
        for ref_asset in ref_assets_list:
            self.scene_references.append(ref_asset[0])
            self.add_reference(ref_asset)

    def add_reference(self, ref_asset):
        if ref_asset:
            visible = ref_asset[3]
            proxy = ref_asset[2]
            count = ref_asset[1]
            asset = ref_asset[0]
            #widget = editable_list_widget.list_widget(asset = asset, icon = defaults._stage_icon_[asset.stage])
            #widget.add_label(asset.stage)
            #widget.add_label(asset.name)
            #self.add_item_to_list(widget)
            widget = reference_list_item_widget.Main(self, asset, count, proxy, visible)
            self.add_item_to_list(widget)
            self.refresh_references_label()


    def add_item_to_list(self, widget):
        item = QtWidgets.QListWidgetItem() 
        item.setSizeHint(QtCore.QSize(0, 28))
        widget.parent_item = item
        self.ui.reference_list_listWidget.addItem(item)
        self.ui.reference_list_listWidget.setItemWidget(item, widget)

    def create_reference(self, asset, proxy = 0, visible = 1):
        if not asset.export_version:
            asset.set_export_version()
        self.set_new_reference(asset, proxy, visible)
        self.scene_references.append(asset)


    def set_new_reference(self, asset, proxy, visible):
        count = references(self.asset).add_reference(asset, proxy, visible)
        self.add_reference([asset, count, proxy, visible])

    def replace_reference(self, asset, count, old_namespace=None, proxy = 0, visible = 1):
        references(self.asset).replace_reference(asset, count, old_namespace, proxy, visible)
        logger.info("Reference modified")

    def delete_asset(self, asset=None, count=None, item=None):
        if asset in self.scene_references:
            self.scene_references.remove(asset)

        print(asset)

        references(self.asset).remove_reference(asset, count)

        row = self.ui.reference_list_listWidget.row(item)
        self.ui.reference_list_listWidget.takeItem(row)
        self.refresh_references_label()
        
    def refresh_references_label(self):
        references_number = len(self.scene_references)
        if references_number > 1:
            text = f'{references_number} references'
        else:
            text = f'{references_number} reference'
        self.ui.references_number_label.setText(text)

    def delete_selection(self):
        items_selection = self.ui.reference_list_listWidget.selectedItems()
        for item in items_selection:
            widget = self.ui.reference_list_listWidget.itemWidget(item)
            widget.remove()

    def update_all(self):
        items_selection = self.ui.reference_list_listWidget.selectedItems()
        for item in items_selection:
            widget = self.ui.reference_list_listWidget.itemWidget(item)
            widget.set_last_version()

    def copy_references(self):
        clipboard.copy_references(self.scene_references)

    def paste_references(self):
        refrences_list = clipboard.get_references()
        self.import_asset_list(refrences_list)

    def connect_functions(self):
        self.ui.trash_pushButton.clicked.connect(self.delete_selection)
        self.ui.update_all_pushButton.clicked.connect(self.update_all)
        self.ui.reference_list_listWidget.customContextMenuRequested.connect(self.show_options_menu)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.RightButton:
            self.show_options_menu()

    def show_options_menu(self):
        self.options_widget = options_widget.Main(self)
        self.options_widget.add_item("Copy references", self.copy_references)
        self.options_widget.add_item("Paste references", self.paste_references)
        build.launch_options(self.options_widget)

    def dragEnterEvent(self, e):
        self.setStyleSheet('#node_editor_frame{border: 2px solid white;}')
        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.accept()

    def dragLeaveEvent(self, e):
        self.setStyleSheet('#node_editor_frame{border: 0px solid white;}')

    def dropEvent(self, e):
        self.setStyleSheet('#node_editor_frame{border: 0px solid white;}')
        mimeData = e.mimeData().text()
        string_assets_list = pickle.loads(mimeData.encode())
        self.import_asset_list(string_assets_list)

    def import_asset_list(self, string_assets_list):
        for string_asset in string_assets_list:
            asset = asset_core.string_to_asset(string_asset)
            if self.asset.software == defaults._painter_:
                if prefs.asset(self.asset).software.references == {}:
                    self.create_reference(asset)
                else:
                    logger.warning(f"{defaults._painter_} accepts only 1 reference...")
            else:
                if self.asset.category == defaults._set_dress_ and prefs.asset(asset).export.is_proxy:
                    proxy = 1
                else:
                    proxy = 0
                self.create_reference(asset, proxy = proxy)
