# coding: utf8

# Import PyQt6 libraries
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QFileDialog

from wizard.tools import utility as utils
utils.init_wizard_env()

from gui.chat_house import Ui_Form
from gui import build
from wizard.tools import log
from wizard.vars import defaults
from wizard.chat_test import client
from wizard.prefs.main import prefs
from wizard.prefs.stats import stats
import chat_room

import sys
import os

# Init main logger
logger = log.pipe_log(__name__)

prefs = prefs()

class Main(QtWidgets.QWidget):

    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.client_thread = None
        self.start_client()

        self.contexts_dic = dict()
        self.add_room()
        self.add_room("admin")
        self.add_room("lbrunel")

    def start_client(self):
        if self.client_thread:
            self.stop_client()

        self.client_thread = client.chat_client()
        self.client_thread.start()
        self.client_thread.msg_recv.connect(self.msg_recv)

    def stop_client(self):
        if self.client_thread:
            self.client_thread.stop()

    def msg_recv(self, msg_dic):
        print(msg_dic)

    def add_room(self, context=defaults._chat_general_):
        if context not in self.contexts_dic.keys():
            index = self.add_room_widget(context)
            self.contexts_dic[context] = index
            self.add_room_button(context, index)

    def add_room_widget(self, context):
        room = chat_room.Main(context)
        index = self.ui.chat_house_stackedWidget.addWidget(room)
        return index

    def add_room_button(self, context, index):
        button = QtWidgets.QPushButton()
        button.setMaximumSize(QtCore.QSize(50, 50))
        button.setMinimumSize(QtCore.QSize(50, 50))
        button.setStyleSheet("border-radius:25px;")
        button.setIconSize(QtCore.QSize(45,45))
        if context != defaults._chat_general_:
            self.round_image(button,  stats(context).get_avatar())
        else:
            self.round_image(button,  defaults._wizard_icon_)
        self.ui.chat_house_rooms_frame_layout.addWidget(button)
        button.clicked.connect(lambda: self.ui.chat_house_stackedWidget.setCurrentIndex(index))

    def round_image(self, label, image):
        label.Antialiasing = True
        label.radius = 25
        label.target = QtGui.QPixmap(label.size())
        label.target.fill(QtCore.Qt.transparent)
        p = QtGui.QPixmap(image).scaled(
            50, 50, QtCore.Qt.KeepAspectRatioByExpanding, QtCore.Qt.SmoothTransformation)
        painter = QtGui.QPainter(label.target)
        if label.Antialiasing:
            painter.setRenderHint(QtGui.QPainter.Antialiasing, True)
            painter.setRenderHint(QtGui.QPainter.HighQualityAntialiasing, True)
            painter.setRenderHint(QtGui.QPainter.SmoothPixmapTransform, True)
        path = QtGui.QPainterPath()
        path.addRoundedRect(
            0, 0, label.width(), label.height(), label.radius, label.radius)
        painter.setClipPath(path)
        painter.drawPixmap(0, 0, p)
        icon = QtGui.QIcon()
        icon.addPixmap(label.target)
        label.setIcon(icon)


if __name__ == '__main__':
    build.launch_chat(Main)
