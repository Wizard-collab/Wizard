from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QTreeWidgetItem
from gui.exports_widget import Ui_Form
from gui import build
from wizard.vars import defaults
from wizard.tools import log
from wizard.tools import batch_export
from wizard.prefs.main import prefs
import export_widget
import export_asset_widget
import copy
import dialog_manual_export
import ui_export_manager

logger = log.pipe_log(__name__)

prefs = prefs()

class Main(QtWidgets.QWidget, QtCore.QThread):

    def __init__(self):
        super(Main, self).__init__()
        # Build the ui from ui converted file
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.asset = None
        self.full = 0
        self.sanity = 1
        self.export_versions_list_full = []
        self.exported_asset_list = []
        self.widgets = []
        self.number = 3
        self.step = 3
        self.count = 1
        self.connect_functions()
        self.ui.sanity_exports_pushButton.setIcon(QtGui.QIcon(defaults._export_list_icon_gray_))
        self.ui.show_all_exports_pushButton.setIcon(QtGui.QIcon(defaults._sd_icon_))
        self.ui.manual_publish_pushButton.setIcon(QtGui.QIcon(defaults._manual_publish_icon_))
        self.ui.batch_publish_pushButton.setIcon(QtGui.QIcon(defaults._batch_publish_icon_))

    def refresh_list(self, asset_tuple = None):
        if asset_tuple:
            self.export_versions_list_full = prefs.asset(asset_tuple[0]).export.versions
        else:
            self.export_versions_list_full = []
        self.export_versions_list = []
        if self.export_versions_list_full and self.export_versions_list_full != []:
            if not self.full:
                self.export_versions_list = self.export_versions_list_full[-self.number:]
            else:
                self.export_versions_list = self.export_versions_list_full

        for version in self.export_versions_list:
            asset_tuple[0] = copy.deepcopy(asset_tuple[0])
            asset_tuple[0].export_version = version         
            widget = export_widget.Main(asset_tuple[0], self.sanity, self.count)
            self.widgets.append(widget)
            new_item = QTreeWidgetItem()
            asset_tuple[1].addChild(new_item)
            new_item.setSizeHint(0, QtCore.QSize(100, 28))
            self.ui.exports_treeWidget.setItemWidget(new_item, 0, widget)

    def update_exported_assets(self, asset=None):
 
        root_parent = self.ui.exports_treeWidget.invisibleRootItem()

        if self.asset.variant:
            exports_list = prefs.asset(self.asset).export_root.exported_assets_list
            for export in exports_list:
                asset = copy.deepcopy(self.asset)
                asset.export_asset = export
                new_item = QTreeWidgetItem([asset.export_asset])
                new_item.setSizeHint(0, QtCore.QSize(100, 28))
                root_parent.addChild(new_item)
                new_item.setExpanded(True)
                asset_tuple = [asset, new_item]
                self.refresh_list(asset_tuple)

                QApplication.processEvents()

    def clear_all(self):
        self.ui.exports_treeWidget.clear()

        QApplication.processEvents()

    def refresh_all(self, asset=None):
        self.get_params()
        self.clear_all()
        if asset:
            self.asset = asset
        self.update_exported_assets(asset)

    def update_sanity(self):
        self.refresh_all()

    def show_more(self, less):
        self.get_params()

        if not less:
            self.number += self.step
            self.refresh_all()
        else:
            self.number -= self.step
            self.refresh_all()

        if len(self.widgets) == len(self.export_versions_list_full):
            self.ui.show_all_exports_pushButton.setChecked(1)
            self.full = 1
            self.number = self.step
        else:
            self.ui.show_all_exports_pushButton.setChecked(0)
            self.full = 0

    def get_params(self):
        if self.ui.show_all_exports_pushButton.isChecked():
            self.full = 1
        else:
            self.full = 0
        if self.ui.sanity_exports_pushButton.isChecked():
            self.sanity = 1
        else:
            self.sanity = 0

    def manual_export(self):
        self.dialog_manual_export = dialog_manual_export.Main(self.asset)
        if build.launch_dialog_as_child(self.dialog_manual_export):
            self.refresh_all()

    def batch_export(self):
        if self.asset.domain == defaults._sequences_:
            self.export_shot()
        elif self.asset.domain == defaults._assets_:
            self.export_asset()

    def export_asset(self):
        print("exporting_asset")
        batch_export.batch_export(self.asset)

    def export_shot(self):
        self.ui_export_manager = ui_export_manager.Main(self.asset)
        build.launch_normal_as_child(self.ui_export_manager)

    def connect_functions(self):
        # area_scroll_bar.rangeChanged.connect(lambda: area_scroll_bar.setValue(area_scroll_bar.maximum()))
        self.ui.show_all_exports_pushButton.clicked.connect(lambda: self.refresh_all())
        self.ui.sanity_exports_pushButton.clicked.connect(lambda: self.update_sanity())
        self.ui.show_more_pushButton.clicked.connect(self.show_more)
        self.ui.show_less_pushButton.clicked.connect(lambda: self.show_more(1))
        self.ui.manual_publish_pushButton.clicked.connect(self.manual_export)
        self.ui.batch_publish_pushButton.clicked.connect(self.batch_export)

    def closeEvent(self, event):
        event.ignore()
        self.hide()
