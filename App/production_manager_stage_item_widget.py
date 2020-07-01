# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtCore, QtGui
from gui.production_manager_stage_item import Ui_Form
from gui import build
from wizard.tools import log
from wizard.vars import defaults
from wizard.prefs.main import prefs
from wizard.prefs import project as project_prefs
import project_widget
import sys
import options_widget
from wizard.prefs import stats_maker
from wizard.prefs.stats import stats
from wizard.asset import checker
import traceback
from wizard.prefs.production import production

logger = log.pipe_log()

class Main(QtWidgets.QWidget):

    def __init__(self, domain, category, name, variant, stage, asset_dic):
        super(Main, self).__init__()
        # Build the ui from ui converted file
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.asset_dic = asset_dic
        self.domain = domain
        self.category = category
        self.name = name
        self.variant = variant
        self.stage = stage
        self.neutral_color = '#pm_stage_item_state_pushButton{background-color:maincolor;}\n'
        self.neutral_color += '#pm_stage_item_state_pushButton::hover{background-color:hovercolor;}'
        self.ui.pm_stage_item_state_pushButton.setIcon(QtGui.QIcon(defaults._down_arrow_))
        self.ui.pm_stage_item_state_pushButton.clicked.connect(self.state_options)
        self.fill_ui()

    def fill_ui(self):

        if self.stage in self.asset_dic.keys():

            user = self.asset_dic[self.stage][defaults._assigned_user_]
            if not user or user == 'null':
                self.round_image(self.ui.pm_stage_item_user_pushButton, defaults._prod_manager_user_image_)
            else:
                user_image = stats(user).get_avatar()
                self.round_image(self.ui.pm_stage_item_user_pushButton, user_image)

            state = self.asset_dic[self.stage][defaults._asset_state_]

            if state == defaults._wip_:
                self.set_wip(0)
            elif state == defaults._error_:
                self.set_error(0)
            elif state == defaults._todo_:
                self.set_todo(0)
            elif state == defaults._done_:
                self.set_done(0)
            elif state == defaults._ignore_:
                self.set_ignore(1)

        else:
            self.set_ignore(0)
            self.round_image(self.ui.pm_stage_item_user_pushButton, defaults._prod_manager_user_image_)

    def set_todo(self, modify = 1):
        try:
            self.ui.pm_stage_item_state_pushButton.setStyleSheet(self.neutral_color.replace('maincolor', '#1287a8').replace('hovercolor', '#149dc4'))
            self.ui.pm_stage_item_state_pushButton.setText(defaults._todo_)
            if modify:
                self.change_state(defaults._todo_)
        except:
            logger.critical(str(traceback.format_exc()))

    def set_ignore(self, modify = 1):
        try:
            self.ui.pm_stage_item_state_pushButton.setStyleSheet(self.neutral_color.replace('maincolor', '#262626').replace('hovercolor', '#404040'))
            self.ui.pm_stage_item_state_pushButton.setText(defaults._ignore_)
            if modify:
                self.change_state(defaults._ignore_)
            else:
                self.ui.pm_stage_item_state_pushButton.setIcon(QtGui.QIcon(''))
                self.ui.pm_stage_item_state_pushButton.setEnabled(0)
        except:
            logger.critical(str(traceback.format_exc()))

    def set_wip(self, modify = 1):
        try:
            self.ui.pm_stage_item_state_pushButton.setStyleSheet(self.neutral_color.replace('maincolor', '#f26d21').replace('hovercolor', '#ff7f36'))
            self.ui.pm_stage_item_state_pushButton.setText(defaults._wip_)
            if modify:
                self.change_state(defaults._wip_)
        except:
            logger.critical(str(traceback.format_exc()))

    def set_error(self, modify = 1):
        try:
            self.ui.pm_stage_item_state_pushButton.setStyleSheet(self.neutral_color.replace('maincolor', '#c02f1d').replace('hovercolor', '#db4330'))
            self.ui.pm_stage_item_state_pushButton.setText(defaults._error_)
            if modify:
                self.change_state(defaults._error_)
        except:
            logger.critical(str(traceback.format_exc()))

    def set_done(self, modify = 1):
        try:
            self.ui.pm_stage_item_state_pushButton.setStyleSheet(self.neutral_color.replace('maincolor', '#93a661').replace('hovercolor', '#abbf75'))
            self.ui.pm_stage_item_state_pushButton.setText(defaults._done_)
            if modify:
                self.change_state(defaults._done_)
        except:
            logger.critical(str(traceback.format_exc()))    

    def change_state(self, state):
        production().change_state(self.domain, self.category, self.name, self.variant, self.stage, state)

    def round_image(self, label, image):
        label.Antialiasing = True
        label.radius = 30

        label.target = QtGui.QPixmap(label.size())
        label.target.fill(QtCore.Qt.transparent)

        p = QtGui.QPixmap(image).scaled(
            38, 38, QtCore.Qt.KeepAspectRatioByExpanding, QtCore.Qt.SmoothTransformation)

        painter = QtGui.QPainter(label.target)
        if label.Antialiasing:
            painter.setRenderHint(QtGui.QPainter.Antialiasing, True)
            painter.setRenderHint(QtGui.QPainter.HighQualityAntialiasing, True)
            painter.setRenderHint(QtGui.QPainter.SmoothPixmapTransform, True)

        path = QtGui.QPainterPath()
        path.addRoundedRect(
            0, 0, label.width(), label.height(), label.radius, label.radius)

        painter.setClipPath(path)
        painter.drawPixmap(0, 0, p)
        icon = QtGui.QIcon()
        icon.addPixmap(label.target)
        label.setIcon(icon)

    def state_options(self):
        self.options_widget = options_widget.Main()
        self.options_widget.add_item('Set ignore', lambda : self.set_ignore(1))
        self.options_widget.add_item('Set todo', lambda : self.set_todo(1))
        self.options_widget.add_item('Set wip', lambda : self.set_wip(1))
        self.options_widget.add_item('Set done', lambda : self.set_done(1))
        self.options_widget.add_item('Set error', lambda : self.set_error(1))
        build.launch_options(self.options_widget)
