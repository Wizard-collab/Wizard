from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import pyqtSignal

from gui.create_site_widget import Ui_Form
import add_site_dialog

from gui import build
from wizard.vars import defaults
from wizard.prefs.main import prefs

prefs = prefs()

class Main(QtWidgets.QWidget):
    site_created = pyqtSignal(str)

    def __init__(self):
        super(Main, self).__init__()
        # Build the ui from ui converted file
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.add_logos()
        self.connect_functions()

    def add_logos(self):
        self.ui.welcome_info_image_label.setPixmap(
            QtGui.QPixmap(defaults._welcom_user_image_).scaled(45, 45, QtCore.Qt.KeepAspectRatio,
                                                               QtCore.Qt.SmoothTransformation))
    def connect_functions(self):
        self.ui.create_pushButton.clicked.connect(self.add_site)

    def add_site(self):
        self.add_site_dialog = add_site_dialog.Main()
        if build.launch_dialog_as_child(self.add_site_dialog):
            self.site_created.emit('')