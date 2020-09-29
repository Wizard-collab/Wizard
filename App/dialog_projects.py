from PyQt5 import QtWidgets
from PyQt5.QtCore import QPoint

from gui.projects_dialog import Ui_Dialog
from gui import build
from wizard.prefs.user import user
from wizard.prefs.site import site
import dialog_new_project
from wizard.tools import log
from gui import log_to_gui

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
        self.update_projects()

    def clean_projects(self):
        self.site.clean_projects()

    def connect_functions(self):
        self.ui.change_project_pushButton.clicked.connect(self.change_project)
        self.ui.new_project_pushButton.clicked.connect(self.new_project)

    def new_project(self):
        self.dialog_new_project = dialog_new_project.Main()
        if build.launch_dialog_as_child(self.dialog_new_project):
            self.reject()

    def update_projects(self):
        # Get all the users from the ite prefs
        projects_list = self.site.get_projects_list()
        # Get the current user
        current_project = self.user.get_current_project_name()
        if current_project:
            # Get the current user index
            index = list(projects_list.keys()).index(current_project)
            # Add each users to the ui
        else:
            index = 0
        if projects_list:
            for project in projects_list:
                self.ui.projects_comboBox.addItem(project)
            self.ui.projects_comboBox.setCurrentIndex(index)

    def change_project(self):
        project_name = self.ui.projects_comboBox.currentText()
        password = self.ui.password_lineEdit.text()
        password_check = self.site.project_password_check(project_name, password)
        if password_check:
            if self.user.change_project(project_name):
                self.accept()
