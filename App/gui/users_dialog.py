# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\conta\Documents\script\Wizard\App\work\ui_files\users_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(293, 276)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.users_comboBox = QtWidgets.QComboBox(self.frame)
        self.users_comboBox.setObjectName("users_comboBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.users_comboBox)
        self.all_users_label = QtWidgets.QLabel(self.frame)
        self.all_users_label.setObjectName("all_users_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.all_users_label)
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.verticalLayout.addLayout(self.formLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.change_user_pushButton = QtWidgets.QPushButton(self.frame)
        self.change_user_pushButton.setMinimumSize(QtCore.QSize(0, 70))
        self.change_user_pushButton.setObjectName("change_user_pushButton")
        self.horizontalLayout.addWidget(self.change_user_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.recover_pushButton = QtWidgets.QPushButton(self.frame)
        self.recover_pushButton.setObjectName("recover_pushButton")
        self.verticalLayout.addWidget(self.recover_pushButton)
        self.verticalLayout_2.addWidget(self.frame)
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
        self.verticalLayout_2.addWidget(self.log_frame)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Please log"))
        self.all_users_label.setText(_translate("Dialog", "User"))
        self.label_2.setText(_translate("Dialog", "Password"))
        self.change_user_pushButton.setText(_translate("Dialog", "Log"))
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
