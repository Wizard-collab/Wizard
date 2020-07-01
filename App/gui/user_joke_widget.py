# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\conta\Documents\script\Wizard\App\work\ui_files\user_joke_widget.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(773, 52)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.user_joke_frame = QtWidgets.QFrame(Form)
        self.user_joke_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.user_joke_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.user_joke_frame.setObjectName("user_joke_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.user_joke_frame)
        self.horizontalLayout.setContentsMargins(4, 4, 4, 4)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.joke_label = QtWidgets.QLabel(self.user_joke_frame)
        self.joke_label.setText("")
        self.joke_label.setWordWrap(True)
        self.joke_label.setObjectName("joke_label")
        self.horizontalLayout.addWidget(self.joke_label)
        self.delete_joke_pushButton = QtWidgets.QPushButton(self.user_joke_frame)
        self.delete_joke_pushButton.setMinimumSize(QtCore.QSize(28, 28))
        self.delete_joke_pushButton.setMaximumSize(QtCore.QSize(28, 28))
        self.delete_joke_pushButton.setText("")
        self.delete_joke_pushButton.setObjectName("delete_joke_pushButton")
        self.horizontalLayout.addWidget(self.delete_joke_pushButton)
        self.verticalLayout.addWidget(self.user_joke_frame)

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
