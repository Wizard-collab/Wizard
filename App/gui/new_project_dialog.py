# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\conta\Documents\script\Wizard\App\work\ui_files\new_project_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(351, 370)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.title_label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.title_label.setFont(font)
        self.title_label.setObjectName("title_label")
        self.verticalLayout_3.addWidget(self.title_label)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.create_project_name_label = QtWidgets.QLabel(self.frame_2)
        self.create_project_name_label.setObjectName("create_project_name_label")
        self.horizontalLayout.addWidget(self.create_project_name_label)
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 24))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.horizontalLayout_6.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.frame_2)
        self.password_project_formFrame_1 = QtWidgets.QFrame(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.password_project_formFrame_1.sizePolicy().hasHeightForWidth())
        self.password_project_formFrame_1.setSizePolicy(sizePolicy)
        self.password_project_formFrame_1.setObjectName("password_project_formFrame_1")
        self.formLayout_2 = QtWidgets.QFormLayout(self.password_project_formFrame_1)
        self.formLayout_2.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout_2.setContentsMargins(11, 11, 11, 11)
        self.formLayout_2.setHorizontalSpacing(1)
        self.formLayout_2.setVerticalSpacing(2)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtWidgets.QLabel(self.password_project_formFrame_1)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.password_lineEdit = QtWidgets.QLineEdit(self.password_project_formFrame_1)
        self.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.horizontalLayout_2.addWidget(self.password_lineEdit)
        self.show_pass_pushButton = QtWidgets.QPushButton(self.password_project_formFrame_1)
        self.show_pass_pushButton.setMinimumSize(QtCore.QSize(22, 22))
        self.show_pass_pushButton.setMaximumSize(QtCore.QSize(22, 22))
        self.show_pass_pushButton.setText("")
        self.show_pass_pushButton.setObjectName("show_pass_pushButton")
        self.horizontalLayout_2.addWidget(self.show_pass_pushButton)
        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.confirm_lineEdit = QtWidgets.QLineEdit(self.password_project_formFrame_1)
        self.confirm_lineEdit.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.confirm_lineEdit.setObjectName("confirm_lineEdit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.confirm_lineEdit)
        self.label_2 = QtWidgets.QLabel(self.password_project_formFrame_1)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.verticalLayout.addWidget(self.password_project_formFrame_1)
        self.settings_project_frame_1 = QtWidgets.QFrame(Dialog)
        self.settings_project_frame_1.setObjectName("settings_project_frame_1")
        self.formLayout = QtWidgets.QFormLayout(self.settings_project_frame_1)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout.setContentsMargins(11, 11, 11, 11)
        self.formLayout.setVerticalSpacing(2)
        self.formLayout.setObjectName("formLayout")
        self.create_project_path_label = QtWidgets.QLabel(self.settings_project_frame_1)
        self.create_project_path_label.setObjectName("create_project_path_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.create_project_path_label)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.project_path_lineEdit = QtWidgets.QLineEdit(self.settings_project_frame_1)
        self.project_path_lineEdit.setMinimumSize(QtCore.QSize(0, 24))
        self.project_path_lineEdit.setText("")
        self.project_path_lineEdit.setObjectName("project_path_lineEdit")
        self.horizontalLayout_4.addWidget(self.project_path_lineEdit)
        self.open_folder_pushButton = QtWidgets.QPushButton(self.settings_project_frame_1)
        self.open_folder_pushButton.setMinimumSize(QtCore.QSize(24, 24))
        self.open_folder_pushButton.setMaximumSize(QtCore.QSize(24, 24))
        self.open_folder_pushButton.setText("")
        self.open_folder_pushButton.setIconSize(QtCore.QSize(14, 14))
        self.open_folder_pushButton.setObjectName("open_folder_pushButton")
        self.horizontalLayout_4.addWidget(self.open_folder_pushButton)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.frame_rate_label = QtWidgets.QLabel(self.settings_project_frame_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_rate_label.sizePolicy().hasHeightForWidth())
        self.frame_rate_label.setSizePolicy(sizePolicy)
        self.frame_rate_label.setObjectName("frame_rate_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.frame_rate_label)
        self.frame_rate_spinBox = QtWidgets.QSpinBox(self.settings_project_frame_1)
        self.frame_rate_spinBox.setMinimumSize(QtCore.QSize(0, 24))
        self.frame_rate_spinBox.setProperty("value", 24)
        self.frame_rate_spinBox.setObjectName("frame_rate_spinBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.frame_rate_spinBox)
        self.format_label = QtWidgets.QLabel(self.settings_project_frame_1)
        self.format_label.setObjectName("format_label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.format_label)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.width_lineEdit = QtWidgets.QLineEdit(self.settings_project_frame_1)
        self.width_lineEdit.setObjectName("width_lineEdit")
        self.horizontalLayout_5.addWidget(self.width_lineEdit)
        self.label_3 = QtWidgets.QLabel(self.settings_project_frame_1)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.height_lineEdit = QtWidgets.QLineEdit(self.settings_project_frame_1)
        self.height_lineEdit.setObjectName("height_lineEdit")
        self.horizontalLayout_5.addWidget(self.height_lineEdit)
        self.formLayout.setLayout(4, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_5)
        self.verticalLayout.addWidget(self.settings_project_frame_1)
        self.project_path_label = QtWidgets.QLabel(Dialog)
        self.project_path_label.setText("")
        self.project_path_label.setObjectName("project_path_label")
        self.verticalLayout.addWidget(self.project_path_label)
        self.create_project_pushButton = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.create_project_pushButton.sizePolicy().hasHeightForWidth())
        self.create_project_pushButton.setSizePolicy(sizePolicy)
        self.create_project_pushButton.setMinimumSize(QtCore.QSize(0, 50))
        self.create_project_pushButton.setBaseSize(QtCore.QSize(0, 0))
        self.create_project_pushButton.setObjectName("create_project_pushButton")
        self.verticalLayout.addWidget(self.create_project_pushButton)
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
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.title_label.setText(_translate("Dialog", "Create new project"))
        self.create_project_name_label.setText(_translate("Dialog", "Project name"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "my_project"))
        self.label.setText(_translate("Dialog", "Password"))
        self.label_2.setText(_translate("Dialog", "Confirm"))
        self.create_project_path_label.setText(_translate("Dialog", "Project path  "))
        self.project_path_lineEdit.setPlaceholderText(_translate("Dialog", "C:/..."))
        self.frame_rate_label.setText(_translate("Dialog", "Frame rate"))
        self.format_label.setText(_translate("Dialog", "Format"))
        self.width_lineEdit.setPlaceholderText(_translate("Dialog", "1920"))
        self.label_3.setText(_translate("Dialog", "x"))
        self.height_lineEdit.setPlaceholderText(_translate("Dialog", "1080"))
        self.create_project_pushButton.setText(_translate("Dialog", "Create project"))
        self.log_lineEdit.setPlaceholderText(_translate("Dialog", "Warnings and logs here..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
