from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication, QFileDialog

import os
from gui.chat import Ui_Form
from wizard.vars import defaults
from wizard.tools import log
import running_item_widget
from wizard.prefs.main import prefs
from wizard.chat.client import client
from wizard.chat.send import send_message_chat
import wizard.asset.main as asset_core
from wizard.tools import utility as util
from wizard.chat.shared_files import shared_files
from wizard.project.chat_archives import archives
import popup

import message_widget

logger = log.pipe_log()

prefs = prefs()

class Main(QtWidgets.QWidget):

    new_message = pyqtSignal(str)

    def __init__(self):
        super(Main, self).__init__()
        # Build the ui from ui converted file
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.chat_file_frame.setVisible(0)

        self.shadow = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(8)
        self.shadow.setColor(QtGui.QColor(0, 0, 0, 180))
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.setGraphicsEffect(self.shadow)

        self.ui.chat_main_lineEdit = PlainTextEdit()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ui.chat_main_lineEdit.sizePolicy().hasHeightForWidth())
        self.ui.chat_main_lineEdit.setMaximumSize(QtCore.QSize(16777215, 60))
        self.ui.chat_main_lineEdit.setSizePolicy(sizePolicy)
        self.ui.chat_main_lineEdit.setObjectName("chat_main_lineEdit")
        self.ui.horizontalLayout_4.insertWidget(0, self.ui.chat_main_lineEdit)
        self.ui.chat_main_lineEdit.setPlaceholderText("Your message")
        self.ui.chat_main_lineEdit.send_signal.connect(self.send_message)

        self.present_keys = []

        self.setWidget()
        
        self.connect_functions()

        self.add_archives(1)

        self.start_chat()
        self.file = None

    def add_archives(self, init = 0):
        messages_dic = archives().history
        count = len(self.present_keys)
        number = len(self.present_keys) + 20
        keys_list = list(messages_dic.keys())
        keys_list.reverse()
        if not init:
            area_scroll_bar = self.ui.chat_main_scrollArea.verticalScrollBar()
            area_scroll_bar.rangeChanged.connect(lambda: area_scroll_bar.setValue(area_scroll_bar.minimum()))
        for key in keys_list:
            if key not in self.present_keys:
                self.present_keys.append(key)
                self.build_message(messages_dic[key], 0, 1, 1)
                count+=1
                if count >= number:
                    break
        if len(self.present_keys) == len(keys_list):
            self.ui.chat_show_more_pushButton.hide()

    def move_ui(self):
        win_size = (self.frameSize().width(), self.frameSize().height())
        posx = QtGui.QCursor.pos().x() - win_size[0] + 12
        posy = int(QtGui.QCursor.pos().y()) - win_size[1] + 12
        self.move(posx, posy)

    def build_message(self, encoded_message = None, encoded = 1, init = 0, insert = 0):
        if encoded:
            message_dic = util.decode_message(encoded_message)
        else:
            message_dic = encoded_message
        user = message_dic[defaults._creation_user_key_]
        date = message_dic[defaults._creation_date_key_]
        id = message_dic[defaults._message_id_key_]
        message = message_dic[defaults._message_key_]
        file = message_dic[defaults._file_key_]
        self.message_widget = message_widget.Main(user, message, file)
        if insert:
            self.ui.chat_messages_layouts_1.insertWidget(0, self.message_widget)
        else:
            self.ui.chat_messages_layouts_1.addWidget(self.message_widget)
        QApplication.processEvents()
        if not self.isVisible() and user != prefs.user and not init:
            if id == defaults._file_message_:
                message = "Sended a new file"
            popup.popup().message_pop(f'{user} : {message}')   
            self.new_message.emit('')

    def start_chat(self):
        try:
            self.client = client(1)
            self.client.start()
            self.client.receive.connect(self.build_message)
            self.client.receive.connect(self.connect_functions)
            self.client.stopped.connect(self.restart)
        except:
            logger.critical(str(traceback.format_exc()))

    def open_file(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);", options=options)
        if fileName:
            sended_file = shared_files().add_file(fileName)
            self.set_file(sended_file)

    def set_file(self, sended_file = None):
        if sended_file:
            self.file = sended_file
            self.ui.chat_file_frame.setVisible(1)
            self.ui.added_chat_file_pushButton.setText(' {}'.format(os.path.basename(self.file)))
            self.ui.added_chat_file_pushButton.setIcon(QtGui.QIcon(defaults._close_popup_icon_))
            self.ui.added_chat_file_pushButton.setIconSize(QtCore.QSize(10,10))
            QApplication.processEvents()
        else:
            self.file = None
            self.ui.chat_file_frame.setVisible(0)


    def send_message(self):
        message = self.ui.chat_main_lineEdit.toPlainText()
        self.ui.chat_main_lineEdit.clear()
        date = util.get_gmtime()
        id = defaults._classic_message_
        message_dic = dict()
        message_dic[defaults._creation_user_key_] = prefs.user
        message_dic[defaults._creation_date_key_] = date
        message_dic[defaults._message_key_] = message
        message_dic[defaults._file_key_] = self.file
        message_dic[defaults._message_id_key_] = id
        message = util.encode_message(message_dic)
        send_message_chat(message)
        self.set_file()

    def connect_functions(self):
        send_shortcut = QtWidgets.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Return), self)
        send_shortcut.activated.connect(self.send_message)
        area_scroll_bar = self.ui.chat_main_scrollArea.verticalScrollBar()
        area_scroll_bar.rangeChanged.connect(lambda: area_scroll_bar.setValue(area_scroll_bar.maximum()))
        self.ui.add_file_pushButton.clicked.connect(self.open_file)
        self.ui.chat_show_more_pushButton.clicked.connect(self.add_archives)

    def restart(self):
        self.client.quit()
        self.start_chat()

    def setWidget(self):
        self.ui.send_message_pushButton.setIcon(QtGui.QIcon(defaults._send_message_icon_))
        self.ui.add_file_pushButton.setIcon(QtGui.QIcon(defaults._join_file_icon_))
        self.ui.send_message_pushButton.setIconSize(QtCore.QSize(18,18))
        self.ui.add_file_pushButton.setIconSize(QtCore.QSize(20,20))
        self.ui.chat_project_label.setText(f'Chat - {prefs.project_name}')

    def closeEvent(self, event):
        event.ignore()
        self.hide()

class PlainTextEdit(QtWidgets.QTextEdit):

    send_signal = pyqtSignal(str)

    def keyPressEvent(self, event):
        if event.key() in (QtCore.Qt.Key_Return, QtCore.Qt.Key_Enter):
            self.send_signal.emit('')
        else:
            super().keyPressEvent(event)
