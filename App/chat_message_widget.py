# coding: utf8
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QThread, pyqtSignal
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

    quote = pyqtSignal(dict)
    remove = pyqtSignal(str)

    def __init__(self, msg_dic, url_thread, thumb=0):
        super(Main, self).__init__()
        '''
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        '''
        self.msg_dic = msg_dic
        self.user = prefs.user
        self.url_thread = url_thread
        self.users_views_dic = dict()
        self.thumb = thumb

        self.font = QtGui.QFont('Segoe UI Emoji', 10)
        self.font.setStyleStrategy(QtGui.QFont.ForceOutline)

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

    def add_quote(self, quote):
        self.parent_quote_frame = QtWidgets.QFrame()
        self.parent_quote_frame.setObjectName('parent_quote_frame')
        self.parent_quote_frame.setStyleSheet('#parent_quote_frame{background:transparent;}')
        self.parent_quote_layout = QtWidgets.QHBoxLayout()
        self.parent_quote_layout.setContentsMargins(0,5,0,0)
        self.parent_quote_frame.setLayout(self.parent_quote_layout)

        self.quote_spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.parent_quote_layout.addItem(self.quote_spacerItem)

        self.quote_frame = QtWidgets.QFrame()
        self.quote_layout = QtWidgets.QVBoxLayout()

        self.quote_frame.setLayout(self.quote_layout)
        self.quote_frame.setObjectName('quote_frame')
        
        self.quote_label = QtWidgets.QLabel()
        self.quote_label.setWordWrap(True)
        self.quote_label.setText(quote)
        self.quote_label.setFont(self.font)
        self.quote_label.setStyleSheet('color:gray;')
        self.quote_layout.addWidget(self.quote_label)
        self.parent_quote_layout.addWidget(self.quote_frame)

        self.main_layout.addWidget(self.parent_quote_frame)

        if self.user == self.msg_dic[defaults._chat_user_]:
            self.parent_quote_frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        else:
            self.parent_quote_frame.setLayoutDirection(QtCore.Qt.RightToLeft)

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
        if (user not in list(self.users_views_dic.keys())) and (user != self.user) and (user != self.msg_dic[defaults._chat_user_]):
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
        
        self.chat_message_label.setFont(self.font)
        if self.user == self.msg_dic[defaults._chat_user_]:
            self.chat_message_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)

    def enterEvent(self, e):
        self.buttons_frame.setVisible(1)

    def leaveEvent(self, e):
        self.buttons_frame.setVisible(0)

    def set_user(self):
        if self.user == self.msg_dic[defaults._chat_user_]:
            self.horizontal_frame.setLayoutDirection(QtCore.Qt.LeftToRight)
            self.setStyleSheet('''#messages_frame{background-color:rgba(217, 204, 255, 30);}''')
            self.users_views_frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        else:
            self.main_layout.setContentsMargins(30,0,0,0)
            self.horizontal_frame.setLayoutDirection(QtCore.Qt.RightToLeft)
            self.users_views_frame.setLayoutDirection(QtCore.Qt.RightToLeft)

    def add_emoji(self):
        pass

    def build_ui(self):
        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.setContentsMargins(0,0,0,0)
        self.main_layout.setSpacing(1)

        if self.msg_dic[defaults._chat_quote_]:
            self.add_quote(self.msg_dic[defaults._chat_quote_])

        self.horizontal_frame = QtWidgets.QFrame()
        self.horizontal_frame.setObjectName('horizontal_frame')
        self.horizontal_frame.setStyleSheet('#horizontal_frame{background-color:transparent;}')
        self.main_layout.addWidget(self.horizontal_frame)

        self.horizontal_layout = QtWidgets.QHBoxLayout()
        self.horizontal_layout.setContentsMargins(0,0,0,0)
        self.horizontal_frame.setLayout(self.horizontal_layout)

        

        self.main_frame = QtWidgets.QFrame()
        #self.horizontal_layout.addWidget(self.main_frame)
        self.main_frame.setObjectName("messages_frame")
        
        self.main_frame_layout = QtWidgets.QVBoxLayout()
        self.main_frame.setLayout(self.main_frame_layout)

        if self.thumb:
            self.main_frame.setStyleSheet('background:transparent;')
            self.main_frame_layout.setContentsMargins(0,0,0,0)

        self.buttons_frame = QtWidgets.QFrame()
        self.buttons_frame.setVisible(0)
        self.buttons_frame.setObjectName('message_button_frame')
        self.buttons_frame.setStyleSheet('#message_button_frame{background:transparent;}')
        self.buttons_layout = QtWidgets.QHBoxLayout()
        self.buttons_layout.setContentsMargins(0,0,0,0)
        self.buttons_frame.setLayout(self.buttons_layout)

        self.quote_button = QtWidgets.QPushButton()
        self.quote_button.setObjectName("quote_button")
        self.quote_button.setIcon(QtGui.QIcon(defaults._quote_icon_))
        self.quote_button.setIconSize(QtCore.QSize(16, 16))
        self.quote_button.setMaximumSize(QtCore.QSize(24, 24))
        self.quote_button.setMinimumSize(QtCore.QSize(24, 24))
        self.quote_button.clicked.connect(lambda:self.quote.emit(self.msg_dic))
        self.buttons_layout.addWidget(self.quote_button)
        
        if self.msg_dic[defaults._chat_user_] == self.user:
            self.remove_button = QtWidgets.QPushButton()
            self.remove_button.setObjectName("quote_button")
            self.remove_button.setIcon(QtGui.QIcon(defaults._trash_icon_))
            self.remove_button.setIconSize(QtCore.QSize(16, 16))
            self.remove_button.setMaximumSize(QtCore.QSize(24, 24))
            self.remove_button.setMinimumSize(QtCore.QSize(24, 24))
            self.remove_button.clicked.connect(lambda:self.remove.emit(self.msg_dic[defaults._chat_key_]))
            self.buttons_layout.addWidget(self.remove_button)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout.addItem(spacerItem)
        self.horizontal_layout.addWidget(self.buttons_frame)
        self.horizontal_layout.addWidget(self.main_frame)
        self.horizontal_layout.setSpacing(11)
        #self.main_layout.addWidget(self.horizontal_frame)

        self.users_views_frame = QtWidgets.QFrame()
        self.users_views_frame.setStyleSheet('background-color:transparent;')
        self.main_layout.addWidget(self.users_views_frame)

        self.users_views_layout = QtWidgets.QHBoxLayout()
        self.users_views_layout.setContentsMargins(0,0,0,0)
        self.users_views_layout.setSpacing(1)
        self.spacerItem_2 = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.users_views_layout.addItem(self.spacerItem_2)
        self.users_views_frame.setLayout(self.users_views_layout)
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

