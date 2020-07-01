from PyQt5 import QtWidgets, QtCore, QtGui

from gui.new_version_dialog import Ui_Dialog
from wizard.vars import defaults
from wizard.prefs.main import prefs
from wizard.tools import log

import webbrowser

import os

logger = log.pipe_log()

prefs = prefs()

class Main(QtWidgets.QDialog):

    def __init__(self, version):
        super(Main, self).__init__()
        # Build the ui from ui converted file
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.version = version
        self.connect_functions()

    def connect_functions(self):
        self.ui.download_pushButton.clicked.connect(self.open_link)
        self.ui.later_pushButton.clicked.connect(self.show_later)
        self.ui.never_pushButton.clicked.connect(self.never_show)
        self.ui.version_label.setText(self.version)

    def open_link(self):
        os.startfile('updater.exe')
        self.accept()

    def show_later(self):
        prefs.set_show_new_version(1)
        self.reject()

    def never_show(self):
        prefs.set_show_new_version(0)
        self.reject()
