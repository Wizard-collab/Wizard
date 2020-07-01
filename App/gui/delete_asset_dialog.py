# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\conta\Documents\script\Wizard\App\work\ui_files\delete_asset_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(356, 141)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.delete_asset_frame = QtWidgets.QFrame(Dialog)
        self.delete_asset_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.delete_asset_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.delete_asset_frame.setObjectName("delete_asset_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.delete_asset_frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.delete_asset_image_label = QtWidgets.QLabel(self.delete_asset_frame)
        self.delete_asset_image_label.setMinimumSize(QtCore.QSize(60, 60))
        self.delete_asset_image_label.setMaximumSize(QtCore.QSize(60, 60))
        self.delete_asset_image_label.setText("")
        self.delete_asset_image_label.setObjectName("delete_asset_image_label")
        self.horizontalLayout.addWidget(self.delete_asset_image_label)
        self.label = QtWidgets.QLabel(self.delete_asset_frame)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.delete_asset_frame)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cancel_delete_pushButton = QtWidgets.QPushButton(Dialog)
        self.cancel_delete_pushButton.setMinimumSize(QtCore.QSize(0, 50))
        self.cancel_delete_pushButton.setObjectName("cancel_delete_pushButton")
        self.horizontalLayout_2.addWidget(self.cancel_delete_pushButton)
        self.delete_asset_pushButton = QtWidgets.QPushButton(Dialog)
        self.delete_asset_pushButton.setMinimumSize(QtCore.QSize(0, 50))
        self.delete_asset_pushButton.setObjectName("delete_asset_pushButton")
        self.horizontalLayout_2.addWidget(self.delete_asset_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        self.delete_asset_pushButton.clicked.connect(Dialog.accept)
        self.cancel_delete_pushButton.clicked.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Do you really want to archive this asset ?"))
        self.cancel_delete_pushButton.setText(_translate("Dialog", "Cancel"))
        self.delete_asset_pushButton.setText(_translate("Dialog", "Archive"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
