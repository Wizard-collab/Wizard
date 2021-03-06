# coding: utf8

# Import PyQt5 libraries
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QFileDialog

# Import wizard gui libraries
from gui.user_widget import Ui_Form
from gui import build

# Import wizard core libraries
from wizard.vars import defaults
from wizard.tools import log
from wizard.prefs.main import prefs
from wizard.prefs.stats import stats
from wizard.asset.tickets import tickets
from wizard.signal import send_signal
from wizard.tools import utility as utils

# Import wizard widgets
import wall_widget
import tickets_widget

# Init the main logger and prefs module
logger = log.pipe_log(__name__)
pref = prefs()

class Main(QtWidgets.QWidget):

    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.init_icons()
        self.refresh_widget()
        self.connect_functions()

    def init_icons(self):
        self.ui.level_label.setPixmap(QtGui.QPixmap(defaults._lvl_icon_).scaled(16, 16, QtCore.Qt.KeepAspectRatio,
                                                                                QtCore.Qt.SmoothTransformation))
        self.ui.xp_label.setPixmap(
            QtGui.QPixmap(defaults._xp_icon_).scaled(16, 16, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
        self.ui.stats_pushButton.setIcon(QtGui.QIcon(defaults._user_events_icon_))
        self.ui.user_tickets_pushButton.setIcon(QtGui.QIcon(defaults._gray_ticket_icon_))
        self.ui.stats_pushButton.setIconSize(QtCore.QSize(14, 14))
        self.ui.user_tickets_pushButton.setIconSize(QtCore.QSize(14, 14))

    def refresh_widget(self):
        self.ui.user_name_label.setText(pref.user)
        user_image = stats(pref.user).get_avatar()
        user_promotion = pref.promotion
        is_admin = pref.admin
        if is_admin:
            self.ui.admin_image_label.setVisible(1)
            self.ui.admin_image_label.setPixmap(
                QtGui.QPixmap(defaults._key_icon_).scaled(16, 16, QtCore.Qt.KeepAspectRatio,
                                                          QtCore.Qt.SmoothTransformation))
        else:
            self.ui.admin_image_label.setVisible(0)
            self.ui.admin_image_label.setPixmap(QtGui.QPixmap(''))
        self.ui.promotion_label.setText(user_promotion)
        level = stats(pref.user).get_level()
        xp = float(stats(pref.user).get_xp())
        self.ui.user_image_pushButton.setIconSize(QtCore.QSize(64, 64))
        self.ui.user_image_pushButton.setIcon(QtGui.QIcon(user_image))
        self.round_image(self.ui.user_image_pushButton, user_image)
        self.ui.level_label_number.setText(level)
        self.ui.xp_progressBar.setValue(xp)
        self.check_opened_tickets()

    def show_user_wall(self):
        self.user_wall = wall_widget.Main(self, user=1)
        build.launch_normal_as_child(self.user_wall)

    def connect_functions(self):
        self.ui.user_image_pushButton.clicked.connect(self.change_avatar)
        self.ui.user_tickets_pushButton.clicked.connect(self.show_tickets)
        self.ui.stats_pushButton.clicked.connect(self.show_user_wall)

    def show_tickets(self):
        self.tickets_widget = tickets_widget.Main(user=1)
        self.tickets_widget.refresh_all(asset = None)
        build.launch_normal_as_child(self.tickets_widget)

    def change_avatar(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            if fileName.split('.')[-1].upper() == 'PNG' or fileName.split('.')[-1].upper() == 'JPG' or fileName.split('.')[-1].upper() == 'JPEG':
                stats().add_avatar(fileName)
                self.refresh_widget()
            else:
                logger.warning('Please select a valid image !')

    def round_image(self, label, image):
        label.Antialiasing = True
        label.radius = 35
        label.target = QtGui.QPixmap(label.size())
        label.target.fill(QtCore.Qt.transparent)
        p = QtGui.QPixmap(image).scaled(
            70, 70, QtCore.Qt.KeepAspectRatioByExpanding, QtCore.Qt.SmoothTransformation)
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

    def check_opened_tickets(self):
        ''' Change tickets button icon if some are adressed to user. '''
        self.tickets = tickets()
        self.tickets.open()
        tickets_data = self.tickets.settings[defaults._all_tickets_]
        tickets_opened = 0
        for ticket in tickets_data:
            ticket_adress_to_user = tickets_data[ticket]['adress']
            ticket_state = tickets_data[ticket]['state']
            if tickets_data[ticket]['adress'] == pref.user and ticket_state == 'opened':
                tickets_opened += 1
        if tickets_opened != 0:
            self.ui.user_tickets_pushButton.setToolTip(f'{tickets_opened} ticket(s) still opened')
            self.ui.user_tickets_pushButton.setIcon(QtGui.QIcon(defaults._red_ticket_icon_))
        else:
            self.ui.user_tickets_pushButton.setToolTip(f'0 ticket still opened')
            self.ui.user_tickets_pushButton.setIcon(QtGui.QIcon(defaults._gray_ticket_icon_))
