from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import pyqtSignal

from gui.create_project_widget import Ui_Form

from gui import build
from wizard.vars import defaults
from wizard.prefs.main import prefs
import dialog_projects
import dialog_new_project

prefs = prefs()

class Main(QtWidgets.QWidget):
    project_openned = pyqtSignal(str)

    def __init__(self):
        super(Main, self).__init__()
        # Build the ui from ui converted file
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.add_logos()
        self.connect_functions()

    def add_logos(self):
        self.ui.welcome_info_image_label.setPixmap(
            QtGui.QPixmap(defaults._welcome_project_image_).scaled(45, 45, QtCore.Qt.KeepAspectRatio,
                                                                   QtCore.Qt.SmoothTransformation))

    def connect_functions(self):
        self.ui.create_pushButton.clicked.connect(self.create_project)
        if prefs.site.projects:
            self.ui.open_pushButton.clicked.connect(self.open)
        else:
            self.ui.open_pushButton.hide()

    def create_project(self):
        self.dialog_new_project = dialog_new_project.Main()
        if build.launch_dialog_as_child(self.dialog_new_project):
            self.project_openned.emit('')

    def open(self):
        self.dialog_projects = dialog_projects.Main()
        if build.launch_dialog_as_child(self.dialog_projects):
            self.project_openned.emit('')
