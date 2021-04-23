from PyQt5 import QtWidgets, QtCore, QtGui
from wizard.vars import defaults
from wizard.prefs.user import user

class recording_ui(QtWidgets.QWidget):
    def __init__(self):
        super(recording_ui, self).__init__()
        self.setMaximumSize(QtCore.QSize(80,80))
        self.setMinimumSize(QtCore.QSize(80,80))
        self.resize(QtCore.QSize(80,80))
        self.build_ui()
        self.move_ui()

    def build_ui(self):
        self.layout = QtWidgets.QHBoxLayout()
        self.layout.setContentsMargins(0,0,0,0)
        self.frame = QtWidgets.QFrame()
        self.frameLayout = QtWidgets.QHBoxLayout()
        self.frame.setObjectName('recording_ui_frame')
        self.frameLayout.setContentsMargins(0,0,0,0)
        self.frame.setLayout(self.frameLayout)
        self.label = QtWidgets.QLabel()
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.setLayout(self.layout)
        self.layout.addWidget(self.frame)
        self.frameLayout.addWidget(self.label)

        self.gif = QtGui.QMovie(defaults._record_gif_)
        #self.gif.setSpeed(150)
        size = QtCore.QSize(50, 50)
        self.gif.setScaledSize(size)
        self.gif.start()

        self.label.setMovie(self.gif)
        #self.label.setPixmap(QtGui.QPixmap(defaults._start_record_icon_).scaled(50, 50, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))

    def move_ui(self):
        screen_geometry = QtWidgets.QApplication.desktop().availableGeometry()
        screen_size = (screen_geometry.width(), screen_geometry.height())
        win_size = (self.frameSize().width(), self.frameSize().height())
        position = (user().get_popup_prefs())[defaults._popup_position_key_]
        if position == defaults._bt_r_key_ or position == defaults._tp_r_key_:
            x = screen_size[0] - win_size[0] - 20
        else:
            x = 20
        if position == defaults._bt_l_key_ or position == defaults._bt_r_key_:
            y = screen_size[1] - win_size[1] - 20
        else:
            y = 20
        self.move(x, y)