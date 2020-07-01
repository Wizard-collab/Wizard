from PyQt5 import QtWidgets, QtCore, QtGui

from gui.email_confirm_dialog import Ui_Dialog
from gui import build
from wizard.tools import log
from gui import log_to_gui

logger = log.pipe_log()

class Main(QtWidgets.QDialog):
    
    def __init__(self, parent, verification_code):
        super(Main, self).__init__()
        # Build the ui from ui converted file
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.connect_functions()
        self.verification_code = verification_code
        self.qtHandler = log_to_gui.log_viewer(self.ui)
        logger.main_logger.addHandler(self.qtHandler)
        self.show=0

    def connect_functions(self):
        self.ui.confirm_pushButton.clicked.connect(self.confirm)

    def confirm(self):
        input_code = self.ui.verification_lineEdit.text()
        if self.verification_code == input_code:
            self.accept()
        else:
            logger.error("The code doesn't match")
            