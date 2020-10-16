from PyQt5 import QtWidgets, QtCore, QtGui
from gui.user_scripts_widget import Ui_Form
from wizard.vars import defaults
from wizard.tools import log
from wizard.prefs.main import prefs
from wizard.prefs.user_scripts import user_scripts
from gui import build
import create_user_script_widget
import traceback
import options_widget

logger = log.pipe_log(__name__)

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
            self.add_button(scripts_dic[defaults._user_scripts_], key)

    def refresh_scripts(self):
        for i in reversed(range(self.ui.scripts_buttons_layout.count())):
            self.ui.scripts_buttons_layout.itemAt(i).widget().setParent(None)
        self.get_scripts_dic()

    def connect_functions(self):
        self.ui.add_user_script_pushButton.clicked.connect(self.create_script)

    def create_script(self):
        self.create_user_script_widget = create_user_script_widget.Main()
        #self.create_user_script_widget.create_signal.connect(self.refresh_scripts)
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
        #self.create_user_script_widget.create_signal.connect(self.refresh_scripts)
        build.launch_normal_as_child(self.create_user_script_widget)

    def delete_script(self, key):
        user_scripts().delete_script(key)
        self.refresh_scripts()

    def execute_script(self, script):
        try:
            exec(script)
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
            #emittion du signal rightClick
            self.show_options_menu()
        else:
            self.parent.execute_script(self.script_dic[self.key][defaults._user_script_])

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
        self.options_widget = options_widget.Main()
        self.options_widget.add_item('Delete', self.delete_script)
        self.options_widget.add_item('Modify', self.modify_script)
        build.launch_options(self.options_widget)