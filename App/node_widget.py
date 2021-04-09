from PyQt5 import QtWidgets, QtCore, QtGui

import os
import copy
from gui.node_widget import Ui_Form
from gui import build
from wizard.tools import utility as utils
from wizard.vars import defaults
import options_widget
from wizard.prefs.main import prefs
import dialog_imported_asset_manager
from wizard.tools import log
from wizard.asset import reference
import open_ticket_widget

logger = log.pipe_log(__name__)

prefs = prefs()

class Main(QtWidgets.QWidget):

    def __init__(self, node_editor, asset=None, count='0001', selectable=True, proxy = 0, visible = 1):
        super(Main, self).__init__()
        # Build the ui from ui converted file
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.selectable = selectable
        self.asset = asset
        self.count = count
        self.proxy = proxy
        self.visible = 1
        self.init_node()
        self.add_name()
        self.node_editor = node_editor
        # Select variable
        self.selected = False

    def init_node(self, image=None):
        if self.asset:
            icon = defaults._nodes_icons_dic_[self.asset.stage]
        else:
            icon = defaults._missing_node_icon_
        self.ui.image_label.setPixmap(
            QtGui.QPixmap(icon).scaled(30, 30, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))

    def add_name(self):
        if self.asset:
            self.ui.asset_name_label.show()
            self.ui.asset_variant_label.show()
            self.ui.asset_name_label.setText(self.asset.name)
            if self.selectable:
                self.ui.asset_variant_label.setText("{}.{}".format(self.asset.variant, self.asset.export_version))
                self.ui.asset_namespace_label.setText("{}".format(self.asset.export_asset))
                if self.asset.export_version != prefs.asset(self.asset).export.last_version:
                    self.ui.asset_variant_label.setStyleSheet("#asset_variant_label{color:rgb(255,153,51);}")
                else:
                    self.ui.asset_variant_label.setStyleSheet("#asset_variant_label{color:rgb(153,255,102);}")
            else:
                self.ui.asset_variant_label.setText("{}".format(self.asset.variant))
                self.ui.asset_namespace_label.hide()
        else:
            self.ui.asset_name_label.hide()
            self.ui.asset_variant_label.hide()

    def enterEvent(self, event):
        if self.selectable and not self.selected:
            self.ui.node_widget_button_frame.setStyleSheet(
                '#node_widget_button_frame{background-color:rgba(255,255,255,60)}')

    def leaveEvent(self, event):
        if not self.selected:
            self.ui.node_widget_button_frame.setStyleSheet('')

    def mousePressEvent(self, event):
        modifiers = QtWidgets.QApplication.keyboardModifiers()
        if modifiers != QtCore.Qt.ShiftModifier:
            widgets_list = self.node_editor.scene_references_widget.copy()
            for widget in widgets_list:
                if widget.selected:
                    widget.deselect()
        if self.selectable:
            if not self.selected:
                self.selected = True
                self.ui.node_widget_button_frame.setStyleSheet('#node_widget_button_frame{border:1px solid grey}')
                self.node_editor.add_selection(self)
            else:
                self.deselect()
        if event.button() == QtCore.Qt.RightButton:
            self.show_options_menu()

    def show_options_menu(self):
        if self.selectable:
            self.options_widget = options_widget.Main()
            self.options_widget.add_item('Remove', self.remove)
            self.options_widget.add_item('Explorer', self.explorer)
            self.options_widget.add_item('Launch', lambda: self.asset.launch(self.node_editor.main_window))
            self.options_widget.add_item('Parameters', self.show_imported_asset_manager)
            self.options_widget.add_item('Open ticket', self.open_ticket)
            self.options_widget.add_item('Set last version', self.set_last_version)
            build.launch_options(self.options_widget)

    def open_ticket(self):
        self.open_ticket_widget = open_ticket_widget.Main(self.asset)
        build.launch_normal_as_child(self.open_ticket_widget)

    def show_imported_asset_manager(self):
        old_namespace = reference.get_name_space(self.asset, self.count)
        logger.info(utils.asset_to_string(self.asset))
        self.dialog_imported_asset_manager = dialog_imported_asset_manager.Main(self.asset, self.count, self.proxy, self.visible)
        if build.launch_dialog_as_child(self.dialog_imported_asset_manager):
            old_asset = copy.deepcopy(self.asset)
            self.asset = copy.deepcopy(self.dialog_imported_asset_manager.asset)
            self.proxy = copy.deepcopy(self.dialog_imported_asset_manager.proxy)
            self.visible = copy.deepcopy(self.dialog_imported_asset_manager.visible)
            self.add_name()
            self.node_editor.replace_reference(self, self.asset, self.count, old_namespace, self.proxy, self.visible)

    def set_last_version(self):
        old_asset = copy.deepcopy(self.asset)
        old_namespace = reference.get_name_space(old_asset, self.count)
        self.asset.export_version = prefs.asset(self.asset).export.last_version
        self.add_name()
        self.node_editor.replace_reference(self, self.asset, self.count, old_namespace)

    def remove(self):
        self.node_editor.delete_asset(self)

    def explorer(self):
        path = prefs.asset(self.asset).export.version_folder
        os.startfile(path)

    def deselect(self):
        if self.selected:
            self.selected = False
            self.ui.node_widget_button_frame.setStyleSheet('#node_widget_button_frame{border:0px solid yellow}')
            self.node_editor.remove_selection(self)
