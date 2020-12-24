# coding: utf8
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QThread, pyqtSignal
from gui.room_button import Ui_Form
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

    select_signal = pyqtSignal(str)

    def __init__(self, context):
        super(Main, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.context = context
        self.count = 0

        self.fill_ui()
        self.unselect()

    def fill_ui(self):
        self.ui.room_button_name_label.setText(self.context)

        if self.context == defaults._chat_general_:
            image = defaults._chat_home_
        else:
            if self.context in prefs.site.users:
                image = stats(self.context).get_avatar()
            else:
                image = defaults._chat_no_image_

        self.rounded_pixmap_label(self.ui.room_button_image_label, image)

    def mousePressEvent(self, e):
        self.select_signal.emit(self.context)
        self.set_selected()

    def set_selected(self):
        self.setStyleSheet("#room_button_frame{background-color:rgba(250,250,250,50);}")
        self.visible = 1
        self.refresh_count()

    def unselect(self):
        self.setStyleSheet("")
        self.visible = 0
        self.refresh_count()

    def set_count(self, count):
        self.count = count
        self.refresh_count()

    def set_last_message(self, message):
        message = message.replace('<font style="font-size:34px;">', '')
        message = message.replace('<font style="font-size:24px;">', '')
        message = message.replace('</font>', '')
        maxlen = 14
        if len(message) >= maxlen:
            message = message[:maxlen] + '...'
        self.ui.room_button_last_message_label.setText(message)

    def refresh_count(self):
        if self.visible:
            self.count = 0
        self.ui.room_button_count_label.setText(str(self.count))
        self.ui.room_button_count_label.setVisible(self.count > 0)


    def rounded_pixmap_label(self, label, image_file):
        pixmap = QtGui.QPixmap(image_file).scaled(28, 28, QtCore.Qt.KeepAspectRatio,
                                                    QtCore.Qt.SmoothTransformation)
        radius = 14

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