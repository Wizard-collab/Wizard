# coding: utf8
from PyQt5 import QtWidgets, QtCore, QtGui
from gui import build
from wizard.vars import defaults
from wizard.tools import log
from wizard.prefs.main import prefs
from wizard.prefs.stats import stats
from datetime import datetime
from wizard.tools import utility as utils
import ui_image_viewer
import os
import traceback
import webbrowser
import validators

logger = log.pipe_log(__name__)

prefs = prefs()

class Main(QtWidgets.QWidget):

    def __init__(self, msg_dic, url_thread):
        super(Main, self).__init__()
        '''
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        '''
        self.msg_dic = msg_dic
        self.user = prefs.user
        self.url_thread = url_thread
        self.users_views_dic = dict()
        self.build_ui()
        self.set_user()
        self.fill_ui()
        self.toggle_users_view_layout()

    def fill_ui(self):
        if self.msg_dic[defaults._chat_message_] != '':
            message_splitted = self.msg_dic[defaults._chat_message_].split(' ')
            url = None
            for item in message_splitted:
                if validators.url(item):
                    self.msg_dic[defaults._chat_message_] = self.msg_dic[defaults._chat_message_].replace(item, '')
                    url = item
                    break
            if self.msg_dic[defaults._chat_message_] != '':
                self.add_text()
            if url:
                self.add_url(url, self.msg_dic[defaults._chat_message_])

        if self.msg_dic[defaults._chat_file_]:
            if self.msg_dic[defaults._chat_file_].endswith('.png') or self.msg_dic[defaults._chat_file_].endswith('.jpg'):
                self.add_image_button()
            else:
                self.add_file_button()

    def add_url(self, url, text):
        self.url_button = QtWidgets.QPushButton(url)
        self.url_button.setMaximumSize(QtCore.QSize(200,40))
        self.url_button.setMinimumSize(QtCore.QSize(200,40))
        self.url_button.setIconSize(QtCore.QSize(20,20))
        self.url_button.setStyleSheet("border-radius:5px;")
        self.url_button.clicked.connect(lambda:self.start_web(url))
        self.main_frame_layout.addWidget(self.url_button)
        if text == '':
            self.main_frame_layout.setContentsMargins(0,0,0,0)
            self.setStyleSheet('''#messages_frame{background:transparent;}''')
        self.url_thread.translate_button((self.url_button, url))

    def add_image_button(self):
        self.file_button = QtWidgets.QPushButton()
        self.file_button.setMaximumSize(QtCore.QSize(150,150))
        self.file_button.setMinimumSize(QtCore.QSize(150,150))
        self.file_button.setIconSize(QtCore.QSize(150,150))
        self.round_image(self.file_button, self.msg_dic[defaults._chat_file_])
        #self.file_button.setIcon(QtGui.QIcon(self.msg_dic[defaults._chat_file_]))
        self.file_button.setStyleSheet("background-color:transparent;border-radius:5px;")
        self.file_button.clicked.connect(lambda:self.show_image(self.msg_dic[defaults._chat_file_]))
        self.main_frame_layout.addWidget(self.file_button)
        self.main_frame_layout.setContentsMargins(0,0,0,0)
        self.setStyleSheet('''#messages_frame{background:transparent;}''')

    def add_user_view(self, user):
        if user not in list(self.users_views_dic.keys()):
            user_label = QtWidgets.QLabel()

            user_label = QtWidgets.QLabel()
            user_label.setMinimumSize(QtCore.QSize(26, 26))
            user_label.setMaximumSize(QtCore.QSize(26, 26))
            user_label.setText("")
            user_label.setAlignment(QtCore.Qt.AlignCenter)

            self.round_image_label(user_label, stats(user).get_avatar())
            self.users_views_dic[user] = user_label
            self.users_views_layout.addWidget(user_label)
        self.toggle_users_view_layout()

    def remove_user_view(self, user):
        if user in list(self.users_views_dic.keys()):
            self.users_views_dic[user].setVisible(0)
            self.users_views_dic[user].setParent(None)
            self.users_views_dic[user].deleteLater()
            del self.users_views_dic[user]
        self.toggle_users_view_layout()

    def toggle_users_view_layout(self):
        if list(self.users_views_dic.keys()) == []:
            self.users_views_frame.setVisible(0)
        else:
            self.users_views_frame.setVisible(1)

    def round_image_label(self, label, image_file):
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

    def round_image(self, label, image):
        label.Antialiasing = True
        label.radius = 5
        label.target = QtGui.QPixmap(label.size())
        label.target.fill(QtCore.Qt.transparent)
        p = QtGui.QPixmap(image).scaled(
            150, 150, QtCore.Qt.KeepAspectRatioByExpanding, QtCore.Qt.SmoothTransformation)
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

    def add_file_button(self):
        self.file_button = QtWidgets.QPushButton(os.path.basename(self.msg_dic[defaults._chat_file_]))
        self.file_button.setMaximumSize(QtCore.QSize(150,40))
        self.file_button.setMinimumSize(QtCore.QSize(150,40))
        self.file_button.setIconSize(QtCore.QSize(20,20))
        self.file_button.setIcon(QtGui.QIcon(defaults._chat_file_icon_))
        self.file_button.setStyleSheet("border-radius:5px;")
        self.file_button.clicked.connect(lambda:self.start_file(self.msg_dic[defaults._chat_file_]))
        self.main_frame_layout.addWidget(self.file_button)
        self.main_frame_layout.setContentsMargins(0,0,0,0)
        self.setStyleSheet('''#messages_frame{background:transparent;}''')

    def start_file(self, file):
        try:
            if os.path.isfile(file):
                os.startfile(file)
        except:
            logger.critical(str(traceback.format_exc()))

    def start_web(self, url):
        webbrowser.open(url, new=0, autoraise=True)

    def show_image(self, image):
        self.image_viewer = ui_image_viewer.Main(image)
        build.launch_normal_as_child_frameless(self.image_viewer)

    def add_text(self):
        text = self.msg_dic[defaults._chat_message_]
        max_len = 16

        parts = text.split(' ')
        new_parts = []

        for text in parts:
            begin = text[:max_len]
            end = text[max_len:]
            while len(end) >= max_len:
                begin += "\n" + end[:max_len]
                end = end[max_len:]
            begin += "\n" + end[:max_len]
            end = end[max_len:]
            text = begin + end
            new_parts.append(text)

        text = ' '.join(new_parts)

        self.chat_message_label = QtWidgets.QLabel(text)
        self.chat_message_label.setTextFormat(QtCore.Qt.RichText)
        self.chat_message_label.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.chat_message_label.setWordWrap(True)
        self.main_frame_layout.addWidget(self.chat_message_label)
        self.font = QtGui.QFont('Segoe UI Emoji', 10)
        self.font.setStyleStrategy(QtGui.QFont.ForceOutline)
        self.chat_message_label.setFont(self.font)
        if self.user == self.msg_dic[defaults._chat_user_]:
            self.chat_message_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)

    def set_user(self):
        if self.user == self.msg_dic[defaults._chat_user_]:
            self.setLayoutDirection(QtCore.Qt.RightToLeft)
            self.setStyleSheet('''#messages_frame{background-color:rgba(217, 204, 255, 30);}''')
            self.users_views_frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        else:
            self.main_layout.setContentsMargins(30,0,0,0)

    def build_ui(self):
        self.main_layout = QtWidgets.QHBoxLayout()
        self.main_layout.setContentsMargins(0,0,0,0)
        self.vertical_layout = QtWidgets.QVBoxLayout()
        self.vertical_layout.setContentsMargins(0,0,0,0)
        self.main_frame = QtWidgets.QFrame()
        self.main_frame.setObjectName("messages_frame")
        self.main_frame_layout = QtWidgets.QVBoxLayout()
        self.main_frame.setLayout(self.main_frame_layout)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.vertical_layout.addWidget(self.main_frame)
        self.vertical_layout.setSpacing(1)

        self.users_views_frame = QtWidgets.QFrame()
        self.users_views_frame.setStyleSheet('background-color:transparent;')
        self.vertical_layout.addWidget(self.users_views_frame)

        self.users_views_layout = QtWidgets.QHBoxLayout()
        self.users_views_layout.setContentsMargins(0,0,0,0)
        self.users_views_layout.setSpacing(1)
        self.spacerItem_2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.users_views_layout.addItem(self.spacerItem_2)
        self.users_views_frame.setLayout(self.users_views_layout)
        self.main_layout.addLayout(self.vertical_layout)
        self.main_layout.addItem(spacerItem)
        self.setLayout(self.main_layout)

