from PyQt5 import QtWidgets, QtCore, QtGui
from gui.user_scripts_widget import Ui_Form
from wizard.vars import defaults
from wizard.tools import log
from wizard.prefs.main import prefs

logger = log.pipe_log()

prefs = prefs()

class Main(QtWidgets.QWidget):

    def __init__(self, asset):
        super(Main, self).__init__()
        # Build the ui from ui converted file
        self.ui = Ui_Form()
        self.ui.setupUi(self)