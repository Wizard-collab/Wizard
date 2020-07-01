from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication
from gui.versions_manager_widget import Ui_Form
from gui import build
from wizard.vars import defaults
from wizard.tools import log
from wizard.prefs.main import prefs
import version_widget
import copy
import shutil

logger = log.pipe_log()

prefs = prefs()

class Main(QtWidgets.QWidget):

    open_signal = pyqtSignal(str)
    refresh_signal = pyqtSignal(str)

    def __init__(self):
        super(Main, self).__init__()
        # Build the ui from ui converted file
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.asset = None

        self.full = 0
        self.sanity = 1
        self.widgets_list = []
        self.number = 3
        self.step = 3
        self.count = 1
        self.connect_functions()

        self.ui.sanity_exports_pushButton.setIcon(QtGui.QIcon(defaults._export_list_icon_gray_))
        self.ui.show_all_exports_pushButton.setIcon(QtGui.QIcon(defaults._sd_icon_))
        self.ui.add_empty_file_pushButton.setIcon(QtGui.QIcon(defaults._add_empty_file_icon_))

    def closeEvent(self, event):
        event.ignore()
        self.hide()

    def add_number(self):
        self.number += 3
        self.update_all()

    def remove_number(self):
        self.number -= 3
        self.update_all()

    def refresh_all(self, asset):
        self.asset = asset
        self.versions_list = []
        if self.asset.variant:
            self.versions_list = prefs.asset(self.asset).software.versions

        self.update_all()

    def add_version(self):

        self.asset.version = prefs.asset(self.asset).software.get_new_version()
        shutil.copyfile(defaults._init_file__dic_[self.asset.software],
                                    self.asset.file)
        prefs.asset(self.asset).software.new_version(self.asset.version)
        self.refresh_signal.emit('')

    def update_all(self):
        self.widgets_list=[]

        self.get_params()
        self.clear_all()

        versions_list = []
        if self.versions_list and self.versions_list != []:

            if not self.full:
                versions_list = self.versions_list[-self.number:]
            else:
                versions_list = self.versions_list

        self.ui.versions_number_label.setText('( {}/{} )'.format(len(versions_list), len(self.versions_list)))
        
        for version in versions_list:
            modifiable_asset = copy.deepcopy(self.asset)
            modifiable_asset.version = version
            self.version_widget = version_widget.Main(modifiable_asset, self.sanity, self.count)
            self.version_widget.open_signal.connect(self.open_signal.emit)
            self.ui.versions_manager_mainLayout.addWidget(self.version_widget)
            self.count = 1-self.count
            self.widgets_list.append(self.version_widget)

    def clear_all(self):
        for i in reversed(range(self.ui.versions_manager_mainLayout.count())):
            widget = self.ui.versions_manager_mainLayout.itemAt(i).widget()
            if widget:
                widget.setParent(None)

    def connect_functions(self):
        self.ui.sanity_exports_pushButton.clicked.connect(self.update_sanity)
        self.ui.show_all_exports_pushButton.clicked.connect(self.update_all)
        self.ui.show_more_pushButton.clicked.connect(self.add_number)
        self.ui.show_less_pushButton.clicked.connect(self.remove_number)
        self.ui.add_empty_file_pushButton.clicked.connect(self.add_version)

    def update_sanity(self):
        self.get_params()
        for widget in self.widgets_list:
            widget.update_sanity(self.sanity)

    def get_params(self):
        if self.ui.show_all_exports_pushButton.isChecked():
            self.full = 1
        else:
            self.full = 0
        if self.ui.sanity_exports_pushButton.isChecked():
            self.sanity = 1
        else:
            self.sanity = 0
