# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\conta\Documents\script\Wizard\App\work\ui_files\create_user_script_widget.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(598, 362)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.create_user_script_tittle_label = QtWidgets.QLabel(self.frame_2)
        self.create_user_script_tittle_label.setObjectName("create_user_script_tittle_label")
        self.verticalLayout_3.addWidget(self.create_user_script_tittle_label)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.script_name_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.script_name_lineEdit.setObjectName("script_name_lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.script_name_lineEdit)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.script_icon_pushButton = QtWidgets.QPushButton(self.frame)
        self.script_icon_pushButton.setMinimumSize(QtCore.QSize(28, 28))
        self.script_icon_pushButton.setMaximumSize(QtCore.QSize(28, 28))
        self.script_icon_pushButton.setText("")
        self.script_icon_pushButton.setObjectName("script_icon_pushButton")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.script_icon_pushButton)
        self.script_plainTextEdit = QtWidgets.QPlainTextEdit(self.frame)
        self.script_plainTextEdit.setObjectName("script_plainTextEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.script_plainTextEdit)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.verticalLayout.addWidget(self.frame)
        self.horizontalFrame = QtWidgets.QFrame(Form)
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.create_script_pushButton = QtWidgets.QPushButton(self.horizontalFrame)
        self.create_script_pushButton.setMinimumSize(QtCore.QSize(100, 40))
        self.create_script_pushButton.setObjectName("create_script_pushButton")
        self.horizontalLayout.addWidget(self.create_script_pushButton)
        self.verticalLayout.addWidget(self.horizontalFrame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.create_user_script_tittle_label.setText(_translate("Form", "Create user script"))
        self.label.setText(_translate("Form", "Name"))
        self.label_2.setText(_translate("Form", "Icon"))
        self.label_3.setText(_translate("Form", "Script"))
        self.create_script_pushButton.setText(_translate("Form", "Apply"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
