import getpass
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QFileDialog

from gui.new_user_dialog import Ui_Dialog
from gui import build
from wizard.prefs.site import site
from wizard.prefs.stats import stats
import dialog_confirm_email
from wizard.email import main as send_email
import random
import time
from wizard.tools import log
from gui import log_to_gui
from wizard.vars import defaults
from wizard.prefs.main import prefs
from wizard.tools import utility as utils

logger = log.pipe_log(__name__)

prefs = prefs()

class Main(QtWidgets.QDialog):

    def __init__(self):
        super(Main, self).__init__()
        # Build the ui from ui converted file
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.site = site()
        self.image_file = None
        self.get_session_name()
        self.connect_functions()
        self.refresh_promos()
        self.init_avatar_button()
        self.init_show_pass_icon()
        self.avatar = 0
        qtHandler = log_to_gui.log_viewer(self.ui)
        logger.main_logger.addHandler(qtHandler)
        self.show = 0

    def refresh_promos(self):
        for promo in defaults._promotions_list_:
            self.ui.class_comboBox.addItem(promo)

    def get_session_name(self):
        user_name = getpass.getuser()
        if user_name:
            self.ui.user_name_lineEdit.setText(user_name)

    def init_show_pass_icon(self):
        self.ui.show_pass_pushButton.setIcon(QtGui.QIcon(defaults._hide_icon_))
        self.ui.show_pass_pushButton.setIconSize(QtCore.QSize(15, 15))

    def connect_functions(self):
        self.ui.create_user_button.clicked.connect(self.create_user)
        self.ui.confirm_lineEdit.textChanged.connect(self.check_confirm)
        self.ui.password_lineEdit.textChanged.connect(self.check_confirm)
        self.ui.show_pass_pushButton.clicked.connect(self.show_passwords)
        self.ui.avatar_pushButton.clicked.connect(self.open_image)
        self.ui.admin_checkBox.stateChanged.connect(self.admin_request)

    def admin_request(self):
        if self.ui.admin_checkBox.isChecked():
            temp_pass = defaults._admin_key_
            self.dialog_confirm_email = dialog_confirm_email.Main(self, temp_pass)
            self.dialog_confirm_email.ui.recover_pushButton.setVisible(0)
            self.dialog_confirm_email.ui.confirm_email_title_label.setText('Enter the administrator password')
            if build.launch_dialog_as_child(self.dialog_confirm_email):
                logger.info("Admin verified !")
                self.ui.admin_checkBox.setChecked(1)
            else:
                self.ui.admin_checkBox.setCheckState(0)

    def create_user(self):
        user_name = self.ui.user_name_lineEdit.text()
        promotion = self.ui.class_comboBox.currentText()
        email = self.ui.user_email_lineEdit.text()
        full_name = self.ui.full_name_lineEdit.text()
        password = self.ui.password_lineEdit.text()
        admin = self.ui.admin_checkBox.isChecked()
        if not self.check_confirm():
            logger.error("Passwords doesn't matches...")
        elif not self.image_file:
            logger.error("Please choose an avatar")
        else:
            QApplication.processEvents()
            self.ui.create_user_button.setText('Checking email...')
            QApplication.processEvents()
            if self.confirm_email(user_name, email, full_name):
                QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
                QApplication.processEvents()
                self.ui.create_user_button.setText('Creating user...')
                QApplication.processEvents()
                if self.site.create_user(user_name, promotion, email, password, admin, full_name):
                    QApplication.processEvents()
                    stats(user_name).create_user(self.image_file)
                    QApplication.processEvents()
                    QApplication.restoreOverrideCursor()
                    QApplication.processEvents()
                    self.ui.create_user_button.setText('Created !')
                    QApplication.processEvents()
                    time.sleep(1)
                    QApplication.processEvents()
                    prefs.set_user(user_name)
                    self.accept()

    def open_image(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Images Files (*.png);;Images Files (*.jpg);;Images Files (*.jpeg)", options=options)
        if fileName:
            if (fileName.split('.')[-1].upper() == 'PNG') or (fileName.split('.')[-1].upper() == 'JPG') or (fileName.split('.')[-1].upper() == 'JPEG'):
                self.image_file = fileName
                self.round_image(self.ui.avatar_pushButton, fileName)
            else:
                logger.warning('{} is not a valid image file...'.format(fileName))

    def show_passwords(self):
        if self.show == 0:
            self.ui.confirm_lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.ui.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.ui.show_pass_pushButton.setIcon(QtGui.QIcon(defaults._show_icon_))
            self.show = 1
        else:
            self.ui.confirm_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
            self.ui.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
            self.ui.show_pass_pushButton.setIcon(QtGui.QIcon(defaults._hide_icon_))
            self.show = 0

    def check_confirm(self):
        password = self.ui.password_lineEdit.text()
        confirm = self.ui.confirm_lineEdit.text()
        if confirm != password:
            self.ui.confirm_lineEdit.setStyleSheet('border:1px solid Red;')
            return 0
        else:
            self.ui.confirm_lineEdit.setStyleSheet('border:1px solid Green;')
            return 1

    def init_avatar_button(self):
        self.ui.avatar_pushButton.setIconSize(QtCore.QSize(140, 140))
        self.round_image(self.ui.avatar_pushButton, defaults._neutral_avatar_)
        self.image_file = defaults._neutral_avatar_

    def round_image(self, label, image):
        label.Antialiasing = True
        label.radius = 75

        label.target = QtGui.QPixmap(label.size())
        label.target.fill(QtCore.Qt.transparent)

        p = QtGui.QPixmap(image).scaled(
            150, 150, QtCore.Qt.KeepAspectRatioByExpanding, QtCore.Qt.SmoothTransformation)

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

    def confirm_email(self, user, email, full_name):
        temp_pass = str(random.randint(1000,9999))
        send_email.send_confirm(user, email, temp_pass, full_name)
        self.dialog_confirm_email = dialog_confirm_email.Main(self, temp_pass)
        if build.launch_dialog_as_child(self.dialog_confirm_email):
            logger.info("Email verified !")
            return 1
        else:
            return 0
