from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QFileDialog

from gui.merge_project_dialog import Ui_Dialog
from gui import build
from wizard.prefs.user import user
from wizard.prefs.site import site
from wizard.tools import log
from gui import log_to_gui
from wizard.vars import defaults

import os

logger = log.pipe_log(__name__)


class Main(QtWidgets.QDialog):

    def __init__(self):
        super(Main, self).__init__()
        # Build the ui from ui converted file
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.site = site()
        self.user = user()
        self.clean_projects()
        self.connect_functions()
        qtHandler = log_to_gui.log_viewer(self.ui)
        logger.main_logger.addHandler(qtHandler)
        self.ui.project_path_pushButton.setIcon(QtGui.QIcon(defaults._folder_icon_))
        self.project_path = None
        self.project_name = None
        self.password = None

    def clean_projects(self):
        self.site.clean_projects()

    def connect_functions(self):
        self.ui.project_path_pushButton.clicked.connect(self.open_path)
        self.ui.project_path_lineEdit.textChanged.connect(self.check_project)
        self.ui.password_lineEdit.textChanged.connect(self.check_password)
        self.ui.confirm_password_lineEdit.textChanged.connect(self.check_password)
        self.ui.change_project_pushButton.clicked.connect(self.merge_project)

    def open_path(self):
        project_path = QFileDialog.getExistingDirectory(self, "Open project directory",
                                       "/home",
                                       QFileDialog.ShowDirsOnly
                                       | QFileDialog.DontResolveSymlinks)
        if project_path:
            self.ui.project_path_lineEdit.setText(project_path)

    def check_project(self):
        self.project_path = self.ui.project_path_lineEdit.text()
        if os.path.isdir(self.project_path):
            if os.path.isfile(os.path.join(self.project_path, 'project.wd')):
                self.ui.project_path_lineEdit.setStyleSheet('border:1px solid Green;')
                self.project_name = os.path.split(self.project_path)[-1]
                logger.info("Project found")
            else:
                self.ui.project_path_lineEdit.setStyleSheet('border:1px solid Red;')
                self.project_path = None
                self.project_name = None
                logger.warning("This project isn't recognized by wizard")
        else:
            self.ui.project_path_lineEdit.setStyleSheet('border:1px solid Red;')
            self.project_path = None
            self.project_name = None
            logger.warning("This folder doesn't exists")

    def check_password(self):
        password = self.ui.password_lineEdit.text()
        password_check = self.ui.confirm_password_lineEdit.text()
        if password and password != '' and password == password_check:
            self.password = password
            self.ui.confirm_password_lineEdit.setStyleSheet('border:1px solid Green;')
        else:
            self.password = None
            self.ui.confirm_password_lineEdit.setStyleSheet('border:1px solid Red;')

    def merge_project(self):
        if self.project_path and self.password:
            self.site.add_project(self.project_name, self.project_path, self.password)