# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\conta\Documents\script\wizard\App\gui\ui_files\asset_creation_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(353, 107)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.shot_crea_main_frame = QtWidgets.QFrame(Dialog)
        self.shot_crea_main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.shot_crea_main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.shot_crea_main_frame.setObjectName("shot_crea_main_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.shot_crea_main_frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.shot_crea_main_frame)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.asset_crea_name_lineEdit = QtWidgets.QLineEdit(self.shot_crea_main_frame)
        self.asset_crea_name_lineEdit.setObjectName("asset_crea_name_lineEdit")
        self.horizontalLayout_3.addWidget(self.asset_crea_name_lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.asset_crea_cancel_pushButton = QtWidgets.QPushButton(self.shot_crea_main_frame)
        self.asset_crea_cancel_pushButton.setObjectName("asset_crea_cancel_pushButton")
        self.horizontalLayout_4.addWidget(self.asset_crea_cancel_pushButton)
        self.asset_crea_create_pushButton = QtWidgets.QPushButton(self.shot_crea_main_frame)
        self.asset_crea_create_pushButton.setDefault(True)
        self.asset_crea_create_pushButton.setObjectName("asset_crea_create_pushButton")
        self.horizontalLayout_4.addWidget(self.asset_crea_create_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout.addWidget(self.shot_crea_main_frame)

        self.retranslateUi(Dialog)
        self.asset_crea_cancel_pushButton.clicked.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Asset_name"))
        self.asset_crea_cancel_pushButton.setText(_translate("Dialog", "Cancel"))
        self.asset_crea_create_pushButton.setText(_translate("Dialog", "Create"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
