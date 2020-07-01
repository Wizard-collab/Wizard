# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\leo\Documents\Script\Wizard\App\gui\ui_files\log.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_log(object):
    def setupUi(self, log):
        log.setObjectName("log")
        log.resize(1126, 759)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(log)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(11, 4, 11, 11)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.critical_checkBox = QtWidgets.QCheckBox(log)
        self.critical_checkBox.setObjectName("critical_checkBox")
        self.verticalLayout.addWidget(self.critical_checkBox)
        self.log_textEdit = QtWidgets.QTextEdit(log)
        font = QtGui.QFont()
        font.setFamily("Courier")
        self.log_textEdit.setFont(font)
        self.log_textEdit.setUndoRedoEnabled(False)
        self.log_textEdit.setReadOnly(True)
        self.log_textEdit.setObjectName("log_textEdit")
        self.verticalLayout.addWidget(self.log_textEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.report_error_pushButton = QtWidgets.QPushButton(log)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.report_error_pushButton.sizePolicy().hasHeightForWidth())
        self.report_error_pushButton.setSizePolicy(sizePolicy)
        self.report_error_pushButton.setMinimumSize(QtCore.QSize(195, 50))
        self.report_error_pushButton.setMaximumSize(QtCore.QSize(195, 16777215))
        self.report_error_pushButton.setObjectName("report_error_pushButton")
        self.horizontalLayout.addWidget(self.report_error_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(log)
        QtCore.QMetaObject.connectSlotsByName(log)

    def retranslateUi(self, log):
        _translate = QtCore.QCoreApplication.translate
        log.setWindowTitle(_translate("log", "Form"))
        self.critical_checkBox.setText(_translate("log", "Critical"))
        self.log_textEdit.setHtml(_translate("log", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Courier\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.report_error_pushButton.setText(_translate("log", "Report log ( Via Email )"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    log = QtWidgets.QWidget()
    ui = Ui_log()
    ui.setupUi(log)
    log.show()
    sys.exit(app.exec_())

