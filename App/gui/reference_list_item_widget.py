# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\conta\Documents\script\Wizard\App\work\ui_files\reference_list_item_widget.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1005, 34)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.reference_list_item_frame = QtWidgets.QFrame(Form)
        self.reference_list_item_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.reference_list_item_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.reference_list_item_frame.setObjectName("reference_list_item_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.reference_list_item_frame)
        self.horizontalLayout.setContentsMargins(4, 4, 4, 4)
        self.horizontalLayout.setSpacing(7)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.asset_stage_image_label = QtWidgets.QLabel(self.reference_list_item_frame)
        self.asset_stage_image_label.setMinimumSize(QtCore.QSize(22, 22))
        self.asset_stage_image_label.setMaximumSize(QtCore.QSize(22, 22))
        self.asset_stage_image_label.setText("")
        self.asset_stage_image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.asset_stage_image_label.setObjectName("asset_stage_image_label")
        self.horizontalLayout.addWidget(self.asset_stage_image_label)
        self.reference_list_item_asset_name_label = QtWidgets.QLabel(self.reference_list_item_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reference_list_item_asset_name_label.sizePolicy().hasHeightForWidth())
        self.reference_list_item_asset_name_label.setSizePolicy(sizePolicy)
        self.reference_list_item_asset_name_label.setMinimumSize(QtCore.QSize(180, 0))
        self.reference_list_item_asset_name_label.setMaximumSize(QtCore.QSize(180, 16777215))
        self.reference_list_item_asset_name_label.setObjectName("reference_list_item_asset_name_label")
        self.horizontalLayout.addWidget(self.reference_list_item_asset_name_label)
        self.line = QtWidgets.QFrame(self.reference_list_item_frame)
        self.line.setMaximumSize(QtCore.QSize(1, 16777215))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.reference_list_item_asset_variant_label = QtWidgets.QLabel(self.reference_list_item_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reference_list_item_asset_variant_label.sizePolicy().hasHeightForWidth())
        self.reference_list_item_asset_variant_label.setSizePolicy(sizePolicy)
        self.reference_list_item_asset_variant_label.setMinimumSize(QtCore.QSize(180, 0))
        self.reference_list_item_asset_variant_label.setMaximumSize(QtCore.QSize(180, 16777215))
        self.reference_list_item_asset_variant_label.setObjectName("reference_list_item_asset_variant_label")
        self.horizontalLayout.addWidget(self.reference_list_item_asset_variant_label)
        self.line_2 = QtWidgets.QFrame(self.reference_list_item_frame)
        self.line_2.setMaximumSize(QtCore.QSize(1, 16777215))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout.addWidget(self.line_2)
        self.reference_list_item_asset_namespace_label = QtWidgets.QLabel(self.reference_list_item_frame)
        self.reference_list_item_asset_namespace_label.setMinimumSize(QtCore.QSize(180, 0))
        self.reference_list_item_asset_namespace_label.setMaximumSize(QtCore.QSize(180, 16777215))
        self.reference_list_item_asset_namespace_label.setObjectName("reference_list_item_asset_namespace_label")
        self.horizontalLayout.addWidget(self.reference_list_item_asset_namespace_label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.ticket_reference_list_item_pushButton = QtWidgets.QPushButton(self.reference_list_item_frame)
        self.ticket_reference_list_item_pushButton.setMinimumSize(QtCore.QSize(24, 24))
        self.ticket_reference_list_item_pushButton.setMaximumSize(QtCore.QSize(24, 24))
        self.ticket_reference_list_item_pushButton.setText("")
        self.ticket_reference_list_item_pushButton.setObjectName("ticket_reference_list_item_pushButton")
        self.horizontalLayout.addWidget(self.ticket_reference_list_item_pushButton)
        self.folder_reference_list_item_pushButton = QtWidgets.QPushButton(self.reference_list_item_frame)
        self.folder_reference_list_item_pushButton.setMinimumSize(QtCore.QSize(24, 24))
        self.folder_reference_list_item_pushButton.setMaximumSize(QtCore.QSize(24, 24))
        self.folder_reference_list_item_pushButton.setText("")
        self.folder_reference_list_item_pushButton.setIconSize(QtCore.QSize(17, 17))
        self.folder_reference_list_item_pushButton.setObjectName("folder_reference_list_item_pushButton")
        self.horizontalLayout.addWidget(self.folder_reference_list_item_pushButton)
        self.parameters_reference_list_item_pushButton = QtWidgets.QPushButton(self.reference_list_item_frame)
        self.parameters_reference_list_item_pushButton.setMinimumSize(QtCore.QSize(24, 24))
        self.parameters_reference_list_item_pushButton.setMaximumSize(QtCore.QSize(24, 24))
        self.parameters_reference_list_item_pushButton.setText("")
        self.parameters_reference_list_item_pushButton.setIconSize(QtCore.QSize(18, 18))
        self.parameters_reference_list_item_pushButton.setObjectName("parameters_reference_list_item_pushButton")
        self.horizontalLayout.addWidget(self.parameters_reference_list_item_pushButton)
        self.refresh_reference_widget_item = QtWidgets.QPushButton(self.reference_list_item_frame)
        self.refresh_reference_widget_item.setMinimumSize(QtCore.QSize(24, 24))
        self.refresh_reference_widget_item.setMaximumSize(QtCore.QSize(24, 24))
        self.refresh_reference_widget_item.setText("")
        self.refresh_reference_widget_item.setObjectName("refresh_reference_widget_item")
        self.horizontalLayout.addWidget(self.refresh_reference_widget_item)
        self.remove_reference_widget_item = QtWidgets.QPushButton(self.reference_list_item_frame)
        self.remove_reference_widget_item.setMinimumSize(QtCore.QSize(24, 24))
        self.remove_reference_widget_item.setMaximumSize(QtCore.QSize(24, 24))
        self.remove_reference_widget_item.setText("")
        self.remove_reference_widget_item.setObjectName("remove_reference_widget_item")
        self.horizontalLayout.addWidget(self.remove_reference_widget_item)
        self.verticalLayout.addWidget(self.reference_list_item_frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.reference_list_item_asset_name_label.setText(_translate("Form", "asset_name"))
        self.reference_list_item_asset_variant_label.setText(_translate("Form", "asset_variant"))
        self.reference_list_item_asset_namespace_label.setText(_translate("Form", "namespace"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
