# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\conta\Documents\script\Wizard\App\work\ui_files\add_variant_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(237, 132)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.variant_name_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.variant_name_lineEdit.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.variant_name_lineEdit.setObjectName("variant_name_lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.variant_name_lineEdit)
        self.verticalLayout.addLayout(self.formLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cancel_pushButton = QtWidgets.QPushButton(self.frame)
        self.cancel_pushButton.setMinimumSize(QtCore.QSize(0, 50))
        self.cancel_pushButton.setObjectName("cancel_pushButton")
        self.horizontalLayout.addWidget(self.cancel_pushButton)
        self.create_variant_pushButton = QtWidgets.QPushButton(self.frame)
        self.create_variant_pushButton.setMinimumSize(QtCore.QSize(0, 50))
        self.create_variant_pushButton.setDefault(True)
        self.create_variant_pushButton.setObjectName("create_variant_pushButton")
        self.horizontalLayout.addWidget(self.create_variant_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addWidget(self.frame)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.retranslateUi(Dialog)
        self.cancel_pushButton.clicked.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Variant name"))
        self.cancel_pushButton.setText(_translate("Dialog", "Cancel"))
        self.create_variant_pushButton.setText(_translate("Dialog", "Create variant"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
