from PyQt5 import QtWidgets, QtCore, QtGui

import time
from gui.jokes_widget import Ui_Form
from gui import build
from wizard.vars import defaults
from wizard.tools import log
from wizard.prefs.jokes import jokes
import add_joke_ui
import random
import ui_jokes_user_list
import traceback

logger = log.pipe_log(__name__)


class Main(QtWidgets.QWidget):

    def __init__(self):
        super(Main, self).__init__()
        # Build the ui from ui converted file
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.displayed_jokes_list = []
        self.current_joke = None
        self.star_1 = self.ui.star1_pushButton
        self.star_2 = self.ui.star2_pushButton
        self.star_3 = self.ui.star3_pushButton
        self.star_4 = self.ui.star4_pushButton
        self.star_5 = self.ui.star5_pushButton
        self.star_1.star_name = defaults._star1_
        self.star_2.star_name = defaults._star2_
        self.star_3.star_name = defaults._star3_
        self.star_4.star_name = defaults._star4_
        self.star_5.star_name = defaults._star5_
        self.star_1.star_note = 1
        self.star_2.star_note = 2
        self.star_3.star_note = 3
        self.star_4.star_note = 4
        self.star_5.star_note = 5
        self.stars_list = [self.star_1, self.star_2, self.star_3, self.star_4, self.star_5]
        self.read_jokes()
        self.set_icons()
        self.init_stars()
        # self.refresh_stars()
        self.show_new_joke()
        self.connect_functions()

    def set_icons(self):
        self.ui.previous_joke_pushButton.setIcon(QtGui.QIcon(defaults._previous_icon_))
        self.ui.next_joke_pushButton.setIcon(QtGui.QIcon(defaults._next_icon_))
        self.ui.add_joke_pushButton.setIcon(QtGui.QIcon(defaults._add_icon_))
        self.ui.user_jokes_pushButton.setIcon(QtGui.QIcon(defaults._user_icon_))
        self.ui.user_jokes_pushButton.setIconSize(QtCore.QSize(10, 10))
        self.ui.high_quote_label.setPixmap(
            QtGui.QPixmap(defaults._high_quote_icon_).scaled(30, 30, QtCore.Qt.KeepAspectRatio,
                                                             QtCore.Qt.SmoothTransformation))
        self.ui.low_quote_label.setPixmap(
            QtGui.QPixmap(defaults._low_quote_icon_).scaled(30, 30, QtCore.Qt.KeepAspectRatio,
                                                            QtCore.Qt.SmoothTransformation))

    def read_jokes(self):
        self.jokes = jokes().get_jokes_list()

    def show_new_joke(self):
        self.jokes = jokes().get_jokes_list()
        if self.jokes:
            index = random.randint(0, len(self.jokes) - 1)
            joke_id = self.jokes[index]
            self.refresh_joke(joke_id)

    def refresh_joke(self, joke_id=None):
        if not joke_id:
            joke_id = self.current_joke
        joke_data = jokes().get_joke_data(joke_id)
        joke_note = jokes().get_joke_note(joke_id)

        self.current_joke = joke_id
        self.displayed_jokes_list.append(joke_id)

        self.ui.joke_label.setText(joke_data)
        self.ui.float_note_label.setText(str(round(joke_note, 1)) + '/5')
        self.refresh_stars(joke_note)

    def init_stars(self):
        for star in self.stars_list:
            star.setIconSize(QtCore.QSize(16, 16))

    def refresh_stars(self, note):
        note = int(round(note + 0.1))
        for star in self.stars_list:
            state = defaults._star_empty_icon_
            if star.star_name in defaults._stars_states_dic_[note]:
                state = defaults._star_full_icon_
            star.setIcon(QtGui.QIcon(state))

    def note_joke(self, note):
        if self.jokes:
            jokes().add_note(self.current_joke, note)
            self.refresh_joke()

    def launch_add_joke_ui(self):
        self.add_joke_ui = add_joke_ui.Main()
        if build.launch_dialog_as_child(self.add_joke_ui):
            joke_data = self.add_joke_ui.joke
            joke_id = jokes().add_joke(joke_data)
            self.refresh_joke(joke_id)

    def launch_jokes_user_list(self):
        try:
            self.ui_jokes_user_list = ui_jokes_user_list.Main()
            build.launch_normal_as_child(self.ui_jokes_user_list)
        except:
            logger.critical(str(traceback.format_exc()))

    def connect_functions(self):
        self.star_1.clicked.connect(lambda: self.note_joke(1))
        self.star_2.clicked.connect(lambda: self.note_joke(2))
        self.star_3.clicked.connect(lambda: self.note_joke(3))
        self.star_4.clicked.connect(lambda: self.note_joke(4))
        self.star_5.clicked.connect(lambda: self.note_joke(5))
        self.ui.next_joke_pushButton.clicked.connect(self.show_new_joke)
        self.ui.add_joke_pushButton.clicked.connect(self.launch_add_joke_ui)
        self.ui.user_jokes_pushButton.clicked.connect(self.launch_jokes_user_list)


class jokes_thread(QtCore.QThread):
    def __init__(self, jokes_widget):
        super().__init__()
        self.jokes_widget = jokes_widget
        self.running = True

    def run(self):
        while self.running:
            time.sleep(60)
            self.jokes_widget.show_new_joke()

    def stop(self):
        self.running=False
