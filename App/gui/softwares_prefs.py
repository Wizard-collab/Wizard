# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\conta\Documents\script\Wizard\App\work\ui_files\softwares_prefs.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(650, 582)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.setup_softwares_comboBox = QtWidgets.QComboBox(Form)
        self.setup_softwares_comboBox.setMinimumSize(QtCore.QSize(200, 0))
        self.setup_softwares_comboBox.setObjectName("setup_softwares_comboBox")
        self.horizontalLayout.addWidget(self.setup_softwares_comboBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setObjectName("frame")
        self.formLayout = QtWidgets.QFormLayout(self.frame)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.executable_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.executable_lineEdit.setReadOnly(False)
        self.executable_lineEdit.setObjectName("executable_lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.executable_lineEdit)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.env_textEdit = QtWidgets.QTextEdit(self.frame)
        self.env_textEdit.setObjectName("env_textEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.env_textEdit)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.additionnal_textEdit = QtWidgets.QTextEdit(self.frame)
        self.additionnal_textEdit.setObjectName("additionnal_textEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.additionnal_textEdit)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.command_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.command_lineEdit.setObjectName("command_lineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.command_lineEdit)
        self.verticalLayout_2.addWidget(self.frame)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.save_setup_pushButton = QtWidgets.QPushButton(Form)
        self.save_setup_pushButton.setMinimumSize(QtCore.QSize(0, 50))
        self.save_setup_pushButton.setObjectName("save_setup_pushButton")
        self.verticalLayout_2.addWidget(self.save_setup_pushButton)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.log_frame = QtWidgets.QFrame(Form)
        self.log_frame.setObjectName("log_frame")
        self.log_layout = QtWidgets.QHBoxLayout(self.log_frame)
        self.log_layout.setContentsMargins(0, 0, 0, 0)
        self.log_layout.setSpacing(0)
        self.log_layout.setObjectName("log_layout")
        spacerItem3 = QtWidgets.QSpacerItem(4, 2, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.log_layout.addItem(spacerItem3)
        self.log_icon = QtWidgets.QPushButton(self.log_frame)
        self.log_icon.setEnabled(False)
        self.log_icon.setMaximumSize(QtCore.QSize(27, 16777215))
        self.log_icon.setText("")
        self.log_icon.setObjectName("log_icon")
        self.log_layout.addWidget(self.log_icon)
        self.log_lineEdit = QtWidgets.QLineEdit(self.log_frame)
        self.log_lineEdit.setReadOnly(True)
        self.log_lineEdit.setObjectName("log_lineEdit")
        self.log_layout.addWidget(self.log_lineEdit)
        self.verticalLayout.addWidget(self.log_frame)
        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Software"))
        self.label_2.setText(_translate("Form", "Executable"))
        self.executable_lineEdit.setPlaceholderText(_translate("Form", "path/to/software/software.exe..."))
        self.label_3.setText(_translate("Form", "Environment variables"))
        self.env_textEdit.setPlaceholderText(_translate("Form", "PYTHONPATH = path/to/python..."))
        self.label_4.setText(_translate("Form", "Additionnal scripts folders"))
        self.additionnal_textEdit.setPlaceholderText(_translate("Form", "path/to/myscripts/..."))
        self.label_5.setText(_translate("Form", "Command"))
        self.command_lineEdit.setPlaceholderText(_translate("Form", "\"[executable]\" \"[file]\""))
        self.save_setup_pushButton.setText(_translate("Form", "Save software setup"))
        self.log_lineEdit.setPlaceholderText(_translate("Form", "Warnings and logs here..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
