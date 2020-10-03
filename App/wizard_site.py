 # external modules
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication

import ctypes, sys
import os

import dialog_add_site
from gui import build
from wizard.site import main as site
from wizard.vars import defaults
from wizard.tools import utility as utils


class wizard():
    def __init__(self):

        # Create the pyqt5 application
        self.app = QtWidgets.QApplication(sys.argv)

        # Add the default wizard icon
        self.app.setWindowIcon(QtGui.QIcon(defaults._wizard_ico_))

        if not site.is_site():
            self.dialog_add_site = dialog_add_site.Main()
            if build.launch_dialog_as_child(self.dialog_add_site):
                site_path = self.dialog_add_site.site_path

                site.modify_site(site_path)

                os.startfile('wizard.exe')
        else:
            import wizard_ui
            wizard_ui.Main_application()

if __name__ == '__main__':
    wizard = wizard()