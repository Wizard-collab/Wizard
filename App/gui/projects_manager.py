# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\leo\Documents\Script\Wizard\App\gui\ui_files\projects_manager.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(804, 594)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.project_manager_header_frame = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.project_manager_header_frame.sizePolicy().hasHeightForWidth())
        self.project_manager_header_frame.setSizePolicy(sizePolicy)
        self.project_manager_header_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.project_manager_header_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.project_manager_header_frame.setObjectName("project_manager_header_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.project_manager_header_frame)
        self.horizontalLayout.setSpacing(11)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.project_manager_image_label = QtWidgets.QLabel(self.project_manager_header_frame)
        self.project_manager_image_label.setMinimumSize(QtCore.QSize(55, 55))
        self.project_manager_image_label.setMaximumSize(QtCore.QSize(55, 55))
        self.project_manager_image_label.setText("")
        self.project_manager_image_label.setObjectName("project_manager_image_label")
        self.horizontalLayout.addWidget(self.project_manager_image_label)
        self.label_2 = QtWidgets.QLabel(self.project_manager_header_frame)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout_2.addWidget(self.project_manager_header_frame)
        self.projects_scrollArea = QtWidgets.QScrollArea(Form)
        self.projects_scrollArea.setWidgetResizable(True)
        self.projects_scrollArea.setObjectName("projects_scrollArea")
        self.projects_scrollAreaWidgetContents = QtWidgets.QWidget()
        self.projects_scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 802, 513))
        self.projects_scrollAreaWidgetContents.setObjectName("projects_scrollAreaWidgetContents")
        self.projects_verticalLayout = QtWidgets.QVBoxLayout(self.projects_scrollAreaWidgetContents)
        self.projects_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.projects_verticalLayout.setSpacing(1)
        self.projects_verticalLayout.setObjectName("projects_verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.projects_verticalLayout.addItem(spacerItem)
        self.projects_scrollArea.setWidget(self.projects_scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.projects_scrollArea)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Projects"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