class date_widget(QtWidgets.QLabel):

    def __init__(self, date):
        super(date_widget, self).__init__()
        ts = float(date)
        # if you encounter a "year is out of range" error the timestamp
        # may be in milliseconds, try `ts /= 1000` in that case
        hour = datetime.utcfromtimestamp(ts).strftime('%H:%M')
        day = datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d')

        today = datetime.utcfromtimestamp(float(utils.id_based_time())).strftime('%Y-%m-%d')

        if day == today:
            text = hour
        else:
            text = '{} - {}' .format(day, hour)

        self.setText(text)
        self.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.setMargin(5)
        self.setStyleSheet("color:gray;")


class user_widget(QtWidgets.QWidget):
    
    def __init__(self, user):
        super(user_widget, self).__init__()
        
        self.main_layout = QtWidgets.QVBoxLayout(self)
        self.setLayout(self.main_layout)

        self.user_image_label = QtWidgets.QLabel()
        self.user_image_label.setMinimumSize(QtCore.QSize(60,60))
        self.user_image_label.setMaximumSize(QtCore.QSize(60,60))

        self.rounded_pixmap_label(self.user_image_label, stats(user).get_avatar())

        self.main_layout.addWidget(self.user_image_label)

        self.setMaximumSize(QtCore.QSize(4000,60))
        self.setMinimumSize(QtCore.QSize(60,60))

        self.main_layout.setContentsMargins(0,5,5,5)

        if user == prefs.user:
            self.setLayoutDirection(QtCore.Qt.RightToLeft)
            self.main_layout.setContentsMargins(5,5,0,5)


    def rounded_pixmap_label(self, label, image_file):
        pixmap = QtGui.QPixmap(image_file).scaled(40, 40, QtCore.Qt.KeepAspectRatio,
                                                    QtCore.Qt.SmoothTransformation)
        radius = 20

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