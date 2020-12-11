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
from wizard.prefs.chat_archives import chat_archives
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

        self.chat_archives = chat_archives()

        self.client_thread = None
        self.start_client()

        self.contexts_dic = dict()
        self.add_room()
        self.add_project_rooms()
        self.add_users_rooms()

        self.select_room()

        self.add_messages_archives()

        self.connect_functions()

    def add_project_rooms(self):
        rooms = self.chat_archives.get_rooms()
        if rooms:
            for room in rooms:
                self.add_room(room)

    def add_users_rooms(self):
        for user in prefs.project_users:
            if user != prefs.user:
                self.add_room(user)

    def add_messages_archives(self):
        messages_archives = self.chat_archives.get_messages()
        if messages_archives:
            for message_key in messages_archives.keys():
                self.msg_recv(messages_archives[message_key])

    def connect_functions(self):
        self.ui.create_room_pushButton.clicked.connect(self.show_create_room_widget)

    def create_room(self, room_name):
        if self.chat_archives.add_room(room_name):
            self.add_room(room_name)

    def show_create_room_widget(self):
        self.create_room_widget = create_room_widget()
        self.create_room_widget.new_room.connect(self.create_room)
        build.launch_position_frameless_ontop_as_child(self.create_room_widget)

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
        message_dic = self.client_thread.send_message(message_tuple[0], destination = message_tuple[-1])
        if message_dic:
            self.chat_archives.add_message(message_dic)

    def show_room(self, context):
        self.unselect_all()
        self.ui.chat_house_stackedWidget.setCurrentIndex(self.contexts_dic[context][0])

    def unselect_all(self):
        for context in  self.contexts_dic.keys():
            self.contexts_dic[context][2].unselect()

    def add_room_button(self, context, index):
        button = room_button.Main(context)
        button.select_signal.connect(self.show_room)
        if context in prefs.site.users:
            self.ui.chat_house_users_frame_layout.addWidget(button)
        else:
            self.ui.chat_house_rooms_frame_layout.addWidget(button)
        return button

class create_room_widget(QtWidgets.QWidget):
    
    new_room = pyqtSignal(str)

    def __init__(self):
        super(create_room_widget, self).__init__()

        self.main_layout = QtWidgets.QVBoxLayout()
        #self.main_layout.setContentsMargins(0,0,0,0)
        self.main_frame = QtWidgets.QFrame()
        self.main_frame.setObjectName('create_room_main_frame')
        self.frame_layout = QtWidgets.QVBoxLayout()
        self.frame_layout.setSpacing(1)
        self.main_frame.setLayout(self.frame_layout)
        self.setLayout(self.main_layout)

        self.title = QtWidgets.QLabel("New room")
        self.frame_layout.addWidget(self.title)
        self.line_edit = QtWidgets.QLineEdit()
        self.frame_layout.addWidget(self.line_edit)
        self.create_button = QtWidgets.QPushButton("Create")
        self.frame_layout.addWidget(self.create_button)
        self.create_button.clicked.connect(self.create_room)

        self.main_layout.addWidget(self.main_frame)

        #self.setMaximumSize(QtCore.QSize(300,150))
        self.setMinimumSize(QtCore.QSize(200,10))
        self.resize(self.minimumSizeHint())
        self.main_frame.setStyleSheet("#create_room_main_frame{border-radius:5px;}")

        self.enter_key = QtWidgets.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Return), self)
        self.enter_key.activated.connect(self.create_room)

    def create_room(self):
        room_name = self.line_edit.text()
        if room_name != '':
            self.new_room.emit(room_name)
            self.hide()
        else:
            logger.warning("Please enter a room name")

    def leaveEvent(self, e):
        self.hide()


if __name__ == '__main__':
    build.launch_chat(Main)
