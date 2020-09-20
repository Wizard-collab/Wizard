from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QFileDialog
from gui.preferences import Ui_Form
from gui import build
from wizard.vars import defaults
from wizard.tools import log
from wizard.prefs.user import user
from wizard.prefs.main import prefs
from playsound import playsound

logger = log.pipe_log()

prefs = prefs()

class Main(QtWidgets.QWidget):

    def __init__(self, main_ui):
        super(Main, self).__init__()
        # Build the ui from ui converted file
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.user = user()
        self.main_ui = main_ui
        self.popup_dic = self.user.get_popup_prefs()
        self.init_windows_prefs()
        self.connect_buttons()
        self.set_icons()

    def init_windows_prefs(self):
        self.init_screen_prefs()
        self.init_popup_prefs()
        self.init_general_prefs()

    def set_icons(self):
        self.ui.local_folder_pushButton.setIcon(QtGui.QIcon(defaults._folder_icon_))

    def closeEvent(self, event):
        event.ignore()
        self.hide()

    def init_general_prefs(self):
        show_updates = prefs.show_updates
        show_new_version = prefs.show_new_version
        show_error_handler = prefs.show_error_handler
        local_project_path = prefs.local_project_path
        shutter = prefs.shutter
        logger.info(local_project_path)
        self.ui.versions_updates_checkBox.setChecked(show_updates)
        self.ui.new_version_checkBox.setChecked(show_new_version)
        self.ui.error_handler_checkBox.setChecked(1-show_error_handler)
        self.ui.local_project_path_lineEdit.setText(local_project_path)
        self.ui.shutter_checkBox.setChecked(shutter)

    def init_screen_prefs(self):
        screen_index = prefs.screen
        screens_list = list(range(QtWidgets.QDesktopWidget().screenCount()))
        for screen in screens_list:
            self.ui.screens_comboBox.addItem(str(screen))
        index = screens_list.index(screen_index)
        self.ui.screens_comboBox.setCurrentIndex(index)

    def open_local_path_finder(self):
        project_path = QFileDialog.getExistingDirectory(self, "Choose local project directory",
                                       "/home",
                                       QFileDialog.ShowDirsOnly
                                       | QFileDialog.DontResolveSymlinks)
        if project_path:
            self.ui.local_project_path_lineEdit.setText(project_path)

    def move_main_ui(self):
        screen_index = int(self.ui.screens_comboBox.currentText())
        prefs.set_screen(screen_index)
        self.main_ui.move_window(1)

    def init_popup_prefs(self):
        enable = self.popup_dic[defaults._popup_enable_key_]
        sound = self.popup_dic[defaults._popup_sound_key_]
        sound_key = self.popup_dic[defaults._popup_sound_file_key_]
        duration = self.popup_dic[defaults._popup_duration_key_]
        creation = self.popup_dic[defaults._popup_creation_key_]
        publish = self.popup_dic[defaults._popup_publish_key_]
        save = self.popup_dic[defaults._popup_save_key_]
        message = self.popup_dic[defaults._popup_message_key_]
        position = self.popup_dic[defaults._popup_position_key_]
        sounds_keys = list(defaults._pop_sounds_dic_.keys())
        positions_keys = defaults._pop_position_dic_

        self.ui.popup_enable_checkBox.setChecked(enable)
        self.ui.popup_sound_checkBox.setChecked(sound)
        self.ui.popup_duration_spinBox.setValue(duration)
        self.ui.popup_creation_checkBox.setChecked(creation)
        self.ui.popup_publish_checkBox.setChecked(publish)
        self.ui.popup_save_checkBox.setChecked(save)
        self.ui.popup_message_checkBox.setChecked(message)
        for sound in sounds_keys:
            self.ui.popup_sounds_comboBox.addItem(sound)
        index = sounds_keys.index(sound_key)
        self.ui.popup_sounds_comboBox.setCurrentIndex(index)
        for pos in positions_keys:
            self.ui.popup_position_comboBox.addItem(pos)
        index = positions_keys.index(position)
        self.ui.popup_position_comboBox.setCurrentIndex(index)

    def play_popup_sound(self):
        QApplication.processEvents()
        playsound(self.get_popup_sound_file())

    def get_popup_sound_file(self):
        sound = self.ui.popup_sounds_comboBox.currentText()
        sound_file = defaults._pop_sounds_dic_[sound]
        return sound_file

    def set_popup_prefs(self):
        enable = self.ui.popup_enable_checkBox.isChecked()
        sound = self.ui.popup_sound_checkBox.isChecked()
        sound_key = self.ui.popup_sounds_comboBox.currentText()
        duration = int(self.ui.popup_duration_spinBox.value())
        creation = self.ui.popup_creation_checkBox.isChecked()
        publish = self.ui.popup_publish_checkBox.isChecked()
        save = self.ui.popup_save_checkBox.isChecked()
        message = self.ui.popup_message_checkBox.isChecked()
        position = self.ui.popup_position_comboBox.currentText()

        self.popup_dic[defaults._popup_enable_key_] = enable
        self.popup_dic[defaults._popup_sound_key_] = sound
        self.popup_dic[defaults._popup_sound_file_key_] = sound_key
        self.popup_dic[defaults._popup_duration_key_] = duration
        self.popup_dic[defaults._popup_creation_key_] = creation
        self.popup_dic[defaults._popup_publish_key_] = publish
        self.popup_dic[defaults._popup_save_key_] = save
        self.popup_dic[defaults._popup_message_key_] = message
        self.popup_dic[defaults._popup_position_key_] = position

        self.user.set_popup_prefs(self.popup_dic)

    def set_general_prefs(self):
        show_updates = self.ui.versions_updates_checkBox.isChecked()
        show_new_version = self.ui.new_version_checkBox.isChecked()
        show_error_handler = self.ui.error_handler_checkBox.isChecked()
        local_project_path = self.ui.local_project_path_lineEdit.text()
        shutter = self.ui.shutter_checkBox.isChecked()
        prefs.set_show_updates(show_updates)
        prefs.set_show_new_version(show_new_version)
        prefs.set_show_error_handler(1-show_error_handler)
        prefs.set_local_project_path(local_project_path)
        prefs.set_shutter(shutter)

    def save_prefs(self):
        self.set_popup_prefs()
        self.set_general_prefs()
        logger.info("Preferences successfully saved !")
        self.close()

    def connect_buttons(self):
        self.ui.save_prefs_pushButton.clicked.connect(self.save_prefs)
        self.ui.popup_sounds_comboBox.currentIndexChanged.connect(self.play_popup_sound)
        self.ui.screens_comboBox.currentIndexChanged.connect(self.move_main_ui)
        self.ui.local_folder_pushButton.clicked.connect(self.open_local_path_finder)
