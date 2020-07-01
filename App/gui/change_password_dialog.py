# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\leo\Documents\Script\Wizard\App\gui\ui_files\change_password_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(297, 332)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.new_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.new_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.new_lineEdit.setObjectName("new_lineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.new_lineEdit)
        self.confirm_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.confirm_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirm_lineEdit.setObjectName("confirm_lineEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.confirm_lineEdit)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.formLayout.setItem(2, QtWidgets.QFormLayout.FieldRole, spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.old_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.old_lineEdit.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.old_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.old_lineEdit.setObjectName("old_lineEdit")
        self.horizontalLayout.addWidget(self.old_lineEdit)
        self.show_pass_pushButton = QtWidgets.QPushButton(self.frame)
        self.show_pass_pushButton.setMinimumSize(QtCore.QSize(22, 22))
        self.show_pass_pushButton.setMaximumSize(QtCore.QSize(22, 22))
        self.show_pass_pushButton.setText("")
        self.show_pass_pushButton.setObjectName("show_pass_pushButton")
        self.horizontalLayout.addWidget(self.show_pass_pushButton)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.formLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 34, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.change_password_pushButton = QtWidgets.QPushButton(self.frame)
        self.change_password_pushButton.setMinimumSize(QtCore.QSize(0, 70))
        self.change_password_pushButton.setMaximumSize(QtCore.QSize(16777215, 70))
        self.change_password_pushButton.setObjectName("change_password_pushButton")
        self.verticalLayout_2.addWidget(self.change_password_pushButton)
        self.recover_pushButton = QtWidgets.QPushButton(self.frame)
        self.recover_pushButton.setObjectName("recover_pushButton")
        self.verticalLayout_2.addWidget(self.recover_pushButton)
        self.verticalLayout.addWidget(self.frame)
        self.log_frame = QtWidgets.QFrame(Dialog)
        self.log_frame.setObjectName("log_frame")
        self.log_layout = QtWidgets.QHBoxLayout(self.log_frame)
        self.log_layout.setContentsMargins(0, 0, 0, 0)
        self.log_layout.setSpacing(0)
        self.log_layout.setObjectName("log_layout")
        self.log_lineEdit = QtWidgets.QLineEdit(self.log_frame)
        self.log_lineEdit.setReadOnly(True)
        self.log_lineEdit.setObjectName("log_lineEdit")
        self.log_layout.addWidget(self.log_lineEdit)
        self.verticalLayout.addWidget(self.log_frame)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Old password"))
        self.label.setText(_translate("Dialog", "New password"))
        self.label_3.setText(_translate("Dialog", "Confirm"))
        self.change_password_pushButton.setText(_translate("Dialog", "Change password"))
        self.recover_pushButton.setText(_translate("Dialog", "Password forgotten ?"))
        self.log_lineEdit.setPlaceholderText(_translate("Dialog", "Warnings and logs here..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

