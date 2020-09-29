from PyQt5 import QtWidgets, QtCore, QtGui
from gui.wizard_desktop import Ui_Form
from wizard.vars import defaults
from wizard.tools import log
from wizard.prefs.main import prefs

logger = log.pipe_log(__name__)

prefs = prefs()

class wizard_desktop(QtWidgets.QWidget):
    def __init__(self, main_ui):

        super(wizard_desktop, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.main_ui = main_ui
        self.main_ui.move_signal.connect(self.move2ScreenTop)
        self.displace_animation = QtCore.QPropertyAnimation(self, b"pos", self)
        self.init_y = -75
        self.end_y = -4
        self.connect_functions()

    def show_wizard(self):
        if self.main_ui.isVisible():
            self.main_ui.hide_animation()
        else:
            self.main_ui.show_animation()

    def move2ScreenTop(self):
        try:
            screen_index = prefs.screen
            monitor = QtWidgets.QDesktopWidget().screenGeometry(screen_index)
            screen_geometry = QtWidgets.QDesktopWidget().availableGeometry(screen_index)
            win_size = (self.frameSize().width(), self.frameSize().height())
            self.x_pos = monitor.left() + ((screen_geometry.width()) - win_size[0]) / 2
            self.move(self.x_pos, monitor.top() - 75)
        except Exception as e:
            print(e)

    def refresh_icon(self):
        if self.main_ui.isVisible():
            self.ui.show_wizard_pushButton.setIcon(QtGui.QIcon(defaults._hide_wizard_icon_))
        else:
            self.ui.show_wizard_pushButton.setIcon(QtGui.QIcon(defaults._show_wizard_icon_))

    def show_animation(self):
        self.refresh_icon()
        self.displace_animation.setDuration(100)
        self.displace_animation.setStartValue(QtCore.QPointF(self.x_pos, self.init_y))
        self.displace_animation.setEndValue(QtCore.QPointF(self.x_pos, self.end_y))
        self.displace_animation.start()

    def hide_animation(self):
        self.displace_animation.setDuration(100)
        self.displace_animation.setStartValue(QtCore.QPointF(self.x_pos, self.end_y))
        self.displace_animation.setEndValue(QtCore.QPointF(self.x_pos, self.init_y))
        self.displace_animation.start()
        self.refresh_icon()

    def enterEvent(self, event):
        self.show_animation()

    def leaveEvent(self, event):
        self.hide_animation()

    def connect_functions(self):
        self.ui.show_wizard_pushButton.setIcon(QtGui.QIcon(defaults._show_wizard_icon_))
        self.ui.show_wizard_pushButton.setIconSize(QtCore.QSize(30, 30))
        self.ui.show_wizard_pushButton.clicked.connect(self.show_wizard)
