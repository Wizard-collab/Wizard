# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\conta\Documents\script\wizard\App\gui\ui_files\running_widget.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(350, 350)
        Form.setMinimumSize(QtCore.QSize(350, 350))
        Form.setMaximumSize(QtCore.QSize(350, 350))
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.running_main_frame = QtWidgets.QFrame(Form)
        self.running_main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.running_main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.running_main_frame.setObjectName("running_main_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.running_main_frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.running_asset_number_label = QtWidgets.QLabel(self.running_main_frame)
        self.running_asset_number_label.setText("")
        self.running_asset_number_label.setObjectName("running_asset_number_label")
        self.horizontalLayout.addWidget(self.running_asset_number_label)
        self.running_close_pushButton = QtWidgets.QPushButton(self.running_main_frame)
        self.running_close_pushButton.setMinimumSize(QtCore.QSize(26, 26))
        self.running_close_pushButton.setMaximumSize(QtCore.QSize(26, 26))
        self.running_close_pushButton.setText("")
        self.running_close_pushButton.setIconSize(QtCore.QSize(14, 14))
        self.running_close_pushButton.setObjectName("running_close_pushButton")
        self.horizontalLayout.addWidget(self.running_close_pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.running_scrollArea = QtWidgets.QScrollArea(self.running_main_frame)
        self.running_scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.running_scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.running_scrollArea.setWidgetResizable(True)
        self.running_scrollArea.setObjectName("running_scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 302, 267))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.running_items_layout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.running_items_layout.setContentsMargins(3, 3, 3, 3)
        self.running_items_layout.setSpacing(2)
        self.running_items_layout.setObjectName("running_items_layout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.running_items_layout.addItem(spacerItem)
        self.running_scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.running_scrollArea)
        self.verticalLayout.addWidget(self.running_main_frame)

        self.retranslateUi(Form)
        self.running_close_pushButton.clicked.connect(Form.close)
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
