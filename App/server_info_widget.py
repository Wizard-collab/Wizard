from PyQt5 import QtWidgets, QtCore, QtGui

from gui.server_info_widget import Ui_Form
from wizard.vars import defaults


class Main(QtWidgets.QWidget):

    def __init__(self):
        super(Main, self).__init__()
        # Build the ui from ui converted file
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.add_logos()

    def add_logos(self):
        self.ui.welcome_info_image_label.setPixmap(
            QtGui.QPixmap(defaults._welcome_server_image_).scaled(45, 45, QtCore.Qt.KeepAspectRatio,
                                                                  QtCore.Qt.SmoothTransformation))
