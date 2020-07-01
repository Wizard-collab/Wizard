# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication
from gui.production_manager import Ui_MainWindow
from gui import build
from wizard.tools import log
from wizard.vars import defaults
from wizard.prefs.main import prefs
from wizard.prefs import project as project_prefs
import project_widget
import sys
from wizard.prefs import stats_maker
from wizard.prefs.stats import stats
import gui.log_to_gui as log_to_gui
from wizard.project import main as project
import traceback
import production_manager_item_widget
from wizard.prefs.production import production

logger = log.pipe_log()

class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        # Build the ui from ui converted file
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.list_all_assets()

    def list_all_assets(self):
        production_dic = production().get_dic()
        count = 0
        for category in production_dic[defaults._assets_].keys():
            for name in production_dic[defaults._assets_][category].keys():
                for variant in production_dic[defaults._assets_][category][name].keys():
                    asset_dic = production_dic[defaults._assets_][category][name][variant]
                    self.production_manager_item_widget = production_manager_item_widget.Main(asset_dic, defaults._assets_, category, name, variant, count)
                    self.ui.assets_item_layout.addWidget(self.production_manager_item_widget)
                    if count == 0:
                        count += 1
                    else:
                        count = 0
