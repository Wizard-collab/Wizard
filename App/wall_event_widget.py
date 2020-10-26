# coding: utf8


from PyQt5 import QtWidgets, QtCore
from gui.wall_event_widget import Ui_Form
from wizard.asset import main as asset_core
from wizard.prefs.main import prefs
import os
from gui import build
from wizard.vars import defaults
from time import strftime
import options_widget
from wizard.tools import log

logger = log.pipe_log(__name__)

prefs = prefs()

class Main(QtWidgets.QWidget):

    def __init__(self, user, date, message, id, time_id, asset=None):
        super(Main, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.user = user
        self.date = date
        self.message = message
        self.id = id
        self.time_id = time_id
        self.asset = asset
        self.convert_ui()

    def convert_ui(self):
        date = strftime("%X", self.date)
        self.ui.wall_event_user_label.setText(f'{self.user} - {date}')
        self.ui.wall_event_message_label.setText(self.message)
        icon = defaults._event_icon_dic_[self.id]
        color = defaults._event_color_dic_[self.id]
        self.ui.color_id_frame.setStyleSheet("#color_id_frame{background-color:%s;}" % color)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.RightButton:
            self.show_options_menu()

    def explorer(self):
        if self.asset:
            asset = asset_core.string_to_asset(self.asset)
            if self.id == defaults._wall_publish_event_:
                folder = prefs.asset(asset).export.version_folder
                os.startfile(folder)
            elif self.id == defaults._wall_creation_event_:
                try:
                    folder = prefs.asset(asset).folder
                    os.startfile(folder)
                except:
                    logger.warning("Can't open that, please access via wizard project tree !")

    def show_options_menu(self):
        self.options_widget = options_widget.Main()
        self.options_widget.add_item('Explorer', self.explorer)
        build.launch_options(self.options_widget)
