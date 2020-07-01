# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\conta\Documents\script\Wizard\App\work\ui_files\error_handler.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(501, 670)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout.addWidget(self.frame)
        self.handler_textEdit = QtWidgets.QTextEdit(Form)
        self.handler_textEdit.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.handler_textEdit.setObjectName("handler_textEdit")
        self.verticalLayout.addWidget(self.handler_textEdit)
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.hide_dialog_checkBox = QtWidgets.QCheckBox(self.frame_2)
        self.hide_dialog_checkBox.setObjectName("hide_dialog_checkBox")
        self.verticalLayout_3.addWidget(self.hide_dialog_checkBox)
        self.verticalLayout.addWidget(self.frame_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cancel_pushButton = QtWidgets.QPushButton(Form)
        self.cancel_pushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.cancel_pushButton.setObjectName("cancel_pushButton")
        self.horizontalLayout.addWidget(self.cancel_pushButton)
        self.submit_error_pushButton = QtWidgets.QPushButton(Form)
        self.submit_error_pushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.submit_error_pushButton.setObjectName("submit_error_pushButton")
        self.horizontalLayout.addWidget(self.submit_error_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Error handler"))
        self.hide_dialog_checkBox.setText(_translate("Form", "Auto submit errors ( Hide this dialog )"))
        self.cancel_pushButton.setText(_translate("Form", "Cancel"))
        self.submit_error_pushButton.setText(_translate("Form", "Submit error to support"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
