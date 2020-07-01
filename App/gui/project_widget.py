# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\leo\Documents\Script\Wizard\App\gui\ui_files\project_widget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(738, 65)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.project_widget_frame = QtWidgets.QFrame(Form)
        self.project_widget_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.project_widget_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.project_widget_frame.setObjectName("project_widget_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.project_widget_frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.project_folder_image_label = QtWidgets.QLabel(self.project_widget_frame)
        self.project_folder_image_label.setMinimumSize(QtCore.QSize(40, 40))
        self.project_folder_image_label.setMaximumSize(QtCore.QSize(40, 40))
        self.project_folder_image_label.setText("")
        self.project_folder_image_label.setObjectName("project_folder_image_label")
        self.horizontalLayout_2.addWidget(self.project_folder_image_label)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.project_name_label = QtWidgets.QLabel(self.project_widget_frame)
        self.project_name_label.setObjectName("project_name_label")
        self.verticalLayout.addWidget(self.project_name_label)
        self.project_path_label = QtWidgets.QLabel(self.project_widget_frame)
        self.project_path_label.setObjectName("project_path_label")
        self.verticalLayout.addWidget(self.project_path_label)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout.addWidget(self.project_widget_frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.project_name_label.setText(_translate("Form", "Project name"))
        self.project_path_label.setText(_translate("Form", "Project path"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

