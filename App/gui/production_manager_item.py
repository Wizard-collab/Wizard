# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\conta\Documents\script\wizard_devellop\App\gui\ui_files\production_manager_item.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1095, 50)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pm_asset_frame = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pm_asset_frame.sizePolicy().hasHeightForWidth())
        self.pm_asset_frame.setSizePolicy(sizePolicy)
        self.pm_asset_frame.setMinimumSize(QtCore.QSize(0, 50))
        self.pm_asset_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pm_asset_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pm_asset_frame.setObjectName("pm_asset_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.pm_asset_frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pm_asset_name_label = QtWidgets.QLabel(self.pm_asset_frame)
        self.pm_asset_name_label.setText("")
        self.pm_asset_name_label.setObjectName("pm_asset_name_label")
        self.horizontalLayout_2.addWidget(self.pm_asset_name_label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.horizontalLayout.addWidget(self.pm_asset_frame)
        self.pm_item_stages_layout = QtWidgets.QHBoxLayout()
        self.pm_item_stages_layout.setObjectName("pm_item_stages_layout")
        self.horizontalLayout.addLayout(self.pm_item_stages_layout)

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
