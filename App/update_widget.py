from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QUrl, QThread
from PyQt5.QtWidgets import QApplication
from gui.update_widget import Ui_Form
from wizard.vars import defaults
import create_user_widget
import create_project_widget
import server_info_widget
from wizard.prefs.main import prefs
import os

class Main(QtWidgets.QWidget):

    def __init__(self, title, path):
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

        state_path = os.path.join(path, defaults._update_state_file_)
        with open(state_path, 'r') as f:
            state = f.read()

        self.ui.update_icon_label.setPixmap(QtGui.QPixmap(defaults._debug_icon_).scaled(24, 24, QtCore.Qt.KeepAspectRatio,
                                                                              QtCore.Qt.SmoothTransformation))

        self.ui.update_title_label.setText(title)
        text_path = os.path.join(path, defaults._update_text_file_)
        with open(text_path, 'r') as f:
            text = f.read()
        self.ui.update_text_label.setText(text)

        image_path = os.path.join(path, defaults._update_image_file_)
        if os.path.isfile(image_path):
            self.ui.update_image_label.setPixmap(QtGui.QPixmap(image_path))
        else:
            self.ui.update_image_label.setVisible(0)

