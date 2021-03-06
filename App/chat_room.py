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
from wizard.prefs.stats import stats
from wizard.prefs.main import prefs

import sys
import os
import time
import yaml


# Init main logger
logger = log.pipe_log(__name__)

prefs = prefs()

class Main(QtWidgets.QWidget):

    message_signal = pyqtSignal(list)
    message_text = pyqtSignal(tuple)
    message_count = pyqtSignal(tuple)
    remove_message_signal = pyqtSignal(str)
    seen_signal = pyqtSignal(list)
    wizz = pyqtSignal(str)

    def __init__(self, context = defaults._chat_general_):
        super(Main, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.context = context
        self.connected_functions()

        self.previous_user = None
        self.previous_date = None
        self.file = None
        self.seen = 1
        self.quote = None
        self.new_msgs_widget = None
        self.emoji_list = []
        self.new_messages = 0

        self.users_views = dict()
        self.users = prefs.project_users
        self.room_messages_dic = dict()
        self.date_widgets = []

        self.thumb = "👍"

        self.get_seen_archive()
        self.update_file()
        self.remove_quote()

    def get_seen_archive(self):
        seen_dic = prefs.chat_seen
        if self.context in prefs.chat_seen.keys():
            self.seen = prefs.chat_seen[self.context]

    def update_user_view(self, user, message_key):
        if message_key:
            if user in self.users_views.keys():
                if self.users_views[user] in self.room_messages_dic.keys():
                    self.room_messages_dic[self.users_views[user]].remove_user_view(user)
            if message_key in self.room_messages_dic.keys():
                self.users_views[user] = message_key
                self.room_messages_dic[message_key].add_user_view(user)

    def connected_functions(self):
        self.ui.chat_room_add_file_pushButton.setIcon(QtGui.QIcon(defaults._attachment_icon_))
        self.ui.chat_room_thumb_pushButton.setIcon(QtGui.QIcon(defaults._thumb_icon_))
        self.ui.chat_send_pushButton.setIcon(QtGui.QIcon(defaults._send_message_icon_))
        self.ui.chat_emoji_pushButton.setIcon(QtGui.QIcon(defaults._emoji_icon_))
        self.ui.chat_message_lineEdit.textChanged.connect(self.analyse_text)
        self.ui.chat_room_thumb_pushButton.clicked.connect(self.send_thumb)
        self.ui.chat_room_close_quote_pushButton.clicked.connect(self.remove_quote)

        if self.context == defaults._chat_general_:
            image = defaults._chat_home_
        else:
            if self.context in prefs.site.users:
                image = stats(self.context).get_avatar()
            else:
                image = defaults._chat_no_image_

        self.rounded_pixmap_label(self.ui.chat_room_image_label, image)

        self.ui.chat_room_add_file_pushButton.clicked.connect(self.attach_file)
        self.ui.chat_room_remove_file_pushButton.setIcon(QtGui.QIcon(defaults._kill_process_icon_))
        self.ui.chat_room_close_quote_pushButton.setIcon(QtGui.QIcon(defaults._kill_process_icon_))

        self.ui.chat_room_remove_file_pushButton.clicked.connect(self.remove_file)
        self.ui.chat_send_pushButton.clicked.connect(self.send_msg)
        self.ui.chat_emoji_pushButton.clicked.connect(self.show_emoji_keyboard)
        self.send_sc = QtWidgets.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Return), self)
        self.send_sc.activated.connect(self.send_msg)
        area_scroll_bar = self.ui.scrollArea.verticalScrollBar()
        area_scroll_bar.rangeChanged.connect(lambda: area_scroll_bar.setValue(area_scroll_bar.maximum()))
        self.ui.chat_room_context_label.setText(self.context)

    def add_message_to_room_dic(self, message_key, message_widget):
        self.room_messages_dic[message_key] = message_widget

    def set_seen(self):
        self.remove_new_msgs_widget()

        if list(self.room_messages_dic.keys()) != []:
            self.seen = list(self.room_messages_dic.keys())[-1]
        else:
            self.seen = None
        if self.seen:
            self.seen_signal.emit([self.seen, self.context])

    def remove_new_msgs_widget(self):
        if self.new_msgs_widget and list(self.room_messages_dic.keys()) != []:
            if list(self.room_messages_dic.keys())[-1] == self.seen:
                self.new_msgs_widget.setParent(None)
                self.new_msgs_widget.deleteLater()
                self.new_msgs_widget = None
                self.new_messages = 0
                self.emit_new_messages()

    def emit_new_messages(self):
        self.message_count.emit((self.context, self.new_messages))

    def msg_recv(self, msg_dic, url_thread):

        if msg_dic[defaults._chat_type_] == defaults._chat_seen_:
            self.update_user_view(msg_dic[defaults._chat_user_], msg_dic[defaults._chat_key_])
        else:
            need_user_widget = 0
            need_date_widget = 0
            need_new_msgs_widget = 0
            if self.previous_date:
                difference = float(msg_dic[defaults._chat_date_]) - float(self.previous_date)
                if difference >= (5*60):
                    need_date_widget = 1
                    need_user_widget = 1
            else:
                need_date_widget = 1
            if not self.new_msgs_widget:
                if self.seen and (float(msg_dic[defaults._chat_key_]) > float(self.seen)) and (not self.isVisible()):
                    need_new_msgs_widget = 1

            if self.previous_user != msg_dic[defaults._chat_user_]:
                need_user_widget = 1

            if need_date_widget:
                date_widget = chat_message_widget.date_widget(msg_dic[defaults._chat_date_])
                self.ui.chat_messages_layout.addWidget(date_widget)
                self.date_widgets.append(date_widget)
            
            self.previous_date = msg_dic[defaults._chat_date_]

            if need_new_msgs_widget and list(self.room_messages_dic.keys()) != []:
                self.new_msgs_widget = chat_message_widget.new_msgs_widget() 
                self.ui.chat_messages_layout.addWidget(self.new_msgs_widget)
            
            if msg_dic[defaults._chat_type_] == defaults._chat_info_:
                info_widget = chat_message_widget.info_widget(msg_dic[defaults._chat_message_])
                self.ui.chat_messages_layout.addWidget(info_widget)
            
            elif msg_dic[defaults._chat_type_] == defaults._chat_conversation_:

                if need_user_widget and msg_dic[defaults._chat_user_] != prefs.user:
                    user_widget = chat_message_widget.user_widget(msg_dic[defaults._chat_user_])
                    self.ui.chat_messages_layout.addWidget(user_widget)

                if msg_dic[defaults._chat_message_] == self.thumb:
                    msg_dic[defaults._chat_message_] = '<font style="font-size:34px;">'+self.thumb+'</font>'
                    new_msg_widget = chat_message_widget.Main(msg_dic, url_thread, thumb=1)
                    new_msg_widget.quote.connect(self.set_quote)
                    new_msg_widget.remove.connect(self.remove_message_signal.emit)
                    self.ui.chat_messages_layout.addWidget(new_msg_widget)
                    self.add_message_to_room_dic(msg_dic[defaults._chat_key_], new_msg_widget)

                elif msg_dic[defaults._chat_message_] == defaults._chat_wizz_:
                    info_widget = chat_message_widget.info_widget("{} sent a wizz".format(msg_dic[defaults._chat_user_]))
                    self.ui.chat_messages_layout.addWidget(info_widget)
                else:
                    new_msg_widget = chat_message_widget.Main(msg_dic, url_thread)
                    new_msg_widget.quote.connect(self.set_quote)
                    new_msg_widget.remove.connect(self.remove_message_signal.emit)
                    self.ui.chat_messages_layout.addWidget(new_msg_widget)
                    self.add_message_to_room_dic(msg_dic[defaults._chat_key_], new_msg_widget)
                
                self.message_text.emit((self.context, msg_dic[defaults._chat_message_]))
                if msg_dic[defaults._chat_message_] == defaults._chat_wizz_:
                    self.wizz.emit('')

                if msg_dic[defaults._chat_key_] and self.seen:
                    if (float(msg_dic[defaults._chat_key_]) > float(self.seen)) and (not self.isVisible()):
                        self.new_messages+=1

                self.emit_new_messages()

                self.previous_user = msg_dic[defaults._chat_user_]
                if self.isVisible():
                    self.set_seen()

    def remove_message(self, key):
        if key in self.room_messages_dic.keys():
            widget = self.room_messages_dic[key]
            widget.setParent(None)
            widget.deleteLater()
            del self.room_messages_dic[key]

    def analyse_text(self):
        text = self.ui.chat_message_lineEdit.text()
        if ':)' in text:
            text = text.replace(':)', '🙂')
            self.emoji_list.append('🙂')
        if ':(' in text:
            text = text.replace(':(', '🙁')
            self.emoji_list.append('🙁')
        if ':p' in text:
            text = text.replace(':p', '😋')
            self.emoji_list.append('😋')
        if '<3' in text:
            text = text.replace('<3', '❤')
            self.emoji_list.append('❤')
        if ':D' in text:
            text = text.replace(':D', '😀')
            self.emoji_list.append('😀')
        if ';)' in text:
            text = text.replace(';)', '😉')
            self.emoji_list.append('😉')
        self.ui.chat_message_lineEdit.setText(text)

    def attach_file(self):
        options = QtWidgets.QFileDialog.Options()
        file, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Choose a file", "",
                                                  "All Files (*);", options=options)
        if file:
            self.file = file
            self.update_file()

    def set_quote(self, message_key):
        user = message_key[defaults._chat_user_]
        text = message_key[defaults._chat_message_]
        self.quote = text
        self.ui.chat_room_reply_title_label.setText("Reply to {}".format(user))
        self.ui.chat_room_reply_text_label.setText(text)
        self.ui.chat_room_quote_frame.setVisible(1)

    def remove_quote(self):
        self.ui.chat_room_quote_frame.setVisible(0)
        self.quote = None

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
        if self.file:
            self.message_signal.emit(['', self.file, self.context])
            time.sleep(0.2)
        if message != '':
            for emoji in self.emoji_list:
                message = message.replace(emoji, '<font style="font-size:24px;">{}</font>'.format(emoji))
            self.message_signal.emit([message, None, self.quote, self.context])
        self.ui.chat_message_lineEdit.clear()
        self.remove_file()
        self.remove_quote()
        self.emoji_list = []

    def send_thumb(self):
        self.message_signal.emit([self.thumb, None, self.quote, self.context])
        self.remove_file()
        self.remove_quote()

    def show_emoji_keyboard(self):
        self.emoji_keyboard = emoji_keyboard()
        self.emoji_keyboard.emoji_signal.connect(self.add_emoji)
        build.launch_position_frameless_ontop_as_child(self.emoji_keyboard)

    def add_emoji(self, emoji):
        self.emoji_list.append(emoji)
        text = self.ui.chat_message_lineEdit.text() + emoji
        self.ui.chat_message_lineEdit.setText(text)

    def rounded_pixmap_label(self, label, image_file):
        pixmap = QtGui.QPixmap(image_file).scaled(20, 20, QtCore.Qt.KeepAspectRatio,
                                                    QtCore.Qt.SmoothTransformation)
        radius = 10

        # create empty pixmap of same size as original 
        rounded = QtGui.QPixmap(pixmap.size())
        rounded.fill(QtGui.QColor("transparent"))

        # draw rounded rect on new pixmap using original pixmap as brush
        painter = QtGui.QPainter(rounded)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.setBrush(QtGui.QBrush(pixmap))
        painter.setPen(QtCore.Qt.NoPen)
        painter.drawRoundedRect(pixmap.rect(), radius, radius)
        painter.end()

        # set pixmap of label
        label.setPixmap(rounded)

