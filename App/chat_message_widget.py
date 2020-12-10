# coding: utf8
from PyQt5 import QtWidgets, QtCore, QtGui
from gui.chat_message_widget import Ui_Form
from gui import build
from wizard.vars import defaults
from wizard.tools import log
from wizard.prefs.main import prefs
from wizard.prefs.stats import stats
from datetime import datetime
from wizard.tools import utility as utils

logger = log.pipe_log(__name__)

prefs = prefs()

class Main(QtWidgets.QWidget):

    def __init__(self, msg_dic):
        super(Main, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.chat_message_text.setText(msg_dic[defaults._chat_message_])

        self.font = QtGui.QFont('Segoe UI Emoji', 10)
        self.font.setStyleStrategy(QtGui.QFont.ForceOutline)
        self.ui.chat_message_text.setFont(self.font)

        if prefs.user == msg_dic[defaults._chat_user_]:
            self.ui.main_frame.setLayoutDirection(QtCore.Qt.RightToLeft)
            self.ui.chat_message_text.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
            self.setStyleSheet('''#messages_frame{background-color:rgba(217, 204, 255, 100);}''')
        else:
            self.ui.main_frame.setContentsMargins(30,0,0,0)

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