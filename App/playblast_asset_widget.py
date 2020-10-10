from PyQt5 import QtWidgets, QtCore, QtGui

import os
from gui.playblast_widget import Ui_Form
from gui import build
from wizard.vars import defaults
from wizard.tools import log
from wizard.prefs.main import prefs
import options_widget
import dialog_comment

logger = log.pipe_log(__name__)

prefs = prefs()

class Main(QtWidgets.QWidget):

    def __init__(self, asset, version, count, sanity):
        super(Main, self).__init__()
        # Build the ui from ui converted file
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.sanity = sanity
        self.count = count
        self.asset = asset
        self.version = version
        self.init_ui()
        self.connect_functions()

    def init_ui(self):
        self.ui.playblast_widget_view_pushButton.setIcon(QtGui.QIcon(defaults._show_playblast_icon_))
        self.ui.playblast_widget_comment_pushButton.setIcon(QtGui.QIcon(defaults._comment_icon_))
        self.ui.playblast_widget_folder_pushButton.setIcon(QtGui.QIcon(defaults._folder_icon_))
        icon = defaults._export_list_neutral_icon_
        pb_prefs = prefs.asset(self.asset).playblast

        self.ui.playblast_widget_version_label.setText(self.version)
        self.ui.playblast_widget_comment_label.setText(pb_prefs.version_comment(self.version))
        self.ui.playblast_widget_date_label.setText(pb_prefs.version_date(self.version))
        self.ui.playblast_widget_user_label.setText(pb_prefs.version_user(self.version))
        if self.count:
            self.ui.list_playblast_widget_frame.setStyleSheet('''#list_playblast_widget_frame{background-color:rgba(255,255,255,5);}
                #list_playblast_widget_frame:hover{
                
                }''')
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
        self.ui.playblast_widget_image_label.setPixmap(
            QtGui.QPixmap(icon).scaled(22, 22, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.RightButton:
            self.show_options_menu()

    def show_options_menu(self):
        self.options_widget = options_widget.Main()
        self.options_widget.add_item('Explorer', self.open_folder)
        self.options_widget.add_item('Open', self.open_file)
        build.launch_options(self.options_widget)

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
            self.ui.playblast_widget_comment_label.setText(self.dialog_comment.comment)

    def connect_functions(self):
        self.ui.playblast_widget_view_pushButton.clicked.connect(self.open_file)
        self.ui.playblast_widget_comment_pushButton.clicked.connect(self.change_comment)
        self.ui.playblast_widget_folder_pushButton.clicked.connect(self.open_folder)

    def closeEvent(self, event):
        event.ignore()
        self.hide()
