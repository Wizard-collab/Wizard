from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import pyqtSignal

import os
from gui.running_widget import Ui_Form
from wizard.vars import defaults
from wizard.tools import log
import running_item_widget
from wizard.prefs.main import prefs
import wizard.asset.main as asset_core

logger = log.pipe_log()

prefs = prefs()

class Main(QtWidgets.QWidget):
    focus = pyqtSignal(str)
    refresh_lock = pyqtSignal(str)

    def __init__(self, lock=0):
        super(Main, self).__init__()
        # Build the ui from ui converted file
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.lock = lock

        self.shadow = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(8)
        self.shadow.setColor(QtGui.QColor(0, 0, 0, 180))
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.setGraphicsEffect(self.shadow)

        self.add_items()

    def leaveEvent(self, event):
        self.close()

    def move_ui(self):
        win_size = (self.frameSize().width(), self.frameSize().height())
        posx = QtGui.QCursor.pos().x() - win_size[0] + 12
        posy = int(QtGui.QCursor.pos().y()) - win_size[1] + 12
        self.move(posx, posy)

    def closeEvent(self, event):
        event.ignore()
        self.hide()

    def refresh_text(self):
        if not self.lock:
            string_assets_list = os.environ[defaults._current_assets_list_].split(':')
            self.ui.running_asset_number_label.setText('{} running assets'.format(len(string_assets_list) - 1))
        else:
            string_assets_list = prefs.locks
            self.ui.running_asset_number_label.setText('{} locked assets'.format(len(string_assets_list)))
        return string_assets_list

    def add_items(self):
        string_assets_list = self.refresh_text()
        self.ui.running_close_pushButton.setIcon(QtGui.QIcon(defaults._close_popup_icon_))
        for string_asset in string_assets_list:
            if string_asset != '':
                asset = asset_core.string_to_asset(string_asset)
                self.running_item_widget = running_item_widget.Main(asset, self)
                self.ui.running_items_layout.insertWidget(0, self.running_item_widget)
                self.running_item_widget.focus.connect(self.focus_emit)
                self.running_item_widget.refresh_lock.connect(self.refresh_lock_emit)

    def focus_emit(self, string_asset):
        self.focus.emit(string_asset)

    def refresh_lock_emit(self):
        self.refresh_text()
        self.refresh_lock.emit('')