class info_widget(QtWidgets.QLabel):

    def __init__(self, message):
        super(info_widget, self).__init__()
        self.setText(message)
        self.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.setMargin(5)
        self.setStyleSheet("color:gray;")

class new_msgs_widget(QtWidgets.QFrame):
    def __init__(self):
        super(new_msgs_widget, self).__init__()

        self.main_layout = QtWidgets.QHBoxLayout()
        self.setObjectName('new_msg_widget_main_frame')
        self.setLayout(self.main_layout)
        self.setStyleSheet('#new_msg_widget_main_frame{background:transparent;}')

        self.line1 = QtWidgets.QFrame(self)
        self.line1.setGeometry(QtCore.QRect(170, 70, 118, 1))
        self.line1.setMaximumSize(QtCore.QSize(10000, 1))
        self.line1.setMinimumSize(QtCore.QSize(1, 1))
        self.line1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line1.setObjectName("line")
        self.line1.setStyleSheet("background-color:#ff5447;")

        self.line2 = QtWidgets.QFrame(self)
        self.line2.setGeometry(QtCore.QRect(170, 70, 118, 1))
        self.line2.setMaximumSize(QtCore.QSize(10000, 1))
        self.line2.setMinimumSize(QtCore.QSize(1, 1))
        self.line2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line2.setObjectName("line")
        self.line2.setStyleSheet("background-color:#ff5447;")

        self.label = QtWidgets.QLabel("New messages")

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.label.setMargin(5)
        self.label.setStyleSheet("color:#ff5447;")

        self.main_layout.addWidget(self.line1)
        self.main_layout.addWidget(self.label)
        self.main_layout.addWidget(self.line2)

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