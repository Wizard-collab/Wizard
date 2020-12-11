# coding: utf8

# Import PyQt6 libraries
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QFileDialog

from wizard.tools import utility as utils
utils.init_wizard_env()

from gui.chat_room import Ui_Form
from gui import build
from wizard.tools import log
from wizard.vars import defaults
from wizard.chat_test import client
import chat_message_widget
from wizard.prefs.main import prefs

import sys
import os

# Init main logger
logger = log.pipe_log(__name__)

prefs = prefs()

class Main(QtWidgets.QWidget):

    message_signal = pyqtSignal(list)
    message_notif = pyqtSignal(str)

    def __init__(self, context = defaults._chat_general_):
        super(Main, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.context = context
        self.connected_functions()

        self.previous_user = None
        self.previous_date = None
        self.file = None

        self.update_file()


    def connected_functions(self):
        self.ui.chat_room_add_file_pushButton.setIcon(QtGui.QIcon(defaults._attachment_icon_))
        self.ui.chat_room_add_file_pushButton.clicked.connect(self.attach_file)
        self.ui.chat_room_remove_file_pushButton.setIcon(QtGui.QIcon(defaults._kill_process_icon_))
        self.ui.chat_room_remove_file_pushButton.clicked.connect(self.remove_file)
        self.ui.chat_send_pushButton.clicked.connect(self.send_msg)
        self.ui.chat_emoji_pushButton.clicked.connect(self.show_emoji_keyboard)
        self.send_sc = QtWidgets.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Return), self)
        self.send_sc.activated.connect(self.send_msg)
        area_scroll_bar = self.ui.scrollArea.verticalScrollBar()
        area_scroll_bar.rangeChanged.connect(lambda: area_scroll_bar.setValue(area_scroll_bar.maximum()))
        self.ui.chat_room_context_label.setText(self.context)

    def msg_recv(self, msg_dic):
        receive = 0
        if msg_dic[defaults._chat_user_] == prefs.user and msg_dic[defaults._chat_destination_] == self.context:
            receive = 1
        if msg_dic[defaults._chat_user_] == self.context and msg_dic[defaults._chat_destination_] == prefs.user:
            receive = 1
        if msg_dic[defaults._chat_destination_] == self.context:
            receive = 1
        if receive:
            need_user_widget = 0
            need_date_widget = 0
            if self.previous_date:
                difference = float(msg_dic[defaults._chat_date_]) - float(self.previous_date)
                if difference >= (5*60):
                    need_date_widget = 1
                    need_user_widget = 1
            else:
                need_date_widget = 1
            if self.previous_user != msg_dic[defaults._chat_user_]:
                need_user_widget = 1
            if need_date_widget:
                date_widget = chat_message_widget.date_widget(msg_dic[defaults._chat_date_])
                self.ui.chat_messages_layout.addWidget(date_widget)
            if need_user_widget and msg_dic[defaults._chat_user_] != prefs.user:
                user_widget = chat_message_widget.user_widget(msg_dic[defaults._chat_user_])
                self.ui.chat_messages_layout.addWidget(user_widget)
            new_msg_widget = chat_message_widget.Main(msg_dic)
            self.ui.chat_messages_layout.addWidget(new_msg_widget)
            self.previous_user = msg_dic[defaults._chat_user_]
            self.previous_date = msg_dic[defaults._chat_date_]
            if msg_dic[defaults._chat_user_] != prefs.user:
                self.message_notif.emit(self.context)

    def attach_file(self):
        options = QtWidgets.QFileDialog.Options()
        file, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Choose a file", "",
                                                  "All Files (*);", options=options)
        if file:
            self.file = file
            self.update_file()

    def remove_file(self):
        self.file = None
        self.update_file()

    def update_file(self):
        if not self.file:
            self.ui.chat_room_files_frame.setVisible(0)
        else:
            self.ui.chat_room_file_name_label.setText(os.path.basename(self.file))
            self.ui.chat_room_files_frame.setVisible(1)

    def send_msg(self):
        message = self.ui.chat_message_lineEdit.text()
        self.message_signal.emit([message, self.file, self.context])
        self.ui.chat_message_lineEdit.clear()
        self.remove_file()

    def show_emoji_keyboard(self):
        self.emoji_keyboard = emoji_keyboard()
        self.emoji_keyboard.emoji_signal.connect(self.add_emoji)
        build.launch_running(self.emoji_keyboard)

    def add_emoji(self, emoji):
        text = self.ui.chat_message_lineEdit.text() + emoji
        self.ui.chat_message_lineEdit.setText(text)

class emoji_keyboard(QtWidgets.QWidget):

    emoji_signal = pyqtSignal(str)

    def __init__(self):
        super(emoji_keyboard, self).__init__()

        self.widget_layout = QtWidgets.QVBoxLayout()
        self.widget_layout.setContentsMargins(0,0,0,0)
        self.setLayout(self.widget_layout)
        self.main_frame = QtWidgets.QFrame()
        self.widget_layout.addWidget(self.main_frame)
        self.frame_layout = QtWidgets.QVBoxLayout()
        self.main_frame.setLayout(self.frame_layout)

        self.list_widget = QtWidgets.QListWidget()
        self.frame_layout.addWidget(self.list_widget)
        self.list_widget.setMovement(QtWidgets.QListView.Static)
        self.list_widget.setResizeMode(QtWidgets.QListView.Adjust)
        self.list_widget.setViewMode(QtWidgets.QListView.IconMode)
        self.list_widget.setStyleSheet("background:transparent;")
        self.list_widget.itemClicked.connect(self.add_emoji)
        self.fill_ui()

        self.font = QtGui.QFont('Arial', 15)
        self.list_widget.setFont(self.font)

        self.setMinimumSize(QtCore.QSize(300, 300))
        self.setMaximumSize(QtCore.QSize(300, 300))

    def add_emoji(self, item):
        self.emoji_signal.emit(item.text())

    def fill_ui(self):
        for emoji in defaults._emojis_list_:
            item = QtWidgets.QListWidgetItem(emoji)
            item.setSizeHint(QtCore.QSize(50, 50))
            self.list_widget.addItem(item)

    def move_ui(self):
        win_size = (self.frameSize().width(), self.frameSize().height())
        posx = QtGui.QCursor.pos().x() - 10
        posy = int(QtGui.QCursor.pos().y()) - win_size[1] + 10
        self.move(posx, posy)

    def leaveEvent(self, event):
        self.hide()

if __name__ == '__main__':
    build.launch_chat(Main)
