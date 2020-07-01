# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\l.brunel\Documents\wizard\App\gui\ui_files\image_viewer.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1371, 857)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.image_label = QtWidgets.QLabel(Form)
        self.image_label.setMinimumSize(QtCore.QSize(1371, 857))
        self.image_label.setMaximumSize(QtCore.QSize(1371, 857))
        self.image_label.setLineWidth(0)
        self.image_label.setText("")
        self.image_label.setObjectName("image_label")
        self.verticalLayout.addWidget(self.image_label)

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

