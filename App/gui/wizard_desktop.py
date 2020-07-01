# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\conta\Documents\script\Wizard_clean\App\work\ui_files\wizard_desktop.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(219, 76)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.wizard_desktop_transparent_frame = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wizard_desktop_transparent_frame.sizePolicy().hasHeightForWidth())
        self.wizard_desktop_transparent_frame.setSizePolicy(sizePolicy)
        self.wizard_desktop_transparent_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.wizard_desktop_transparent_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.wizard_desktop_transparent_frame.setObjectName("wizard_desktop_transparent_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.wizard_desktop_transparent_frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.show_wizard_pushButton = QtWidgets.QPushButton(self.wizard_desktop_transparent_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.show_wizard_pushButton.sizePolicy().hasHeightForWidth())
        self.show_wizard_pushButton.setSizePolicy(sizePolicy)
        self.show_wizard_pushButton.setMinimumSize(QtCore.QSize(60, 60))
        self.show_wizard_pushButton.setText("")
        self.show_wizard_pushButton.setObjectName("show_wizard_pushButton")
        self.horizontalLayout.addWidget(self.show_wizard_pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.wizard_desktop_transparent_frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
