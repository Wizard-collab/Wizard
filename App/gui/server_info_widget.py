# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\conta\Documents\script\wizard\App\gui\ui_files\server_info_widget.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(458, 269)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(25, 25, 25, 25)
        self.verticalLayout_3.setSpacing(8)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.welcome_info_title_frame = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.welcome_info_title_frame.sizePolicy().hasHeightForWidth())
        self.welcome_info_title_frame.setSizePolicy(sizePolicy)
        self.welcome_info_title_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.welcome_info_title_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.welcome_info_title_frame.setObjectName("welcome_info_title_frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.welcome_info_title_frame)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.welcome_info_image_label = QtWidgets.QLabel(self.welcome_info_title_frame)
        self.welcome_info_image_label.setMinimumSize(QtCore.QSize(50, 50))
        self.welcome_info_image_label.setMaximumSize(QtCore.QSize(50, 50))
        self.welcome_info_image_label.setText("")
        self.welcome_info_image_label.setObjectName("welcome_info_image_label")
        self.horizontalLayout_5.addWidget(self.welcome_info_image_label)
        self.welcome_info_title_label = QtWidgets.QLabel(self.welcome_info_title_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.welcome_info_title_label.sizePolicy().hasHeightForWidth())
        self.welcome_info_title_label.setSizePolicy(sizePolicy)
        self.welcome_info_title_label.setObjectName("welcome_info_title_label")
        self.horizontalLayout_5.addWidget(self.welcome_info_title_label)
        self.verticalLayout_3.addWidget(self.welcome_info_title_frame)
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setMaximumSize(QtCore.QSize(16777215, 1))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_3.addWidget(self.line_2)
        self.welcome_main_textEdit = QtWidgets.QTextEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.welcome_main_textEdit.sizePolicy().hasHeightForWidth())
        self.welcome_main_textEdit.setSizePolicy(sizePolicy)
        self.welcome_main_textEdit.setMaximumSize(QtCore.QSize(16777215, 90))
        self.welcome_main_textEdit.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.welcome_main_textEdit.setObjectName("welcome_main_textEdit")
        self.verticalLayout_3.addWidget(self.welcome_main_textEdit)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.ok_pushButton = QtWidgets.QPushButton(Form)
        self.ok_pushButton.setMinimumSize(QtCore.QSize(120, 50))
        self.ok_pushButton.setObjectName("ok_pushButton")
        self.horizontalLayout_2.addWidget(self.ok_pushButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.welcome_info_title_label.setText(_translate("Form", "What\'s the server ?"))
        self.welcome_main_textEdit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Wizard will quit now, please run a server and restart.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">For a production under wizard managment, launch the server to host the production events of all users connected to the project and allow an automatic update.</p></body></html>"))
        self.ok_pushButton.setText(_translate("Form", "Got it !"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
