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

logger = log.pipe_log(__name__)

prefs = prefs()

class Main(QtWidgets.QWidget):

    def __init__(self, msg_dic):
        super(Main, self).__init__()
        '''
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        '''
        self.msg_dic = msg_dic
        self.user = prefs.user
        self.build_ui()
        self.fill_ui()
        self.set_user()

    def fill_ui(self):
        if self.msg_dic[defaults._chat_message_] != '':
            self.add_text()
        if self.msg_dic[defaults._chat_file_]:
            if self.msg_dic[defaults._chat_file_].endswith('.png') or self.msg_dic[defaults._chat_file_].endswith('.jpg'):
                self.add_image_button()
            else:
                self.add_file_button()

    def add_image_button(self):
        self.file_button = QtWidgets.QPushButton()
        self.file_button.setMaximumSize(QtCore.QSize(150,150))
        self.file_button.setMinimumSize(QtCore.QSize(150,150))
        self.file_button.setIconSize(QtCore.QSize(150,150))
        self.file_button.setIcon(QtGui.QIcon(self.msg_dic[defaults._chat_file_]))
        self.file_button.setStyleSheet("background-color:transparent;border-radius:5px;")
        self.file_button.clicked.connect(lambda:self.show_image(self.msg_dic[defaults._chat_file_]))
        self.main_frame_layout.addWidget(self.file_button)

    def add_file_button(self):
        self.file_button = QtWidgets.QPushButton(os.path.basename(self.msg_dic[defaults._chat_file_]))
        self.file_button.setMaximumSize(QtCore.QSize(150,40))
        self.file_button.setMinimumSize(QtCore.QSize(150,40))
        self.file_button.setIconSize(QtCore.QSize(20,20))
        self.file_button.setIcon(QtGui.QIcon(defaults._chat_file_icon_))
        self.file_button.setStyleSheet("border-radius:5px;")
        #self.file_button.clicked.connect(lambda:self.show_image(defaults._wizard_icon_))
        self.main_frame_layout.addWidget(self.file_button)

    def show_image(self, image):
        self.image_viewer = ui_image_viewer.Main(image)
        build.launch_normal_as_child_frameless(self.image_viewer)

    def add_text(self):
        self.chat_message_label = QtWidgets.QLabel(self.msg_dic[defaults._chat_message_])
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
            self.setStyleSheet('''#messages_frame{background-color:rgba(217, 204, 255, 100);}''')
        else:
            self.main_layout.setContentsMargins(30,0,0,0)

    def build_ui(self):
        self.main_layout = QtWidgets.QHBoxLayout()
        self.main_layout.setContentsMargins(0,0,0,0)
        self.main_frame = QtWidgets.QFrame()
        self.main_frame.setObjectName("messages_frame")
        self.main_frame_layout = QtWidgets.QVBoxLayout()
        self.main_frame.setLayout(self.main_frame_layout)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.main_layout.addWidget(self.main_frame)
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