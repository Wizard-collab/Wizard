# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\conta\Documents\script\Wizard\App\ui_files\export_manager.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(576, 501)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(0, 46))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 46))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.horizontalLayout_2.addWidget(self.frame)
        self.frame_3 = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 46))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 46))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.export_ma_stage_lineEdit = QtWidgets.QLineEdit(self.frame_3)
        self.export_ma_stage_lineEdit.setReadOnly(True)
        self.export_ma_stage_lineEdit.setObjectName("export_ma_stage_lineEdit")
        self.horizontalLayout_3.addWidget(self.export_ma_stage_lineEdit)
        self.horizontalLayout_2.addWidget(self.frame_3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.frame_5 = QtWidgets.QFrame(Form)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.frame_5)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.export_ma_sequence_lineEdit = QtWidgets.QLineEdit(self.frame_5)
        self.export_ma_sequence_lineEdit.setReadOnly(True)
        self.export_ma_sequence_lineEdit.setObjectName("export_ma_sequence_lineEdit")
        self.horizontalLayout_6.addWidget(self.export_ma_sequence_lineEdit)
        self.verticalLayout.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(Form)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_4 = QtWidgets.QLabel(self.frame_6)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_7.addWidget(self.label_4)
        self.export_m_preroll_lineEdit = QtWidgets.QLineEdit(self.frame_6)
        self.export_m_preroll_lineEdit.setMaximumSize(QtCore.QSize(50, 16777215))
        self.export_m_preroll_lineEdit.setReadOnly(True)
        self.export_m_preroll_lineEdit.setObjectName("export_m_preroll_lineEdit")
        self.horizontalLayout_7.addWidget(self.export_m_preroll_lineEdit)
        self.export_ma_in_frange_lineEdit = QtWidgets.QLineEdit(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.export_ma_in_frange_lineEdit.sizePolicy().hasHeightForWidth())
        self.export_ma_in_frange_lineEdit.setSizePolicy(sizePolicy)
        self.export_ma_in_frange_lineEdit.setMaximumSize(QtCore.QSize(90, 16777215))
        self.export_ma_in_frange_lineEdit.setReadOnly(False)
        self.export_ma_in_frange_lineEdit.setObjectName("export_ma_in_frange_lineEdit")
        self.horizontalLayout_7.addWidget(self.export_ma_in_frange_lineEdit)
        self.export_ma_out_frange_lineEdit = QtWidgets.QLineEdit(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.export_ma_out_frange_lineEdit.sizePolicy().hasHeightForWidth())
        self.export_ma_out_frange_lineEdit.setSizePolicy(sizePolicy)
        self.export_ma_out_frange_lineEdit.setMaximumSize(QtCore.QSize(90, 16777215))
        self.export_ma_out_frange_lineEdit.setObjectName("export_ma_out_frange_lineEdit")
        self.horizontalLayout_7.addWidget(self.export_ma_out_frange_lineEdit)
        self.export_m_postroll_lineEdit = QtWidgets.QLineEdit(self.frame_6)
        self.export_m_postroll_lineEdit.setMaximumSize(QtCore.QSize(50, 16777215))
        self.export_m_postroll_lineEdit.setReadOnly(True)
        self.export_m_postroll_lineEdit.setObjectName("export_m_postroll_lineEdit")
        self.horizontalLayout_7.addWidget(self.export_m_postroll_lineEdit)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.verticalLayout.addWidget(self.frame_6)
        self.assets_list_frame = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.assets_list_frame.sizePolicy().hasHeightForWidth())
        self.assets_list_frame.setSizePolicy(sizePolicy)
        self.assets_list_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.assets_list_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.assets_list_frame.setObjectName("assets_list_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.assets_list_frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.assets_list_frame)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.export_ma_assets_listWidget = QtWidgets.QListWidget(self.assets_list_frame)
        self.export_ma_assets_listWidget.setSelectionMode(QtWidgets.QAbstractItemView.ContiguousSelection)
        self.export_ma_assets_listWidget.setIconSize(QtCore.QSize(12, 12))
        self.export_ma_assets_listWidget.setViewMode(QtWidgets.QListView.ListMode)
        self.export_ma_assets_listWidget.setObjectName("export_ma_assets_listWidget")
        self.verticalLayout_2.addWidget(self.export_ma_assets_listWidget)
        self.verticalLayout.addWidget(self.assets_list_frame)
        self.export_options_frame = QtWidgets.QFrame(Form)
        self.export_options_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.export_options_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.export_options_frame.setObjectName("export_options_frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.export_options_frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.export_auto_hair_checkBox = QtWidgets.QCheckBox(self.export_options_frame)
        self.export_auto_hair_checkBox.setObjectName("export_auto_hair_checkBox")
        self.horizontalLayout_4.addWidget(self.export_auto_hair_checkBox)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addWidget(self.export_options_frame)
        self.playblast_options_frame = QtWidgets.QFrame(Form)
        self.playblast_options_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.playblast_options_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.playblast_options_frame.setObjectName("playblast_options_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.playblast_options_frame)
        self.verticalLayout_3.setSpacing(12)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSpacing(10)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.playblast_show_checkBox = QtWidgets.QCheckBox(self.playblast_options_frame)
        self.playblast_show_checkBox.setObjectName("playblast_show_checkBox")
        self.horizontalLayout_8.addWidget(self.playblast_show_checkBox)
        self.line_2 = QtWidgets.QFrame(self.playblast_options_frame)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_8.addWidget(self.line_2)
        self.playblast_ornaments_checkBox = QtWidgets.QCheckBox(self.playblast_options_frame)
        self.playblast_ornaments_checkBox.setChecked(True)
        self.playblast_ornaments_checkBox.setObjectName("playblast_ornaments_checkBox")
        self.horizontalLayout_8.addWidget(self.playblast_ornaments_checkBox)
        self.line = QtWidgets.QFrame(self.playblast_options_frame)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_8.addWidget(self.line)
        self.playblast_only_geo_checkBox = QtWidgets.QCheckBox(self.playblast_options_frame)
        self.playblast_only_geo_checkBox.setEnabled(False)
        self.playblast_only_geo_checkBox.setChecked(True)
        self.playblast_only_geo_checkBox.setObjectName("playblast_only_geo_checkBox")
        self.horizontalLayout_8.addWidget(self.playblast_only_geo_checkBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.verticalLayout.addWidget(self.playblast_options_frame)
        self.frame_4 = QtWidgets.QFrame(Form)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.export_m_refresh_assets_checkBox = QtWidgets.QCheckBox(self.frame_4)
        self.export_m_refresh_assets_checkBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.export_m_refresh_assets_checkBox.setChecked(True)
        self.export_m_refresh_assets_checkBox.setObjectName("export_m_refresh_assets_checkBox")
        self.horizontalLayout_5.addWidget(self.export_m_refresh_assets_checkBox)
        self.line_3 = QtWidgets.QFrame(self.frame_4)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_5.addWidget(self.line_3)
        self.preroll_postroll_checkBox = QtWidgets.QCheckBox(self.frame_4)
        self.preroll_postroll_checkBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.preroll_postroll_checkBox.setChecked(True)
        self.preroll_postroll_checkBox.setObjectName("preroll_postroll_checkBox")
        self.horizontalLayout_5.addWidget(self.preroll_postroll_checkBox)
        self.export_ma_export_pushButton = QtWidgets.QPushButton(self.frame_4)
        self.export_ma_export_pushButton.setMinimumSize(QtCore.QSize(100, 40))
        self.export_ma_export_pushButton.setMaximumSize(QtCore.QSize(100, 40))
        self.export_ma_export_pushButton.setObjectName("export_ma_export_pushButton")
        self.horizontalLayout_5.addWidget(self.export_ma_export_pushButton)
        self.verticalLayout.addWidget(self.frame_4)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Export manager"))
        self.label_2.setText(_translate("Form", "Stage :"))
        self.label_3.setText(_translate("Form", "Shot :"))
        self.label_4.setText(_translate("Form", "Frame range :"))
        self.label_6.setText(_translate("Form", "Assets list :"))
        self.export_auto_hair_checkBox.setText(_translate("Form", "Auto hair"))
        self.playblast_show_checkBox.setText(_translate("Form", "Show playblast after creation"))
        self.playblast_ornaments_checkBox.setText(_translate("Form", "Ornaments"))
        self.playblast_only_geo_checkBox.setText(_translate("Form", "Show only geo"))
        self.export_m_refresh_assets_checkBox.setText(_translate("Form", "Refresh assets in scene"))
        self.preroll_postroll_checkBox.setText(_translate("Form", "Preroll / Postroll"))
        self.export_ma_export_pushButton.setText(_translate("Form", "Export"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
