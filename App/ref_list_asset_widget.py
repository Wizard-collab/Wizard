from PyQt5 import QtWidgets, QtCore, QtGui

import os
import copy
from gui.ref_list_asset_widget import Ui_Form
from gui import build
from wizard.vars import defaults
import options_widget
from wizard.prefs.main import prefs
import dialog_imported_asset_manager
from wizard.tools import log
from wizard.asset import reference

logger = log.pipe_log()

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
        self.node_editor = node_editor
        self.visible = 1
        self.init_node()
        self.add_name()
        # Select variable
        self.selected = False

    def init_node(self, image=None):
        if self.asset:
            icon = defaults._stage_icon_[self.asset.stage]
        else:
            icon = ''
        self.ui.ref_list_asset_image_label.setPixmap(
            QtGui.QPixmap(icon).scaled(14, 14, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))

    def add_name(self):
        if self.asset:

            self.ui.ref_list_asset_name_label.setText(self.asset.name)
            self.ui.ref_list_asset_variant_label.setText(self.asset.variant)
            self.ui.ref_list_asset_version_label.setText(self.asset.export_version)
            self.ui.ref_list_asset_count_label.setText(str(self.count))

            if self.selectable:
                if self.asset.export_version != prefs.asset(self.asset).export.last_version:
                    self.ui.ref_list_asset_variant_label.setStyleSheet("#asset_variant_label{color:rgb(255,153,51);}")
                else:
                    self.ui.ref_list_asset_variant_label.setStyleSheet("#asset_variant_label{color:rgb(153,255,102);}")

    def enterEvent(self, event):
        if self.selectable and not self.selected:
            self.ui.ref_list_asset_frame.setStyleSheet(
                '#ref_list_asset_frame{background-color:rgba(255,255,255,60)}')

    def leaveEvent(self, event):
        if not self.selected:
            self.ui.ref_list_asset_frame.setStyleSheet('')

    '''
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
                self.ui.ref_list_asset_frame.setStyleSheet('#ref_list_asset_frame{border:1px solid grey}')
                #self.node_editor.add_selection(self)
            else:
                self.deselect()
        if event.button() == QtCore.Qt.RightButton:
            self.show_options_menu()
    '''

    def show_options_menu(self):
        if self.selectable:
            self.options_widget = options_widget.Main()
            self.options_widget.add_item('Remove', self.remove)
            self.options_widget.add_item('Explorer', self.explorer)
            #self.options_widget.add_item('Launch', lambda: self.asset.launch(self.node_editor.main_window))
            self.options_widget.add_item('Parameters', self.show_imported_asset_manager)
            self.options_widget.add_item('Set last version', self.set_last_version)
            build.launch_options(self.options_widget)

    def show_imported_asset_manager(self):
        old_namespace = reference.get_name_space(self.asset, self.count)
        self.dialog_imported_asset_manager = dialog_imported_asset_manager.Main(self.asset, self.count, self.proxy, self.visible)
        if build.launch_dialog_as_child(self.dialog_imported_asset_manager):
            old_asset = copy.deepcopy(self.asset)
            self.asset = copy.deepcopy(self.dialog_imported_asset_manager.asset)
            self.proxy = copy.deepcopy(self.dialog_imported_asset_manager.proxy)
            self.visible = copy.deepcopy(self.dialog_imported_asset_manager.visible)
            self.add_name()
            self.node_editor.replace_reference(self, old_namespace, self.proxy, self.visible)

    def set_last_version(self):
        old_asset = copy.deepcopy(self.asset)
        self.asset.export_version = prefs.asset(self.asset).export.last_version
        self.add_name()
        #self.node_editor.replace_reference(self)

    def remove(self):
        pass
        #self.node_editor.delete_asset(self)

    def explorer(self):
        path = prefs.asset(self.asset).export.version_folder
        os.startfile(path)

    '''
    def deselect(self):
        if self.selected:
            self.selected = False
            self.ui.node_widget_button_frame.setStyleSheet('#node_widget_button_frame{border:0px solid yellow}')
            self.node_editor.remove_selection(self)
    '''
