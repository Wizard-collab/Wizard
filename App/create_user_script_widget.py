from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import pyqtSignal
from gui.create_user_script_widget import Ui_Form
from wizard.vars import defaults
from wizard.tools import log
from wizard.prefs.main import prefs
import traceback
from wizard.prefs.user_scripts import user_scripts
import icons_list_dialog
from gui import build

logger = log.pipe_log(__name__)

prefs = prefs()

class Main(QtWidgets.QWidget):

    create_signal = pyqtSignal(str)

    def __init__(self, script_dic=None):
        super(Main, self).__init__()
        # Build the ui from ui converted file
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.icon = defaults._log_icon_
        self.update_icon()
        self.connect_functions()
        self.script_dic = script_dic
        if self.script_dic:
            self.fill_ui()
            self.ui.create_user_script_tittle_label.setText("Modify script")

    def update_icon(self):
        self.ui.script_icon_pushButton.setIcon(QtGui.QIcon(self.icon))

    def fill_ui(self):
        name = self.script_dic[-1][defaults._user_script_name_]
        script = self.script_dic[-1][defaults._user_script_]
        self.icon = self.script_dic[-1][defaults._user_script_image_]
        self.ui.script_name_lineEdit.setText(name)
        self.ui.script_plainTextEdit.appendPlainText(script)
        self.ui.script_icon_pushButton.setIcon(QtGui.QIcon(self.icon))

    def create(self):
        name = self.ui.script_name_lineEdit.text()
        script = self.ui.script_plainTextEdit.toPlainText()
        user_scripts().create_user_script(name, self.icon, script)
        self.create_signal.emit("")
        self.hide()

    def select_icon(self):
        self.icons_list_dialog = icons_list_dialog.Main()
        if build.launch_dialog_as_child(self.icons_list_dialog):
            self.icon = defaults._icon_path_ + self.icons_list_dialog.icon
            self.ui.script_icon_pushButton.setIcon(QtGui.QIcon(self.icon))

    def connect_functions(self):
        self.ui.create_script_pushButton.clicked.connect(self.create)
        self.ui.script_icon_pushButton.clicked.connect(self.select_icon)