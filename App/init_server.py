import fix_qt

from PyQt5 import QtWidgets, QtGui
import sys
import os

import wizard.vars.defaults as defaults

from wizard.prefs.user import user
from wizard.prefs.site import site

site_path = os.path.join(os.environ[defaults._wizard_site_], defaults._site_)
stats_path = os.path.join(os.environ[defaults._wizard_site_], defaults._stats_)

os.environ[defaults._site_var_] = site_path
os.environ[defaults._stats_var_] = stats_path

import gui.build as build
import ui_main_server


class main_server():
    def __init__(self):
        self.user = user()
        self.site = site()

        self.app = QtWidgets.QApplication(sys.argv)
        self.app.setWindowIcon(QtGui.QIcon(defaults._server_ico_black_))

        self.ui_main_server = ui_main_server.Main()
        build.launch_stray_server(self.ui_main_server, self.app)

if __name__ == '__main__':
    main_app = main_server()
