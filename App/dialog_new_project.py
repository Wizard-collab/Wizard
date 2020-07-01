from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QFileDialog

from wizard.project import create as create_project
from gui.new_project_dialog import Ui_Dialog
from wizard.tools import log
from wizard.vars import defaults
from gui import log_to_gui
import os

logger = log.pipe_log()


class Main(QtWidgets.QDialog):

    def __init__(self):
        super(Main, self).__init__()
        # Build the ui from ui converted file
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.init_show_pass_icon()
        self.connect_functions()
        self.show = 0
        qtHandler = log_to_gui.log_viewer(self.ui)
        logger.main_logger.addHandler(qtHandler)
        self.ui.open_folder_pushButton.setIcon(QtGui.QIcon(defaults._folder_icon_))

    def show_passwords(self):
        if self.show == 0:
            self.ui.confirm_lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.ui.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.ui.show_pass_pushButton.setIcon(QtGui.QIcon(defaults._show_icon_))
            self.show = 1
        else:
            self.ui.confirm_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
            self.ui.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
            self.ui.show_pass_pushButton.setIcon(QtGui.QIcon(defaults._hide_icon_))
            self.show = 0

    def init_show_pass_icon(self):
        self.ui.show_pass_pushButton.setIcon(QtGui.QIcon(defaults._hide_icon_))
        self.ui.show_pass_pushButton.setIconSize(QtCore.QSize(15, 15))

    def connect_functions(self):
        self.ui.create_project_pushButton.clicked.connect(self.create_project)
        self.ui.show_pass_pushButton.clicked.connect(self.show_passwords)
        self.ui.confirm_lineEdit.textChanged.connect(self.check_confirm)
        self.ui.password_lineEdit.textChanged.connect(self.check_confirm)
        self.ui.open_folder_pushButton.clicked.connect(self.open_path)
        self.ui.project_path_lineEdit.textChanged.connect(self.update_path)
        self.ui.lineEdit.textChanged.connect(self.update_path)

    def open_path(self):
        project_path = QFileDialog.getExistingDirectory(self, "Open project directory",
                                       "/home",
                                       QFileDialog.ShowDirsOnly
                                       | QFileDialog.DontResolveSymlinks)
        if project_path:
            self.ui.project_path_lineEdit.setText(project_path)

    def update_path(self):
        project_name = self.ui.lineEdit.text()
        project_path = self.ui.project_path_lineEdit.text()

        if project_path != '' and project_name != '':
            self.ui.project_path_label.setText("Destination : {}".format(os.path.join(project_path, project_name).replace('\\', '/')))
        else:
            self.ui.project_path_label.setText("Destination : None")

    def check_confirm(self):
        password = self.ui.password_lineEdit.text()
        confirm = self.ui.confirm_lineEdit.text()
        if confirm != password:
            self.ui.confirm_lineEdit.setStyleSheet('border:1px solid Red;')
            return 0
        else:
            self.ui.confirm_lineEdit.setStyleSheet('border:1px solid Green;')
            return 1

    def create_project(self):

        project_name = self.ui.lineEdit.text()
        project_path = self.ui.project_path_lineEdit.text()
        password = self.ui.password_lineEdit.text()

        format_width = self.ui.width_lineEdit.text()
        format_height = self.ui.height_lineEdit.text()
        if format_width and format_width != '' and format_height and format_height != '':
            format = [format_width, format_height]
        else:
            format = None

        if project_name != '':
            if password and self.check_confirm():
                if format:
                    frame_rate = self.ui.frame_rate_spinBox.value()
                    if create_project.create_project(project_name, project_path, frame_rate, format, password):
                        logger.info('Project {} created!'.format(project_name))
                        self.accept()
                else:
                    logger.warning("Please enter a format ( pixels )")
            else:
                logger.warning("Please enter a valid password !")
        else:
            logger.warning("Please enter a project name !")
