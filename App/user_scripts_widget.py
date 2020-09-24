from PyQt5 import QtWidgets, QtCore, QtGui
from gui.user_scripts_widget import Ui_Form
from wizard.vars import defaults
from wizard.tools import log
from wizard.prefs.main import prefs
from wizard.prefs.user_scripts import user_scripts
from gui import build
import create_user_script_widget
import traceback

logger = log.pipe_log()

prefs = prefs()

class Main(QtWidgets.QWidget):

    def __init__(self):
        super(Main, self).__init__()
        # Build the ui from ui converted file
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.connect_functions()
        self.user_scripts = user_scripts()
        self.refresh_scripts()

    def get_scripts_dic(self):
        scripts_dic = self.user_scripts.get_scripts_as_dic()
        for key in scripts_dic[defaults._user_scripts_].keys():
            logger.info(scripts_dic[defaults._user_scripts_][key])
            logger.info(key)
            logger.info(scripts_dic[defaults._user_scripts_][key][defaults._user_script_])

            self.add_button(scripts_dic[defaults._user_scripts_][key])

    def refresh_scripts(self):
        for i in reversed(range(self.ui.scripts_buttons_layout.count())):
            self.ui.scripts_buttons_layout.itemAt(i).widget().setParent(None)
        self.get_scripts_dic()

    def connect_functions(self):
        self.ui.add_user_script_pushButton.clicked.connect(self.create_script)

    def create_script(self):
        self.create_user_script_widget = create_user_script_widget.Main()
        self.create_user_script_widget.create_signal.connect(self.refresh_scripts)
        build.launch_normal_as_child(self.create_user_script_widget)

    def add_button(self, script):
        button = QtWidgets.QPushButton()
        button.setIcon(QtGui.QIcon(script[defaults._user_script_image_]))
        button.setIconSize(QtCore.QSize(20, 20))
        button.setMaximumSize(QtCore.QSize(30,30))
        button.setMinimumSize(QtCore.QSize(30,30))
        button.setToolTip(script[defaults._user_script_name_])
        button.clicked.connect(lambda:self.execute_script(script[defaults._user_script_]))
        self.ui.scripts_buttons_layout.addWidget(button)

    def execute_script(self, script):
        try:
            exec(script)
        except:
            logger.error(str(traceback.format_exc()))