# coding: utf8

# Import PyQt5 libraries
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import pyqtSignal

# Import python base libraries
import os

# Import wizard gui libraries
#from gui.version_widget import Ui_Form
from editable_list_widget import icon_widget
from editable_list_widget import list_widget
from gui import build

# Import wizard core libraries
from wizard.vars import defaults
from wizard.tools import log
from wizard.prefs.main import prefs
from wizard.tools import utility as utils

# Import wizard widgets
import options_widget
import dialog_comment
import dialog_delete_asset

# Init the main logger and prefs module
logger = log.pipe_log(__name__)
prefs = prefs()

class list(list_widget):

    open_signal = pyqtSignal(str)

    def __init__(self, asset, sanity, count):
        super(list, self).__init__()
        self.asset = asset
        self.count = count
        self.sanity = sanity
        self.init_ui()
        self.connect_functions()

    def init_ui(self):

        self.version_widget_delete_pushButton = self.add_button(defaults._trash_large_icon_)
        self.version_widget_comment_pushButton = self.add_button(defaults._comment_icon_)
        self.version_open_software_pushButton = self.add_button(defaults._soft_icons_dic_[self.asset.software])
        version_prefs = prefs.asset(self.asset).software
        self.version_widget_version_label = self.add_label(self.asset.version, "version_widget_version_label", 40)
        self.version_widget_user_label = self.add_label(version_prefs.version_user, "version_widget_user_label", 120)
        self.version_widget_date_label = self.add_label(version_prefs.version_date, "version_widget_date_label", 180)
        self.version_widget_comment_label = self.add_label(version_prefs.version_comment, "version_widget_comment_label", 230, QtCore.Qt.AlignLeft)
        self.update_sanity(self.sanity)

    def update_sanity(self, sanity):
        if sanity:
            file = self.asset.file
            if not os.path.isfile(file):
                icon = defaults._missing_file_export_list_icon_
            else:
                icon = defaults._export_list_icon_
        else:
            icon = defaults._export_list_neutral_icon_
        self.set_icon(icon)

    def open_folder(self):
        file = prefs.asset(self.asset).software.version_folder
        os.startfile(file)

    def change_comment(self):
        self.dialog_comment = dialog_comment.Main(self.asset, 0)
        if build.launch_dialog_comment(self.dialog_comment):
            self.version_widget_comment_label.setText(self.dialog_comment.comment)

    def delete_version(self):
        self.dialog_delete_asset = dialog_delete_asset.Main()
        if build.launch_dialog_as_child_frameless(self.dialog_delete_asset):
            if prefs.asset(self.asset).software.remove_version(self.asset.version):
                self.setParent(None)
                self.deleteLater()

    def open(self):
        self.open_signal.emit(utils.asset_to_string(self.asset))

    def connect_functions(self):
        self.version_widget_delete_pushButton.clicked.connect(self.delete_version)
        self.version_widget_comment_pushButton.clicked.connect(self.change_comment)
        self.version_open_software_pushButton.clicked.connect(self.open)

    def closeEvent(self, event):
        event.ignore()
        self.hide()

class icon(icon_widget):

    open_signal = pyqtSignal(str)

    def __init__(self, asset, sanity, count):
        super(icon, self).__init__()
        self.asset = asset
        self.count = count
        self.sanity = sanity
        self.init_ui()

    def init_ui(self):
        version_prefs = prefs.asset(self.asset).software
        self.set_name("{} - {} - {}".format(self.asset.version, version_prefs.version_user, version_prefs.version_date))
        self.set_comment(version_prefs.version_comment)
        image = version_prefs.image
        if not os.path.isfile(image):
            image = defaults._missing_pb_image_
        self.set_image(image)
        self.update_sanity(self.sanity)

        '''
        self.version_widget_delete_pushButton = self.add_button(defaults._trash_large_icon_)
        self.version_widget_comment_pushButton = self.add_button(defaults._comment_icon_)
        self.version_open_software_pushButton = self.add_button(defaults._soft_icons_dic_[self.asset.software])
        version_prefs = prefs.asset(self.asset).software
        self.version_widget_version_label = self.add_label(self.asset.version, "version_widget_version_label", 40)
        self.version_widget_user_label = self.add_label(version_prefs.version_user, "version_widget_user_label", 120)
        self.version_widget_date_label = self.add_label(version_prefs.version_date, "version_widget_date_label", 180)
        self.version_widget_comment_label = self.add_label(version_prefs.version_comment, "version_widget_comment_label", 230, QtCore.Qt.AlignLeft)
        self.update_sanity(self.sanity)
        '''

    def update_sanity(self, sanity):
        if sanity:
            file = self.asset.file
            if not os.path.isfile(file):
                icon = defaults._missing_file_export_list_icon_
            else:
                icon = defaults._export_list_icon_
        else:
            icon = defaults._export_list_neutral_icon_
        self.set_icon(icon)

    def open_folder(self):
        file = prefs.asset(self.asset).software.version_folder
        os.startfile(file)

    def change_comment(self):
        self.dialog_comment = dialog_comment.Main(self.asset, 0)
        if build.launch_dialog_comment(self.dialog_comment):
            self.version_widget_comment_label.setText(self.dialog_comment.comment)

    def delete_version(self):
        self.dialog_delete_asset = dialog_delete_asset.Main()
        if build.launch_dialog_as_child_frameless(self.dialog_delete_asset):
            if prefs.asset(self.asset).software.remove_version(self.asset.version):
                self.setParent(None)
                self.deleteLater()

    def open(self):
        self.open_signal.emit(utils.asset_to_string(self.asset))

    def closeEvent(self, event):
        event.ignore()
        self.hide()