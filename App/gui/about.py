# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\conta\Documents\script\Wizard\App\work\ui_files\about.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(906, 548)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(5, 11, 5, 11)
        self.verticalLayout_2.setSpacing(11)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.about_wizard_icon_label = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.about_wizard_icon_label.sizePolicy().hasHeightForWidth())
        self.about_wizard_icon_label.setSizePolicy(sizePolicy)
        self.about_wizard_icon_label.setMinimumSize(QtCore.QSize(40, 40))
        self.about_wizard_icon_label.setMaximumSize(QtCore.QSize(40, 40))
        self.about_wizard_icon_label.setText("")
        self.about_wizard_icon_label.setObjectName("about_wizard_icon_label")
        self.horizontalLayout_3.addWidget(self.about_wizard_icon_label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setVerticalSpacing(1)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.about_release_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.about_release_lineEdit.setReadOnly(True)
        self.about_release_lineEdit.setObjectName("about_release_lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.about_release_lineEdit)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.about_license_textEdit = QtWidgets.QTextEdit(self.frame)
        self.about_license_textEdit.setMinimumSize(QtCore.QSize(0, 400))
        self.about_license_textEdit.setReadOnly(True)
        self.about_license_textEdit.setObjectName("about_license_textEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.about_license_textEdit)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.about_install_dir_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.about_install_dir_lineEdit.setObjectName("about_install_dir_lineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.about_install_dir_lineEdit)
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.about_contact_lineEdit = QtWidgets.QLineEdit(self.frame)
        self.about_contact_lineEdit.setReadOnly(True)
        self.about_contact_lineEdit.setObjectName("about_contact_lineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.about_contact_lineEdit)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.horizontalFrame = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalFrame.sizePolicy().hasHeightForWidth())
        self.horizontalFrame.setSizePolicy(sizePolicy)
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2.addWidget(self.horizontalFrame)
        self.horizontalFrame_2 = QtWidgets.QFrame(self.frame)
        self.horizontalFrame_2.setObjectName("horizontalFrame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalFrame_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2.addWidget(self.horizontalFrame_2)
        self.about_author_label = QtWidgets.QLabel(self.frame)
        self.about_author_label.setAlignment(QtCore.Qt.AlignCenter)
        self.about_author_label.setObjectName("about_author_label")
        self.verticalLayout_2.addWidget(self.about_author_label)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Release "))
        self.label_3.setText(_translate("Form", "License "))
        self.label_5.setText(_translate("Form", "Install directory"))
        self.label_6.setText(_translate("Form", "Contact"))
        self.about_author_label.setText(_translate("Form", "Authors : Leo BRUNEL - Alexandre Manzanares"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
