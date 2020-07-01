from PyQt5 import QtWidgets, QtGui

from gui.user_joke_widget import Ui_Form
from wizard.vars import defaults
from wizard.tools import log
from wizard.prefs.jokes import jokes

logger = log.pipe_log()

class Main(QtWidgets.QDialog):

    def __init__(self, joke_data, joke_id):
        super(Main, self).__init__()
        # Build the ui from ui converted file
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.joke_data = joke_data
        self.joke_id = joke_id
        self.connect_functions()
        self.init_widget()

    def closeEvent(self, event):
        event.ignore()
        self.hide()

    def init_widget(self):
        self.ui.joke_label.setText(self.joke_data)
        self.ui.delete_joke_pushButton.setIcon(QtGui.QIcon(defaults._trash_icon_))

    def delete_joke(self):
        if jokes().delete_joke(self.joke_id):
            self.setParent(None)

    def connect_functions(self):
        self.ui.delete_joke_pushButton.clicked.connect(self.delete_joke)
