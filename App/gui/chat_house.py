# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\conta\Documents\script\Wizard\App\ui_files\chat_house.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(686, 607)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName("splitter")
        self.chat_house_rooms_frame = QtWidgets.QFrame(self.splitter)
        self.chat_house_rooms_frame.setMinimumSize(QtCore.QSize(230, 0))
        self.chat_house_rooms_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.chat_house_rooms_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.chat_house_rooms_frame.setObjectName("chat_house_rooms_frame")
        self.frame_layout = QtWidgets.QVBoxLayout(self.chat_house_rooms_frame)
        self.frame_layout.setContentsMargins(0, 0, 0, 0)
        self.frame_layout.setSpacing(1)
        self.frame_layout.setObjectName("frame_layout")
        self.room_category_frame_1 = QtWidgets.QFrame(self.chat_house_rooms_frame)
        self.room_category_frame_1.setObjectName("room_category_frame_1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.room_category_frame_1)
        self.horizontalLayout_2.setContentsMargins(8, 8, 8, 8)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.room_category_frame_1)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.create_room_pushButton = QtWidgets.QPushButton(self.room_category_frame_1)
        self.create_room_pushButton.setMinimumSize(QtCore.QSize(26, 26))
        self.create_room_pushButton.setMaximumSize(QtCore.QSize(26, 26))
        self.create_room_pushButton.setStyleSheet("border-radius:13px;")
        self.create_room_pushButton.setObjectName("create_room_pushButton")
        self.horizontalLayout_2.addWidget(self.create_room_pushButton)
        self.frame_layout.addWidget(self.room_category_frame_1)
        self.scrollArea = QtWidgets.QScrollArea(self.chat_house_rooms_frame)
        self.scrollArea.setStyleSheet("#scrollAreaWidgetContents_4, #scrollArea{background-color:transparent;}")
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 226, 560))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.chat_house_rooms_frame_layout = QtWidgets.QVBoxLayout()
        self.chat_house_rooms_frame_layout.setSpacing(1)
        self.chat_house_rooms_frame_layout.setObjectName("chat_house_rooms_frame_layout")
        self.verticalLayout_2.addLayout(self.chat_house_rooms_frame_layout)
        self.room_category_frame = QtWidgets.QFrame(self.scrollAreaWidgetContents_4)
        self.room_category_frame.setObjectName("room_category_frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.room_category_frame)
        self.horizontalLayout_3.setContentsMargins(8, 8, 8, 8)
        self.horizontalLayout_3.setSpacing(1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.room_category_frame)
        self.label.setMinimumSize(QtCore.QSize(0, 26))
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.verticalLayout_2.addWidget(self.room_category_frame)
        self.chat_house_users_frame_layout = QtWidgets.QVBoxLayout()
        self.chat_house_users_frame_layout.setSpacing(1)
        self.chat_house_users_frame_layout.setObjectName("chat_house_users_frame_layout")
        self.verticalLayout_2.addLayout(self.chat_house_users_frame_layout)
        spacerItem = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_4)
        self.frame_layout.addWidget(self.scrollArea)
        self.chat_house_stackedWidget = QtWidgets.QStackedWidget(self.splitter)
        self.chat_house_stackedWidget.setMinimumSize(QtCore.QSize(450, 0))
        self.chat_house_stackedWidget.setObjectName("chat_house_stackedWidget")
        self.verticalLayout.addWidget(self.splitter)

        self.retranslateUi(Form)
        self.chat_house_stackedWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Rooms"))
        self.create_room_pushButton.setText(_translate("Form", "+"))
        self.label.setText(_translate("Form", "Users"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
