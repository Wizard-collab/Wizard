 # -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import pyqtSignal
from gui.wall_widget import Ui_Form
from wizard.tools import log
from wizard.asset import main as asset_core
from wizard.prefs.main import prefs
from wizard.vars import defaults
from wizard.project.wall import wall
import traceback
from gui import build
import wall_event_widget
from time import strftime
from gui.date_widget import Ui_Date_widget
from gui.seen_widget import Ui_Seen_widget
import popup
from wizard.chat.client import client
import dialog_comment

logger = log.pipe_log(__name__)

prefs = prefs()

class Main(QtWidgets.QWidget):

    refresh_signal = pyqtSignal(int)

    def __init__(self, parent, asset=None, user=None):
        super(Main, self).__init__()
        # Build the ui from ui converted file
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.asset = asset
        self.user = user
        self.parent = parent
        self.count = 20
        self.wall = wall()
        self.continuity = None
        self.previous_widget = None
        self.previous_event = None
        self.first_widget = None
        self.all_widgets = []
        self.creation_widgets = []
        self.publish_widgets = []
        self.remove_widgets = []
        self.new_widgets = []
        self.new_notif_widget = None
        self.init_wall()
        self.start_wall()
        self.connect_functions()

    def refresh(self, asset):
        QApplication.processEvents()
        self.asset = asset
        self.clear_wall()
        self.init_wall()

    def clear_wall(self):
        for i in reversed(range(self.ui.verticalLayout_10.count())):
            widget = self.ui.verticalLayout_10.itemAt(i).widget()
            if widget:
                widget.setParent(None)
        self.continuity = None
        self.previous_widget = None
        self.previous_event = None
        self.first_widget = None
        self.all_widgets = []
        self.creation_widgets = []
        self.publish_widgets = []
        self.remove_widgets = []
        self.new_widgets = []
        self.new_notif_widget = None

    def init_wall(self):
        if self.asset and self.asset.name:
            keys_list = prefs.asset(self.asset).events
            environment = f'{self.asset.domain} - {self.asset.category} - {self.asset.name}'
        elif self.user:
            keys_list = prefs.events
            environment = prefs.user
        else:
            keys_list = wall().get_all_keys()
            environment = prefs.project_name
        settings = wall().open_wall_file()
        keys_list = keys_list[-self.count:]

        self.ui.wall_environment_label_2.setText(environment)
        self.ui.notif_image_label.setPixmap(
            QtGui.QPixmap(defaults._wall_icon_).scaled(35, 35, QtCore.Qt.KeepAspectRatio,
                                                       QtCore.Qt.SmoothTransformation))

        if len(keys_list) >= 1:
            for key in keys_list:
                if key in settings.keys():
                    event = settings[key]
                    self.build_wall_event(event, 0, 0)
                else:
                    pass

    def refresh_wall(self):
        creation = self.ui.creation_filter_pushButton.isChecked()
        publish = self.ui.publish_filter_pushButton.isChecked()
        remove = self.ui.remove_filter_pushButton.isChecked()
        new = self.ui.new_filter_pushButton.isChecked()
        for widget in self.creation_widgets:
            is_new = 1
            if new:
                is_new = (widget in self.new_widgets)
            widget.setVisible(creation * is_new)
        for widget in self.publish_widgets:
            is_new = 1
            if new:
                is_new = (widget in self.new_widgets)
            widget.setVisible(publish * is_new)
        for widget in self.remove_widgets:
            is_new = 1
            if new:
                is_new = (widget in self.new_widgets)
            widget.setVisible(remove * is_new)

    def start_wall(self):
        try:
            if not self.asset and not self.user:
                self.client = client()
                self.client.start()
                self.client.receive.connect(self.build_wall_event)
                self.client.stopped.connect(self.restart)
        except:
            logger.critical(str(traceback.format_exc()))

    def new_user_pop(self, message):
        popup.popup().new_chat_user_pop(message)

    def restart(self):
        self.client.quit()
        self.start_wall()

    def closeEvent(self, event):
        event.ignore()
        self.hide()

    def build_wall_event(self, event=None, pop=1, new=1):
        try:
            user = self.wall.get_user(event)
            date = self.wall.get_date(event)
            message = self.wall.get_message(event)
            id = self.wall.get_id(event)
            time_id = self.wall.get_time_id(event)
            asset = self.wall.get_asset(event)
            if self.previous_widget and date:
                if strftime("%d", self.previous_widget.date) != strftime("%d", date):
                    self.continuity = 0
                else:
                    previous_hour = int(strftime("%H", self.previous_widget.date))
                    hour = int(strftime("%H", date))
                    if (previous_hour < 8) and (hour > 8):
                        self.continuity = 0
                    elif (previous_hour < 22) and (hour > 22):
                        self.continuity = 0
                    else:
                        self.continuity = 1
            else:
                self.continuity = 0

            if not self.continuity and date:
                self.date_widget = Date_widget(strftime("%A %B, %d %Y", date), strftime("%H", date))
                self.ui.verticalLayout_10.addWidget(self.date_widget)

            if user and date and message and id:
                widget = wall_event_widget.Main(user, date, message, id, time_id, asset)
                if not self.continuity:
                    self.first_widget = widget
                self.previous_widget = widget
                if id == defaults._wall_creation_event_:
                    self.creation_widgets.append(widget)
                elif id == defaults._wall_publish_event_:
                    self.publish_widgets.append(widget)
                elif id == defaults._wall_remove_event_:
                    self.remove_widgets.append(widget)
                if not self.user and new:
                    if user != prefs.user:
                        self.parent.update_tree()
                        self.parent.asset_item_changed()
                    self.parent.user_widget.refresh_widget()
                    if not self.isVisible() and new:
                        self.parent.new_notif()
                        if not self.new_notif_widget:
                            self.new_notif_widget = Seen_widget()
                            self.ui.verticalLayout_10.addWidget(self.new_notif_widget)
                            self.new_widgets = []
                self.new_widgets.append(widget)
                self.all_widgets.append(widget)
                self.ui.verticalLayout_10.addWidget(widget)
                self.refresh_wall()
                self.refresh_signal.emit(1)

                if pop and not self.asset and not self.user:
                    if id == defaults._wall_creation_event_:
                        self.parent.ui.treeWidget.refresh_asset(asset_core.string_to_asset(asset))
                        
                        popup.popup().creation_pop(f'{user} {message}')
                    elif id == defaults._wall_remove_event_:
                        popup.popup().remove_pop(f'{user} {message}')
                    elif id == defaults._wall_publish_event_:
                        if user == prefs.user:
                            asset = asset_core.string_to_asset(asset)
                        popup.popup().publish_pop(f'{user} {message}')
                    elif id == defaults._wall_xp_event_:
                        popup.popup().xp_pop(f'{user} {message}')
                    elif id == defaults._wall_playblast_event_:
                        popup.popup().playblast_pop(f'{user} {message}')
                    elif id == defaults._wall_ticket_event_:
                        if prefs.user in message:
                            popup.popup().ticket_pop(f'{user} {message}')
                    elif id == defaults._wall_close_ticket_event_:
                        if prefs.user in message:
                            popup.popup().closed_ticket_pop(f'{user} {message}')
        except:
            logger.critical(str(traceback.format_exc()))

    def connect_functions(self):
        area_scroll_bar = self.ui.wall_scrollArea.verticalScrollBar()
        area_scroll_bar.rangeChanged.connect(lambda: area_scroll_bar.setValue(area_scroll_bar.maximum()))
        self.ui.creation_filter_pushButton.clicked.connect(self.refresh_wall)
        self.ui.publish_filter_pushButton.clicked.connect(self.refresh_wall)
        self.ui.remove_filter_pushButton.clicked.connect(self.refresh_wall)
        self.ui.new_filter_pushButton.clicked.connect(self.refresh_wall)

    def add_comment(self, asset):
        self.dialog_comment = dialog_comment.Main(asset)
        build.launch_dialog_comment(self.dialog_comment)


class Date_widget(QtWidgets.QWidget):

    def __init__(self, date, hour):
        super(Date_widget, self).__init__()
        self.ui = Ui_Date_widget()
        self.ui.setupUi(self)
        icon = defaults._night_icon_
        if 8 < int(hour) < 22:
            icon = defaults._day_icon_
        self.ui.message_date_label.setText(date)
        self.ui.date_logo_label.setPixmap(
            QtGui.QPixmap(icon).scaled(16, 16, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))


class Seen_widget(QtWidgets.QWidget):

    def __init__(self):
        super(Seen_widget, self).__init__()
        self.ui = Ui_Seen_widget()
        self.ui.setupUi(self)
        self.ui.seen_logo_label.setPixmap(QtGui.QPixmap(defaults._new_notif_).scaled(20, 20, QtCore.Qt.KeepAspectRatio,
                                                                                     QtCore.Qt.SmoothTransformation))
