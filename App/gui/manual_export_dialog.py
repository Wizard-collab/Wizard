# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\conta\Documents\script\Wizard\App\gui\ui_files\manual_export_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(777, 471)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Infos_frame = QtWidgets.QWidget(Dialog)
        self.Infos_frame.setObjectName("Infos_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Infos_frame)
        self.horizontalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.manual_export_image_label = QtWidgets.QLabel(self.Infos_frame)
        self.manual_export_image_label.setMinimumSize(QtCore.QSize(50, 50))
        self.manual_export_image_label.setMaximumSize(QtCore.QSize(50, 50))
        self.manual_export_image_label.setText("")
        self.manual_export_image_label.setObjectName("manual_export_image_label")
        self.horizontalLayout_2.addWidget(self.manual_export_image_label)
        self.manual_export_asset_name_label = QtWidgets.QLabel(self.Infos_frame)
        self.manual_export_asset_name_label.setText("")
        self.manual_export_asset_name_label.setObjectName("manual_export_asset_name_label")
        self.horizontalLayout_2.addWidget(self.manual_export_asset_name_label)
        self.verticalLayout.addWidget(self.Infos_frame)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.manual_export_main_frame = QtWidgets.QFrame(Dialog)
        self.manual_export_main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.manual_export_main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.manual_export_main_frame.setObjectName("manual_export_main_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.manual_export_main_frame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame = QtWidgets.QFrame(self.manual_export_main_frame)
        self.frame.setObjectName("frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.folder_pushButton = QtWidgets.QPushButton(self.frame)
        self.folder_pushButton.setMinimumSize(QtCore.QSize(28, 28))
        self.folder_pushButton.setMaximumSize(QtCore.QSize(28, 28))
        self.folder_pushButton.setText("")
        self.folder_pushButton.setObjectName("folder_pushButton")
        self.verticalLayout_4.addWidget(self.folder_pushButton)
        self.clear_pushButton = QtWidgets.QPushButton(self.frame)
        self.clear_pushButton.setMinimumSize(QtCore.QSize(28, 28))
        self.clear_pushButton.setMaximumSize(QtCore.QSize(28, 28))
        self.clear_pushButton.setText("")
        self.clear_pushButton.setIconSize(QtCore.QSize(25, 25))
        self.clear_pushButton.setObjectName("clear_pushButton")
        self.verticalLayout_4.addWidget(self.clear_pushButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.manual_export_main_frame_2 = QtWidgets.QFrame(self.frame)
        self.manual_export_main_frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.manual_export_main_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.manual_export_main_frame_2.setObjectName("manual_export_main_frame_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.manual_export_main_frame_2)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_4.addWidget(self.manual_export_main_frame_2)
        self.verticalLayout_3.addWidget(self.frame)
        self.texture_tex_check_frame = QtWidgets.QFrame(self.manual_export_main_frame)
        self.texture_tex_check_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.texture_tex_check_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.texture_tex_check_frame.setObjectName("texture_tex_check_frame")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.texture_tex_check_frame)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label = QtWidgets.QLabel(self.texture_tex_check_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label)
        self.create_tex_comboBox = QtWidgets.QComboBox(self.texture_tex_check_frame)
        self.create_tex_comboBox.setObjectName("create_tex_comboBox")
        self.create_tex_comboBox.addItem("")
        self.create_tex_comboBox.addItem("")
        self.create_tex_comboBox.addItem("")
        self.horizontalLayout_6.addWidget(self.create_tex_comboBox)
        self.verticalLayout_3.addWidget(self.texture_tex_check_frame)
        self.frame1 = QtWidgets.QFrame(self.manual_export_main_frame)
        self.frame1.setObjectName("frame1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame1)
        self.horizontalLayout.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cancel_pushButton = QtWidgets.QPushButton(self.frame1)
        self.cancel_pushButton.setMinimumSize(QtCore.QSize(150, 50))
        self.cancel_pushButton.setMaximumSize(QtCore.QSize(150, 50))
        self.cancel_pushButton.setObjectName("cancel_pushButton")
        self.horizontalLayout.addWidget(self.cancel_pushButton)
        self.manual_export_pushButton = QtWidgets.QPushButton(self.frame1)
        self.manual_export_pushButton.setMinimumSize(QtCore.QSize(100, 50))
        self.manual_export_pushButton.setMaximumSize(QtCore.QSize(16777215, 50))
        self.manual_export_pushButton.setObjectName("manual_export_pushButton")
        self.horizontalLayout.addWidget(self.manual_export_pushButton)
        self.verticalLayout_3.addWidget(self.frame1)
        self.horizontalLayout_3.addWidget(self.manual_export_main_frame)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Create "))
        self.create_tex_comboBox.setItemText(0, _translate("Dialog", ".tex"))
        self.create_tex_comboBox.setItemText(1, _translate("Dialog", ".tx"))
        self.create_tex_comboBox.setItemText(2, _translate("Dialog", "Nothing"))
        self.cancel_pushButton.setText(_translate("Dialog", "Cancel"))
        self.manual_export_pushButton.setText(_translate("Dialog", "Commit files"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
