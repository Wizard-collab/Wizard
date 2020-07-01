# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\conta\Documents\script\wizard_devellop\App\gui\ui_files\update_widget.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(708, 188)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.update_widget_frame = QtWidgets.QFrame(Form)
        self.update_widget_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.update_widget_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.update_widget_frame.setObjectName("update_widget_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.update_widget_frame)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.update_title_frame = QtWidgets.QFrame(self.update_widget_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.update_title_frame.sizePolicy().hasHeightForWidth())
        self.update_title_frame.setSizePolicy(sizePolicy)
        self.update_title_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.update_title_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.update_title_frame.setObjectName("update_title_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.update_title_frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.update_icon_label = QtWidgets.QLabel(self.update_title_frame)
        self.update_icon_label.setMinimumSize(QtCore.QSize(24, 24))
        self.update_icon_label.setMaximumSize(QtCore.QSize(24, 24))
        self.update_icon_label.setText("")
        self.update_icon_label.setObjectName("update_icon_label")
        self.horizontalLayout_2.addWidget(self.update_icon_label)
        self.update_title_label = QtWidgets.QLabel(self.update_title_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.update_title_label.sizePolicy().hasHeightForWidth())
        self.update_title_label.setSizePolicy(sizePolicy)
        self.update_title_label.setStyleSheet("font: 87 9pt \"Segoe UI Black\";")
        self.update_title_label.setObjectName("update_title_label")
        self.horizontalLayout_2.addWidget(self.update_title_label)
        self.verticalLayout_2.addWidget(self.update_title_frame)
        self.update_text_label = QtWidgets.QLabel(self.update_widget_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.update_text_label.sizePolicy().hasHeightForWidth())
        self.update_text_label.setSizePolicy(sizePolicy)
        self.update_text_label.setWordWrap(True)
        self.update_text_label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.update_text_label.setObjectName("update_text_label")
        self.verticalLayout_2.addWidget(self.update_text_label)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.update_image_label = QtWidgets.QLabel(self.update_widget_frame)
        self.update_image_label.setObjectName("update_image_label")
        self.horizontalLayout_3.addWidget(self.update_image_label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addWidget(self.update_widget_frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.update_title_label.setText(_translate("Form", "UPDATE TITLE"))
        self.update_text_label.setText(_translate("Form", "update text update text update text update text update text update textupdate textupdate textupdate textupdate textupdate text update text"))
        self.update_image_label.setText(_translate("Form", "image"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
