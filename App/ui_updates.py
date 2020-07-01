from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QUrl, QThread
from PyQt5.QtWidgets import QApplication
from gui.updates import Ui_Form
from wizard.vars import defaults
import create_user_widget
import create_project_widget
import server_info_widget
from wizard.prefs.main import prefs
from wizard.chat.client import test_conn_once
import update_widget
from wizard.tools import log
import os

logger = log.pipe_log()

prefs = prefs()

class Main(QtWidgets.QWidget):

    def __init__(self):
        super(Main, self).__init__()
        # Build the ui from ui converted file
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.shadow = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(8)
        self.shadow.setColor(QtGui.QColor(0, 0, 0, 180))
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.setGraphicsEffect(self.shadow)

        self.add_widgets()

        self.ui.show_startup_checkBox.stateChanged.connect(self.show_updates)

    def show_updates(self):
        prefs.set_show_updates(self.ui.show_startup_checkBox.isChecked())

    def add_widgets(self):

        updates_list = os.listdir(os.path.abspath(defaults._updates_folder_))

        for folder in updates_list:
            if folder != defaults._update_version_file_:
                self.update_widget = update_widget.Main(folder, os.path.join(defaults._updates_folder_, folder))
                self.ui.widgets_verticalLayout.addWidget(self.update_widget)


