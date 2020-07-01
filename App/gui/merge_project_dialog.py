# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\conta\Documents\script\Wizard\App\work\ui_files\merge_project_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(434, 198)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setHorizontalSpacing(7)
        self.formLayout.setVerticalSpacing(3)
        self.formLayout.setObjectName("formLayout")
        self.all_projects_label = QtWidgets.QLabel(self.frame)
        self.all_projects_label.setObjectName("all_projects_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.all_projects_label)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.project_path_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.project_path_lineEdit.setObjectName("project_path_lineEdit")
        self.horizontalLayout_3.addWidget(self.project_path_lineEdit)
        self.project_path_pushButton = QtWidgets.QPushButton(self.frame)
        self.project_path_pushButton.setMinimumSize(QtCore.QSize(24, 24))
        self.project_path_pushButton.setMaximumSize(QtCore.QSize(24, 24))
        self.project_path_pushButton.setText("")
        self.project_path_pushButton.setIconSize(QtCore.QSize(14, 14))
        self.project_path_pushButton.setObjectName("project_path_pushButton")
        self.horizontalLayout_3.addWidget(self.project_path_pushButton)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label)
        self.password_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.password_lineEdit)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.confirm_password_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.confirm_password_lineEdit.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.confirm_password_lineEdit.setObjectName("confirm_password_lineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.confirm_password_lineEdit)
        self.verticalLayout.addLayout(self.formLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.change_project_pushButton = QtWidgets.QPushButton(self.frame)
        self.change_project_pushButton.setMinimumSize(QtCore.QSize(0, 50))
        self.change_project_pushButton.setDefault(True)
        self.change_project_pushButton.setObjectName("change_project_pushButton")
        self.horizontalLayout.addWidget(self.change_project_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
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
        self.all_projects_label.setText(_translate("Dialog", "Project path"))
        self.label.setText(_translate("Dialog", "Add a password"))
        self.label_2.setText(_translate("Dialog", "Confirm password"))
        self.change_project_pushButton.setText(_translate("Dialog", "Append"))
        self.log_lineEdit.setPlaceholderText(_translate("Dialog", "Warnings and logs here..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
