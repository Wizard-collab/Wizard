from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import pyqtSignal
import os
from gui.version_widget import Ui_Form
from gui import build
from wizard.vars import defaults
from wizard.tools import log
from wizard.prefs.main import prefs
from wizard.tools import utility as utils
import options_widget
import dialog_comment
import dialog_delete_asset

logger = log.pipe_log()

prefs = prefs()

class Main(QtWidgets.QWidget):

    open_signal = pyqtSignal(str)

    def __init__(self, asset, sanity, count):
        super(Main, self).__init__()
        # Build the ui from ui converted file
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.asset = asset
        self.count = count
        self.sanity = sanity
        self.init_ui()
        self.connect_functions()

    def init_ui(self):
        self.ui.version_widget_delete_pushButton.setIcon(QtGui.QIcon(defaults._trash_large_icon_))
        self.ui.version_widget_comment_pushButton.setIcon(QtGui.QIcon(defaults._comment_icon_))
        self.ui.version_open_software_pushButton.setIcon(QtGui.QIcon(defaults._soft_icons_dic_[self.asset.software]))
        version_prefs = prefs.asset(self.asset).software

        self.ui.version_widget_version_label.setText(self.asset.version)
        self.ui.version_widget_comment_label.setText(version_prefs.version_comment)
        self.ui.version_widget_date_label.setText(version_prefs.version_date)
        self.ui.version_widget_user_label.setText(version_prefs.version_user)

        if self.count:
            self.ui.list_version_widget_frame.setStyleSheet('''#list_version_widget_frame{background-color:rgba(255,255,255,5);}
                #list_version_widget_frame:hover{
                
                }''')

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
        self.ui.version_widget_image_label.setPixmap(
            QtGui.QPixmap(icon).scaled(22, 22, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))

    def open_folder(self):
        file = prefs.asset(self.asset).software.version_folder
        os.startfile(file)

    def change_comment(self):
        self.dialog_comment = dialog_comment.Main(self.asset, 0)
        build.launch_dialog_comment(self.dialog_comment)
        self.ui.version_widget_comment_label.setText(self.dialog_comment.comment)

    def delete_version(self):
        self.dialog_delete_asset = dialog_delete_asset.Main()
        if build.launch_dialog_as_child_frameless(self.dialog_delete_asset):
            if prefs.asset(self.asset).software.remove_version(self.asset.version):
                self.setParent(None)
                self.deleteLater()

    def open(self):
        self.open_signal.emit(utils.asset_to_string(self.asset))

    def connect_functions(self):
        self.ui.version_widget_delete_pushButton.clicked.connect(self.delete_version)
        self.ui.version_widget_comment_pushButton.clicked.connect(self.change_comment)
        self.ui.version_open_software_pushButton.clicked.connect(self.open)

    def closeEvent(self, event):
        event.ignore()
        self.hide()
