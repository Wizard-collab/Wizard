# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\conta\Documents\script\Wizard\App\work\ui_files\email_confirm_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(327, 304)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.confirm_email_title_label = QtWidgets.QLabel(self.frame)
        self.confirm_email_title_label.setObjectName("confirm_email_title_label")
        self.verticalLayout_2.addWidget(self.confirm_email_title_label)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.verification_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.verification_lineEdit.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.verification_lineEdit.setObjectName("verification_lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.verification_lineEdit)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.verticalLayout_2.addLayout(self.formLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 34, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.confirm_pushButton = QtWidgets.QPushButton(self.frame)
        self.confirm_pushButton.setMinimumSize(QtCore.QSize(0, 70))
        self.confirm_pushButton.setMaximumSize(QtCore.QSize(16777215, 70))
        self.confirm_pushButton.setObjectName("confirm_pushButton")
        self.verticalLayout_2.addWidget(self.confirm_pushButton)
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
        self.recover_pushButton.clicked.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.confirm_email_title_label.setText(_translate("Dialog", "Your received a  code by email"))
        self.label_2.setText(_translate("Dialog", "Verification code"))
        self.confirm_pushButton.setText(_translate("Dialog", "Confirm"))
        self.recover_pushButton.setText(_translate("Dialog", "I don\'t receive this email, change email"))
        self.log_lineEdit.setPlaceholderText(_translate("Dialog", "Warnings and logs here..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
