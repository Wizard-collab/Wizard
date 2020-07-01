from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import pyqtSignal

import os
from gui.message_widget import Ui_Form
from wizard.vars import defaults
from wizard.tools import log
import running_item_widget
from wizard.prefs.main import prefs
import wizard.asset.main as asset_core
from wizard.prefs.stats import stats
import traceback

logger = log.pipe_log()

prefs = prefs()

class Main(QtWidgets.QWidget):

    def __init__(self, user, text, file):
        super(Main, self).__init__()
        # Build the ui from ui converted file
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.user = user
        self.file = file
        if not self.file:
            self.ui.chat_file_pushButton.hide()
        self.user_image = stats(self.user).get_avatar()
        self.text = text
        if not self.text or self.text == '':
            self.ui.message_widget_label.hide()
        self.setup_widget()

        self.shadow = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(8)
        self.shadow.setColor(QtGui.QColor(0, 0, 0, 180))
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.setGraphicsEffect(self.shadow)

    def move_ui(self):
        win_size = (self.frameSize().width(), self.frameSize().height())
        posx = QtGui.QCursor.pos().x() - win_size[0] + 12
        posy = int(QtGui.QCursor.pos().y()) - win_size[1] + 12
        self.move(posx, posy)

    def setup_widget(self):
        self.ui.message_widget_label.setText(self.text)
        if self.file:
            if self.file.endswith('.png') or self.file.endswith('.jpg'):
                self.ui.chat_file_pushButton.setIcon(QtGui.QIcon(self.file))
                self.ui.chat_file_pushButton.setIconSize(QtCore.QSize(200,200))
                self.ui.chat_file_pushButton.setMinimumSize(10, 232)
            else:
                self.ui.chat_file_pushButton.setText(os.path.basename(self.file))
                self.ui.chat_file_pushButton.setIcon(QtGui.QIcon(defaults._chat_file_icon_))
            self.ui.chat_file_pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
            self.ui.chat_file_pushButton.clicked.connect(self.open_file)
        self.ui.message_user_label.setText(self.user)
        self.round_image(self.ui.message_widget_image_label, self.user_image)
        if self.user == prefs.user:
            self.ui.message_user_label.setText('me')
            self.setLayoutDirection(QtCore.Qt.RightToLeft)
            self.ui.message_main_frame.setLayoutDirection(QtCore.Qt.RightToLeft)
            self.ui.message_widget_label.setAlignment(QtCore.Qt.AlignRight)
            self.ui.message_user_label.setAlignment(QtCore.Qt.AlignRight)

    def open_file(self):
        try:
            os.startfile(self.file)
        except:
            logger.critical(str(traceback.format_exc()))

    def closeEvent(self, event):
        event.ignore()
        self.hide()

    def round_image(self, label, image):
        label.Antialiasing = True
        label.radius = 38

        label.target = QtGui.QPixmap(label.size())
        label.target.fill(QtCore.Qt.transparent)

        p = QtGui.QPixmap(image).scaled(
            38, 38, QtCore.Qt.KeepAspectRatioByExpanding, QtCore.Qt.SmoothTransformation)

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
