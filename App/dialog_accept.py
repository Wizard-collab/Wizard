from PyQt5 import QtWidgets, QtCore, QtGui

from gui.accept_dialog import Ui_Dialog
from wizard.tools import log

logger = log.pipe_log()


class Main(QtWidgets.QDialog):

    def __init__(self, title, text, icon=None):
        super(Main, self).__init__()
        # Build the ui from ui converted file
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle(title)

        self.ui.accept_widget_label.setText(text)
        if icon:
            self.ui.accept_widget_image_label.setPixmap(
                QtGui.QPixmap(icon).scaled(60, 60, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
        else:
            self.ui.accept_widget_image_label.hide()

    def closeEvent(self, event):
        event.ignore()
        self.hide()
