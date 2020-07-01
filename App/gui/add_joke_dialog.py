# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\conta\Documents\script\Wizard\App\work\ui_files\add_joke_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(704, 292)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.joke_data_plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.joke_data_plainTextEdit.sizePolicy().hasHeightForWidth())
        self.joke_data_plainTextEdit.setSizePolicy(sizePolicy)
        self.joke_data_plainTextEdit.setObjectName("joke_data_plainTextEdit")
        self.verticalLayout.addWidget(self.joke_data_plainTextEdit)
        self.chart_frame = QtWidgets.QFrame(Dialog)
        self.chart_frame.setObjectName("chart_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.chart_frame)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.chart_image_label = QtWidgets.QLabel(self.chart_frame)
        self.chart_image_label.setMinimumSize(QtCore.QSize(80, 80))
        self.chart_image_label.setMaximumSize(QtCore.QSize(80, 80))
        self.chart_image_label.setText("")
        self.chart_image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.chart_image_label.setObjectName("chart_image_label")
        self.horizontalLayout.addWidget(self.chart_image_label)
        self.chart_textEdit = QtWidgets.QTextEdit(self.chart_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chart_textEdit.sizePolicy().hasHeightForWidth())
        self.chart_textEdit.setSizePolicy(sizePolicy)
        self.chart_textEdit.setMaximumSize(QtCore.QSize(16777215, 85))
        self.chart_textEdit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.chart_textEdit.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.chart_textEdit.setObjectName("chart_textEdit")
        self.horizontalLayout.addWidget(self.chart_textEdit)
        self.verticalLayout.addWidget(self.chart_frame)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cancel_pushButton = QtWidgets.QPushButton(Dialog)
        self.cancel_pushButton.setMinimumSize(QtCore.QSize(0, 50))
        self.cancel_pushButton.setObjectName("cancel_pushButton")
        self.horizontalLayout_2.addWidget(self.cancel_pushButton)
        self.submit_pushButton = QtWidgets.QPushButton(Dialog)
        self.submit_pushButton.setMinimumSize(QtCore.QSize(0, 50))
        self.submit_pushButton.setObjectName("submit_pushButton")
        self.horizontalLayout_2.addWidget(self.submit_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        self.cancel_pushButton.clicked.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.joke_data_plainTextEdit.setPlaceholderText(_translate("Dialog", "Your joke here..."))
        self.chart_textEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Please ensure that you\'re respectful, everybody has access to your publication.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Do not name anybody.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Every publication is submitted to the technical team.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">If the publication doesn\'t match the chart, you will be asked to delete it.</p></body></html>"))
        self.cancel_pushButton.setText(_translate("Dialog", "Cancel"))
        self.submit_pushButton.setText(_translate("Dialog", "Submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
