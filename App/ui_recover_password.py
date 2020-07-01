from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication

from gui.recover_password import Ui_Dialog
from wizard.prefs.user import user
from wizard.prefs.site import site
from wizard.tools import log
from gui import log_to_gui
import time
from wizard.tools import password as pwd

logger = log.pipe_log()


class Main(QtWidgets.QDialog):

    def __init__(self, parent):
        super(Main, self).__init__()
        self.site = site()
        self.user = user()
        QtWidgets.QDialog.__init__(self, parent)
        # Build the ui from ui converted file
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.connect_functions()
        self.qtHandler = log_to_gui.log_viewer(self.ui)
        logger.main_logger.addHandler(self.qtHandler)
        self.update_users()

    def connect_functions(self):
        self.ui.recover_pushButton.clicked.connect(self.recover)

    def closeEvent(self, event):
        event.ignore()
        self.hide()

    def update_users(self):
        # Get all the users from the ite prefs
        users_list = self.site.get_users_list()
        # Get the current user
        current_user = self.user.get_user()
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

    def recover(self):
        user = self.ui.users_comboBox.currentText()
        email = self.ui.email_lineEdit.text()
        user_email = self.site.get_email_from_user(user)
        if email != user_email:
            logger.error("The email doesn't correspond to this user")
        else:
            QApplication.processEvents()
            QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
            self.ui.recover_pushButton.setText('Sending...')
            QApplication.processEvents()
            new_pwd = pwd.recover(user, email)
            if new_pwd:
                self.site.change_user_password(user, encrypted)
                QApplication.processEvents()
                logger.info('We sent you a new password by email!')
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                time.sleep(1)
                QApplication.processEvents()
                self.accept()
