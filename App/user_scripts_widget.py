# coding: utf8

# Import PyQt5 libraries
from PyQt5 import QtWidgets, QtCore, QtGui

# Import wizard gui libraries
from gui.user_scripts_widget import Ui_Form
from gui import build

# Import wizard core libraries
from wizard.vars import defaults
from wizard.tools import log
from wizard.prefs.main import prefs
from wizard.prefs.user_scripts import user_scripts
from wizard.tools import utility as utils
from wizard.user_scripts import user_session

# Import wizard widgets
import create_user_script_widget
import options_widget
import ui_subprocess_manager

# Import python base libraries
import traceback
import os
import sys

# Init the main logger and the prefs module
logger = log.pipe_log(__name__)
prefs = prefs()

class Main(QtWidgets.QWidget):

    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.connect_functions()
        self.user_scripts = user_scripts()
        self.refresh_scripts()

    def get_scripts_dic(self):
        scripts_dic = self.user_scripts.get_scripts_as_dic()
        for key in scripts_dic[defaults._user_scripts_].keys():
            self.add_button(scripts_dic[defaults._user_scripts_], key)
        self.separator = QtWidgets.QLabel()
        self.separator.setText('-')
        self.ui.scripts_buttons_layout.addWidget(self.separator)
        project_scripts_dic = self.user_scripts.get_project_scripts_as_dic()
        for key in project_scripts_dic[defaults._user_scripts_].keys():
            self.add_button(project_scripts_dic[defaults._user_scripts_], key)

    def refresh_scripts(self):
        for i in reversed(range(self.ui.scripts_buttons_layout.count())):
            self.ui.scripts_buttons_layout.itemAt(i).widget().setParent(None)
        self.get_scripts_dic()

    def connect_functions(self):
        self.ui.add_user_script_pushButton.clicked.connect(self.create_script)

    def create_script(self):
        self.create_user_script_widget = create_user_script_widget.Main()
        build.launch_normal_as_child(self.create_user_script_widget)

    def add_button(self, script_dic, key):
        button = customButton(self, key, script_dic)
        button.setIcon(QtGui.QIcon(script_dic[key][defaults._user_script_image_]))
        button.setIconSize(QtCore.QSize(20, 20))
        button.setMaximumSize(QtCore.QSize(30,30))
        button.setMinimumSize(QtCore.QSize(30,30))
        button.setToolTip(script_dic[key][defaults._user_script_name_])
        self.ui.scripts_buttons_layout.addWidget(button)

    def modify_script(self, key, script_dic):
        self.create_user_script_widget = create_user_script_widget.Main([key, script_dic[key]])
        build.launch_normal_as_child(self.create_user_script_widget)

    def delete_script(self, key):
        user_scripts().delete_script(key)
        self.refresh_scripts()

    def execute_script(self, script):
        user_session.execute_session_script(script)

    def batch_execute_script(self, script):
        try:
            file = utils.temp_file_from_command(script)
            env = os.environ.copy()
            python_system = 'pywizard'
            if sys.argv[0].endswith('.py'):
                python_system = 'python pywizard.py'
            self.ui_subprocess_manager = ui_subprocess_manager.Main(f'{python_system} {file}', env, cwd=os.path.abspath(''))
            build.launch_normal_as_child(self.ui_subprocess_manager, minimized = 1)
        except:
            logger.error(str(traceback.format_exc()))

class customButton(QtWidgets.QPushButton):
    def __init__(self, parent, key, script_dic):
        super(customButton, self).__init__(parent)
        self.parent = parent
        self.key = key
        self.script_dic = script_dic
        self.setStyleSheet("background-color: rgb(44,44,51);")

    def mousePressEvent(self, event):
        self.setStyleSheet("background-color: rgb(16,16,23);")
        if event.button() == QtCore.Qt.RightButton :
            self.show_options_menu()
        else:
            if defaults._subprocess_ in self.script_dic[self.key].keys():
                if self.script_dic[self.key][defaults._subprocess_]:
                    self.batch_execute()
                else:
                    self.parent.execute_script(self.script_dic[self.key][defaults._user_script_])
            else:
                self.parent.execute_script(self.script_dic[self.key][defaults._user_script_])

    def batch_execute(self):
        self.parent.batch_execute_script(self.script_dic[self.key][defaults._user_script_])

    def enterEvent(self, *args, **kwargs):
        self.setStyleSheet("background-color: rgb(50,50,57);")

    def leaveEvent(self, *args, **kwargs):
        self.setStyleSheet("background-color: rgb(44,44,51);")

    def mouseReleaseEvent(self, event,*args, **kwargs):
        button_used = self.text()
        self.setStyleSheet("background-color: rgb(50,50,57);")

    def modify_script(self):
        self.parent.modify_script(self.key, self.script_dic)

    def delete_script(self):
        self.parent.delete_script(self.key)

    def show_options_menu(self):
        self.options_widget = options_widget.Main(self)
        self.options_widget.add_item('Delete', self.delete_script)
        self.options_widget.add_item('Modify', self.modify_script)
        self.options_widget.add_item('Subprocess', self.batch_execute)
        build.launch_options(self.options_widget)