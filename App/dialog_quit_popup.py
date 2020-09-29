from PyQt5 import QtWidgets, QtCore, QtGui

from gui.quit_popup_dialog import Ui_Dialog
from wizard.vars import defaults
from wizard.prefs.main import prefs
from wizard.tools import log
from wizard.tools import utility as utils
from wizard.asset import main as asset_core

logger = log.pipe_log(__name__)

prefs = prefs()

class Main(QtWidgets.QDialog):

    def __init__(self, runs, locks):
        super(Main, self).__init__()
        # Build the ui from ui converted file
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.runs = runs
        self.locks = locks
        self.add_images()
        self.setup_widget()
        self.ui.quit_popup_unlock_all_pushButton.clicked.connect(self.unlock_all)

        self.shadow = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(8)
        self.shadow.setColor(QtGui.QColor(0, 0, 0, 180))
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.ui.quit_popup_main_frame.setGraphicsEffect(self.shadow)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def unlock_all(self):
        locks_list = prefs.locks
        for lock in locks_list:
            asset = asset_core.string_to_asset(lock)
            if prefs.asset(asset).software.get_lock:
                prefs.asset(asset).software.unlock()
                prefs.remove_lock(utils.short_asset_to_string(asset))
        self.locks = None
        self.setup_widget()

    def setup_widget(self):
        if not self.locks:
            self.ui.quit_popup_lock_label.setText('0 locked asset')
            self.ui.quit_popup_unlock_all_pushButton.setVisible(0)
        else:
            self.ui.quit_popup_lock_label.setText(f'{self.locks} locked assets')
        if not self.runs:
            self.ui.quit_popup_run_label.setText('0 running asset')
        else:
            self.ui.quit_popup_run_label.setText(f'{self.runs} running assets')

    def add_images(self):
        self.ui.quit_popup_warning_image_label.setPixmap(
            QtGui.QPixmap(defaults._missing_file_export_list_icon_).scaled(28, 28, QtCore.Qt.KeepAspectRatio,
                                                          QtCore.Qt.SmoothTransformation))
        self.ui.quit_popup_lock_image_label.setPixmap(
            QtGui.QPixmap(defaults._locked_icon_).scaled(28, 28, QtCore.Qt.KeepAspectRatio,
                                                         QtCore.Qt.SmoothTransformation))
        self.ui.quit_popup_run_image_label.setPixmap(
            QtGui.QPixmap(defaults._running_icon_).scaled(28, 28, QtCore.Qt.KeepAspectRatio,
                                                          QtCore.Qt.SmoothTransformation))
