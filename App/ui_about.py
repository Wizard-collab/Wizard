from PyQt5 import QtWidgets, QtGui, QtCore

from gui.about import Ui_Form
from wizard.vars import defaults
from wizard.tools import log

import os

logger = log.pipe_log()

class Main(QtWidgets.QWidget):

    def __init__(self):
        super(Main, self).__init__()
        # Build the ui from ui converted file
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.add_version()
        self.add_license()
        self.add_install_dir()
        self.add_contact()
        self.ui.about_wizard_icon_label.setPixmap(QtGui.QPixmap(defaults._wizard_icon_).scaled(40, 40, QtCore.Qt.KeepAspectRatio,
                                                                              QtCore.Qt.SmoothTransformation))

    def closeEvent(self, event):
        event.ignore()
        self.hide()

    def add_version(self):
        self.ui.about_release_lineEdit.setText( defaults._wizard_version_ )

    def add_license(self):
        with open(defaults._license_file_, 'r') as f:
            license = f.read()

        self.ui.about_license_textEdit.setText( license )

    def add_install_dir(self):
        install_dir = os.path.abspath('.')
        self.ui.about_install_dir_lineEdit.setText( install_dir )

    def add_contact(self):
        self.ui.about_contact_lineEdit.setText( defaults._contact_email_ )