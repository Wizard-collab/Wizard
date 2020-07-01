# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\leo\Documents\Script\Wizard\App\gui\ui_files\date_widget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Date_widget(object):
    def setupUi(self, Date_widget):
        Date_widget.setObjectName("Date_widget")
        Date_widget.resize(657, 44)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Date_widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.date_widget_frame = QtWidgets.QFrame(Date_widget)
        self.date_widget_frame.setMinimumSize(QtCore.QSize(0, 44))
        self.date_widget_frame.setMaximumSize(QtCore.QSize(16777215, 44))
        self.date_widget_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.date_widget_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.date_widget_frame.setObjectName("date_widget_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.date_widget_frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.date_logo_label = QtWidgets.QLabel(self.date_widget_frame)
        self.date_logo_label.setMinimumSize(QtCore.QSize(20, 20))
        self.date_logo_label.setMaximumSize(QtCore.QSize(20, 20))
        self.date_logo_label.setText("")
        self.date_logo_label.setObjectName("date_logo_label")
        self.horizontalLayout_2.addWidget(self.date_logo_label)
        self.message_date_label = QtWidgets.QLabel(self.date_widget_frame)
        self.message_date_label.setObjectName("message_date_label")
        self.horizontalLayout_2.addWidget(self.message_date_label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.horizontalLayout.addWidget(self.date_widget_frame)

        self.retranslateUi(Date_widget)
        QtCore.QMetaObject.connectSlotsByName(Date_widget)

    def retranslateUi(self, Date_widget):
        _translate = QtCore.QCoreApplication.translate
        Date_widget.setWindowTitle(_translate("Date_widget", "Form"))
        self.message_date_label.setText(_translate("Date_widget", "Date"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Date_widget = QtWidgets.QWidget()
    ui = Ui_Date_widget()
    ui.setupUi(Date_widget)
    Date_widget.show()
    sys.exit(app.exec_())

