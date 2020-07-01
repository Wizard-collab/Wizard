from PyQt5 import QtWidgets, QtCore, QtGui

from gui.image_viewer import Ui_Form


class Main(QtWidgets.QWidget):

    def __init__(self, image):
        super(Main, self).__init__()
        # Build the ui from ui converted file
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.image = image
        self.load_image()

    def mousePressEvent(self, event):
        self.hide()

    def closeEvent(self, event):
        event.ignore()
        self.hide()

    def load_image(self):
        self.ui.image_label.setPixmap(
            QtGui.QPixmap(self.image).scaled(1371, 857, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
