# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\conta\Documents\script\Wizard\App\work\ui_files\node_widget.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(116, 116)
        Form.setMinimumSize(QtCore.QSize(116, 0))
        Form.setMaximumSize(QtCore.QSize(116, 100000))
        Form.setStyleSheet("")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.node_widget_button_frame = QtWidgets.QFrame(Form)
        self.node_widget_button_frame.setMinimumSize(QtCore.QSize(116, 116))
        self.node_widget_button_frame.setMaximumSize(QtCore.QSize(116, 116))
        self.node_widget_button_frame.setStyleSheet("")
        self.node_widget_button_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.node_widget_button_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.node_widget_button_frame.setObjectName("node_widget_button_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.node_widget_button_frame)
        self.verticalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.image_label = QtWidgets.QLabel(self.node_widget_button_frame)
        self.image_label.setMinimumSize(QtCore.QSize(40, 40))
        self.image_label.setMaximumSize(QtCore.QSize(40, 40))
        self.image_label.setText("")
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.image_label.setObjectName("image_label")
        self.horizontalLayout.addWidget(self.image_label)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.asset_name_label = QtWidgets.QLabel(self.node_widget_button_frame)
        self.asset_name_label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.asset_name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.asset_name_label.setObjectName("asset_name_label")
        self.verticalLayout_3.addWidget(self.asset_name_label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.asset_variant_label = QtWidgets.QLabel(self.node_widget_button_frame)
        self.asset_variant_label.setAlignment(QtCore.Qt.AlignCenter)
        self.asset_variant_label.setObjectName("asset_variant_label")
        self.horizontalLayout_2.addWidget(self.asset_variant_label)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.node_widget_button_frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.asset_name_label.setText(_translate("Form", "AssetName"))
        self.asset_variant_label.setText(_translate("Form", "Asset Variant"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
