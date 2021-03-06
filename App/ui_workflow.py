# coding: utf8

# Import PyQt5 libraries
from PyQt5 import QtWidgets, QtCore, QtGui

# Import wizard gui libraries
from gui.workflow import Ui_Form
from gui import build

# Import wizard core libraries
from wizard.tools import log
from wizard.vars import defaults
from wizard.prefs.main import prefs
from wizard.prefs import project as project_prefs

# Import wizard widgets
import project_widget

# Import python base libraries
import sys

# Init main logger
logger = log.pipe_log(__name__)

class Main(QtWidgets.QWidget):

    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.fill_project_settings()
        self.ui.save_workflow_pushButton.clicked.connect(self.save_workflow)

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

    def save_workflow(self):
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