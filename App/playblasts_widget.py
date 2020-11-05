from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication
from gui.playblasts_widget import Ui_Form
from gui import build
from wizard.vars import defaults
from wizard.tools import log
from wizard.prefs.main import prefs
import export_widget
import export_asset_widget
import copy
import dialog_manual_export
import ui_export_manager
import ui_subprocess_manager
from wizard.tools import utility as utils
import ui_export_manager
import playblast_asset_widget
from editable_list_widget import icon_widget
import os

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
        self.number = 3
        self.step = 3
        self.count = 1
        self.as_list = 0
        self.get_params()
        self.connect_functions()
        self.ui.sanity_exports_pushButton.setIcon(QtGui.QIcon(defaults._export_list_icon_gray_))
        self.ui.show_all_exports_pushButton.setIcon(QtGui.QIcon(defaults._sd_icon_))
        self.ui.batch_playblast_pushButton.setIcon(QtGui.QIcon(defaults._batch_playblast_icon_))

    def connect_functions(self):
        self.ui.batch_playblast_pushButton.clicked.connect(self.do_playblast)
        self.ui.sanity_exports_pushButton.clicked.connect(self.update_all)
        self.ui.show_all_exports_pushButton.clicked.connect(self.update_all)
        self.ui.show_more_pushButton.clicked.connect(self.add_number)
        self.ui.show_less_pushButton.clicked.connect(self.remove_number)
        self.ui.display_pushButton.clicked.connect(self.change_view)

    def change_view(self):
        self.as_list = 1-self.as_list
        self.update_all()

    def get_params(self):
        if self.ui.show_all_exports_pushButton.isChecked():
            self.full = 1
        else:
            self.full = 0
        if self.ui.sanity_exports_pushButton.isChecked():
            self.sanity = 1
        else:
            self.sanity = 0
        if self.as_list:
            self.ui.reference_list_listWidget.setMovement(QtWidgets.QListView.Static)
            self.ui.reference_list_listWidget.setResizeMode(QtWidgets.QListView.Adjust)
            self.ui.reference_list_listWidget.setViewMode(QtWidgets.QListView.ListMode)
            self.ui.display_pushButton.setIcon(QtGui.QIcon(defaults._reference_list_icon_))
        else:
            self.ui.reference_list_listWidget.setMovement(QtWidgets.QListView.Static)
            self.ui.reference_list_listWidget.setResizeMode(QtWidgets.QListView.Adjust)
            self.ui.reference_list_listWidget.setViewMode(QtWidgets.QListView.IconMode)
            self.ui.display_pushButton.setIcon(QtGui.QIcon(defaults._icon_mode_view_))

    def add_number(self):
        self.number += 3
        self.update_all()

    def remove_number(self):
        self.number -= 3
        self.update_all()

    def refresh_all(self, asset):
        self.asset = asset

        self.versions_list = []

        if self.asset.variant:
            pb_prefs = prefs.asset(self.asset).playblast
            self.versions_list = pb_prefs.versions
        
        self.update_all()

    def update_all(self):
        self.get_params()
        self.clear_all()
        versions_list =[]
        if self.versions_list and self.versions_list != []:
            if not self.full:
                versions_list = self.versions_list[-self.number:]
            else:
                versions_list = self.versions_list
        self.ui.playblast_number_label.setText('( {}/{} )'.format(len(versions_list), len(self.versions_list)))
        for version in versions_list:
            if self.as_list:
                pb_widget = playblast_asset_widget.list(self.asset, version, self.count, self.sanity)
            else:
                pb_widget = playblast_asset_widget.icon(self.asset, version, self.count, self.sanity)
            self.add_item_to_list(pb_widget)

    def add_item_to_list(self, widget):
        item = QtWidgets.QListWidgetItem() 
        item.setSizeHint(widget.sizeHint())
        widget.parent_item = item
        self.ui.reference_list_listWidget.addItem(item)
        self.ui.reference_list_listWidget.setItemWidget(item, widget)

    def clear_all(self):
        self.ui.reference_list_listWidget.clear()

    def do_playblast_1(self):
        if self.asset:
            if self.asset.software == defaults._maya_ or self.asset.software == defaults._maya_yeti_:
                command = 'from wizard.tools.playblast import playblast/n'
                command += 'playblast("{}").playblast()'.format(utils.asset_to_string(self.asset))
                file = utils.temp_file_from_command(command)
                self.ui_subprocess_manager = ui_subprocess_manager.Main(["python", "-u", file])
                build.launch_normal_as_child(self.ui_subprocess_manager, minimized = 1)

    def do_playblast(self):
        if self.asset:
            self.ui_export_manager = ui_export_manager.Main(self.asset, 'playblast')
            build.launch_normal_as_child(self.ui_export_manager)

    def closeEvent(self, event):
        event.ignore()
        self.hide()
