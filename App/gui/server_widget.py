# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\conta\Documents\script\Wizard\App\work\ui_files\server_widget.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(384, 564)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_2.setSpacing(1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.server_quit_pushButton = QtWidgets.QPushButton(self.frame_2)
        self.server_quit_pushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.server_quit_pushButton.setObjectName("server_quit_pushButton")
        self.horizontalLayout_2.addWidget(self.server_quit_pushButton)
        self.server_reduce_pushButton = QtWidgets.QPushButton(self.frame_2)
        self.server_reduce_pushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.server_reduce_pushButton.setObjectName("server_reduce_pushButton")
        self.horizontalLayout_2.addWidget(self.server_reduce_pushButton)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(Form)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.server_project_label = QtWidgets.QLabel(self.frame_3)
        self.server_project_label.setObjectName("server_project_label")
        self.horizontalLayout_3.addWidget(self.server_project_label)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.server_ip_label = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.server_ip_label.sizePolicy().hasHeightForWidth())
        self.server_ip_label.setSizePolicy(sizePolicy)
        self.server_ip_label.setObjectName("server_ip_label")
        self.horizontalLayout.addWidget(self.server_ip_label)
        self.server_connexions_label = QtWidgets.QLabel(self.frame)
        self.server_connexions_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.server_connexions_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.server_connexions_label.setObjectName("server_connexions_label")
        self.horizontalLayout.addWidget(self.server_connexions_label)
        self.verticalLayout.addWidget(self.frame)
        self.server__users_verticalFrame = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.server__users_verticalFrame.sizePolicy().hasHeightForWidth())
        self.server__users_verticalFrame.setSizePolicy(sizePolicy)
        self.server__users_verticalFrame.setObjectName("server__users_verticalFrame")
        self.users_layout_0 = QtWidgets.QVBoxLayout(self.server__users_verticalFrame)
        self.users_layout_0.setObjectName("users_layout_0")
        self.users_layout = QtWidgets.QVBoxLayout()
        self.users_layout.setObjectName("users_layout")
        self.users_layout_0.addLayout(self.users_layout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.users_layout_0.addItem(spacerItem)
        self.verticalLayout.addWidget(self.server__users_verticalFrame)
        self.log_textEdit = QtWidgets.QTextEdit(Form)
        self.log_textEdit.setReadOnly(True)
        self.log_textEdit.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.log_textEdit.setObjectName("log_textEdit")
        self.verticalLayout.addWidget(self.log_textEdit)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.server_quit_pushButton.setText(_translate("Form", "Quit"))
        self.server_reduce_pushButton.setText(_translate("Form", "Reduce"))
        self.server_project_label.setText(_translate("Form", "Project"))
        self.server_ip_label.setText(_translate("Form", "IP Label"))
        self.server_connexions_label.setText(_translate("Form", "Connexions"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
