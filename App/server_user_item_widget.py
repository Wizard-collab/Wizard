from PyQt5 import QtWidgets, QtCore, QtGui

from gui.server_user_item_widget import Ui_Form
from wizard.vars import defaults
from wizard.tools import log

from wizard.prefs.stats import stats

logger = log.server_log()


class Main(QtWidgets.QWidget):

    def __init__(self, user, addr):
        super(Main, self).__init__()
        # Build the ui from ui converted file
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.server_user_name_label.setText('{} - adress : {}'.format(user, addr))
        self.ui.server_user_item_conn_label.setPixmap(
            QtGui.QPixmap(defaults._server_icon_).scaled(20, 20, QtCore.Qt.KeepAspectRatio,
                                                         QtCore.Qt.SmoothTransformation))
        user_image = stats(user).get_avatar()
        self.round_image(self.ui.server_user_image_label, user_image)

    def round_image(self, label, image):
        label.Antialiasing = True
        label.radius = 13

        label.target = QtGui.QPixmap(label.size())
        label.target.fill(QtCore.Qt.transparent)

        p = QtGui.QPixmap(image).scaled(
            26, 26, QtCore.Qt.KeepAspectRatioByExpanding, QtCore.Qt.SmoothTransformation)

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
