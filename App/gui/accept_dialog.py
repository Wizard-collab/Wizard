# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\leo\Documents\Script\Wizard\App\gui\ui_files\accept_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(462, 133)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.accept_widget_image_label = QtWidgets.QLabel(Dialog)
        self.accept_widget_image_label.setMinimumSize(QtCore.QSize(60, 60))
        self.accept_widget_image_label.setMaximumSize(QtCore.QSize(60, 60))
        self.accept_widget_image_label.setText("")
        self.accept_widget_image_label.setObjectName("accept_widget_image_label")
        self.horizontalLayout.addWidget(self.accept_widget_image_label)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.accept_widget_label = QtWidgets.QLabel(Dialog)
        self.accept_widget_label.setText("")
        self.accept_widget_label.setObjectName("accept_widget_label")
        self.verticalLayout.addWidget(self.accept_widget_label)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cancel_pushButton = QtWidgets.QPushButton(Dialog)
        self.cancel_pushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.cancel_pushButton.setObjectName("cancel_pushButton")
        self.horizontalLayout_2.addWidget(self.cancel_pushButton)
        self.yes_pushButton = QtWidgets.QPushButton(Dialog)
        self.yes_pushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.yes_pushButton.setObjectName("yes_pushButton")
        self.horizontalLayout_2.addWidget(self.yes_pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        self.cancel_pushButton.clicked.connect(Dialog.reject)
        self.yes_pushButton.clicked.connect(Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.cancel_pushButton.setText(_translate("Dialog", "Cancel"))
        self.yes_pushButton.setText(_translate("Dialog", "Yes"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
