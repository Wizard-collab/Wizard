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
from wizard.user_scripts import user_scripts_library

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
        self.ui.create_user_script_warning_label.setVisible(0)
        if self.script_dic:
            self.fill_ui()
            self.edit = 1
            self.ui.create_user_script_tittle_label.setText("Modify script")
            self.ui.script_name_lineEdit.setEnabled(0)
        if new_script:
            self.ui.script_editor.setText(new_script)
        self.fill_scripts_template()

    def fill_scripts_template(self):
        for script_name in user_scripts_library.scripts_dic.keys():
            self.ui.scripts_templates_listWidget.addItem(script_name)

    def import_template(self, item):
        script_name = item.text()
        script_data = user_scripts_library.scripts_dic[script_name]

        self.ui.script_editor.setText(script_data)
        if not self.edit:
            self.ui.script_name_lineEdit.setText(script_name)

    def update_icon(self):
        self.ui.script_icon_pushButton.setIcon(QtGui.QIcon(self.icon))

    def fill_ui(self):
        name = self.script_dic[-1][defaults._user_script_name_]
        script = self.script_dic[-1][defaults._user_script_]
        if defaults._subprocess_ in self.script_dic[-1].keys():
            only_subprocess = self.script_dic[-1][defaults._subprocess_]
        else:
            only_subprocess = 0

        if defaults._project_ in self.script_dic[-1].keys():
            project = self.script_dic[-1][defaults._project_]
        else:
            project = 0

        self.icon = self.script_dic[-1][defaults._user_script_image_]
        self.ui.script_name_lineEdit.setText(name)
        self.ui.script_editor.setText(script)
        self.ui.script_icon_pushButton.setIcon(QtGui.QIcon(self.icon))
        self.ui.only_subprocess_checkBox.setChecked(only_subprocess)
        self.ui.create_script_project_radioButton.setChecked(project)
        self.ui.create_script_project_radioButton.setEnabled(0)
        self.ui.create_script_user_radioButton.setEnabled(0)

    def create(self):
        name = self.ui.script_name_lineEdit.text()
        script = self.ui.script_editor.text().decode('utf-8')
        only_subprocess = self.ui.only_subprocess_checkBox.isChecked()
        project = self.ui.create_script_project_radioButton.isChecked()
        if name != '':
            logger.info(user_scripts().get_scripts_as_dic())

            is_in_local = name in user_scripts().get_scripts_as_dic()[defaults._user_scripts_].keys()
            is_in_project = name in user_scripts().get_project_scripts_as_dic()[defaults._user_scripts_].keys()

            if (is_in_project or is_in_project) and not self.edit:
                logger.warning(f'{name} already exists')
            else:
                user_scripts().create_user_script(name, self.icon, script, only_subprocess=only_subprocess, project = project)
                send_signal.refresh_signal()
                self.hide()
        else:
            logger.warning('Please enter a script name')

    def check_for_loop(self):
        script_data = self.ui.script_editor.text().decode('utf-8')
        if 'for 'in script_data or 'while ' in script_data:
            self.ui.create_user_script_warning_label.setVisible(1)
            self.ui.create_user_script_warning_label.setText('There seems to be a loop inside your code, you should activate "Only Subprocess"')
        else:
            self.ui.create_user_script_warning_label.setVisible(0)

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
        self.ui.scripts_templates_listWidget.itemDoubleClicked.connect(self.import_template)
        self.ui.script_editor.textChanged.connect(self.check_for_loop)
