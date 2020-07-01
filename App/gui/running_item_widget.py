# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\conta\Documents\script\wizard\App\gui\ui_files\running_item_widget.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(527, 50)
        Form.setMinimumSize(QtCore.QSize(0, 50))
        Form.setMaximumSize(QtCore.QSize(16777215, 50))
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.running_item_main_frame = QtWidgets.QFrame(Form)
        self.running_item_main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.running_item_main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.running_item_main_frame.setObjectName("running_item_main_frame")
        self.items_layout = QtWidgets.QHBoxLayout(self.running_item_main_frame)
        self.items_layout.setSpacing(3)
        self.items_layout.setObjectName("items_layout")
        self.running_item_image_label = QtWidgets.QLabel(self.running_item_main_frame)
        self.running_item_image_label.setMinimumSize(QtCore.QSize(26, 26))
        self.running_item_image_label.setMaximumSize(QtCore.QSize(26, 26))
        self.running_item_image_label.setText("")
        self.running_item_image_label.setObjectName("running_item_image_label")
        self.items_layout.addWidget(self.running_item_image_label)
        self.running_item_asset_label = QtWidgets.QLabel(self.running_item_main_frame)
        self.running_item_asset_label.setText("")
        self.running_item_asset_label.setObjectName("running_item_asset_label")
        self.items_layout.addWidget(self.running_item_asset_label)
        self.running_item_lock_pushButton = QtWidgets.QPushButton(self.running_item_main_frame)
        self.running_item_lock_pushButton.setMinimumSize(QtCore.QSize(26, 26))
        self.running_item_lock_pushButton.setMaximumSize(QtCore.QSize(26, 26))
        self.running_item_lock_pushButton.setText("")
        self.running_item_lock_pushButton.setObjectName("running_item_lock_pushButton")
        self.items_layout.addWidget(self.running_item_lock_pushButton)
        self.focus_pushButton = QtWidgets.QPushButton(self.running_item_main_frame)
        self.focus_pushButton.setMinimumSize(QtCore.QSize(26, 26))
        self.focus_pushButton.setMaximumSize(QtCore.QSize(26, 26))
        self.focus_pushButton.setText("")
        self.focus_pushButton.setObjectName("focus_pushButton")
        self.items_layout.addWidget(self.focus_pushButton)
        self.horizontalLayout.addWidget(self.running_item_main_frame)

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
