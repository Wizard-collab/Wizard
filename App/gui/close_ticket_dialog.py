# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\conta\Documents\script\Wizard\App\work\ui_files\close_ticket_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(506, 209)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ticket_icon_label = QtWidgets.QLabel(self.frame_2)
        self.ticket_icon_label.setMinimumSize(QtCore.QSize(24, 24))
        self.ticket_icon_label.setMaximumSize(QtCore.QSize(24, 24))
        self.ticket_icon_label.setText("")
        self.ticket_icon_label.setObjectName("ticket_icon_label")
        self.horizontalLayout_2.addWidget(self.ticket_icon_label)
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame = QtWidgets.QFrame(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.close_ticket_plainTextEdit = QtWidgets.QPlainTextEdit(self.frame)
        self.close_ticket_plainTextEdit.setObjectName("close_ticket_plainTextEdit")
        self.verticalLayout_2.addWidget(self.close_ticket_plainTextEdit)
        self.verticalLayout.addWidget(self.frame)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.close_ticket_widget_cancel_pushButton = QtWidgets.QPushButton(Dialog)
        self.close_ticket_widget_cancel_pushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.close_ticket_widget_cancel_pushButton.setObjectName("close_ticket_widget_cancel_pushButton")
        self.horizontalLayout.addWidget(self.close_ticket_widget_cancel_pushButton)
        self.close_ticket_widget_close_pushButton = QtWidgets.QPushButton(Dialog)
        self.close_ticket_widget_close_pushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.close_ticket_widget_close_pushButton.setObjectName("close_ticket_widget_close_pushButton")
        self.horizontalLayout.addWidget(self.close_ticket_widget_close_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Close ticket"))
        self.close_ticket_widget_cancel_pushButton.setText(_translate("Dialog", "Cancel"))
        self.close_ticket_widget_close_pushButton.setText(_translate("Dialog", "Close ticket"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
