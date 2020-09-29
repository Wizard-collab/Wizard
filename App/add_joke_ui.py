from PyQt5 import QtWidgets, QtCore, QtGui

from gui.add_joke_dialog import Ui_Dialog
from gui import build
from wizard.vars import defaults
from wizard.tools import log

logger = log.pipe_log(__name__)


class Main(QtWidgets.QDialog):

    def __init__(self):
        super(Main, self).__init__()
        # Build the ui from ui converted file
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.chart_image_label.setPixmap(
            QtGui.QPixmap(defaults._police_icon_).scaled(60, 60, QtCore.Qt.KeepAspectRatio,
                                                         QtCore.Qt.SmoothTransformation))
        self.connect_functions()

    def submit(self):
        self.joke = self.ui.joke_data_plainTextEdit.toPlainText()
        self.accept()

    def connect_functions(self):
        self.ui.submit_pushButton.clicked.connect(self.submit)
