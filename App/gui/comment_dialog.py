# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\conta\Documents\script\wizard_devellop\App\gui\ui_files\comment_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(657, 283)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.comment_dialog_frame = QtWidgets.QFrame(Dialog)
        self.comment_dialog_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.comment_dialog_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.comment_dialog_frame.setObjectName("comment_dialog_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.comment_dialog_frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.comment_dialog_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.comment_asset_label = QtWidgets.QLabel(self.comment_dialog_frame)
        self.comment_asset_label.setText("")
        self.comment_asset_label.setObjectName("comment_asset_label")
        self.horizontalLayout_2.addWidget(self.comment_asset_label)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addWidget(self.comment_dialog_frame)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.comment_dialog_plainTextEdit = QtWidgets.QPlainTextEdit(self.frame)
        self.comment_dialog_plainTextEdit.setObjectName("comment_dialog_plainTextEdit")
        self.verticalLayout_3.addWidget(self.comment_dialog_plainTextEdit)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.comment_dialog_pushButton = QtWidgets.QPushButton(self.frame_2)
        self.comment_dialog_pushButton.setMinimumSize(QtCore.QSize(100, 35))
        self.comment_dialog_pushButton.setMaximumSize(QtCore.QSize(100, 35))
        self.comment_dialog_pushButton.setObjectName("comment_dialog_pushButton")
        self.horizontalLayout.addWidget(self.comment_dialog_pushButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.frame_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Asset :  "))
        self.comment_dialog_plainTextEdit.setPlaceholderText(_translate("Dialog", "Your comment here..."))
        self.comment_dialog_pushButton.setText(_translate("Dialog", "Submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
