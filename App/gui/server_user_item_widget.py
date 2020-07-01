# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\conta\Documents\script\wizard\App\gui\ui_files\server_user_item_widget.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(455, 38)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.server_users_frame = QtWidgets.QFrame(Form)
        self.server_users_frame.setMinimumSize(QtCore.QSize(0, 38))
        self.server_users_frame.setMaximumSize(QtCore.QSize(16777215, 38))
        self.server_users_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.server_users_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.server_users_frame.setObjectName("server_users_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.server_users_frame)
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.server_user_image_label = QtWidgets.QPushButton(self.server_users_frame)
        self.server_user_image_label.setMinimumSize(QtCore.QSize(26, 26))
        self.server_user_image_label.setMaximumSize(QtCore.QSize(26, 26))
        self.server_user_image_label.setText("")
        self.server_user_image_label.setObjectName("server_user_image_label")
        self.horizontalLayout_2.addWidget(self.server_user_image_label)
        self.server_user_name_label = QtWidgets.QLabel(self.server_users_frame)
        self.server_user_name_label.setObjectName("server_user_name_label")
        self.horizontalLayout_2.addWidget(self.server_user_name_label)
        self.server_user_item_conn_label = QtWidgets.QLabel(self.server_users_frame)
        self.server_user_item_conn_label.setMinimumSize(QtCore.QSize(26, 26))
        self.server_user_item_conn_label.setMaximumSize(QtCore.QSize(26, 26))
        self.server_user_item_conn_label.setText("")
        self.server_user_item_conn_label.setObjectName("server_user_item_conn_label")
        self.horizontalLayout_2.addWidget(self.server_user_item_conn_label)
        self.horizontalLayout.addWidget(self.server_users_frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.server_user_name_label.setText(_translate("Form", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
