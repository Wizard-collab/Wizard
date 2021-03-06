# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\conta\Documents\script\Wizard\App\ui_files\workflow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(437, 216)
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
        self.frame_4 = QtWidgets.QFrame(Form)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.formLayout_2 = QtWidgets.QFormLayout(self.frame_4)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_8 = QtWidgets.QLabel(self.frame_4)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.frame_rate_spinBox = QtWidgets.QSpinBox(self.frame_4)
        self.frame_rate_spinBox.setObjectName("frame_rate_spinBox")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.frame_rate_spinBox)
        self.label_9 = QtWidgets.QLabel(self.frame_4)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.f_width_lineEdit = QtWidgets.QLineEdit(self.frame_4)
        self.f_width_lineEdit.setObjectName("f_width_lineEdit")
        self.horizontalLayout.addWidget(self.f_width_lineEdit)
        self.label_10 = QtWidgets.QLabel(self.frame_4)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout.addWidget(self.label_10)
        self.f_height_lineEdit = QtWidgets.QLineEdit(self.frame_4)
        self.f_height_lineEdit.setObjectName("f_height_lineEdit")
        self.horizontalLayout.addWidget(self.f_height_lineEdit)
        self.formLayout_2.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.formLayout = QtWidgets.QFormLayout(self.frame_2)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.cfx_ext_comboBox = QtWidgets.QComboBox(self.frame_2)
        self.cfx_ext_comboBox.setObjectName("cfx_ext_comboBox")
        self.cfx_ext_comboBox.addItem("")
        self.cfx_ext_comboBox.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cfx_ext_comboBox)
        self.verticalLayout.addWidget(self.frame_2)
        self.save_workflow_pushButton = QtWidgets.QPushButton(Form)
        self.save_workflow_pushButton.setMinimumSize(QtCore.QSize(0, 50))
        self.save_workflow_pushButton.setObjectName("save_workflow_pushButton")
        self.verticalLayout.addWidget(self.save_workflow_pushButton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Setup your project"))
        self.label_8.setText(_translate("Form", "Frame rate"))
        self.label_9.setText(_translate("Form", "Format"))
        self.label_10.setText(_translate("Form", "x"))
        self.label_2.setText(_translate("Form", "CFX (fur) exports"))
        self.cfx_ext_comboBox.setItemText(0, _translate("Form", ".fur"))
        self.cfx_ext_comboBox.setItemText(1, _translate("Form", ".abc"))
        self.save_workflow_pushButton.setText(_translate("Form", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
