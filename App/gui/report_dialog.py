# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\conta\Documents\script\Wizard\App\work\ui_files\report_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(397, 320)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setMinimumSize(QtCore.QSize(0, 30))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.verticalLayout.addWidget(self.frame)
        self.message_textEdit = QtWidgets.QTextEdit(Dialog)
        self.message_textEdit.setObjectName("message_textEdit")
        self.verticalLayout.addWidget(self.message_textEdit)
        self.report_error_pushButton = QtWidgets.QPushButton(Dialog)
        self.report_error_pushButton.setMinimumSize(QtCore.QSize(0, 50))
        self.report_error_pushButton.setObjectName("report_error_pushButton")
        self.verticalLayout.addWidget(self.report_error_pushButton)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Please add a message to your report"))
        self.message_textEdit.setPlaceholderText(_translate("Dialog", "I was publishing an asset and it gave me this error..."))
        self.report_error_pushButton.setText(_translate("Dialog", "Send"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
