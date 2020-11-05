from PyQt5 import QtWidgets, QtCore, QtGui

import os
#from gui.playblast_widget import Ui_Form
from editable_list_widget import list_widget
from editable_list_widget import icon_widget
from gui import build
from wizard.vars import defaults
from wizard.tools import log
from wizard.prefs.main import prefs
import options_widget
import dialog_comment

logger = log.pipe_log(__name__)

prefs = prefs()

class list(list_widget):

    def __init__(self, asset, version, count, sanity):
        super(list, self).__init__()
        self.sanity = sanity
        self.count = count
        self.asset = asset
        self.version = version
        self.init_ui()
        self.connect_functions()

    def init_ui(self):

        self.playblast_widget_folder_pushButton = self.add_button(defaults._folder_icon_)
        self.playblast_widget_comment_pushButton = self.add_button(defaults._comment_icon_)
        self.playblast_widget_view_pushButton = self.add_button(defaults._show_playblast_icon_)
        icon = defaults._export_list_neutral_icon_
        pb_prefs = prefs.asset(self.asset).playblast
        self.playblast_widget_version_label = self.add_label(self.version, "playblast_widget_version_label", 40)
        self.playblast_widget_user_label = self.add_label(pb_prefs.version_user(self.version), "playblast_widget_user_label", 120)
        self.playblast_widget_date_label = self.add_label(pb_prefs.version_date(self.version), "playblast_widget_date_label", 180)
        self.playblast_widget_comment_label = self.add_label(pb_prefs.version_comment(self.version), "playblast_widget_comment_label", 230, QtCore.Qt.AlignLeft)
        self.update_sanity(self.sanity)

    def update_sanity(self, sanity):
        if sanity:
            file = prefs.asset(self.asset).playblast.full_file(self.version)
            if not os.path.isfile(file):
                icon = defaults._missing_file_export_list_icon_
            else:
                icon = defaults._export_list_icon_
        else:
            icon = defaults._export_list_neutral_icon_
        self.set_icon(icon)

    def connect_functions(self):
        self.playblast_widget_view_pushButton.clicked.connect(lambda:open_file(self))
        self.playblast_widget_comment_pushButton.clicked.connect(lambda:change_comment(self))
        self.playblast_widget_folder_pushButton.clicked.connect(lambda:open_folder(self))

    def closeEvent(self, event):
        event.ignore()
        self.hide()

class icon(icon_widget):
    def __init__(self, asset, version, count, sanity):
        super(icon, self).__init__()
        self.sanity = sanity
        self.count = count
        self.asset = asset
        self.version = version
        self.init_ui()

    def init_ui(self):
        asset_prefs = prefs.asset(self.asset).playblast
        self.set_name("{} - {} - {}".format(self.version, asset_prefs.version_user(self.version), asset_prefs.version_date(self.version)))
        self.set_comment(asset_prefs.version_comment(self.version))
        pb_image = asset_prefs.version_image(self.version)
        if not os.path.isfile(pb_image):
            pb_image = defaults._missing_pb_image_
        self.set_image(pb_image)
        self.update_sanity(self.sanity)

    def update_sanity(self, sanity):
        if sanity:
            file = prefs.asset(self.asset).playblast.full_file(self.version)
            if not os.path.isfile(file):
                icon = defaults._missing_file_export_list_icon_
            else:
                icon = defaults._export_list_icon_
        else:
            icon = defaults._export_list_neutral_icon_
        self.set_icon(icon)

    def closeEvent(self, event):
        event.ignore()
        self.hide()

def open_file(self):
    file = prefs.asset(self.asset).playblast.full_file(self.version)
    if os.path.isfile(file):
        os.startfile(file)
    else:
        logger.info('{} not found'.format(file))

def open_folder(self):
    folder = prefs.asset(self.asset).playblast.folder
    os.startfile(folder)

def change_comment(self):
    self.dialog_comment = dialog_comment.Main(self.asset, 0, self.version)
    if build.launch_dialog_comment(self.dialog_comment):
        self.playblast_widget_comment_label.setText(self.dialog_comment.comment)

    