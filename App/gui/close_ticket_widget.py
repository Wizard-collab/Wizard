# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\conta\Documents\script\Wizard\App\work\ui_files\close_ticket_widget.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(556, 298)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(Form)
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
        self.frame_3 = QtWidgets.QFrame(Form)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.open_ticket_asset_label = QtWidgets.QLabel(self.frame_3)
        self.open_ticket_asset_label.setText("")
        self.open_ticket_asset_label.setObjectName("open_ticket_asset_label")
        self.horizontalLayout_3.addWidget(self.open_ticket_asset_label)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame = QtWidgets.QFrame(Form)
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
        self.open_ticket_widget_cancel_pushButton = QtWidgets.QPushButton(Form)
        self.open_ticket_widget_cancel_pushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.open_ticket_widget_cancel_pushButton.setObjectName("open_ticket_widget_cancel_pushButton")
        self.horizontalLayout.addWidget(self.open_ticket_widget_cancel_pushButton)
        self.open_ticket_widget_open_pushButton = QtWidgets.QPushButton(Form)
        self.open_ticket_widget_open_pushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.open_ticket_widget_open_pushButton.setObjectName("open_ticket_widget_open_pushButton")
        self.horizontalLayout.addWidget(self.open_ticket_widget_open_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Close ticket"))
        self.label_2.setText(_translate("Form", "Asset :"))
        self.open_ticket_widget_cancel_pushButton.setText(_translate("Form", "Cancel"))
        self.open_ticket_widget_open_pushButton.setText(_translate("Form", "Close ticket"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
