# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\leo\Documents\Script\Wizard\App\gui\ui_files\seen_widget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Seen_widget(object):
    def setupUi(self, Seen_widget):
        Seen_widget.setObjectName("Seen_widget")
        Seen_widget.resize(641, 44)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Seen_widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.seen_widget_frame = QtWidgets.QFrame(Seen_widget)
        self.seen_widget_frame.setMinimumSize(QtCore.QSize(0, 44))
        self.seen_widget_frame.setMaximumSize(QtCore.QSize(16777215, 44))
        self.seen_widget_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.seen_widget_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.seen_widget_frame.setObjectName("seen_widget_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.seen_widget_frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.seen_logo_label = QtWidgets.QLabel(self.seen_widget_frame)
        self.seen_logo_label.setMinimumSize(QtCore.QSize(24, 24))
        self.seen_logo_label.setMaximumSize(QtCore.QSize(24, 24))
        self.seen_logo_label.setText("")
        self.seen_logo_label.setObjectName("seen_logo_label")
        self.horizontalLayout_2.addWidget(self.seen_logo_label)
        self.seen_label = QtWidgets.QLabel(self.seen_widget_frame)
        self.seen_label.setObjectName("seen_label")
        self.horizontalLayout_2.addWidget(self.seen_label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.horizontalLayout.addWidget(self.seen_widget_frame)

        self.retranslateUi(Seen_widget)
        QtCore.QMetaObject.connectSlotsByName(Seen_widget)

    def retranslateUi(self, Seen_widget):
        _translate = QtCore.QCoreApplication.translate
        Seen_widget.setWindowTitle(_translate("Seen_widget", "Form"))
        self.seen_label.setText(_translate("Seen_widget", "What\'s new ?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Seen_widget = QtWidgets.QWidget()
    ui = Ui_Seen_widget()
    ui.setupUi(Seen_widget)
    Seen_widget.show()
    sys.exit(app.exec_())

