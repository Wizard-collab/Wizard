from PyQt5 import QtWidgets, QtCore, QtGui
from gui.close_ticket_dialog import Ui_Dialog
from wizard.vars import defaults
from wizard.tools import log
from wizard.prefs.main import prefs
from wizard.tools import utility as utils
from wizard.asset.tickets import tickets

import ticket_widget

logger = log.pipe_log(__name__)

prefs = prefs()

class Main(QtWidgets.QDialog):

    def __init__(self):
        super(Main, self).__init__()
        # Build the ui from ui converted file
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.connect_functions()
        self.setup_ui()

    def connect_functions(self):
        self.ui.close_ticket_widget_close_pushButton.clicked.connect(self.close_ticket)
        self.ui.close_ticket_widget_cancel_pushButton.clicked.connect(self.reject)

    def setup_ui(self):
        self.ui.ticket_icon_label.setPixmap(
                    QtGui.QPixmap(defaults._ticket_icon_).scaled(24, 24, QtCore.Qt.KeepAspectRatio,
                                                                              QtCore.Qt.SmoothTransformation))

    def close_ticket(self):
        self.comment = self.ui.close_ticket_plainTextEdit.toPlainText()
        if self.comment and self.comment != '':
            self.accept()
        else:
            logger.info("Please enter your retakes or bugs solves") 