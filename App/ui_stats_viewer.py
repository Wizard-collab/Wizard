# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtCore, QtGui
from gui.stats_viewer import Ui_Form
from gui import build
from wizard.tools import log
from wizard.vars import defaults
from wizard.prefs.main import prefs
from wizard.prefs import project as project_prefs
import project_widget
import sys
from wizard.prefs import stats_maker
from wizard.prefs.stats import stats

logger = log.pipe_log()


class Main(QtWidgets.QWidget):

    def __init__(self):
        super(Main, self).__init__()
        # Build the ui from ui converted file
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        if not stats().is_version_count():
            stats().reset_versions_count()
            stats_maker.rebuild_work_stats()
        
        self.setIcons()
        self.fill_ui()


    def fill_ui(self):
        stats = stats_maker.show_stats()
        self.ui.design_stats_progressBar.setValue(stats[0])
        self.ui.geo_stats_progressBar.setValue(stats[1])
        self.ui.rig_stats_progressBar.setValue(stats[2])
        self.ui.hair_stats_progressBar.setValue(stats[3])
        self.ui.texturing_stats_progressBar.setValue(stats[4])
        self.ui.shading_stats_progressBar.setValue(stats[5])

        saves_stats = stats_maker.get_save_stats()
        self.ui.design_work_label.setText(f'{saves_stats[0]} saves')
        self.ui.geo_work_label.setText(f'{saves_stats[1]} saves')
        self.ui.rig_work_label.setText(f'{saves_stats[2]} saves')
        self.ui.texturing_work_label.setText(f'{saves_stats[3]} saves')
        self.ui.hair_work_label.setText(f'{saves_stats[4]} saves')
        self.ui.shading_work_label.setText(f'{saves_stats[5]} saves')

        pub_stats = stats_maker.get_publish_stats()
        self.ui.design_publish_label.setText(f'{pub_stats[0]} publishes |')
        self.ui.geo_publish_label.setText(f'{pub_stats[1]} publishes |')
        self.ui.rig_publish_label.setText(f'{pub_stats[2]} publishes |')
        self.ui.texturing_publish_label.setText(f'{pub_stats[3]} publishes |')
        self.ui.hair_publish_label.setText(f'{pub_stats[4]} publishes |')
        self.ui.shading_publish_label.setText(f'{pub_stats[5]} publishes |')

    def setIcons(self):
        self.ui.design_image_label.setPixmap(QtGui.QPixmap(defaults._design_icon_large_).scaled(20, 20, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
        self.ui.geo_image_label.setPixmap(QtGui.QPixmap(defaults._geo_icon_large_).scaled(20, 20, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
        self.ui.rig_image_label.setPixmap(QtGui.QPixmap(defaults._rig_icon_large_).scaled(20, 20, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
        self.ui.texturing_image_label.setPixmap(QtGui.QPixmap(defaults._texturing_icon_large_).scaled(20, 20, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
        self.ui.hair_image_label.setPixmap(QtGui.QPixmap(defaults._hair_icon_large_).scaled(20, 20, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
        self.ui.shading_image_label.setPixmap(QtGui.QPixmap(defaults._shading_icon_large_).scaled(20, 20, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
        
        