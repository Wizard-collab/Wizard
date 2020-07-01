# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\conta\Documents\script\wizard_devellop\App\gui\ui_files\modify_range_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(316, 109)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.shot_crea_main_frame = QtWidgets.QFrame(Dialog)
        self.shot_crea_main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.shot_crea_main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.shot_crea_main_frame.setObjectName("shot_crea_main_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.shot_crea_main_frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.shot_crea_main_frame)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.shot_inFrame_spinBox = QtWidgets.QSpinBox(self.shot_crea_main_frame)
        self.shot_inFrame_spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.shot_inFrame_spinBox.setMinimum(100)
        self.shot_inFrame_spinBox.setMaximum(10000000)
        self.shot_inFrame_spinBox.setObjectName("shot_inFrame_spinBox")
        self.horizontalLayout_2.addWidget(self.shot_inFrame_spinBox)
        self.shot_outFrame_spinBox = QtWidgets.QSpinBox(self.shot_crea_main_frame)
        self.shot_outFrame_spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.shot_outFrame_spinBox.setMinimum(100)
        self.shot_outFrame_spinBox.setMaximum(1000000000)
        self.shot_outFrame_spinBox.setProperty("value", 220)
        self.shot_outFrame_spinBox.setObjectName("shot_outFrame_spinBox")
        self.horizontalLayout_2.addWidget(self.shot_outFrame_spinBox)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.shot_crea_cancel_pushButton = QtWidgets.QPushButton(self.shot_crea_main_frame)
        self.shot_crea_cancel_pushButton.setObjectName("shot_crea_cancel_pushButton")
        self.horizontalLayout_4.addWidget(self.shot_crea_cancel_pushButton)
        self.shot_crea_create_pushButton = QtWidgets.QPushButton(self.shot_crea_main_frame)
        self.shot_crea_create_pushButton.setDefault(True)
        self.shot_crea_create_pushButton.setObjectName("shot_crea_create_pushButton")
        self.horizontalLayout_4.addWidget(self.shot_crea_create_pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addWidget(self.shot_crea_main_frame)

        self.retranslateUi(Dialog)
        self.shot_crea_cancel_pushButton.clicked.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Frame range"))
        self.shot_crea_cancel_pushButton.setText(_translate("Dialog", "Cancel"))
        self.shot_crea_create_pushButton.setText(_translate("Dialog", "Modify"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
