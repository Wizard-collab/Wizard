from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QFileDialog
from gui.preferences import Ui_Form
from gui import build
from wizard.vars import defaults
from wizard.tools import log
from wizard.prefs.user import user
from wizard.prefs.site import site
from wizard.prefs.main import prefs
from playsound import playsound
import ui_recover_password
from wizard.tools import password as pwd

logger = log.pipe_log(__name__)

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
        self.init_listWidget()
        self.init_show_pass_icon()

    def init_listWidget(self):
        self.ui.preferences_ui_listWidget.FocusPolicy = QtCore.Qt.NoFocus
        self.ui.preferences_ui_listWidget.setCurrentRow(0)
        self.ui.preferences_ui_listWidget.currentRowChanged.connect(self.ui.stackedWidget.setCurrentIndex)

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
        server_ip = prefs.server_ip
        self.ui.versions_updates_checkBox.setChecked(show_updates)
        #self.ui.new_version_checkBox.setChecked(show_new_version)
        #self.ui.error_handler_checkBox.setChecked(1-show_error_handler)
        self.ui.local_project_path_lineEdit.setText(local_project_path)
        self.ui.shutter_checkBox.setChecked(shutter)
        self.ui.preferences_server_ip_lineEdit.setText(server_ip)

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
        local_project_path = self.ui.local_project_path_lineEdit.text()
        shutter = self.ui.shutter_checkBox.isChecked()
        server_ip = self.ui.preferences_server_ip_lineEdit.text()
        prefs.set_show_updates(show_updates)
        prefs.set_local_project_path(local_project_path)
        prefs.set_shutter(shutter)
        prefs.set_server_ip(server_ip)

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
        self.ui.change_password_pushButton.clicked.connect(self.change)
        self.ui.confirm_lineEdit.textChanged.connect(self.check_confirm)
        self.ui.new_lineEdit.textChanged.connect(self.check_confirm)
        self.ui.show_pass_pushButton.clicked.connect(self.show_passwords)
        self.ui.recover_pushButton.clicked.connect(self.recover)

    def init_show_pass_icon(self):
            self.show_pw = 0
            self.ui.show_pass_pushButton.setIcon(QtGui.QIcon(defaults._hide_icon_))
            self.ui.show_pass_pushButton.setIconSize(QtCore.QSize(15, 15))

    def change(self):
        old_pass = self.ui.old_lineEdit.text()
        user = self.user.get_user()
        if not site().password_check(user, old_pass):
            logger.error('Wrong password...')
        elif not self.check_confirm():
            logger.error("Passwords doesn't matches...")
        else:
            QApplication.processEvents()
            QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
            self.ui.change_password_pushButton.setText('Changing password...')
            QApplication.processEvents()
            new_pass = self.ui.new_lineEdit.text()
            encrypted_pass = pwd.encrypt(new_pass)
            site().change_user_password(user, encrypted_pass)
            QApplication.processEvents()
            logger.info('Password changed !')
            QApplication.processEvents()
            self.ui.change_password_pushButton.setText('Password changed !')
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            QApplication.processEvents()

    def recover(self):
        self.ui_recover_password = ui_recover_password.Main(self)
        build.launch_dialog_as_child(self.ui_recover_password)

    def show_passwords(self):
        if self.show_pw == 0:
            self.ui.confirm_lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.ui.new_lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.ui.old_lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.ui.show_pass_pushButton.setIcon(QtGui.QIcon(defaults._show_icon_))
            self.show_pw = 1
        else:
            self.ui.confirm_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
            self.ui.new_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
            self.ui.old_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
            self.ui.show_pass_pushButton.setIcon(QtGui.QIcon(defaults._hide_icon_))
            self.show_pw = 0

    def check_confirm(self):
        password = self.ui.new_lineEdit.text()
        confirm = self.ui.confirm_lineEdit.text()
        if confirm != password:
            self.ui.confirm_lineEdit.setStyleSheet('border:1px solid Red;')
            return 0
        else:
            self.ui.confirm_lineEdit.setStyleSheet('border:1px solid Green;')
            return 1