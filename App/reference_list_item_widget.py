from PyQt5 import QtWidgets, QtCore, QtGui

import os
import copy
from gui.reference_list_item_widget import Ui_Form
from gui import build
from wizard.vars import defaults
import options_widget
from wizard.prefs.main import prefs
import dialog_imported_asset_manager
from wizard.tools import log
from wizard.asset import reference
import open_ticket_widget

logger = log.pipe_log()

prefs = prefs()

class Main(QtWidgets.QWidget):

    def __init__(self, reference_list_widget, asset=None, count='0001', selectable=True, proxy = 0, visible = 1, item = None):
        super(Main, self).__init__()
        # Build the ui from ui converted file
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.asset = asset
        self.count = count
        self.proxy = proxy
        self.visible = 1
        self.parent_item = item
        self.reference_list_widget = reference_list_widget
        self.connect_functions()
        self.init_widget()

    def init_widget(self):

        icon = defaults._nodes_icons_dic_[self.asset.stage]

        self.ui.refresh_reference_widget_item.setIcon(QtGui.QIcon(defaults._refresh_icon_))
        self.ui.remove_reference_widget_item.setIcon(QtGui.QIcon(defaults._trash_large_icon_))
        self.ui.parameters_reference_list_item_pushButton.setIcon(QtGui.QIcon(defaults._settings_icon_))
        self.ui.folder_reference_list_item_pushButton.setIcon(QtGui.QIcon(defaults._folder_icon_))
        self.ui.ticket_reference_list_item_pushButton.setIcon(QtGui.QIcon(defaults._tickets_icon_))

        self.ui.asset_stage_image_label.setPixmap(QtGui.QPixmap(icon).scaled(22, 22, QtCore.Qt.KeepAspectRatio,
                                                                                  QtCore.Qt.SmoothTransformation))

        self.ui.reference_list_item_asset_name_label.setText(self.asset.name)
        self.ui.reference_list_item_asset_variant_label.setText("{}.{}".format(self.asset.variant, self.asset.export_version))
        self.ui.reference_list_item_asset_namespace_label.setText(self.asset.export_asset)

        if self.asset.export_version != prefs.asset(self.asset).export.last_version:
            self.ui.reference_list_item_asset_variant_label.setStyleSheet("#reference_list_item_asset_variant_label{color:rgb(255,153,51);}")
        else:
            self.ui.reference_list_item_asset_variant_label.setStyleSheet("#reference_list_item_asset_variant_label{color:rgb(153,255,102);}")

    def connect_functions(self):
        self.ui.parameters_reference_list_item_pushButton.clicked.connect(self.show_imported_asset_manager)
        self.ui.remove_reference_widget_item.clicked.connect(self.remove)
        self.ui.refresh_reference_widget_item.clicked.connect(self.set_last_version)
        self.ui.folder_reference_list_item_pushButton.clicked.connect(self.explorer)
        self.ui.ticket_reference_list_item_pushButton.clicked.connect(self.open_ticket)

    def open_ticket(self):
        self.open_ticket_widget = open_ticket_widget.Main(self.asset)
        build.launch_normal_as_child(self.open_ticket_widget)

    def show_imported_asset_manager(self):
        old_namespace = reference.get_name_space(self.asset, self.count)
        self.dialog_imported_asset_manager = dialog_imported_asset_manager.Main(self.asset, self.count, self.proxy, self.visible)
        if build.launch_dialog_as_child(self.dialog_imported_asset_manager):
            old_asset = copy.deepcopy(self.asset)
            self.asset = copy.deepcopy(self.dialog_imported_asset_manager.asset)
            self.proxy = copy.deepcopy(self.dialog_imported_asset_manager.proxy)
            self.visible = copy.deepcopy(self.dialog_imported_asset_manager.visible)
            self.init_widget()
            self.reference_list_widget.replace_reference(self.asset, self.count, old_namespace, self.proxy, self.visible)

    def set_last_version(self):
        old_asset = copy.deepcopy(self.asset)
        self.asset.export_version = prefs.asset(self.asset).export.last_version
        self.init_widget()
        self.reference_list_widget.replace_reference(self.asset, self.count)

    def remove(self):
        self.reference_list_widget.delete_asset(self.asset, self.count, self.parent_item)

    def explorer(self):
        path = prefs.asset(self.asset).export.version_folder
        os.startfile(path)