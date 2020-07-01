from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication
import os
import time
from gui.loading import Ui_loading_Form
from wizard.vars import defaults
import random

class Main(QtWidgets.QWidget):

    def __init__(self):
        super(Main, self).__init__()
        # Build the ui from ui converted file
        self.ui = Ui_loading_Form()
        self.ui.setupUi(self)
        self.conform_ui()
        self.go = None

        self.shadow = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(8)
        self.shadow.setColor(QtGui.QColor(0, 0, 0, 180))
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.setGraphicsEffect(self.shadow)

    def conform_ui(self):
        icon = defaults._wizard_load_image_
        self.ui.logo_label.setPixmap(
            QtGui.QPixmap(icon).scaled(500, 500, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
        version = defaults._wizard_version_
        self.ui.wizard_version_label.setText('Version : {} 2020'.format(version))

    def start_gif(self):
        self.logo_gif = QtGui.QMovie(defaults._wizard_load_image_)
        self.ui.logo_label.setMovie(self.logo_gif)
        self.logo_gif.setScaledSize(QtCore.QSize(500, 500))
        self.logo_gif.setSpeed(150)
        self.logo_gif.start()
        self.logo_gif.finished.connect(self.stop_anim)

    def stop_anim(self):
        self.go = 1

