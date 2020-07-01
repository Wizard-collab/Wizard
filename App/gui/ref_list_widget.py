# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\conta\Documents\script\wizard_devellop\App\gui\ui_files\ref_list_widget.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 719)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.node_editor_frame = QtWidgets.QFrame(Form)
        self.node_editor_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.node_editor_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.node_editor_frame.setObjectName("node_editor_frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.node_editor_frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.scene_manager_label = QtWidgets.QLabel(self.node_editor_frame)
        self.scene_manager_label.setObjectName("scene_manager_label")
        self.verticalLayout_4.addWidget(self.scene_manager_label)
        self.node_editor_scrollArea = QtWidgets.QScrollArea(self.node_editor_frame)
        self.node_editor_scrollArea.setStyleSheet("")
        self.node_editor_scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.node_editor_scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.node_editor_scrollArea.setWidgetResizable(True)
        self.node_editor_scrollArea.setObjectName("node_editor_scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 774, 670))
        self.scrollAreaWidgetContents.setStyleSheet("")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.ref_assets_verticalLayout = QtWidgets.QVBoxLayout()
        self.ref_assets_verticalLayout.setSpacing(1)
        self.ref_assets_verticalLayout.setObjectName("ref_assets_verticalLayout")
        self.verticalLayout_3.addLayout(self.ref_assets_verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.node_editor_scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_4.addWidget(self.node_editor_scrollArea)
        self.verticalLayout_2.addWidget(self.node_editor_frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.scene_manager_label.setText(_translate("Form", "Scene manager"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
