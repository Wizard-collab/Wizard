from PyQt5 import QtWidgets, QtCore, QtGui

import os
import copy
from editable_list_widget import list_widget
from gui import build
from wizard.vars import defaults
import options_widget
from wizard.prefs.main import prefs
import dialog_imported_asset_manager
from wizard.tools import log
from wizard.asset import reference
import open_ticket_widget

logger = log.pipe_log(__name__)

prefs = prefs()

class Main(list_widget):

    def __init__(self, reference_list_widget, asset=None, count='0001', selectable=True, proxy = 0, visible = 1, item = None):
        super(Main, self).__init__()
        self.asset = asset
        self.count = count
        self.proxy = proxy
        self.visible = 1
        self.parent_item = item
        self.reference_list_widget = reference_list_widget
        self.init_widget()
        self.connect_functions()

    def init_widget(self):

        icon = defaults._nodes_icons_dic_[self.asset.stage]

        self.refresh_reference_button = self.add_button(defaults._refresh_icon_)
        self.remove_reference_button = self.add_button(defaults._trash_large_icon_)
        self.parameters_button = self.add_button(defaults._settings_icon_)
        self.folder_button = self.add_button(defaults._folder_icon_)
        self.ticket_button = self.add_button(defaults._tickets_icon_)

        self.set_icon(icon)

        self.stage_label = self.add_label(self.asset.stage, 'stage_label')
        self.name_label = self.add_label(self.asset.name, 'name_label')
        self.variant_label = self.add_label("{}.{}".format(self.asset.variant, self.asset.export_version), 'variant_label')
        self.ns_label = self.add_label(self.asset.export_asset, 'ns_label')

        if self.asset.export_version != prefs.asset(self.asset).export.last_version:
            self.variant_label.setStyleSheet("#variant_label{color:rgb(255,153,51);}")
        else:
            self.variant_label.setStyleSheet("#variant_label{color:rgb(153,255,102);}")

    def refresh_widget(self):
        self.stage_label.setText(self.asset.stage)
        self.name_label.setText(self.asset.name)
        self.variant_label.setText("{}.{}".format(self.asset.variant, self.asset.export_version))
        self.ns_label.setText(self.asset.export_asset)

    def connect_functions(self):
        self.parameters_button.clicked.connect(self.show_imported_asset_manager)
        self.remove_reference_button.clicked.connect(self.remove)
        self.refresh_reference_button.clicked.connect(self.set_last_version)
        self.folder_button.clicked.connect(self.explorer)
        self.ticket_button.clicked.connect(self.open_ticket)

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
            self.refresh_widget()
            self.reference_list_widget.replace_reference(self.asset, self.count, old_namespace, self.proxy, self.visible)

    def set_last_version(self):
        old_asset = copy.deepcopy(self.asset)
        self.asset.export_version = prefs.asset(self.asset).export.last_version
        self.refresh_widget()
        self.reference_list_widget.replace_reference(self.asset, self.count)

    def remove(self):
        self.reference_list_widget.delete_asset(self.asset, self.count, self.parent_item)

    def explorer(self):
        path = prefs.asset(self.asset).export.version_folder
        os.startfile(path)