from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QPoint

from gui.softwares_prefs_dialog import Ui_Dialog
from gui import build
from wizard.vars import defaults
from wizard.prefs import software as software_prefs
from wizard.tools import log
import gui.log_to_gui as log_to_gui
import dialog_accept
from softwares_env.softwares.guerilla_render_wizard import setup_guerilla
from softwares_env.softwares.painter_wizard import setup_painter
from wizard.vars import softwares

logger = log.pipe_log()


class Main(QtWidgets.QDialog):

    def __init__(self):
        super(Main, self).__init__()
        # Build the ui from ui converted file

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        qtHandler = log_to_gui.log_viewer(self.ui)
        logger.main_logger.addHandler(qtHandler)
        self.update_softwares()
        self.refresh_ui()
        self.connect_functions()

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
            self.ui.save_setup_pushButton.setIconSize(QtCore.QSize(38, 38))

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
        if software == defaults._painter_:
            self.dialog_accept = dialog_accept.Main('Substance Painter/Wizard',
                                                    'Do you want to setup Substance Painter for Wizard ?\nThis will modify the install.',
                                                    defaults._setup_icon_)
            if build.launch_dialog_as_child(self.dialog_accept):
                setup_painter.setup_painter()

    def connect_functions(self):
        self.ui.setup_softwares_comboBox.currentIndexChanged.connect(self.refresh_ui)
        self.ui.save_setup_pushButton.clicked.connect(self.update_prefs)
