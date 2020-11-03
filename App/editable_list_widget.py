from PyQt5 import QtWidgets, QtGui, QtCore
from gui.editable_list_item_widget import Ui_Form
from gui import build

class list_widget(QtWidgets.QWidget):
    def __init__(self):

        super(list_widget, self).__init__()

        # Build the ui from ui converted file
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setStyleSheet(build.load_stylesheet())

    def set_icon(self, icon):
        self.ui.icon_label.setPixmap(QtGui.QPixmap(icon).scaled(22, 22, QtCore.Qt.KeepAspectRatio,
                                                                                  QtCore.Qt.SmoothTransformation))

    def add_label(self, data, name, width = 130):
        self.add_line()
        label = QtWidgets.QLabel(self)
        label.setText(data)
        label.setMinimumSize(QtCore.QSize(width, 0))
        label.setMaximumSize(QtCore.QSize(width, 1000))
        label.setObjectName(name)
        self.ui.datas_list.addWidget(label)
        return label

    def add_line(self):
        line = QtWidgets.QFrame(self)
        line.setMaximumSize(QtCore.QSize(1, 16777215))
        line.setFrameShape(QtWidgets.QFrame.VLine)
        line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.ui.datas_list.addWidget(line)

    def add_button(self, icon):
        button = QtWidgets.QPushButton(self)
        button.setIcon(QtGui.QIcon(icon))
        button.setFixedSize(QtCore.QSize(20, 20))
        button.setIconSize(QtCore.QSize(16, 16))
        self.ui.buttons_list.addWidget(button)
        return button