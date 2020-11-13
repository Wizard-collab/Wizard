# coding: utf8

# Import PyQt5 libraries
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication

# Import wizard gui libraries
from gui.project_preferences import Ui_Form
from gui import build

# Import wizard core libraries
from wizard.tools import log
from wizard.vars import defaults
from wizard.prefs.main import prefs
from wizard.prefs import project as project_prefs
from wizard.prefs import software as software_prefs
from wizard.vars import softwares
from wizard.prefs.site import site
from wizard.tools import password as pwd
from wizard.tools import utility as utils
import workflow_widget

# Import wizard widgets
import project_widget

# Import python base libraries
import sys
import os

# Init main logger
logger = log.pipe_log(__name__)
prefs = prefs()

ICON_SIZE = 18

class Main(QtWidgets.QWidget):

    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.fill_project_settings()
        self.ui.save_prefs_pushButton.clicked.connect(self.save_prefs)
        self.init_listWidget()
        self.update_softwares()
        self.refresh_ui()
        self.connect_functions()
        self.init_show_pass_icon()
        self.fill_project_infos()
        self.init_workflow_widget()

    def fill_project_infos(self):
        site_path = os.environ[defaults._wizard_site_]
        project_path = prefs.project_path
        project_name = prefs.project_name
        project_size = 0
        start_path = project_path  # To get size of current directory
        for path, dirs, files in os.walk(start_path):
            for f in files:
                fp = os.path.join(path, f)
                project_size += os.path.getsize(fp)
        self.ui.site_path_label.setText(site_path)
        self.ui.project_path_label.setText(project_path)
        self.ui.project_name_label.setText(project_name)
        self.ui.project_size_label.setText(str(utils.convert_size(project_size)))

    def init_listWidget(self):
        self.ui.preferences_ui_listWidget.FocusPolicy = QtCore.Qt.NoFocus
        self.ui.preferences_ui_listWidget.setCurrentRow(0)
        self.ui.preferences_ui_listWidget.currentRowChanged.connect(self.ui.stackedWidget.setCurrentIndex)

    def init_workflow_widget(self):
        self.workflow_widget = workflow_widget.Main()
        self.ui.stackedWidget.insertWidget(2, self.workflow_widget)

    def fill_project_settings(self):
        self.custom_ext_dic = project_prefs.get_custom_pub_ext_dic()
        format = project_prefs.get_format()
        format_width = format[0]
        format_height = format[1]
        fur_ext = self.custom_ext_dic[defaults._cfx_][defaults._maya_]
        self.ui.f_width_lineEdit.setText(str(format_width))
        self.ui.f_height_lineEdit.setText(str(format_height))
        if fur_ext == 'fur':
            index = 0
        else:
            index = 1
        self.ui.cfx_ext_comboBox.setCurrentIndex(index)
        f_rate = project_prefs.get_frame_rate()
        self.ui.frame_rate_spinBox.setValue(f_rate)

    def save_prefs(self):
        format_width = self.ui.f_width_lineEdit.text()
        format_height = self.ui.f_height_lineEdit.text()
        format = [format_width, format_height]
        fur_ext = (self.ui.cfx_ext_comboBox.currentText()).replace('.', '')
        self.custom_ext_dic[defaults._cfx_][defaults._maya_] = fur_ext
        self.custom_ext_dic[defaults._cfx_][defaults._maya_yeti_] = fur_ext
        frame_rate = self.ui.frame_rate_spinBox.value()
        project_prefs.set_frame_rate(frame_rate)
        project_prefs.set_format(format)
        project_prefs.set_custom_pub_ext_dic(self.custom_ext_dic)
        logger.info("Preferences saved !")
        self.hide()

    def refresh_ui(self):
        self.update_launch_button()
        software = self.ui.setup_softwares_comboBox.currentText()
        executable = software_prefs.software(software).get_path()
        command = softwares._cmd_dic_[software]
        env = software_prefs.software(software).get_env()
        env_paths = software_prefs.software(software).get_env_paths()
        if executable:
            self.ui.executable_lineEdit.setText(executable)
        else:
            self.ui.executable_lineEdit.clear()

        self.ui.command_lineEdit.setText(command)

        if env:
            self.ui.additionnal_textEdit.setText(env)
        else:
            self.ui.additionnal_textEdit.clear()
        if env_paths:
            self.ui.env_textEdit.setText(env_paths)
        else:
            self.ui.env_textEdit.clear()

    def update_softwares(self):
        for software in defaults._softwares_list_:
            self.ui.setup_softwares_comboBox.addItem(software)

    def update_launch_button(self):
        current_software = self.ui.setup_softwares_comboBox.currentText()
        if current_software:
            icon = defaults._soft_icons_dic_[current_software]
            self.ui.save_setup_pushButton.setIcon(QtGui.QIcon(icon))
            self.ui.save_setup_pushButton.setIconSize(QtCore.QSize(28, 28))

    def update_prefs(self):
        executable = self.ui.executable_lineEdit.text()
        scripts_path = self.ui.additionnal_textEdit.toPlainText()
        env_paths = self.ui.env_textEdit.toPlainText()
        software = self.ui.setup_softwares_comboBox.currentText()
        if executable.endswith('"'):
            executable = executable[:-1]
        if executable.startswith('"'):
            executable = executable[1:]
        software_prefs.software(software).init_settings(executable, env_paths, scripts_path)

    def connect_functions(self):
        self.ui.setup_softwares_comboBox.currentIndexChanged.connect(self.refresh_ui)
        self.ui.save_setup_pushButton.clicked.connect(self.update_prefs)
        self.ui.change_password_pushButton.clicked.connect(self.change)
        self.ui.confirm_lineEdit.textChanged.connect(self.check_confirm)
        self.ui.new_lineEdit.textChanged.connect(self.check_confirm)
        self.ui.show_pass_pushButton.clicked.connect(self.show_passwords)

    def init_show_pass_icon(self):
        self.show_pw = 0
        self.ui.show_pass_pushButton.setIcon(QtGui.QIcon(defaults._hide_icon_))
        self.ui.show_pass_pushButton.setIconSize(QtCore.QSize(15, 15))

    def change(self):
        old_pass = self.ui.old_lineEdit.text()
        project = prefs.project_name
        if not site().project_password_check(project, old_pass):
            logger.error('Wrong password...')
        elif not self.check_confirm():
            logger.error("Passwords doesn't matches...")
        else:
            QApplication.processEvents()
            QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
            self.ui.change_password_pushButton.setText('Changing password...')
            QApplication.processEvents()
            new_pass = self.ui.new_lineEdit.text()
            encrypted_pass = pwd.encrypt(new_pass)
            site().change_project_password(project, encrypted_pass)
            QApplication.processEvents()
            logger.info('Password changed !')
            QApplication.processEvents()
            self.ui.change_password_pushButton.setText('Password changed !')
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()

    def show_passwords(self):
        if self.show_pw == 0:
            self.ui.confirm_lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.ui.new_lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.ui.old_lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.ui.show_pass_pushButton.setIcon(QtGui.QIcon(defaults._show_icon_))
            self.show_pw = 1
        else:
            self.ui.confirm_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
            self.ui.new_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
            self.ui.old_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
            self.ui.show_pass_pushButton.setIcon(QtGui.QIcon(defaults._hide_icon_))
            self.show_pw = 0

    def check_confirm(self):
        password = self.ui.new_lineEdit.text()
        confirm = self.ui.confirm_lineEdit.text()
        if confirm != password:
            self.ui.confirm_lineEdit.setStyleSheet('border:1px solid Red;')
            return 0
        else:
            self.ui.confirm_lineEdit.setStyleSheet('border:1px solid Green;')
            return 1