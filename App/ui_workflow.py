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

logger = log.pipe_log()

class Main(QtWidgets.QWidget):

    def __init__(self):
        super(Main, self).__init__()
        # Build the ui from ui converted file
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.fill_combos()
        project_prefs.init_extension_dic()
        project_prefs.init_setdress_workflow()
        self.fill_project_settings()
        self.read_settings()
        self.ui.save_workflow_pushButton.clicked.connect(self.save_workflow)

    def fill_combos(self):

        for software in defaults._stage_softs_dic_[defaults._rig_]:
            extension = defaults._workflow_ext_dic_custom_[defaults._rig_][software]
            self.ui.rig_ex_comboBox.addItem(f'{software} ( .{extension} )')
        for software in defaults._stage_softs_dic_[defaults._shading_]:
            extension = defaults._workflow_ext_dic_custom_[defaults._shading_][software]
            self.ui.shading_ex_comboBox.addItem(f'{software} ( .{extension} )')
        for extension in defaults._textures_ext_list_:
            self.ui.textures_ex_comboBox.addItem(f'( .{extension} )')
        for software in defaults._stage_softs_dic_[defaults._hair_]:
            extension = defaults._workflow_ext_dic_custom_[defaults._hair_][software]
            self.ui.hair_ex_comboBox.addItem(f'{software} ( .{extension} )')

    def fill_project_settings(self):
        format = project_prefs.get_format()
        format_width = format[0]
        format_height = format[1]
        self.ui.f_width_lineEdit.setText(str(format_width))
        self.ui.f_height_lineEdit.setText(str(format_height))

        f_rate = project_prefs.get_frame_rate()
        self.ui.frame_rate_spinBox.setValue(f_rate)

    def read_settings(self):

        extension_dic = project_prefs.get_extension_dic()

        rig_ext = extension_dic[defaults._rig_]
        shading_ext = extension_dic[defaults._shading_]
        textures_ext = extension_dic[defaults._texturing_]
        hair_ext = extension_dic[defaults._hair_]
        setdress_workflow = project_prefs.get_setdress_workflow()

        extensions_list = []
        for software in defaults._stage_softs_dic_[defaults._rig_]:
            extensions_list.append(defaults._workflow_ext_dic_custom_[defaults._rig_][software])
        index = extensions_list.index(rig_ext)
        self.ui.rig_ex_comboBox.setCurrentIndex(index)

        extensions_list = []
        for software in defaults._stage_softs_dic_[defaults._shading_]:
            extensions_list.append(defaults._workflow_ext_dic_custom_[defaults._shading_][software])
        index = extensions_list.index(shading_ext)
        self.ui.shading_ex_comboBox.setCurrentIndex(index)

        index = defaults._textures_ext_list_.index(textures_ext)
        self.ui.textures_ex_comboBox.setCurrentIndex(index)
        
        extensions_list = []
        for software in defaults._stage_softs_dic_[defaults._hair_]:
            extensions_list.append(defaults._workflow_ext_dic_custom_[defaults._hair_][software])
        index = extensions_list.index(hair_ext)
        self.ui.hair_ex_comboBox.setCurrentIndex(index)

        if setdress_workflow == defaults._abc_workflow_:
            index = 0
        else:
            index = 1
        self.ui.setdress_workflow_comboBox.setCurrentIndex(index)

    def save_workflow(self):

        rig_ext = self.ui.rig_ex_comboBox.currentText().split('.')[-1].split(' ')[0]
        shading_ext = self.ui.shading_ex_comboBox.currentText().split('.')[-1].split(' ')[0]
        textures_ext = self.ui.textures_ex_comboBox.currentText().split('.')[-1].split(' ')[0]
        hair_ext = self.ui.hair_ex_comboBox.currentText().split('.')[-1].split(' ')[0]
        setdress_workflow = self.ui.setdress_workflow_comboBox.currentText()

        extension_dic = project_prefs.get_extension_dic()
        extension_dic[defaults._rig_] = rig_ext
        extension_dic[defaults._shading_] = shading_ext
        extension_dic[defaults._texturing_] = textures_ext
        extension_dic[defaults._hair_] = hair_ext
        project_prefs.set_extension_dic(extension_dic)
        project_prefs.set_setdress_workflow(setdress_workflow)

        format_width = self.ui.f_width_lineEdit.text()
        format_height = self.ui.f_height_lineEdit.text()
        format = [format_width, format_height]

        frame_rate = self.ui.frame_rate_spinBox.value()

        project_prefs.set_frame_rate(frame_rate)
        project_prefs.set_format(format)

        logger.info("Preferences saved !")
        self.hide()