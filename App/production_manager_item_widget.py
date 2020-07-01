# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication
from gui.production_manager_item import Ui_Form
from gui import build
from wizard.tools import log
from wizard.vars import defaults
from wizard.prefs.main import prefs
from wizard.prefs import project as project_prefs
import project_widget
import sys
from wizard.prefs import stats_maker
from wizard.prefs.stats import stats
import production_manager_stage_item_widget

logger = log.pipe_log()

class Main(QtWidgets.QWidget):

    def __init__(self, asset_dic, asset_domain, asset_category, asset_name, asset_variant, count):
        super(Main, self).__init__()
        # Build the ui from ui converted file
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.asset_dic = asset_dic
        self.asset_domain = asset_domain
        self.asset_category = asset_category
        self.asset_name = asset_name
        self.asset_variant = asset_variant
        self.count = count
        self.fill_ui()

    def fill_ui(self):

        if self.count:
            self.ui.pm_asset_frame.setStyleSheet('#pm_asset_frame{background-color:#1b1b28;}')


        self.ui.pm_asset_name_label.setText(f'{self.asset_name}-{self.asset_variant}')

        for stage in defaults._assets_stages_:
            self.production_manager_stage_item_widget = production_manager_stage_item_widget.Main(self.asset_domain\
                                                                                                , self.asset_category\
                                                                                                , self.asset_name\
                                                                                                , self.asset_variant\
                                                                                                , stage\
                                                                                                , self.asset_dic)
            self.ui.pm_item_stages_layout.addWidget(self.production_manager_stage_item_widget)
            if self.count:
                self.production_manager_stage_item_widget.ui.pm_stage_item_main_frame.setStyleSheet('#pm_stage_item_main_frame{background-color:#1b1b28;}')