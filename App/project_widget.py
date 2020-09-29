# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtCore, QtGui
from gui.project_widget import Ui_Form
from wizard.tools import log
from wizard.vars import defaults
from wizard.prefs import site as site_prefs

import os

logger = log.pipe_log(__name__)


class Main(QtWidgets.QWidget):

    def __init__(self, project_name):
        super(Main, self).__init__()
        # Build the ui from ui converted file
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.project_name = project_name
        self.project_path = site_prefs.site().get_project_path_from_name(self.project_name)
        self.init_ui()

    def init_ui(self):
        self.ui.project_name_label.setText(self.project_name)
        self.ui.project_path_label.setText(self.project_path)
        if not os.path.isdir(self.project_path):
            self.ui.project_path_label.setStyleSheet("#project_path_label{color:orange}")
        self.ui.project_folder_image_label.setPixmap(
            QtGui.QPixmap(defaults._project_folder_icon_).scaled(40, 40, QtCore.Qt.KeepAspectRatio,
                                                                 QtCore.Qt.SmoothTransformation))
