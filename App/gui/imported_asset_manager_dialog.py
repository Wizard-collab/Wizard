# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\conta\Documents\script\wizard_devellop\App\gui\ui_files\imported_asset_manager_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(421, 600)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.background_frame = QtWidgets.QFrame(Dialog)
        self.background_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.background_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.background_frame.setObjectName("background_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.background_frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.image_label = QtWidgets.QLabel(self.background_frame)
        self.image_label.setMinimumSize(QtCore.QSize(50, 50))
        self.image_label.setText("")
        self.image_label.setObjectName("image_label")
        self.horizontalLayout.addWidget(self.image_label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.imported_scene_label = QtWidgets.QLabel(self.background_frame)
        self.imported_scene_label.setObjectName("imported_scene_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.imported_scene_label)
        self.working_scene_label = QtWidgets.QLabel(self.background_frame)
        self.working_scene_label.setText("")
        self.working_scene_label.setObjectName("working_scene_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.working_scene_label)
        self.imported_variant_label = QtWidgets.QLabel(self.background_frame)
        self.imported_variant_label.setObjectName("imported_variant_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.imported_variant_label)
        self.variant_comboBox = QtWidgets.QComboBox(self.background_frame)
        self.variant_comboBox.setObjectName("variant_comboBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.variant_comboBox)
        self.imported_asset_label = QtWidgets.QLabel(self.background_frame)
        self.imported_asset_label.setObjectName("imported_asset_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.imported_asset_label)
        self.exported_asset_comboBox = QtWidgets.QComboBox(self.background_frame)
        self.exported_asset_comboBox.setObjectName("exported_asset_comboBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.exported_asset_comboBox)
        self.imported_version_label = QtWidgets.QLabel(self.background_frame)
        self.imported_version_label.setObjectName("imported_version_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.imported_version_label)
        self.exported_version_comboBox = QtWidgets.QComboBox(self.background_frame)
        self.exported_version_comboBox.setObjectName("exported_version_comboBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.exported_version_comboBox)
        self.imported_date_label = QtWidgets.QLabel(self.background_frame)
        self.imported_date_label.setObjectName("imported_date_label")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.imported_date_label)
        self.date_label = QtWidgets.QLabel(self.background_frame)
        self.date_label.setText("")
        self.date_label.setObjectName("date_label")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.date_label)
        self.imported_user_name_label = QtWidgets.QLabel(self.background_frame)
        self.imported_user_name_label.setObjectName("imported_user_name_label")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.imported_user_name_label)
        self.user_name_label = QtWidgets.QLabel(self.background_frame)
        self.user_name_label.setText("")
        self.user_name_label.setObjectName("user_name_label")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.user_name_label)
        self.imported_comment_label = QtWidgets.QLabel(self.background_frame)
        self.imported_comment_label.setObjectName("imported_comment_label")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.imported_comment_label)
        self.comment_label = QtWidgets.QLabel(self.background_frame)
        self.comment_label.setText("")
        self.comment_label.setObjectName("comment_label")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.comment_label)
        self.file_name_label = QtWidgets.QLabel(self.background_frame)
        self.file_name_label.setObjectName("file_name_label")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.file_name_label)
        self.file_label = QtWidgets.QLabel(self.background_frame)
        self.file_label.setText("")
        self.file_label.setObjectName("file_label")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.file_label)
        self.imported_namespace_label = QtWidgets.QLabel(self.background_frame)
        self.imported_namespace_label.setObjectName("imported_namespace_label")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.imported_namespace_label)
        self.namespace_label = QtWidgets.QLabel(self.background_frame)
        self.namespace_label.setText("")
        self.namespace_label.setObjectName("namespace_label")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.namespace_label)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.line = QtWidgets.QFrame(self.background_frame)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.label = QtWidgets.QLabel(self.background_frame)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.imported_asset_m_wsd_frame = QtWidgets.QFrame(self.background_frame)
        self.imported_asset_m_wsd_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.imported_asset_m_wsd_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.imported_asset_m_wsd_frame.setObjectName("imported_asset_m_wsd_frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.imported_asset_m_wsd_frame)
        self.verticalLayout_4.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_4.setSpacing(1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.imported_asset_m_wsd_frame)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.wsd_proxy_file_lineEdit = QtWidgets.QLineEdit(self.imported_asset_m_wsd_frame)
        self.wsd_proxy_file_lineEdit.setReadOnly(True)
        self.wsd_proxy_file_lineEdit.setObjectName("wsd_proxy_file_lineEdit")
        self.horizontalLayout_5.addWidget(self.wsd_proxy_file_lineEdit)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.imported_asset_m_wsd_frame)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.wsd_file_size_lineEdit = QtWidgets.QLineEdit(self.imported_asset_m_wsd_frame)
        self.wsd_file_size_lineEdit.setMinimumSize(QtCore.QSize(150, 0))
        self.wsd_file_size_lineEdit.setMaximumSize(QtCore.QSize(150, 16777215))
        self.wsd_file_size_lineEdit.setObjectName("wsd_file_size_lineEdit")
        self.horizontalLayout_6.addWidget(self.wsd_file_size_lineEdit)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_6 = QtWidgets.QLabel(self.imported_asset_m_wsd_frame)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.wsd_proxy_size_lineEdit = QtWidgets.QLineEdit(self.imported_asset_m_wsd_frame)
        self.wsd_proxy_size_lineEdit.setMinimumSize(QtCore.QSize(150, 0))
        self.wsd_proxy_size_lineEdit.setMaximumSize(QtCore.QSize(150, 16777215))
        self.wsd_proxy_size_lineEdit.setObjectName("wsd_proxy_size_lineEdit")
        self.horizontalLayout_7.addWidget(self.wsd_proxy_size_lineEdit)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.imported_asset_m_wsd_frame)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.wsd_proxy_pushButton = QtWidgets.QPushButton(self.imported_asset_m_wsd_frame)
        self.wsd_proxy_pushButton.setMinimumSize(QtCore.QSize(60, 40))
        self.wsd_proxy_pushButton.setMaximumSize(QtCore.QSize(60, 40))
        self.wsd_proxy_pushButton.setCheckable(True)
        self.wsd_proxy_pushButton.setChecked(True)
        self.wsd_proxy_pushButton.setObjectName("wsd_proxy_pushButton")
        self.horizontalLayout_3.addWidget(self.wsd_proxy_pushButton)
        self.wsd_asset_pushButton = QtWidgets.QPushButton(self.imported_asset_m_wsd_frame)
        self.wsd_asset_pushButton.setMinimumSize(QtCore.QSize(60, 40))
        self.wsd_asset_pushButton.setMaximumSize(QtCore.QSize(60, 40))
        self.wsd_asset_pushButton.setCheckable(True)
        self.wsd_asset_pushButton.setObjectName("wsd_asset_pushButton")
        self.horizontalLayout_3.addWidget(self.wsd_asset_pushButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.imported_asset_m_wsd_frame)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.wsd_visible_pushButton = QtWidgets.QPushButton(self.imported_asset_m_wsd_frame)
        self.wsd_visible_pushButton.setMinimumSize(QtCore.QSize(90, 40))
        self.wsd_visible_pushButton.setMaximumSize(QtCore.QSize(90, 40))
        self.wsd_visible_pushButton.setCheckable(True)
        self.wsd_visible_pushButton.setChecked(True)
        self.wsd_visible_pushButton.setObjectName("wsd_visible_pushButton")
        self.horizontalLayout_4.addWidget(self.wsd_visible_pushButton)
        self.wsd_hidden_pushButton = QtWidgets.QPushButton(self.imported_asset_m_wsd_frame)
        self.wsd_hidden_pushButton.setMinimumSize(QtCore.QSize(90, 40))
        self.wsd_hidden_pushButton.setMaximumSize(QtCore.QSize(90, 40))
        self.wsd_hidden_pushButton.setCheckable(True)
        self.wsd_hidden_pushButton.setObjectName("wsd_hidden_pushButton")
        self.horizontalLayout_4.addWidget(self.wsd_hidden_pushButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.addWidget(self.imported_asset_m_wsd_frame)
        self.line_2 = QtWidgets.QFrame(self.background_frame)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.imported_asset_update_pushButton = QtWidgets.QPushButton(self.background_frame)
        self.imported_asset_update_pushButton.setObjectName("imported_asset_update_pushButton")
        self.horizontalLayout_2.addWidget(self.imported_asset_update_pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addWidget(self.background_frame)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.imported_scene_label.setText(_translate("Dialog", "Asset"))
        self.imported_variant_label.setText(_translate("Dialog", "Variant"))
        self.imported_asset_label.setText(_translate("Dialog", "Exported asset"))
        self.imported_version_label.setText(_translate("Dialog", "Export version"))
        self.imported_date_label.setText(_translate("Dialog", "Date"))
        self.imported_user_name_label.setText(_translate("Dialog", "User"))
        self.imported_comment_label.setText(_translate("Dialog", "Comment"))
        self.file_name_label.setText(_translate("Dialog", "File name"))
        self.imported_namespace_label.setText(_translate("Dialog", "Namespace"))
        self.label.setText(_translate("Dialog", "WSD"))
        self.label_4.setText(_translate("Dialog", "Proxy file :"))
        self.label_5.setText(_translate("Dialog", "File size"))
        self.label_6.setText(_translate("Dialog", "Proxy size"))
        self.label_2.setText(_translate("Dialog", "Level"))
        self.wsd_proxy_pushButton.setText(_translate("Dialog", "Proxy"))
        self.wsd_asset_pushButton.setText(_translate("Dialog", "Asset"))
        self.label_3.setText(_translate("Dialog", "Visibility"))
        self.wsd_visible_pushButton.setText(_translate("Dialog", "Visible"))
        self.wsd_hidden_pushButton.setText(_translate("Dialog", "Hidden"))
        self.imported_asset_update_pushButton.setText(_translate("Dialog", "Update"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
