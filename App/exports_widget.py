from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication
from gui.exports_widget import Ui_Form
from gui import build
from wizard.vars import defaults
from wizard.tools import log
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

            asset_tuple[1].ui.export_asset_widget_number_label.setText(
                f'( {len(self.export_versions_list)}/{len(self.export_versions_list_full)} )')

        for version in self.export_versions_list:
            exported_version = copy.deepcopy(asset_tuple[0])
            exported_version.export_version = version
            widget = export_widget.Main(exported_version, self.sanity, self.count)
            self.widgets.append(widget)
            asset_tuple[1].widgets_list.append(widget)
            self.ui.export_list_verticalLayout_2.addWidget(widget)
            self.count = 1 - self.count

    def update_exported_assets(self, asset=None):
        if self.asset.variant:
            exports_list = prefs.asset(self.asset).export_root.exported_assets_list
            for export in exports_list:
                exported_asset = copy.deepcopy(self.asset)
                exported_asset.export_asset = export

                asset_widget = export_asset_widget.Main(exported_asset)
                asset_tuple = [exported_asset, asset_widget]
                self.ui.export_list_verticalLayout_2.addWidget(asset_widget)
                self.refresh_list(asset_tuple)
        else:
            self.refresh_list()

    def clear_all(self):
        QApplication.processEvents()

        for i in reversed(range(self.ui.export_list_verticalLayout_2.count())):
            widget = self.ui.export_list_verticalLayout_2.itemAt(i).widget()
            if widget:
                widget.setParent(None)

        self.exported_asset_list = []
        self.widgets = []

    def refresh_all(self, asset=None):
        self.get_params()
        self.clear_all()
        if asset:
            self.asset = asset
        self.update_exported_assets(asset)

    def update_sanity(self):
        self.get_params()
        for widget in self.widgets:
            widget.update_sanity(self.sanity)

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
