from PyQt5 import QtWidgets, QtCore, QtGui
from gui.save_popup_widget import Ui_Form
from gui import build
import sys
from playsound import playsound
from wizard.vars import defaults
from wizard.tools import log
from wizard.prefs.user import user

logger = log.pipe_log(__name__)


class popup(QtWidgets.QWidget):
    popuphidden = QtCore.pyqtSignal()

    def __init__(self, time=4000, sound=1):

        super(popup, self).__init__()

        self.user = user()
        self.time = time
        self.sound = sound

        # Build the ui from ui converted file
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.setup_infos()

        self.setWindowFlags(QtCore.Qt.SplashScreen | QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.animation = QtCore.QPropertyAnimation(self, b"windowOpacity", self)
        self.displace_animation = QtCore.QPropertyAnimation(self, b"pos", self)
        self.animation.finished.connect(self.hide)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.hideAnimation)

    def setup_infos(self):
        self.gif = QtGui.QMovie(defaults._check_icon_)
        self.ui.popup_image_label.setMovie(self.gif)
        self.gif.setSpeed(200)
        size = QtCore.QSize(74, 74)
        self.gif.setScaledSize(size)
        self.gif.start()

    def show(self):
        self.setWindowOpacity(0.0)
        self.animation.setDuration(100)
        self.displace_animation.setDuration(100)

        self.animation.setStartValue(0.0)
        self.displace_animation.setStartValue(QtCore.QPointF(self.init_x, self.init_y))
        self.animation.setEndValue(1.0)
        self.displace_animation.setEndValue(QtCore.QPointF(self.end_x, self.end_y))

        QtWidgets.QWidget.show(self)
        self.animation.start()
        self.displace_animation.start()
        self.timer.start(self.time)

    def hideAnimation(self):
        self.timer.stop()
        self.animation.setDuration(100)
        self.displace_animation.setDuration(100)
        self.animation.setStartValue(1.0)
        self.displace_animation.setStartValue(QtCore.QPointF(self.end_x, self.end_y))
        self.animation.setEndValue(0.0)
        self.displace_animation.setEndValue(QtCore.QPointF(self.init_x, self.init_y))
        self.animation.start()
        self.displace_animation.start()

    def hide(self):
        if self.windowOpacity() == 0:
            QtWidgets.QWidget.hide(self)
            self.popuphidden.emit()
            if __name__ == '__main__':
                sys.exit()

    def get_initial_pos(self):
        screen_geometry = QtWidgets.QApplication.desktop().availableGeometry()
        screen_size = (screen_geometry.width(), screen_geometry.height())
        win_size = (self.frameSize().width(), self.frameSize().height())
        position = (self.user.get_popup_prefs())[defaults._popup_position_key_]
        if position == defaults._bt_r_key_ or position == defaults._tp_r_key_:
            x = screen_size[0] - win_size[0] + 300
        else:
            x = - 300
        if position == defaults._bt_l_key_ or position == defaults._bt_r_key_:
            y = screen_size[1] - win_size[1] - 20
        else:
            y = 20
        self.init_x = x
        self.init_y = y

    def get_end_pos(self):
        screen_geometry = QtWidgets.QApplication.desktop().availableGeometry()
        screen_size = (screen_geometry.width(), screen_geometry.height())
        win_size = (self.frameSize().width(), self.frameSize().height())
        position = (self.user.get_popup_prefs())[defaults._popup_position_key_]
        if position == defaults._bt_r_key_ or position == defaults._tp_r_key_:
            x = screen_size[0] - win_size[0] - 20
        else:
            x = 20
        if position == defaults._bt_l_key_ or position == defaults._bt_r_key_:
            y = screen_size[1] - win_size[1] - 20
        else:
            y = 20
        self.end_x = x
        self.end_y = y

    def move2ScreenBottom(self):
        try:
            screen_geometry = QtWidgets.QApplication.desktop().availableGeometry()
            screen_size = (screen_geometry.width(), screen_geometry.height())
            win_size = (self.frameSize().width(), self.frameSize().height())
            position = (self.user.get_popup_prefs())[defaults._popup_position_key_]
            if position == defaults._bt_r_key_ or position == defaults._tp_r_key_:
                x = screen_size[0] - win_size[0] - 20
            else:
                x = 20
            if position == defaults._bt_l_key_ or position == defaults._bt_r_key_:
                y = screen_size[1] - win_size[1] - 20
            else:
                y = 20
            self.move(x, y)
            self.get_initial_pos()
            self.get_end_pos()
        except Exception as e:
            print(e)

    def pop(self):
        if self.sound:
            popup_dic = self.user.get_popup_prefs()
            sound_file = defaults._pop_sounds_dic_[popup_dic[defaults._popup_sound_file_key_]]
            playsound(sound_file, False)
        build.launch_popup(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = popup()
    main_window.move2ScreenBottom()
    main_window.show()

    sys.exit(app.exec_())
