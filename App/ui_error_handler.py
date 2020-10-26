# coding: utf8

# Import pytohn base libraries
import traceback

# Import PyQt5 libraries
from PyQt5 import QtWidgets, QtCore, QtGui

# Import wizard gui libraries
from gui.error_handler import Ui_Form
from gui import build

# Import wizard core libraries
from wizard.vars import defaults
from wizard.tools import log
from wizard.email import main as email
from wizard.prefs.main import prefs

# Initializing the logger and the prefs module
logger = log.pipe_log(__name__)
prefs = prefs()

class Main(QtWidgets.QWidget):

    def __init__(self, record):
        super(Main, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.record = record
        self.setup_ui()
        self.connect_functions()

    def setup_ui(self):
        self.ui.handler_textEdit.setText(self.record)

    def connect_functions(self):
        self.ui.submit_error_pushButton.clicked.connect(self.submit_error)
        self.ui.cancel_pushButton.clicked.connect(self.close)
        self.ui.hide_dialog_checkBox.stateChanged.connect(self.hide_dialog)

    def submit_error(self):
        email.error_submit(prefs.user, self.record)
        self.close()

    def hide_dialog(self):
        state = self.ui.hide_dialog_checkBox.isChecked()
        prefs.set_show_error_handler(1-state)

    def closeEvent(self, event):
        event.ignore()
        self.hide()
