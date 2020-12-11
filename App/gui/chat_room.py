# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\conta\Documents\script\Wizard\App\ui_files\chat_room.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(371, 574)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.chat_room_context_label = QtWidgets.QLabel(self.frame)
        self.chat_room_context_label.setObjectName("chat_room_context_label")
        self.verticalLayout_2.addWidget(self.chat_room_context_label)
        self.verticalLayout.addWidget(self.frame)
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 369, 450))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.scrollAreaLayout.setSpacing(0)
        self.scrollAreaLayout.setObjectName("scrollAreaLayout")
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.scrollAreaLayout.addItem(spacerItem)
        self.chat_messages_layout = QtWidgets.QVBoxLayout()
        self.chat_messages_layout.setSpacing(1)
        self.chat_messages_layout.setObjectName("chat_messages_layout")
        self.scrollAreaLayout.addLayout(self.chat_messages_layout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.chat_room_files_frame = QtWidgets.QFrame(Form)
        self.chat_room_files_frame.setObjectName("chat_room_files_frame")
        self.chat_room_file_layout = QtWidgets.QVBoxLayout(self.chat_room_files_frame)
        self.chat_room_file_layout.setContentsMargins(4, 4, 4, 4)
        self.chat_room_file_layout.setSpacing(1)
        self.chat_room_file_layout.setObjectName("chat_room_file_layout")
        self.chat_room_file_layout_2 = QtWidgets.QHBoxLayout()
        self.chat_room_file_layout_2.setContentsMargins(-1, 0, -1, -1)
        self.chat_room_file_layout_2.setSpacing(0)
        self.chat_room_file_layout_2.setObjectName("chat_room_file_layout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.chat_room_file_layout_2.addItem(spacerItem1)
        self.chat_room_file_frame = QtWidgets.QFrame(self.chat_room_files_frame)
        self.chat_room_file_frame.setMinimumSize(QtCore.QSize(150, 40))
        self.chat_room_file_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.chat_room_file_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.chat_room_file_frame.setObjectName("chat_room_file_frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.chat_room_file_frame)
        self.horizontalLayout_4.setContentsMargins(8, 8, 8, 8)
        self.horizontalLayout_4.setSpacing(8)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.chat_room_file_name_label = QtWidgets.QLabel(self.chat_room_file_frame)
        self.chat_room_file_name_label.setObjectName("chat_room_file_name_label")
        self.horizontalLayout_4.addWidget(self.chat_room_file_name_label)
        self.chat_room_remove_file_pushButton = QtWidgets.QPushButton(self.chat_room_file_frame)
        self.chat_room_remove_file_pushButton.setMinimumSize(QtCore.QSize(20, 20))
        self.chat_room_remove_file_pushButton.setMaximumSize(QtCore.QSize(20, 20))
        self.chat_room_remove_file_pushButton.setText("")
        self.chat_room_remove_file_pushButton.setIconSize(QtCore.QSize(12, 12))
        self.chat_room_remove_file_pushButton.setObjectName("chat_room_remove_file_pushButton")
        self.horizontalLayout_4.addWidget(self.chat_room_remove_file_pushButton)
        self.chat_room_file_layout_2.addWidget(self.chat_room_file_frame)
        self.chat_room_file_layout.addLayout(self.chat_room_file_layout_2)
        self.verticalLayout.addWidget(self.chat_room_files_frame)
        self.horizontalFrame = QtWidgets.QFrame(Form)
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
        self.chat_message_lineEdit = QtWidgets.QLineEdit(self.horizontalFrame)
        self.chat_message_lineEdit.setMinimumSize(QtCore.QSize(0, 28))
        self.chat_message_lineEdit.setMaximumSize(QtCore.QSize(16777215, 28))
        self.chat_message_lineEdit.setObjectName("chat_message_lineEdit")
        self.horizontalLayout.addWidget(self.chat_message_lineEdit)
        self.chat_room_add_file_pushButton = QtWidgets.QPushButton(self.horizontalFrame)
        self.chat_room_add_file_pushButton.setMinimumSize(QtCore.QSize(28, 28))
        self.chat_room_add_file_pushButton.setMaximumSize(QtCore.QSize(28, 28))
        self.chat_room_add_file_pushButton.setText("")
        self.chat_room_add_file_pushButton.setObjectName("chat_room_add_file_pushButton")
        self.horizontalLayout.addWidget(self.chat_room_add_file_pushButton)
        self.chat_emoji_pushButton = QtWidgets.QPushButton(self.horizontalFrame)
        self.chat_emoji_pushButton.setMinimumSize(QtCore.QSize(28, 28))
        self.chat_emoji_pushButton.setMaximumSize(QtCore.QSize(28, 28))
        self.chat_emoji_pushButton.setObjectName("chat_emoji_pushButton")
        self.horizontalLayout.addWidget(self.chat_emoji_pushButton)
        self.chat_send_pushButton = QtWidgets.QPushButton(self.horizontalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chat_send_pushButton.sizePolicy().hasHeightForWidth())
        self.chat_send_pushButton.setSizePolicy(sizePolicy)
        self.chat_send_pushButton.setMinimumSize(QtCore.QSize(80, 28))
        self.chat_send_pushButton.setMaximumSize(QtCore.QSize(80, 28))
        self.chat_send_pushButton.setObjectName("chat_send_pushButton")
        self.horizontalLayout.addWidget(self.chat_send_pushButton)
        self.verticalLayout.addWidget(self.horizontalFrame)
        self.horizontalFrame1 = QtWidgets.QFrame(Form)
        self.horizontalFrame1.setObjectName("horizontalFrame1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalFrame1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout.addWidget(self.horizontalFrame1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.chat_room_context_label.setText(_translate("Form", "context"))
        self.chat_room_file_name_label.setText(_translate("Form", "file"))
        self.chat_emoji_pushButton.setText(_translate("Form", "😃"))
        self.chat_send_pushButton.setText(_translate("Form", "send"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
