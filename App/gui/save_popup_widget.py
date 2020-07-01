# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\conta\Documents\script\wizard_devellop\App\gui\ui_files\save_popup_widget.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(116, 116)
        Form.setMinimumSize(QtCore.QSize(116, 116))
        Form.setMaximumSize(QtCore.QSize(116, 116))
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(20, 24, 20, 16)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.save_popup_frame = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_popup_frame.sizePolicy().hasHeightForWidth())
        self.save_popup_frame.setSizePolicy(sizePolicy)
        self.save_popup_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.save_popup_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.save_popup_frame.setObjectName("save_popup_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.save_popup_frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.popup_image_label = QtWidgets.QLabel(self.save_popup_frame)
        self.popup_image_label.setText("")
        self.popup_image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.popup_image_label.setObjectName("popup_image_label")
        self.verticalLayout_2.addWidget(self.popup_image_label)
        self.verticalLayout.addWidget(self.save_popup_frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
