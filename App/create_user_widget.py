from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import pyqtSignal

from gui.create_user_widget import Ui_Form

from gui import build
from wizard.vars import defaults
from wizard.prefs.main import prefs
import dialog_new_user
import dialog_users

prefs = prefs()

class Main(QtWidgets.QWidget):
    user_created = pyqtSignal(str)

    def __init__(self):
        super(Main, self).__init__()
        # Build the ui from ui converted file
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.add_logos()
        self.connect_functions()

    def add_logos(self):
        self.ui.welcome_info_image_label.setPixmap(
            QtGui.QPixmap(defaults._welcom_user_image_).scaled(45, 45, QtCore.Qt.KeepAspectRatio,
                                                               QtCore.Qt.SmoothTransformation))

    def connect_functions(self):
        self.ui.create_pushButton.clicked.connect(self.create_user)
        if prefs.site.users:
            self.ui.log_pushButton.clicked.connect(self.log)
        else:
            self.ui.log_pushButton.hide()

    def create_user(self):
        self.dialog_new_user = dialog_new_user.Main()
        if build.launch_dialog_as_child(self.dialog_new_user):
            self.user_created.emit('')

    def log(self):
        self.dialog_users = dialog_users.Main()
        if build.launch_dialog_as_child(self.dialog_users):
            self.user_created.emit('')
