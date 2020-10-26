# coding: utf8

# Import PyQt5 libraries
from PyQt5 import QtWidgets, QtCore, QtGui

# Import wizard gui libraries
from gui.updates import Ui_Form

# Import wizard core libraries
from wizard.vars import defaults
from wizard.prefs.main import prefs
from wizard.tools import log
from wizard.vars import updates

# Import python base librariess
import webbrowser
import os

# Init the main logger and prefs module
logger = log.pipe_log(__name__)
prefs = prefs()

class Main(QtWidgets.QWidget):

    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.shadow = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(8)
        self.shadow.setColor(QtGui.QColor(0, 0, 0, 180))
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.setGraphicsEffect(self.shadow)
        self.ui.updates_history_plainTextEdit.setVisible(0)
        self.connect_functions()
        self.fill_updates()

    def show_updates(self):
        prefs.set_show_updates(self.ui.show_startup_checkBox.isChecked())

    def show_history(self):
        if not self.ui.updates_history_plainTextEdit.isVisible():
            self.ui.updates_history_plainTextEdit.setVisible(1)
            for key in updates.updates.keys():
                self.ui.updates_history_plainTextEdit.appendPlainText(updates.updates[key])
        else:
            self.ui.updates_history_plainTextEdit.setVisible(0)
            self.ui.updates_history_plainTextEdit.clear()

    def fill_updates(self):
        if defaults._wizard_version_ in updates.updates.keys():
            updates_text = updates.updates[defaults._wizard_version_]
        else:
            updates_text = "No updates"
        self.ui.update_updates_plainTextEdit.appendPlainText(updates_text)

    def connect_functions(self):
        self.ui.update_doc_pushButton.clicked.connect(self.show_doc)
        self.ui.update_web_pushButton.clicked.connect(self.show_web)
        self.ui.show_startup_checkBox.stateChanged.connect(self.show_updates)
        self.ui.updates_history_pushButton.clicked.connect(self.show_history)

    def show_doc(self):
        os.startfile(os.path.abspath(defaults._doc_index_path_))

    def show_web(self):
        webbrowser.open(defaults._wizard_url_, new=0, autoraise=True)
