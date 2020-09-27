from PyQt5 import QtWidgets, QtCore, QtGui
from gui.updates import Ui_Form
from wizard.vars import defaults
from wizard.prefs.main import prefs
from wizard.tools import log
import webbrowser
import os
from wizard.vars import updates

logger = log.pipe_log()

prefs = prefs()

class Main(QtWidgets.QWidget):

    def __init__(self):
        super(Main, self).__init__()
        # Build the ui from ui converted file
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.shadow = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(8)
        self.shadow.setColor(QtGui.QColor(0, 0, 0, 180))
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.setGraphicsEffect(self.shadow)

        self.connect_functions()
        self.fill_updates()

    def show_updates(self):
        prefs.set_show_updates(self.ui.show_startup_checkBox.isChecked())

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

    def show_doc(self):
        os.startfile(os.path.abspath(defaults._doc_index_path_))

    def show_web(self):
        webbrowser.open(defaults._wizard_url_, new=0, autoraise=True)
