from PyQt5 import QtWidgets, QtCore, QtGui

from gui.change_password_dialog import Ui_Dialog

from gui import build
from wizard.prefs.site import site
from wizard.prefs.user import user
from wizard.tools import password as pwd
from wizard.tools import log
from gui import log_to_gui
from wizard.vars import defaults
import ui_recover_password

logger = log.pipe_log(__name__)


class Main(QtWidgets.QDialog):

    def __init__(self):
        super(Main, self).__init__()
        # Build the ui from ui converted file
        self.site = site()
        self.user = user()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.connect_functions()
        self.init_show_pass_icon()
        qtHandler = log_to_gui.log_viewer(self.ui)
        logger.main_logger.addHandler(qtHandler)
        self.show = 0

    def init_show_pass_icon(self):
        self.ui.show_pass_pushButton.setIcon(QtGui.QIcon(defaults._hide_icon_))
        self.ui.show_pass_pushButton.setIconSize(QtCore.QSize(15, 15))

    def connect_functions(self):
        self.ui.change_password_pushButton.clicked.connect(self.change)
        self.ui.confirm_lineEdit.textChanged.connect(self.check_confirm)
        self.ui.new_lineEdit.textChanged.connect(self.check_confirm)
        self.ui.show_pass_pushButton.clicked.connect(self.show_passwords)
        self.ui.recover_pushButton.clicked.connect(self.recover)

    def change(self):
        old_pass = self.ui.old_lineEdit.text()
        user = self.user.get_user()
        if not self.site.password_check(user, old_pass):
            logger.error('Wrong password...')
        elif not self.check_confirm():
            logger.error("Passwords doesn't matches...")
        else:
            QApplication.processEvents()
            QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
            self.ui.change_password_pushButton.setText('Changing password...')
            QApplication.processEvents()
            new_pass = self.ui.new_lineEdit.text()
            encrypted_pass = pwd.encrypt(new_pass)
            self.site.change_user_password(user, encrypted_pass)
            QApplication.processEvents()
            logger.info('Password changed !')
            QApplication.processEvents()
            self.ui.change_password_pushButton.setText('Password changed !')
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            QApplication.processEvents()
            self.accept()

    def recover(self):
        self.ui_recover_password = ui_recover_password.Main(self)
        build.launch_dialog_as_child(self.ui_recover_password)

    def show_passwords(self):
        if self.show_pw == 0:
            self.ui.confirm_lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.ui.new_lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.ui.old_lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.ui.show_pass_pushButton.setIcon(QtGui.QIcon(defaults._show_icon_))
            self.show_pw = 1
        else:
            self.ui.confirm_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
            self.ui.new_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
            self.ui.old_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
            self.ui.show_pass_pushButton.setIcon(QtGui.QIcon(defaults._hide_icon_))
            self.show_pw = 0

    def check_confirm(self):
        password = self.ui.new_lineEdit.text()
        confirm = self.ui.confirm_lineEdit.text()
        if confirm != password:
            self.ui.confirm_lineEdit.setStyleSheet('border:1px solid Red;')
            return 0
        else:
            self.ui.confirm_lineEdit.setStyleSheet('border:1px solid Green;')
            return 1
