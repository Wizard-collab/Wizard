# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\conta\Documents\script\wizard_devellop\App\gui\ui_files\ref_list_asset_widget.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1001, 26)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ref_list_asset_frame = QtWidgets.QFrame(Form)
        self.ref_list_asset_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ref_list_asset_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ref_list_asset_frame.setObjectName("ref_list_asset_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.ref_list_asset_frame)
        self.horizontalLayout.setContentsMargins(10, 2, 10, 2)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ref_list_asset_image_label = QtWidgets.QLabel(self.ref_list_asset_frame)
        self.ref_list_asset_image_label.setMinimumSize(QtCore.QSize(16, 16))
        self.ref_list_asset_image_label.setMaximumSize(QtCore.QSize(16, 16))
        self.ref_list_asset_image_label.setText("")
        self.ref_list_asset_image_label.setObjectName("ref_list_asset_image_label")
        self.horizontalLayout.addWidget(self.ref_list_asset_image_label)
        self.ref_list_asset_name_label = QtWidgets.QLabel(self.ref_list_asset_frame)
        self.ref_list_asset_name_label.setMinimumSize(QtCore.QSize(160, 0))
        self.ref_list_asset_name_label.setMaximumSize(QtCore.QSize(160, 16777215))
        self.ref_list_asset_name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.ref_list_asset_name_label.setObjectName("ref_list_asset_name_label")
        self.horizontalLayout.addWidget(self.ref_list_asset_name_label)
        self.ref_list_asset_variant_label = QtWidgets.QLabel(self.ref_list_asset_frame)
        self.ref_list_asset_variant_label.setMinimumSize(QtCore.QSize(160, 0))
        self.ref_list_asset_variant_label.setMaximumSize(QtCore.QSize(160, 16777215))
        self.ref_list_asset_variant_label.setAlignment(QtCore.Qt.AlignCenter)
        self.ref_list_asset_variant_label.setObjectName("ref_list_asset_variant_label")
        self.horizontalLayout.addWidget(self.ref_list_asset_variant_label)
        self.ref_list_asset_version_label = QtWidgets.QLabel(self.ref_list_asset_frame)
        self.ref_list_asset_version_label.setMinimumSize(QtCore.QSize(160, 0))
        self.ref_list_asset_version_label.setMaximumSize(QtCore.QSize(160, 16777215))
        self.ref_list_asset_version_label.setAlignment(QtCore.Qt.AlignCenter)
        self.ref_list_asset_version_label.setObjectName("ref_list_asset_version_label")
        self.horizontalLayout.addWidget(self.ref_list_asset_version_label)
        self.ref_list_asset_count_label = QtWidgets.QLabel(self.ref_list_asset_frame)
        self.ref_list_asset_count_label.setMinimumSize(QtCore.QSize(160, 0))
        self.ref_list_asset_count_label.setMaximumSize(QtCore.QSize(160, 16777215))
        self.ref_list_asset_count_label.setAlignment(QtCore.Qt.AlignCenter)
        self.ref_list_asset_count_label.setObjectName("ref_list_asset_count_label")
        self.horizontalLayout.addWidget(self.ref_list_asset_count_label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addWidget(self.ref_list_asset_frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.ref_list_asset_name_label.setText(_translate("Form", "Asset_name"))
        self.ref_list_asset_variant_label.setText(_translate("Form", "Asset_variant"))
        self.ref_list_asset_version_label.setText(_translate("Form", "Export_version"))
        self.ref_list_asset_count_label.setText(_translate("Form", "Count"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
