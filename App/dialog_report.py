from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication
from gui.report_dialog import Ui_Dialog
from wizard.vars import defaults
from wizard.email import main as email
from wizard.prefs.main import prefs
from wizard.tools import log

logger = log.pipe_log()

prefs = prefs()

class Main(QtWidgets.QDialog):

    def __init__(self, error):
        super(Main, self).__init__()
        # Build the ui from ui converted file
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.connect_functions()
        self.error = error
        self.init_report_button()

    def init_report_button(self):
        self.ui.report_error_pushButton.setIcon(QtGui.QIcon(defaults._email_icon_))
        self.ui.report_error_pushButton.setIconSize(QtCore.QSize(38, 38))

    def send_report(self):
        message = self.ui.message_textEdit.toPlainText()
        if message or message != '':
            QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
            email.send_error(prefs.user, prefs.user_email, self.error.replace('\n', '<br>'),
                             message.replace('\n', '<br>'))
            QApplication.restoreOverrideCursor()
            self.accept()
        else:
            logger.warning('Please write a little message !')

    def connect_functions(self):
        self.ui.report_error_pushButton.clicked.connect(self.send_report)
