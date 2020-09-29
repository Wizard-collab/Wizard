from PyQt5 import QtWidgets, QtCore, QtGui

from gui.delete_asset_dialog import Ui_Dialog
from wizard.vars import defaults
from wizard.tools import log

logger = log.pipe_log(__name__)


class Main(QtWidgets.QDialog):

    def __init__(self):
        super(Main, self).__init__()
        # Build the ui from ui converted file
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.add_image()

        self.shadow = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(8)
        self.shadow.setColor(QtGui.QColor(0, 0, 0, 180))
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.ui.delete_asset_frame.setGraphicsEffect(self.shadow)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def add_image(self):
        self.ui.delete_asset_image_label.setPixmap(
            QtGui.QPixmap(defaults._trash_large_icon_).scaled(50, 50, QtCore.Qt.KeepAspectRatio,
                                                               QtCore.Qt.SmoothTransformation))
