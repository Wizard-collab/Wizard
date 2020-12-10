# coding: utf8

# Import python base libraries
import traceback
import sys
import os

# Import PyQt5 libraries
from PyQt5 import QtWidgets, QtCore, QtGui

# Import wizard gui libraries
from gui.error_handler import Ui_Form
from gui import build
from wizard.tools import utility as utils
utils.init_wizard_env()

# Import wizard core libraries
from wizard.vars import defaults
from wizard.tools import log
from wizard.email import main as email
from wizard.prefs.main import prefs


# Initializing the logger and the prefs module
logger = log.pipe_log(__name__)
prefs = prefs()

class Main(QtWidgets.QWidget):

    def __init__(self, record = None):
        super(Main, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.record = record
        if self.record == None:
            self.get_records()
        self.setup_ui()
        self.connect_functions()

    def setup_ui(self):
        self.ui.error_handler_icon_label.setPixmap(QtGui.QPixmap(defaults._warning_).scaled(40, 40, QtCore.Qt.KeepAspectRatio,
                                                                              QtCore.Qt.SmoothTransformation))
        self.ui.handler_textEdit.setText(self.record)
        self.area_scroll_bar = self.ui.handler_textEdit.verticalScrollBar()
        self.area_scroll_bar.setValue(self.area_scroll_bar.maximum())

    def get_records(self):
        if os.path.isfile(defaults._log_file_):
            with open(defaults._log_file_, 'r') as f:
                self.record = f.read()
        else:
            self.record = ''

    def connect_functions(self):
        self.ui.submit_error_pushButton.clicked.connect(self.submit_error)
        self.ui.cancel_pushButton.clicked.connect(self.close)

    def submit_error(self):
        email.error_submit(prefs.user, self.record)
        self.close()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(defaults._wizard_ico_))
    error_handler = Main()
    error_handler.show()
    area_scroll_bar = error_handler.ui.handler_textEdit.verticalScrollBar()
    area_scroll_bar.setValue(area_scroll_bar.maximum())
    error_handler.setStyleSheet(build.load_stylesheet())
    #build.launch_file_viewer(error_handler, title = 'Crash')
    sys.exit(app.exec_())