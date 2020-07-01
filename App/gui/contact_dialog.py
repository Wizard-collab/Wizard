# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\conta\Documents\script\Wizard\App\work\ui_files\contact_dialog.ui'
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
        self.main_frame = QtWidgets.QFrame(Dialog)
        self.main_frame.setObjectName("main_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.main_frame)
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.message_textEdit = QtWidgets.QTextEdit(self.main_frame)
        self.message_textEdit.setObjectName("message_textEdit")
        self.verticalLayout.addWidget(self.message_textEdit)
        self.verticalLayout_2.addWidget(self.main_frame)
        self.report_error_pushButton = QtWidgets.QPushButton(Dialog)
        self.report_error_pushButton.setMinimumSize(QtCore.QSize(0, 50))
        self.report_error_pushButton.setObjectName("report_error_pushButton")
        self.verticalLayout_2.addWidget(self.report_error_pushButton)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.message_textEdit.setPlaceholderText(_translate("Dialog", "How to add an empty scene in an existing asset ?"))
        self.report_error_pushButton.setText(_translate("Dialog", "Send"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
