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
import room_button

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
        self.add_room("anim")

        self.select_room()

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
        for context in self.contexts_dic.keys():
            self.contexts_dic[context][1].msg_recv(msg_dic)

    def add_room(self, context=defaults._chat_general_):
        if context not in self.contexts_dic.keys():
            index, room = self.add_room_widget(context)
            button = self.add_room_button(context, index)
            self.contexts_dic[context] = [index, room, button]

    def select_room(self, context = defaults._chat_general_):
        self.contexts_dic[context][2].set_selected()

    def add_room_widget(self, context):
        room = chat_room.Main(context)
        room.message_signal.connect(self.send_msg)
        room.message_notif.connect(self.update_notifs)
        index = self.ui.chat_house_stackedWidget.addWidget(room)
        return (index, room)

    def update_notifs(self, context):
        self.contexts_dic[context][2].add_count()

    def send_msg(self, message_tuple):
        self.client_thread.send_message(message_tuple[0], destination = message_tuple[-1])

    def show_room(self, context):
        self.unselect_all()
        self.ui.chat_house_stackedWidget.setCurrentIndex(self.contexts_dic[context][0])

    def unselect_all(self):
        for context in  self.contexts_dic.keys():
            self.contexts_dic[context][2].unselect()

    def add_room_button(self, context, index):
        button = room_button.Main(context)
        button.select_signal.connect(self.show_room)
        self.ui.chat_house_rooms_frame_layout.addWidget(button)
        return button


if __name__ == '__main__':
    build.launch_chat(Main)
