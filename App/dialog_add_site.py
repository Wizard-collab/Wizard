from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import pyqtSignal

from gui.site_selection_dialog import Ui_Dialog

from wizard.vars import defaults

import os

class Main(QtWidgets.QDialog):

    def __init__(self):
        super(Main, self).__init__()
        # Build the ui from ui converted file
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.connect_functions()
        self.site_path = None

    def connect_functions(self):

        self.ui.accept_pushButton.clicked.connect(self.add_site)
        self.ui.site_image_label.setPixmap(QtGui.QPixmap(defaults._site_icon_).scaled(60, 60, QtCore.Qt.KeepAspectRatio,
                                                                              QtCore.Qt.SmoothTransformation))
        self.ui.site_lineEdit.textChanged.connect(self.update_site_path)

    def update_site_path(self, text):

        if text != '':
            path = os.path.join(text, 'wizard_site')
            self.ui.site_destination_label.setText("Destination folder : {}".format(path))
            if os.path.isdir(text):
                self.ui.site_destination_label.setStyleSheet("color:green")
            else:
                self.ui.site_destination_label.setStyleSheet("color:red")
        else:
            self.ui.site_destination_label.setStyleSheet("color:white")
            self.ui.site_destination_label.setText("Destination folder : ")

    def add_site(self):

        site_path = self.ui.site_lineEdit.text()
        if site_path and site_path != '':
            self.site_path = site_path
            self.accept()