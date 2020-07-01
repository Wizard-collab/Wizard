# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\conta\Documents\script\wizard_devellop\App\gui\ui_files\production_manager_stage_item.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(190, 60)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pm_stage_item_main_frame = QtWidgets.QFrame(Form)
        self.pm_stage_item_main_frame.setMinimumSize(QtCore.QSize(190, 0))
        self.pm_stage_item_main_frame.setMaximumSize(QtCore.QSize(190, 16777215))
        self.pm_stage_item_main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pm_stage_item_main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pm_stage_item_main_frame.setObjectName("pm_stage_item_main_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.pm_stage_item_main_frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pm_stage_item_user_pushButton = QtWidgets.QPushButton(self.pm_stage_item_main_frame)
        self.pm_stage_item_user_pushButton.setMinimumSize(QtCore.QSize(38, 38))
        self.pm_stage_item_user_pushButton.setMaximumSize(QtCore.QSize(38, 38))
        self.pm_stage_item_user_pushButton.setText("")
        self.pm_stage_item_user_pushButton.setIconSize(QtCore.QSize(30, 30))
        self.pm_stage_item_user_pushButton.setObjectName("pm_stage_item_user_pushButton")
        self.horizontalLayout_3.addWidget(self.pm_stage_item_user_pushButton)
        self.pm_stage_item_state_pushButton = QtWidgets.QPushButton(self.pm_stage_item_main_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pm_stage_item_state_pushButton.sizePolicy().hasHeightForWidth())
        self.pm_stage_item_state_pushButton.setSizePolicy(sizePolicy)
        self.pm_stage_item_state_pushButton.setMinimumSize(QtCore.QSize(0, 38))
        self.pm_stage_item_state_pushButton.setObjectName("pm_stage_item_state_pushButton")
        self.horizontalLayout_3.addWidget(self.pm_stage_item_state_pushButton)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout.addWidget(self.pm_stage_item_main_frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pm_stage_item_state_pushButton.setText(_translate("Form", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
