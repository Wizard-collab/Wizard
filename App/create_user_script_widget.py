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
import os
import script_editor
from wizard.signal import send_signal

logger = log.pipe_log(__name__)

prefs = prefs()

class Main(QtWidgets.QWidget):

    #create_signal = pyqtSignal(str)

    def __init__(self, script_dic=None, new_script=None):
        super(Main, self).__init__()
        # Build the ui from ui converted file
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.icon = defaults._log_icon_
        self.ui.script_editor = script_editor.SimplePythonEditor()
        self.ui.script_editor_layout.addWidget(self.ui.script_editor)
        self.update_icon()
        self.connect_functions()
        self.script_dic = script_dic
        self.edit = None
        if self.script_dic:
            self.fill_ui()
            self.edit = 1
            self.ui.create_user_script_tittle_label.setText("Modify script")
        if new_script:
            self.ui.script_editor.setText(new_script)

    def update_icon(self):
        self.ui.script_icon_pushButton.setIcon(QtGui.QIcon(self.icon))

    def fill_ui(self):
        name = self.script_dic[-1][defaults._user_script_name_]
        script = self.script_dic[-1][defaults._user_script_]
        self.icon = self.script_dic[-1][defaults._user_script_image_]
        self.ui.script_name_lineEdit.setText(name)
        self.ui.script_editor.setText(script)
        self.ui.script_icon_pushButton.setIcon(QtGui.QIcon(self.icon))

    def create(self):
        name = self.ui.script_name_lineEdit.text()
        script = self.ui.script_editor.text().decode('utf-8')
        if name != '':
            logger.info(user_scripts().get_scripts_as_dic())
            if name in user_scripts().get_scripts_as_dic()[defaults._user_scripts_].keys() and not self.edit:
                logger.warning(f'{name} already exists')
            else:
                user_scripts().create_user_script(name, self.icon, script)
                send_signal.refresh_signal()
                self.hide()
        else:
            logger.warning('Please enter a script name')

    def select_icon(self):
        self.icons_list_dialog = icons_list_dialog.Main()
        if build.launch_dialog_as_child(self.icons_list_dialog):
            # if file exists (means that's a custom_icon) set icon with full path and not based on defaults module
            if os.path.isfile(self.icons_list_dialog.icon):
                self.icon = self.icons_list_dialog.icon
            else:
                self.icon = defaults._icon_path_ + self.icons_list_dialog.icon
            self.ui.script_icon_pushButton.setIcon(QtGui.QIcon(self.icon))

    def connect_functions(self):
        self.ui.create_script_pushButton.clicked.connect(self.create)
        self.ui.script_icon_pushButton.clicked.connect(self.select_icon)
