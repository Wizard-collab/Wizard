from PyQt5 import QtWidgets, QtGui, QtCore

class list_widget(QtWidgets.QWidget):
    def __init__(self, asset = None, icon = None, name = None):

        super(list_widget, self).__init__()

        self.asset = asset
        self.icon = icon
        self.name = name

        self.setMinimumSize(QtCore.QSize(0, 34))
        self.setMaximumSize(QtCore.QSize(100000, 34))


        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout.setSpacing(1)

        

        if self.icon:
            self.icon_label = QtWidgets.QLabel()
            self.icon_label.setFixedSize(QtCore.QSize(22,22))
            self.icon_label.setPixmap(QtGui.QPixmap(self.icon).scaled(20, 20, QtCore.Qt.KeepAspectRatio,
                                                                              QtCore.Qt.SmoothTransformation))

            self.horizontalLayout.addWidget(self.icon_label)

    def add_label(self, data, width = 150, color = None):
        self.add_line()
        label = QtWidgets.QLabel(self)
        label.setText(data)
        label.setMinimumSize(QtCore.QSize(width, 0))
        label.setMaximumSize(QtCore.QSize(width, 1000))
        self.horizontalLayout.addWidget(label)

    def add_line(self):
        line = QtWidgets.QFrame(self)
        line.setMaximumSize(QtCore.QSize(1, 16777215))
        line.setFrameShape(QtWidgets.QFrame.VLine)
        line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.horizontalLayout.addWidget(line)