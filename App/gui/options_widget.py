# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\leo\Documents\Script\Wizard\App\gui\ui_files\options_widget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(116, 22)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.options_frame = QtWidgets.QFrame(Form)
        self.options_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.options_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.options_frame.setObjectName("options_frame")
        self.buttons_layout = QtWidgets.QVBoxLayout(self.options_frame)
        self.buttons_layout.setContentsMargins(0, 0, 0, 0)
        self.buttons_layout.setSpacing(0)
        self.buttons_layout.setObjectName("buttons_layout")
        self.horizontalLayout.addWidget(self.options_frame)

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