class emoji_keyboard(QtWidgets.QWidget):

    emoji_signal = pyqtSignal(str)

    def __init__(self):
        super(emoji_keyboard, self).__init__()
        self.widget_layout = QtWidgets.QVBoxLayout()
        self.widget_layout.setContentsMargins(11,11,11,11)
        self.setLayout(self.widget_layout)
        self.main_frame = QtWidgets.QFrame()
        self.widget_layout.addWidget(self.main_frame)
        self.frame_layout = QtWidgets.QVBoxLayout()
        self.frame_layout.setContentsMargins(0,0,0,0)
        self.main_frame.setLayout(self.frame_layout)
        self.tabWidget = QtWidgets.QTabWidget()
        self.tabWidget.setStyleSheet('''QTabBar::tab{height:30px;width:30px;padding:6px;margin:0px;}
            QTabWidget::pane{background-color:transparent;}''')
        self.frame_layout.addWidget(self.tabWidget)
        self.font = QtGui.QFont('Arial', 15)
        self.fill_ui()
        self.setMinimumSize(QtCore.QSize(382, 400))
        self.setMaximumSize(QtCore.QSize(382, 400))

    def add_emoji(self, item):
        self.emoji_signal.emit(item.text())

    def fill_ui(self):
        with open(defaults._emojis_file_, 'r') as f:
            emojis_dic = yaml.load(f, Loader=yaml.Loader)
        for category in emojis_dic.keys():
            self.add_tab(category, emojis_dic[category])

    def add_tab(self, category, data):
        list_widget = QtWidgets.QListWidget()
        list_widget.setMovement(QtWidgets.QListView.Static)
        list_widget.setResizeMode(QtWidgets.QListView.Adjust)
        list_widget.setViewMode(QtWidgets.QListView.IconMode)
        list_widget.setStyleSheet("background:transparent;")
        list_widget.itemClicked.connect(self.add_emoji)
        list_widget.setFont(self.font)
        for emoji in list(data):
            item = QtWidgets.QListWidgetItem(emoji)
            item.setSizeHint(QtCore.QSize(50, 50))
            list_widget.addItem(item)
        self.tabWidget.addTab(list_widget, list(data)[0])

    def move_ui(self):
        win_size = (self.frameSize().width(), self.frameSize().height())
        posx = QtGui.QCursor.pos().x() - 10
        posy = int(QtGui.QCursor.pos().y()) - win_size[1] + 10
        self.move(posx, posy)

    def leaveEvent(self, event):
        self.hide()

if __name__ == '__main__':
    build.launch_chat(Main)
