# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'projects_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(339, 201)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.all_projects_label = QtWidgets.QLabel(self.frame)
        self.all_projects_label.setObjectName("all_projects_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.all_projects_label)
        self.projects_comboBox = QtWidgets.QComboBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.projects_comboBox.sizePolicy().hasHeightForWidth())
        self.projects_comboBox.setSizePolicy(sizePolicy)
        self.projects_comboBox.setMinimumSize(QtCore.QSize(0, 30))
        self.projects_comboBox.setObjectName("projects_comboBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.projects_comboBox)
        self.verticalLayout_3.addLayout(self.formLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.password_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.password_lineEdit.setText("")
        self.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.horizontalLayout_2.addWidget(self.password_lineEdit)
        self.password_visibility_pushButton = QtWidgets.QPushButton(self.frame)
        self.password_visibility_pushButton.setMinimumSize(QtCore.QSize(25, 25))
        self.password_visibility_pushButton.setMaximumSize(QtCore.QSize(25, 25))
        self.password_visibility_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.password_visibility_pushButton.setText("")
        self.password_visibility_pushButton.setCheckable(True)
        self.password_visibility_pushButton.setObjectName("password_visibility_pushButton")
        self.horizontalLayout_2.addWidget(self.password_visibility_pushButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.new_project_pushButton = QtWidgets.QPushButton(self.frame)
        self.new_project_pushButton.setMinimumSize(QtCore.QSize(0, 50))
        self.new_project_pushButton.setObjectName("new_project_pushButton")
        self.horizontalLayout.addWidget(self.new_project_pushButton)
        self.change_project_pushButton = QtWidgets.QPushButton(self.frame)
        self.change_project_pushButton.setMinimumSize(QtCore.QSize(0, 50))
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
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.all_projects_label.setText(_translate("Dialog", "Project"))
        self.label.setText(_translate("Dialog", "Password"))
        self.password_visibility_pushButton.setToolTip(_translate("Dialog", "Show password"))
        self.new_project_pushButton.setText(_translate("Dialog", "New project"))
        self.change_project_pushButton.setText(_translate("Dialog", "Open"))
        self.log_lineEdit.setPlaceholderText(_translate("Dialog", "Warnings and logs here..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
