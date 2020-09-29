from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication

from gui.users_dialog import Ui_Dialog
from gui import build
from wizard.prefs.main import prefs
from wizard.tools import log
from gui import log_to_gui
import ui_recover_password
import time

logger = log.pipe_log(__name__)

prefs = prefs()

class Main(QtWidgets.QDialog):

    def __init__(self, force=None):
        super(Main, self).__init__()
        # Build the ui from ui converted file
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.force = force
        self.connect_functions()
        qtHandler = log_to_gui.log_viewer(self.ui)
        logger.main_logger.addHandler(qtHandler)
        self.update_users()

    def recover(self):
        self.ui_recover_password = ui_recover_password.Main(self)
        build.launch_dialog_as_child(self.ui_recover_password)

    def connect_functions(self):
        self.ui.change_user_pushButton.clicked.connect(self.change_user)
        self.ui.recover_pushButton.clicked.connect(self.recover)

    def closeEvent(self, event):
        if self.force:
            event.ignore()
        else:
            event.accept()

    def update_users(self):
        # Get all the users from the site prefs
        users_list = prefs.site.users
        # Get the current user
        current_user = prefs.user
        if current_user:
            # Get the current user index
            index = list(users_list.keys()).index(current_user)
            # Add each users to the ui
        else:
            index = 0
        if users_list:
            for user in users_list:
                self.ui.users_comboBox.addItem(user)
            self.ui.users_comboBox.setCurrentIndex(index)

    def change_user(self):
        user_name = self.ui.users_comboBox.currentText()
        password = self.ui.lineEdit.text()
        QApplication.processEvents()
        QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        self.ui.change_user_pushButton.setText('Logging...')
        QApplication.processEvents()
        if prefs.change_user(user_name=user_name, password=password):
            time.sleep(1)
            QApplication.restoreOverrideCursor()
            QApplication.processEvents()
            self.ui.change_user_pushButton.setText('Verified !')
            QApplication.processEvents()
            time.sleep(2)
            QApplication.processEvents()
            self.accept()
        else:
            self.ui.change_user_pushButton.setText('Log')
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
