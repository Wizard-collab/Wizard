# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\conta\Documents\script\Wizard\App\ui_files\editable_list_item_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1022, 30)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.reference_list_item_frame = QtWidgets.QFrame(Form)
        self.reference_list_item_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.reference_list_item_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.reference_list_item_frame.setObjectName("reference_list_item_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.reference_list_item_frame)
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.icon_label = QtWidgets.QLabel(self.reference_list_item_frame)
        self.icon_label.setMinimumSize(QtCore.QSize(24, 24))
        self.icon_label.setMaximumSize(QtCore.QSize(24, 24))
        self.icon_label.setText("")
        self.icon_label.setScaledContents(False)
        self.icon_label.setAlignment(QtCore.Qt.AlignCenter)
        self.icon_label.setObjectName("icon_label")
        self.horizontalLayout.addWidget(self.icon_label)
        self.datas_list = QtWidgets.QHBoxLayout()
        self.datas_list.setObjectName("datas_list")
        self.horizontalLayout.addLayout(self.datas_list)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.buttons_list = QtWidgets.QHBoxLayout()
        self.buttons_list.setSpacing(1)
        self.buttons_list.setObjectName("buttons_list")
        self.horizontalLayout.addLayout(self.buttons_list)
        self.horizontalLayout_2.addWidget(self.reference_list_item_frame)

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
