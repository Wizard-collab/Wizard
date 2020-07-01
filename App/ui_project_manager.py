# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtCore, QtGui
from gui.projects_manager import Ui_Form
from gui import build
from wizard.tools import log
from wizard.vars import defaults
from wizard.prefs.main import prefs
import project_widget
import sys

logger = log.pipe_log()

prefs = prefs()

class Main(QtWidgets.QWidget):

    def __init__(self):
        super(Main, self).__init__()
        # Build the ui from ui converted file
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.init_icons()
        self.load_projects()

    def load_projects(self):
        for project_name in prefs.site.projects:
            widget = project_widget.Main(project_name)
            self.ui.projects_verticalLayout.insertWidget(0, widget)

    def init_icons(self):
        self.ui.project_manager_image_label.setPixmap(
            QtGui.QPixmap(defaults._projects_icon_).scaled(55, 55, QtCore.Qt.KeepAspectRatio,
                                                           QtCore.Qt.SmoothTransformation))

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(defaults._wizard_ico_))
    project_manager = Main
    build.launch_normal(project_manager)
