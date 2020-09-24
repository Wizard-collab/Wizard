# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\conta\Documents\script\Wizard\App\work\ui_files\user_scripts_widget.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(822, 30)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(Form)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 30))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.add_user_script_pushButton = QtWidgets.QPushButton(self.frame_3)
        self.add_user_script_pushButton.setMinimumSize(QtCore.QSize(30, 30))
        self.add_user_script_pushButton.setMaximumSize(QtCore.QSize(30, 30))
        self.add_user_script_pushButton.setObjectName("add_user_script_pushButton")
        self.horizontalLayout_15.addWidget(self.add_user_script_pushButton)
        self.scripts_buttons_layout = QtWidgets.QHBoxLayout()
        self.scripts_buttons_layout.setSpacing(1)
        self.scripts_buttons_layout.setObjectName("scripts_buttons_layout")
        self.horizontalLayout_15.addLayout(self.scripts_buttons_layout)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem)
        self.verticalLayout.addWidget(self.frame_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.add_user_script_pushButton.setText(_translate("Form", "+"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
