# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtCore, QtGui
from gui.workflow import Ui_Form
from gui import build
from wizard.tools import log
from wizard.vars import defaults
from wizard.prefs.main import prefs
from wizard.prefs import project as project_prefs
import project_widget
import sys

logger = log.pipe_log(__name__)

class Main(QtWidgets.QWidget):

    def __init__(self):
        super(Main, self).__init__()
        # Build the ui from ui converted file
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.fill_project_settings()
        self.ui.save_workflow_pushButton.clicked.connect(self.save_workflow)

    def fill_project_settings(self):
        format = project_prefs.get_format()
        format_width = format[0]
        format_height = format[1]
        self.ui.f_width_lineEdit.setText(str(format_width))
        self.ui.f_height_lineEdit.setText(str(format_height))

        f_rate = project_prefs.get_frame_rate()
        self.ui.frame_rate_spinBox.setValue(f_rate)

    def save_workflow(self):

        format_width = self.ui.f_width_lineEdit.text()
        format_height = self.ui.f_height_lineEdit.text()
        format = [format_width, format_height]

        frame_rate = self.ui.frame_rate_spinBox.value()

        project_prefs.set_frame_rate(frame_rate)
        project_prefs.set_format(format)

        logger.info("Preferences saved !")
        self.hide()