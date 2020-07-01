# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\leo\Documents\Script\Wizard\App\gui\ui_files\recover_password.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(299, 249)
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
        self.all_users_label = QtWidgets.QLabel(self.frame)
        self.all_users_label.setObjectName("all_users_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.all_users_label)
        self.users_comboBox = QtWidgets.QComboBox(self.frame)
        self.users_comboBox.setObjectName("users_comboBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.users_comboBox)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.email_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.email_lineEdit.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.email_lineEdit.setObjectName("email_lineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.email_lineEdit)
        self.verticalLayout_2.addLayout(self.formLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 34, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.recover_pushButton = QtWidgets.QPushButton(self.frame)
        self.recover_pushButton.setMinimumSize(QtCore.QSize(0, 70))
        self.recover_pushButton.setMaximumSize(QtCore.QSize(16777215, 70))
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
        self.all_users_label.setText(_translate("Dialog", "User"))
        self.label_2.setText(_translate("Dialog", "email"))
        self.recover_pushButton.setText(_translate("Dialog", "Recover password"))
        self.log_lineEdit.setPlaceholderText(_translate("Dialog", "Warnings and logs here..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

