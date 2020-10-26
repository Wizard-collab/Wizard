# coding: utf8

# Importing PyQt5 libraries
from PyQt5 import QtWidgets

# Import wizard gui libraries
from gui.jokes_user_list import Ui_Form

# Import wizard core libraries
from wizard.tools import log
from wizard.prefs.main import prefs
from wizard.prefs.jokes import jokes

# Import wizard widgets
import user_joke_widget

# Initializing the logger and the prefs module
logger = log.pipe_log(__name__)
prefs = prefs()

class Main(QtWidgets.QDialog):

    def __init__(self):
        super(Main, self).__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.init_widgets()

    def closeEvent(self, event):
        event.ignore()
        self.hide()

    def init_widgets(self):
        user = prefs.user
        jokes_list = jokes().get_jokes_list()
        self.jokes_list = []
        if jokes_list and jokes_list != []:
            for joke_id in jokes_list:
                if user == jokes().get_joke_user(joke_id):
                    self.jokes_list.append(joke_id)
        if self.jokes_list and self.jokes_list != []:
            for joke_id in self.jokes_list:
                joke_data = jokes().get_joke_data(joke_id)
                widget = user_joke_widget.Main(joke_data, joke_id)
                self.ui.verticalLayout.insertWidget(0,widget)
