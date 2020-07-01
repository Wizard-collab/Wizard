# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\leo\Documents\Script\Wizard\App\gui\ui_files\avatars.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1062, 329)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.avatars_scrollArea = QtWidgets.QScrollArea(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.avatars_scrollArea.sizePolicy().hasHeightForWidth())
        self.avatars_scrollArea.setSizePolicy(sizePolicy)
        self.avatars_scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.avatars_scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.avatars_scrollArea.setWidgetResizable(True)
        self.avatars_scrollArea.setObjectName("avatars_scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1036, 259))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.avatars_scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.avatars_scrollArea)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Choose your avatar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

