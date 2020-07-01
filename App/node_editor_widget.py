from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication

from gui.node_editor import Ui_NodeEditorWidget
from wizard.tools import log
from wizard.vars import defaults
import node_widget
import pickle
from wizard.prefs.main import prefs
from wizard.asset.reference import references

logger = log.pipe_log()

prefs = prefs()

class Main(QtWidgets.QWidget):

    def __init__(self, main_window):
        super(Main, self).__init__()
        # Build the ui from ui converted file
        self.ui = Ui_NodeEditorWidget()
        self.ui.setupUi(self)
        self.init_scene()
        self.ui.arrow_label.setPixmap(QtGui.QPixmap(defaults._edge_image_).scaled(45, 45, QtCore.Qt.KeepAspectRatio,
                                                                                  QtCore.Qt.SmoothTransformation))
        self.setAcceptDrops(True)
        self.asset = None
        self.main_window = main_window
        self.connect_functions()
        self.working_scene_widget = None
        self.scene_references = []
        self.scene_references_widget = []
        self.working_asset = None
        self.selection_list = []
        self.refresh_scene() 

    def init_scene(self):
        self.references = 0
        self.row = 0

    def add_reference(self, asset=None, selectable=True):
        if asset:
            visible = asset[3]
            proxy = asset[2]
            count = asset[1]
            asset = asset[0]
            widget = node_widget.Main(self, asset, count, selectable, proxy, visible)
            if self.references > 5:
                self.references = 0
                self.row += 1
            if asset.export_version:
                self.ui.gridLayout.addWidget(widget, self.row, self.references, 1, 1)
                self.references += 1
                self.scene_references_widget.append(widget)
                self.scene_references.append(asset)
            else:
                logger.warning("This asset is not published !")
        self.refresh_references_label()

    def create_reference(self, asset, proxy = 0, visible = 1):
        if not asset.export_version:
            asset.set_export_version()
        self.set_new_reference(asset, proxy, visible)

    def set_new_reference(self, asset, proxy, visible):
        count = references(self.asset).add_reference(asset, proxy, visible)
        self.add_reference([asset, count, proxy, visible], 1 )

    def replace_reference(self, widget, old_namespace=None, proxy = 0, visible = 1):
        self.scene_references_widget[self.scene_references_widget.index(widget)] = widget
        references(self.asset).replace_reference(widget, old_namespace, proxy, visible)
        logger.info("Reference modified")

    def add_main_asset(self, asset=None):
        self.working_scene_widget = node_widget.Main(self, asset, 0, 0)
        self.asset = asset
        self.ui.horizontalLayout.addWidget(self.working_scene_widget)

    def refresh_scene(self, asset=None):
        self.init_scene()
        self.refresh_working_scene(asset)
        self.refresh_references(asset)

    def refresh_working_scene(self, asset=None):
        for i in reversed(range(self.ui.horizontalLayout.count())):
            self.ui.horizontalLayout.itemAt(i).widget().setParent(None)
        if asset:
            if asset.stage and asset.variant:
                self.add_main_asset(asset)
                self.working_asset = asset
            else:
                self.add_main_asset()
                self.working_asset = None
        else:
            self.add_main_asset()
            self.working_asset = None

    def refresh_references(self, asset=None):
        for i in reversed(range(self.ui.gridLayout.count())):
            self.ui.gridLayout.itemAt(i).widget().hide()
            self.ui.gridLayout.itemAt(i).widget().setParent(None)
        if asset:
            if asset.stage and asset.variant:
                self.get_references(asset)
            else:
                self.scene_references = []
                self.add_reference()
        else:
            self.scene_references = []
            self.add_reference()
        self.refresh_references_label()
        self.selection_list = []

    def refresh_references_label(self):
        references_number = len(self.scene_references)
        if references_number > 1:
            text = f'{references_number} references'
        else:
            text = f'{references_number} reference'
        self.ui.references_number_label.setText(text)

    def get_references(self, asset):
        self.scene_references = []
        assets_list = references(asset).references
        for asset in assets_list:
            self.scene_references.append(asset)
            self.add_reference(asset)

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
        mimeData = e.mimeData().text().encode('utf-8')
        asset = pickle.loads(mimeData)
        #if asset.stage in defaults._reference_autorization_dic_[self.asset.stage]:
        if self.asset.software == defaults._painter_:
            if prefs.asset(self.asset).variant.references == {}:
                self.create_reference(asset)
            else:
                logger.warning(f"{defaults._painter_} accepts only 1 reference...")
        else:
            if self.asset.category == defaults._set_dress_ and prefs.asset(asset).export.is_proxy:
                proxy = 1
            else:
                proxy = 0
            self.create_reference(asset, proxy = proxy)
        #else:
        #logger.info(f"Can't reference a {asset.stage} in a {self.asset.stage}")

    def delete_asset(self, widget=None):
        if not widget:
            widgets_list = self.scene_references_widget.copy()
            for widget in widgets_list:
                if widget.selected:
                    if widget.asset in self.scene_references:
                        self.scene_references.remove(widget.asset)
                    self.delete_widget(widget)
        else:
            self.scene_references.remove(widget.asset)
            self.delete_widget(widget)

    def delete_widget(self, widget):
        widget.setParent(None)
        self.scene_references_widget.remove(widget)
        if widget in self.selection_list:
            self.remove_selection(widget)
        references(self.asset).remove_reference(widget)
        self.refresh_references_label()

    def add_selection(self, widget):
        self.selection_list.append(widget)

    def remove_selection(self, widget):
        if widget in self.selection_list:
            self.selection_list.remove(widget)

    def update_all(self):
        for widget in self.scene_references_widget:
            widget.set_last_version()

    def connect_functions(self):
        self.ui.trash_pushButton.clicked.connect(self.delete_asset)
        self.ui.update_all_pushButton.clicked.connect(self.update_all)

    def deselect_all(self):
        selection_list = self.selection_list.copy()
        for widget in selection_list:
            widget.deselect()
            self.remove_selection(widget)

    def mousePressEvent(self, event):
        self.deselect_all()
