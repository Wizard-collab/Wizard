# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\conta\Documents\script\Wizard\App\ui_files\project_preferences.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(950, 623)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout.addWidget(self.frame)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.preferences_ui_listWidget = QtWidgets.QListWidget(Form)
        self.preferences_ui_listWidget.setMaximumSize(QtCore.QSize(250, 16777215))
        self.preferences_ui_listWidget.setAlternatingRowColors(False)
        self.preferences_ui_listWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.preferences_ui_listWidget.setSelectionRectVisible(True)
        self.preferences_ui_listWidget.setObjectName("preferences_ui_listWidget")
        item = QtWidgets.QListWidgetItem()
        self.preferences_ui_listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.preferences_ui_listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.preferences_ui_listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.preferences_ui_listWidget.addItem(item)
        self.horizontalLayout_4.addWidget(self.preferences_ui_listWidget)
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.page_3)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 696, 537))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_15 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frame_15)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_25 = QtWidgets.QLabel(self.frame_15)
        self.label_25.setObjectName("label_25")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_25)
        self.site_path_label = QtWidgets.QLabel(self.frame_15)
        self.site_path_label.setStyleSheet("color:gray;")
        self.site_path_label.setObjectName("site_path_label")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.site_path_label)
        self.label_19 = QtWidgets.QLabel(self.frame_15)
        self.label_19.setMinimumSize(QtCore.QSize(100, 0))
        self.label_19.setObjectName("label_19")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_19)
        self.project_name_label = QtWidgets.QLabel(self.frame_15)
        self.project_name_label.setStyleSheet("color:gray;")
        self.project_name_label.setObjectName("project_name_label")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.project_name_label)
        self.label_20 = QtWidgets.QLabel(self.frame_15)
        self.label_20.setObjectName("label_20")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_20)
        self.project_path_label = QtWidgets.QLabel(self.frame_15)
        self.project_path_label.setStyleSheet("color:gray;")
        self.project_path_label.setObjectName("project_path_label")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.project_path_label)
        self.label_21 = QtWidgets.QLabel(self.frame_15)
        self.label_21.setObjectName("label_21")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_21)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.project_size_label = QtWidgets.QLabel(self.frame_15)
        self.project_size_label.setStyleSheet("color:gray;")
        self.project_size_label.setObjectName("project_size_label")
        self.horizontalLayout_7.addWidget(self.project_size_label)
        self.calculate_project_size_pushButton = QtWidgets.QPushButton(self.frame_15)
        self.calculate_project_size_pushButton.setObjectName("calculate_project_size_pushButton")
        self.horizontalLayout_7.addWidget(self.calculate_project_size_pushButton)
        self.formLayout_3.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_7)
        self.verticalLayout_15.addLayout(self.formLayout_3)
        self.verticalLayout_3.addWidget(self.frame_15)
        self.frame_4 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.formLayout_2 = QtWidgets.QFormLayout(self.frame_4)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_8 = QtWidgets.QLabel(self.frame_4)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.frame_rate_spinBox = QtWidgets.QSpinBox(self.frame_4)
        self.frame_rate_spinBox.setObjectName("frame_rate_spinBox")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.frame_rate_spinBox)
        self.label_9 = QtWidgets.QLabel(self.frame_4)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.f_width_lineEdit = QtWidgets.QLineEdit(self.frame_4)
        self.f_width_lineEdit.setObjectName("f_width_lineEdit")
        self.horizontalLayout.addWidget(self.f_width_lineEdit)
        self.label_10 = QtWidgets.QLabel(self.frame_4)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout.addWidget(self.label_10)
        self.f_height_lineEdit = QtWidgets.QLineEdit(self.frame_4)
        self.f_height_lineEdit.setObjectName("f_height_lineEdit")
        self.horizontalLayout.addWidget(self.f_height_lineEdit)
        self.formLayout_2.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.verticalLayout_3.addWidget(self.frame_4)
        self.frame_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 364, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout_3.addWidget(self.frame_3)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.stackedWidget.addWidget(self.page_3)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.page)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 292, 355))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_6 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_14 = QtWidgets.QLabel(self.frame_6)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_5.addWidget(self.label_14)
        self.setup_softwares_comboBox = QtWidgets.QComboBox(self.frame_6)
        self.setup_softwares_comboBox.setMinimumSize(QtCore.QSize(200, 0))
        self.setup_softwares_comboBox.setObjectName("setup_softwares_comboBox")
        self.horizontalLayout_5.addWidget(self.setup_softwares_comboBox)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.verticalLayout_5.addWidget(self.frame_6)
        self.frame_5 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.frame_5.setObjectName("frame_5")
        self.formLayout_4 = QtWidgets.QFormLayout(self.frame_5)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_7 = QtWidgets.QLabel(self.frame_5)
        self.label_7.setObjectName("label_7")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.executable_lineEdit = QtWidgets.QLineEdit(self.frame_5)
        self.executable_lineEdit.setReadOnly(False)
        self.executable_lineEdit.setObjectName("executable_lineEdit")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.executable_lineEdit)
        self.label_11 = QtWidgets.QLabel(self.frame_5)
        self.label_11.setObjectName("label_11")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.env_textEdit = QtWidgets.QTextEdit(self.frame_5)
        self.env_textEdit.setObjectName("env_textEdit")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.env_textEdit)
        self.label_12 = QtWidgets.QLabel(self.frame_5)
        self.label_12.setObjectName("label_12")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.additionnal_textEdit = QtWidgets.QTextEdit(self.frame_5)
        self.additionnal_textEdit.setObjectName("additionnal_textEdit")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.additionnal_textEdit)
        self.label_13 = QtWidgets.QLabel(self.frame_5)
        self.label_13.setObjectName("label_13")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.command_lineEdit = QtWidgets.QLineEdit(self.frame_5)
        self.command_lineEdit.setObjectName("command_lineEdit")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.command_lineEdit)
        self.verticalLayout_5.addWidget(self.frame_5)
        self.save_setup_pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.save_setup_pushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.save_setup_pushButton.setObjectName("save_setup_pushButton")
        self.verticalLayout_5.addWidget(self.save_setup_pushButton)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_4.addWidget(self.scrollArea_2)
        self.stackedWidget.addWidget(self.page)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.page_4)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setSpacing(1)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.scrollArea_4 = QtWidgets.QScrollArea(self.page_4)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 229, 190))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_18.setSpacing(1)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.frame_14 = QtWidgets.QFrame(self.scrollAreaWidgetContents_4)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.frame_14)
        self.verticalLayout_17.setContentsMargins(-1, -1, -1, 11)
        self.verticalLayout_17.setSpacing(7)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.formLayout_6 = QtWidgets.QFormLayout()
        self.formLayout_6.setObjectName("formLayout_6")
        self.label_22 = QtWidgets.QLabel(self.frame_14)
        self.label_22.setObjectName("label_22")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_22)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.old_lineEdit = QtWidgets.QLineEdit(self.frame_14)
        self.old_lineEdit.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.old_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.old_lineEdit.setObjectName("old_lineEdit")
        self.horizontalLayout_8.addWidget(self.old_lineEdit)
        self.show_pass_pushButton = QtWidgets.QPushButton(self.frame_14)
        self.show_pass_pushButton.setMinimumSize(QtCore.QSize(22, 22))
        self.show_pass_pushButton.setMaximumSize(QtCore.QSize(22, 22))
        self.show_pass_pushButton.setText("")
        self.show_pass_pushButton.setObjectName("show_pass_pushButton")
        self.horizontalLayout_8.addWidget(self.show_pass_pushButton)
        self.formLayout_6.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_8)
        self.label_23 = QtWidgets.QLabel(self.frame_14)
        self.label_23.setObjectName("label_23")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_23)
        self.new_lineEdit = QtWidgets.QLineEdit(self.frame_14)
        self.new_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.new_lineEdit.setObjectName("new_lineEdit")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.new_lineEdit)
        self.label_24 = QtWidgets.QLabel(self.frame_14)
        self.label_24.setObjectName("label_24")
        self.formLayout_6.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_24)
        self.confirm_lineEdit = QtWidgets.QLineEdit(self.frame_14)
        self.confirm_lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirm_lineEdit.setObjectName("confirm_lineEdit")
        self.formLayout_6.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.confirm_lineEdit)
        self.verticalLayout_17.addLayout(self.formLayout_6)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_9.setSpacing(1)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem2)
        self.verticalLayout_20 = QtWidgets.QVBoxLayout()
        self.verticalLayout_20.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_20.setSpacing(1)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.change_password_pushButton = QtWidgets.QPushButton(self.frame_14)
        self.change_password_pushButton.setMinimumSize(QtCore.QSize(200, 40))
        self.change_password_pushButton.setObjectName("change_password_pushButton")
        self.verticalLayout_20.addWidget(self.change_password_pushButton)
        self.horizontalLayout_9.addLayout(self.verticalLayout_20)
        self.verticalLayout_17.addLayout(self.horizontalLayout_9)
        self.verticalLayout_18.addWidget(self.frame_14)
        self.frame_10 = QtWidgets.QFrame(self.scrollAreaWidgetContents_4)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        spacerItem3 = QtWidgets.QSpacerItem(20, 315, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_21.addItem(spacerItem3)
        self.verticalLayout_18.addWidget(self.frame_10)
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)
        self.verticalLayout_14.addWidget(self.scrollArea_4)
        self.stackedWidget.addWidget(self.page_4)
        self.horizontalLayout_4.addWidget(self.stackedWidget)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.save_prefs_pushButton = QtWidgets.QPushButton(Form)
        self.save_prefs_pushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.save_prefs_pushButton.setObjectName("save_prefs_pushButton")
        self.verticalLayout.addWidget(self.save_prefs_pushButton)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Project preferences"))
        __sortingEnabled = self.preferences_ui_listWidget.isSortingEnabled()
        self.preferences_ui_listWidget.setSortingEnabled(False)
        item = self.preferences_ui_listWidget.item(0)
        item.setText(_translate("Form", "General"))
        item = self.preferences_ui_listWidget.item(1)
        item.setText(_translate("Form", "Softwares"))
        item = self.preferences_ui_listWidget.item(2)
        item.setText(_translate("Form", "Workflow"))
        item = self.preferences_ui_listWidget.item(3)
        item.setText(_translate("Form", "Security"))
        self.preferences_ui_listWidget.setSortingEnabled(__sortingEnabled)
        self.label_25.setText(_translate("Form", "Site path"))
        self.site_path_label.setText(_translate("Form", "site_path_label"))
        self.label_19.setText(_translate("Form", "Project name"))
        self.project_name_label.setText(_translate("Form", "project_name_label"))
        self.label_20.setText(_translate("Form", "Project path"))
        self.project_path_label.setText(_translate("Form", "project_path_label"))
        self.label_21.setText(_translate("Form", "Project size"))
        self.project_size_label.setText(_translate("Form", "project_size_label"))
        self.calculate_project_size_pushButton.setText(_translate("Form", "calculate"))
        self.label_8.setText(_translate("Form", "Frame rate"))
        self.label_9.setText(_translate("Form", "Format"))
        self.label_10.setText(_translate("Form", "x"))
        self.label_14.setText(_translate("Form", "Software"))
        self.label_7.setText(_translate("Form", "Executable"))
        self.executable_lineEdit.setPlaceholderText(_translate("Form", "path/to/software/software.exe..."))
        self.label_11.setText(_translate("Form", "Environment variables"))
        self.env_textEdit.setPlaceholderText(_translate("Form", "PYTHONPATH = path/to/python..."))
        self.label_12.setText(_translate("Form", "Additionnal scripts folders"))
        self.additionnal_textEdit.setPlaceholderText(_translate("Form", "path/to/myscripts/..."))
        self.label_13.setText(_translate("Form", "Command"))
        self.command_lineEdit.setPlaceholderText(_translate("Form", "\"[executable]\" \"[file]\""))
        self.save_setup_pushButton.setText(_translate("Form", "Save software setup"))
        self.label_22.setText(_translate("Form", "Old password"))
        self.label_23.setText(_translate("Form", "New password"))
        self.label_24.setText(_translate("Form", "Confirm"))
        self.change_password_pushButton.setText(_translate("Form", "Accept"))
        self.save_prefs_pushButton.setText(_translate("Form", "Apply"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
