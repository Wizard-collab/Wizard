# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\conta\Documents\script\wizard_devellop\App\gui\ui_files\popup_widget.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(356, 130)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.popup_background_frame = QtWidgets.QFrame(Form)
        self.popup_background_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.popup_background_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.popup_background_frame.setObjectName("popup_background_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.popup_background_frame)
        self.horizontalLayout_2.setContentsMargins(11, 8, 8, 8)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.popup_image_frame = QtWidgets.QFrame(self.popup_background_frame)
        self.popup_image_frame.setMinimumSize(QtCore.QSize(90, 90))
        self.popup_image_frame.setMaximumSize(QtCore.QSize(90, 90))
        self.popup_image_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.popup_image_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.popup_image_frame.setObjectName("popup_image_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.popup_image_frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.popup_image_label = QtWidgets.QLabel(self.popup_image_frame)
        self.popup_image_label.setText("")
        self.popup_image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.popup_image_label.setObjectName("popup_image_label")
        self.verticalLayout_2.addWidget(self.popup_image_label)
        self.horizontalLayout_2.addWidget(self.popup_image_frame)
        self.popup_data_frame = QtWidgets.QFrame(self.popup_background_frame)
        self.popup_data_frame.setObjectName("popup_data_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.popup_data_frame)
        self.verticalLayout.setContentsMargins(3, 0, 0, 0)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.popup_wizard_label = QtWidgets.QLabel(self.popup_data_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.popup_wizard_label.sizePolicy().hasHeightForWidth())
        self.popup_wizard_label.setSizePolicy(sizePolicy)
        self.popup_wizard_label.setObjectName("popup_wizard_label")
        self.verticalLayout.addWidget(self.popup_wizard_label)
        self.popup_message_label = QtWidgets.QLabel(self.popup_data_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.popup_message_label.sizePolicy().hasHeightForWidth())
        self.popup_message_label.setSizePolicy(sizePolicy)
        self.popup_message_label.setMinimumSize(QtCore.QSize(190, 0))
        self.popup_message_label.setWordWrap(True)
        self.popup_message_label.setOpenExternalLinks(False)
        self.popup_message_label.setObjectName("popup_message_label")
        self.verticalLayout.addWidget(self.popup_message_label)
        spacerItem1 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_2.addWidget(self.popup_data_frame)
        spacerItem2 = QtWidgets.QSpacerItem(11, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.popup_close_pushButton = QtWidgets.QPushButton(self.popup_background_frame)
        self.popup_close_pushButton.setMinimumSize(QtCore.QSize(28, 28))
        self.popup_close_pushButton.setMaximumSize(QtCore.QSize(28, 28))
        self.popup_close_pushButton.setText("")
        self.popup_close_pushButton.setObjectName("popup_close_pushButton")
        self.verticalLayout_3.addWidget(self.popup_close_pushButton)
        spacerItem3 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.horizontalLayout.addWidget(self.popup_background_frame)

        self.retranslateUi(Form)
        self.popup_close_pushButton.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.popup_wizard_label.setText(_translate("Form", "Wizard"))
        self.popup_message_label.setText(_translate("Form", "Text"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
