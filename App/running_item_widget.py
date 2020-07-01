from PyQt5 import QtWidgets, QtCore, QtGui

from PyQt5.QtCore import pyqtSignal

from gui.running_item_widget import Ui_Form
from wizard.vars import defaults
from wizard.tools import log
from wizard.tools import utility as utils
from wizard.prefs.main import prefs

logger = log.pipe_log()

prefs = prefs()

class Main(QtWidgets.QWidget):
    focus = pyqtSignal(str)
    refresh_lock = pyqtSignal(str)

    def __init__(self, asset, parent):
        super(Main, self).__init__()
        # Build the ui from ui converted file
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.asset = asset
        self.parent = parent
        self.setup_widget()

    def setup_widget(self):
        self.ui.running_item_asset_label.setText(
            '{}|{}|{}'.format(self.asset.category, self.asset.name, self.asset.stage))
        self.ui.running_item_image_label.setPixmap(
            QtGui.QPixmap(defaults._soft_icons_dic_[self.asset.software]).scaled(20, 20, QtCore.Qt.KeepAspectRatio,
                                                                                 QtCore.Qt.SmoothTransformation))
        self.ui.focus_pushButton.setIcon(QtGui.QIcon(defaults._focus_icon_))
        self.ui.focus_pushButton.clicked.connect(self.focus_emit)
        if prefs.asset(self.asset).software.get_lock:
            self.set_locked_appearence()
        else:
            self.set_unlocked_appearence()
        self.ui.running_item_lock_pushButton.clicked.connect(self.lock_clicked)

    def set_locked_appearence(self):
        self.ui.running_item_lock_pushButton.setIcon(QtGui.QIcon(defaults._locked_icon_))
        stylesheet = "#running_item_lock_pushButton{background-color: #eb5250;}\n"
        stylesheet += "#running_item_lock_pushButton:hover{background-color: #ff8685;}\n"
        stylesheet += "#running_item_lock_pushButton:pressed{background-color: #9c4443;}"
        self.ui.running_item_lock_pushButton.setStyleSheet(stylesheet)

    def set_unlocked_appearence(self):
        self.ui.running_item_lock_pushButton.setIcon(QtGui.QIcon(defaults._unlocked_icon_))
        self.ui.running_item_lock_pushButton.setStyleSheet("")

    def lock_clicked(self):
        if prefs.asset(self.asset).software.get_lock:
            prefs.asset(self.asset).software.unlock()
            prefs.remove_lock(utils.short_asset_to_string(self.asset))
            self.set_unlocked_appearence()
            self.refresh_lock.emit('')
            if self.parent.lock:
                self.close()
        else:
            prefs.asset(self.asset).software.lock()
            prefs.add_lock(utils.short_asset_to_string(self.asset))
            self.set_locked_appearence()
            self.refresh_lock.emit('')

    def focus_emit(self):
        string_asset = utils.asset_to_string(self.asset)
        self.focus.emit(string_asset)
