# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\conta\Documents\script\Wizard\App\ui_files\project_workflow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(512, 605)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.frame)
        self.tabWidget.setObjectName("tabWidget")
        self.assets_tab = QtWidgets.QWidget()
        self.assets_tab.setObjectName("assets_tab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.assets_tab)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_3 = QtWidgets.QFrame(self.assets_tab)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.p_w_rigging_label = QtWidgets.QLabel(self.frame_3)
        self.p_w_rigging_label.setMinimumSize(QtCore.QSize(28, 28))
        self.p_w_rigging_label.setMaximumSize(QtCore.QSize(28, 28))
        self.p_w_rigging_label.setText("")
        self.p_w_rigging_label.setObjectName("p_w_rigging_label")
        self.gridLayout.addWidget(self.p_w_rigging_label, 1, 0, 1, 1)
        self.p_w_modeling_label = QtWidgets.QLabel(self.frame_3)
        self.p_w_modeling_label.setMinimumSize(QtCore.QSize(28, 28))
        self.p_w_modeling_label.setMaximumSize(QtCore.QSize(28, 28))
        self.p_w_modeling_label.setText("")
        self.p_w_modeling_label.setObjectName("p_w_modeling_label")
        self.gridLayout.addWidget(self.p_w_modeling_label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 1, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.frame_3)
        self.comboBox_3.setObjectName("comboBox_3")
        self.gridLayout.addWidget(self.comboBox_3, 2, 2, 1, 1)
        self.comboBox_4 = QtWidgets.QComboBox(self.frame_3)
        self.comboBox_4.setObjectName("comboBox_4")
        self.gridLayout.addWidget(self.comboBox_4, 3, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.frame_3)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 4, 1, 1, 1)
        self.comboBox_5 = QtWidgets.QComboBox(self.frame_3)
        self.comboBox_5.setObjectName("comboBox_5")
        self.gridLayout.addWidget(self.comboBox_5, 4, 2, 1, 1)
        self.p_w_grooming_label = QtWidgets.QLabel(self.frame_3)
        self.p_w_grooming_label.setMinimumSize(QtCore.QSize(28, 28))
        self.p_w_grooming_label.setMaximumSize(QtCore.QSize(28, 28))
        self.p_w_grooming_label.setText("")
        self.p_w_grooming_label.setObjectName("p_w_grooming_label")
        self.gridLayout.addWidget(self.p_w_grooming_label, 2, 0, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.frame_3)
        self.comboBox_2.setObjectName("comboBox_2")
        self.gridLayout.addWidget(self.comboBox_2, 1, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 1, 1, 1)
        self.p_w_shading_label = QtWidgets.QLabel(self.frame_3)
        self.p_w_shading_label.setMinimumSize(QtCore.QSize(28, 28))
        self.p_w_shading_label.setMaximumSize(QtCore.QSize(28, 28))
        self.p_w_shading_label.setText("")
        self.p_w_shading_label.setObjectName("p_w_shading_label")
        self.gridLayout.addWidget(self.p_w_shading_label, 4, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.frame_3)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.p_w_texturing_label = QtWidgets.QLabel(self.frame_3)
        self.p_w_texturing_label.setMinimumSize(QtCore.QSize(28, 28))
        self.p_w_texturing_label.setMaximumSize(QtCore.QSize(28, 28))
        self.p_w_texturing_label.setText("")
        self.p_w_texturing_label.setObjectName("p_w_texturing_label")
        self.gridLayout.addWidget(self.p_w_texturing_label, 3, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 5, 1, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout)
        self.verticalLayout_3.addWidget(self.frame_3)
        self.tabWidget.addTab(self.assets_tab, "")
        self.libraries_tab = QtWidgets.QWidget()
        self.libraries_tab.setObjectName("libraries_tab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.libraries_tab)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_4 = QtWidgets.QFrame(self.libraries_tab)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_19 = QtWidgets.QLabel(self.frame_4)
        self.label_19.setObjectName("label_19")
        self.gridLayout_2.addWidget(self.label_19, 13, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.frame_4)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 2, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.frame_4)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 6, 1, 1, 1)
        self.p_w_sounds_label = QtWidgets.QLabel(self.frame_4)
        self.p_w_sounds_label.setMinimumSize(QtCore.QSize(28, 28))
        self.p_w_sounds_label.setMaximumSize(QtCore.QSize(28, 28))
        self.p_w_sounds_label.setText("")
        self.p_w_sounds_label.setObjectName("p_w_sounds_label")
        self.gridLayout_2.addWidget(self.p_w_sounds_label, 11, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.frame_4)
        self.label_18.setObjectName("label_18")
        self.gridLayout_2.addWidget(self.label_18, 12, 1, 1, 1)
        self.p_w_fx_setup_label = QtWidgets.QLabel(self.frame_4)
        self.p_w_fx_setup_label.setMinimumSize(QtCore.QSize(28, 28))
        self.p_w_fx_setup_label.setMaximumSize(QtCore.QSize(28, 28))
        self.p_w_fx_setup_label.setText("")
        self.p_w_fx_setup_label.setObjectName("p_w_fx_setup_label")
        self.gridLayout_2.addWidget(self.p_w_fx_setup_label, 3, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.frame_4)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 3, 1, 1, 1)
        self.comboBox_12 = QtWidgets.QComboBox(self.frame_4)
        self.comboBox_12.setObjectName("comboBox_12")
        self.gridLayout_2.addWidget(self.comboBox_12, 6, 2, 1, 1)
        self.p_w_gizmo_label = QtWidgets.QLabel(self.frame_4)
        self.p_w_gizmo_label.setMinimumSize(QtCore.QSize(28, 28))
        self.p_w_gizmo_label.setMaximumSize(QtCore.QSize(28, 28))
        self.p_w_gizmo_label.setText("")
        self.p_w_gizmo_label.setObjectName("p_w_gizmo_label")
        self.gridLayout_2.addWidget(self.p_w_gizmo_label, 4, 0, 1, 1)
        self.comboBox_18 = QtWidgets.QComboBox(self.frame_4)
        self.comboBox_18.setObjectName("comboBox_18")
        self.gridLayout_2.addWidget(self.comboBox_18, 12, 2, 1, 1)
        self.comboBox_17 = QtWidgets.QComboBox(self.frame_4)
        self.comboBox_17.setObjectName("comboBox_17")
        self.gridLayout_2.addWidget(self.comboBox_17, 11, 2, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.frame_4)
        self.label_17.setObjectName("label_17")
        self.gridLayout_2.addWidget(self.label_17, 11, 1, 1, 1)
        self.comboBox_10 = QtWidgets.QComboBox(self.frame_4)
        self.comboBox_10.setObjectName("comboBox_10")
        self.gridLayout_2.addWidget(self.comboBox_10, 4, 2, 1, 1)
        self.comboBox_6 = QtWidgets.QComboBox(self.frame_4)
        self.comboBox_6.setObjectName("comboBox_6")
        self.gridLayout_2.addWidget(self.comboBox_6, 0, 2, 1, 1)
        self.comboBox_19 = QtWidgets.QComboBox(self.frame_4)
        self.comboBox_19.setObjectName("comboBox_19")
        self.gridLayout_2.addWidget(self.comboBox_19, 13, 2, 1, 1)
        self.comboBox_8 = QtWidgets.QComboBox(self.frame_4)
        self.comboBox_8.setObjectName("comboBox_8")
        self.gridLayout_2.addWidget(self.comboBox_8, 2, 2, 1, 1)
        self.comboBox_16 = QtWidgets.QComboBox(self.frame_4)
        self.comboBox_16.setObjectName("comboBox_16")
        self.gridLayout_2.addWidget(self.comboBox_16, 10, 2, 1, 1)
        self.comboBox_13 = QtWidgets.QComboBox(self.frame_4)
        self.comboBox_13.setObjectName("comboBox_13")
        self.gridLayout_2.addWidget(self.comboBox_13, 7, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame_4)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 1, 1, 1)
        self.comboBox_11 = QtWidgets.QComboBox(self.frame_4)
        self.comboBox_11.setObjectName("comboBox_11")
        self.gridLayout_2.addWidget(self.comboBox_11, 5, 2, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.frame_4)
        self.label_15.setObjectName("label_15")
        self.gridLayout_2.addWidget(self.label_15, 9, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.frame_4)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 5, 1, 1, 1)
        self.p_w_scripts_label = QtWidgets.QLabel(self.frame_4)
        self.p_w_scripts_label.setMinimumSize(QtCore.QSize(28, 28))
        self.p_w_scripts_label.setMaximumSize(QtCore.QSize(28, 28))
        self.p_w_scripts_label.setText("")
        self.p_w_scripts_label.setObjectName("p_w_scripts_label")
        self.gridLayout_2.addWidget(self.p_w_scripts_label, 10, 0, 1, 1)
        self.comboBox_9 = QtWidgets.QComboBox(self.frame_4)
        self.comboBox_9.setObjectName("comboBox_9")
        self.gridLayout_2.addWidget(self.comboBox_9, 3, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.frame_4)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.frame_4)
        self.label_16.setObjectName("label_16")
        self.gridLayout_2.addWidget(self.label_16, 10, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.frame_4)
        self.label_14.setObjectName("label_14")
        self.gridLayout_2.addWidget(self.label_14, 8, 1, 1, 1)
        self.p_w_video_label = QtWidgets.QLabel(self.frame_4)
        self.p_w_video_label.setMinimumSize(QtCore.QSize(28, 28))
        self.p_w_video_label.setMaximumSize(QtCore.QSize(28, 28))
        self.p_w_video_label.setText("")
        self.p_w_video_label.setObjectName("p_w_video_label")
        self.gridLayout_2.addWidget(self.p_w_video_label, 13, 0, 1, 1)
        self.p_w_light_rig_label = QtWidgets.QLabel(self.frame_4)
        self.p_w_light_rig_label.setMinimumSize(QtCore.QSize(28, 28))
        self.p_w_light_rig_label.setMaximumSize(QtCore.QSize(28, 28))
        self.p_w_light_rig_label.setText("")
        self.p_w_light_rig_label.setObjectName("p_w_light_rig_label")
        self.gridLayout_2.addWidget(self.p_w_light_rig_label, 5, 0, 1, 1)
        self.comboBox_15 = QtWidgets.QComboBox(self.frame_4)
        self.comboBox_15.setObjectName("comboBox_15")
        self.gridLayout_2.addWidget(self.comboBox_15, 9, 2, 1, 1)
        self.comboBox_14 = QtWidgets.QComboBox(self.frame_4)
        self.comboBox_14.setObjectName("comboBox_14")
        self.gridLayout_2.addWidget(self.comboBox_14, 8, 2, 1, 1)
        self.p_w_lut_label = QtWidgets.QLabel(self.frame_4)
        self.p_w_lut_label.setMinimumSize(QtCore.QSize(28, 28))
        self.p_w_lut_label.setMaximumSize(QtCore.QSize(28, 28))
        self.p_w_lut_label.setText("")
        self.p_w_lut_label.setObjectName("p_w_lut_label")
        self.gridLayout_2.addWidget(self.p_w_lut_label, 6, 0, 1, 1)
        self.p_w_stockshots_label = QtWidgets.QLabel(self.frame_4)
        self.p_w_stockshots_label.setMinimumSize(QtCore.QSize(28, 28))
        self.p_w_stockshots_label.setMaximumSize(QtCore.QSize(28, 28))
        self.p_w_stockshots_label.setText("")
        self.p_w_stockshots_label.setObjectName("p_w_stockshots_label")
        self.gridLayout_2.addWidget(self.p_w_stockshots_label, 12, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.frame_4)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 4, 1, 1, 1)
        self.comboBox_7 = QtWidgets.QComboBox(self.frame_4)
        self.comboBox_7.setObjectName("comboBox_7")
        self.gridLayout_2.addWidget(self.comboBox_7, 1, 2, 1, 1)
        self.p_w_autorig_label = QtWidgets.QLabel(self.frame_4)
        self.p_w_autorig_label.setMinimumSize(QtCore.QSize(28, 28))
        self.p_w_autorig_label.setMaximumSize(QtCore.QSize(28, 28))
        self.p_w_autorig_label.setText("")
        self.p_w_autorig_label.setObjectName("p_w_autorig_label")
        self.gridLayout_2.addWidget(self.p_w_autorig_label, 0, 0, 1, 1)
        self.p_w_cyclo_label = QtWidgets.QLabel(self.frame_4)
        self.p_w_cyclo_label.setMinimumSize(QtCore.QSize(28, 28))
        self.p_w_cyclo_label.setMaximumSize(QtCore.QSize(28, 28))
        self.p_w_cyclo_label.setText("")
        self.p_w_cyclo_label.setObjectName("p_w_cyclo_label")
        self.gridLayout_2.addWidget(self.p_w_cyclo_label, 2, 0, 1, 1)
        self.p_w_render_graph_label = QtWidgets.QLabel(self.frame_4)
        self.p_w_render_graph_label.setMinimumSize(QtCore.QSize(28, 28))
        self.p_w_render_graph_label.setMaximumSize(QtCore.QSize(28, 28))
        self.p_w_render_graph_label.setText("")
        self.p_w_render_graph_label.setObjectName("p_w_render_graph_label")
        self.gridLayout_2.addWidget(self.p_w_render_graph_label, 8, 0, 1, 1)
        self.p_w_material_label = QtWidgets.QLabel(self.frame_4)
        self.p_w_material_label.setMinimumSize(QtCore.QSize(28, 28))
        self.p_w_material_label.setMaximumSize(QtCore.QSize(28, 28))
        self.p_w_material_label.setText("")
        self.p_w_material_label.setObjectName("p_w_material_label")
        self.gridLayout_2.addWidget(self.p_w_material_label, 7, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.frame_4)
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 7, 1, 1, 1)
        self.p_w_camera_rig_label = QtWidgets.QLabel(self.frame_4)
        self.p_w_camera_rig_label.setMinimumSize(QtCore.QSize(28, 28))
        self.p_w_camera_rig_label.setMaximumSize(QtCore.QSize(28, 28))
        self.p_w_camera_rig_label.setText("")
        self.p_w_camera_rig_label.setObjectName("p_w_camera_rig_label")
        self.gridLayout_2.addWidget(self.p_w_camera_rig_label, 1, 0, 1, 1)
        self.p_w_render_pass_label = QtWidgets.QLabel(self.frame_4)
        self.p_w_render_pass_label.setMinimumSize(QtCore.QSize(28, 28))
        self.p_w_render_pass_label.setMaximumSize(QtCore.QSize(28, 28))
        self.p_w_render_pass_label.setText("")
        self.p_w_render_pass_label.setObjectName("p_w_render_pass_label")
        self.gridLayout_2.addWidget(self.p_w_render_pass_label, 9, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 14, 1, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout_2)
        self.verticalLayout_4.addWidget(self.frame_4)
        self.tabWidget.addTab(self.libraries_tab, "")
        self.sequences_tab = QtWidgets.QWidget()
        self.sequences_tab.setObjectName("sequences_tab")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.sequences_tab)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_5 = QtWidgets.QFrame(self.sequences_tab)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_20 = QtWidgets.QLabel(self.frame_5)
        self.label_20.setObjectName("label_20")
        self.gridLayout_3.addWidget(self.label_20, 0, 1, 1, 1)
        self.comboBox_25 = QtWidgets.QComboBox(self.frame_5)
        self.comboBox_25.setObjectName("comboBox_25")
        self.gridLayout_3.addWidget(self.comboBox_25, 5, 2, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.frame_5)
        self.label_21.setObjectName("label_21")
        self.gridLayout_3.addWidget(self.label_21, 1, 1, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.frame_5)
        self.label_25.setObjectName("label_25")
        self.gridLayout_3.addWidget(self.label_25, 5, 1, 1, 1)
        self.comboBox_22 = QtWidgets.QComboBox(self.frame_5)
        self.comboBox_22.setObjectName("comboBox_22")
        self.gridLayout_3.addWidget(self.comboBox_22, 2, 2, 1, 1)
        self.comboBox_27 = QtWidgets.QComboBox(self.frame_5)
        self.comboBox_27.setObjectName("comboBox_27")
        self.gridLayout_3.addWidget(self.comboBox_27, 7, 2, 1, 1)
        self.comboBox_20 = QtWidgets.QComboBox(self.frame_5)
        self.comboBox_20.setObjectName("comboBox_20")
        self.gridLayout_3.addWidget(self.comboBox_20, 0, 2, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.frame_5)
        self.label_22.setObjectName("label_22")
        self.gridLayout_3.addWidget(self.label_22, 2, 1, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.frame_5)
        self.label_24.setObjectName("label_24")
        self.gridLayout_3.addWidget(self.label_24, 4, 1, 1, 1)
        self.p_w_concept_label = QtWidgets.QLabel(self.frame_5)
        self.p_w_concept_label.setMinimumSize(QtCore.QSize(28, 28))
        self.p_w_concept_label.setMaximumSize(QtCore.QSize(28, 28))
        self.p_w_concept_label.setText("")
        self.p_w_concept_label.setObjectName("p_w_concept_label")
        self.gridLayout_3.addWidget(self.p_w_concept_label, 0, 0, 1, 1)
        self.comboBox_21 = QtWidgets.QComboBox(self.frame_5)
        self.comboBox_21.setObjectName("comboBox_21")
        self.gridLayout_3.addWidget(self.comboBox_21, 1, 2, 1, 1)
        self.comboBox_24 = QtWidgets.QComboBox(self.frame_5)
        self.comboBox_24.setObjectName("comboBox_24")
        self.gridLayout_3.addWidget(self.comboBox_24, 4, 2, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.frame_5)
        self.label_26.setObjectName("label_26")
        self.gridLayout_3.addWidget(self.label_26, 6, 1, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.frame_5)
        self.label_23.setObjectName("label_23")
        self.gridLayout_3.addWidget(self.label_23, 3, 1, 1, 1)
        self.comboBox_23 = QtWidgets.QComboBox(self.frame_5)
        self.comboBox_23.setObjectName("comboBox_23")
        self.gridLayout_3.addWidget(self.comboBox_23, 3, 2, 1, 1)
        self.comboBox_26 = QtWidgets.QComboBox(self.frame_5)
        self.comboBox_26.setObjectName("comboBox_26")
        self.gridLayout_3.addWidget(self.comboBox_26, 6, 2, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.frame_5)
        self.label_27.setObjectName("label_27")
        self.gridLayout_3.addWidget(self.label_27, 7, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem2, 8, 1, 1, 1)
        self.p_w_layout_label = QtWidgets.QLabel(self.frame_5)
        self.p_w_layout_label.setMinimumSize(QtCore.QSize(28, 28))
        self.p_w_layout_label.setMaximumSize(QtCore.QSize(28, 28))
        self.p_w_layout_label.setText("")
        self.p_w_layout_label.setObjectName("p_w_layout_label")
        self.gridLayout_3.addWidget(self.p_w_layout_label, 1, 0, 1, 1)
        self.p_w_animation_label = QtWidgets.QLabel(self.frame_5)
        self.p_w_animation_label.setMinimumSize(QtCore.QSize(28, 28))
        self.p_w_animation_label.setMaximumSize(QtCore.QSize(28, 28))
        self.p_w_animation_label.setText("")
        self.p_w_animation_label.setObjectName("p_w_animation_label")
        self.gridLayout_3.addWidget(self.p_w_animation_label, 2, 0, 1, 1)
        self.p_w_lighting_label = QtWidgets.QLabel(self.frame_5)
        self.p_w_lighting_label.setMinimumSize(QtCore.QSize(28, 28))
        self.p_w_lighting_label.setMaximumSize(QtCore.QSize(28, 28))
        self.p_w_lighting_label.setText("")
        self.p_w_lighting_label.setObjectName("p_w_lighting_label")
        self.gridLayout_3.addWidget(self.p_w_lighting_label, 3, 0, 1, 1)
        self.p_w_cfx_label = QtWidgets.QLabel(self.frame_5)
        self.p_w_cfx_label.setMinimumSize(QtCore.QSize(28, 28))
        self.p_w_cfx_label.setMaximumSize(QtCore.QSize(28, 28))
        self.p_w_cfx_label.setText("")
        self.p_w_cfx_label.setObjectName("p_w_cfx_label")
        self.gridLayout_3.addWidget(self.p_w_cfx_label, 4, 0, 1, 1)
        self.p_w_fx_label = QtWidgets.QLabel(self.frame_5)
        self.p_w_fx_label.setMinimumSize(QtCore.QSize(28, 28))
        self.p_w_fx_label.setMaximumSize(QtCore.QSize(28, 28))
        self.p_w_fx_label.setText("")
        self.p_w_fx_label.setObjectName("p_w_fx_label")
        self.gridLayout_3.addWidget(self.p_w_fx_label, 5, 0, 1, 1)
        self.p_w_compositing_label = QtWidgets.QLabel(self.frame_5)
        self.p_w_compositing_label.setMinimumSize(QtCore.QSize(28, 28))
        self.p_w_compositing_label.setMaximumSize(QtCore.QSize(28, 28))
        self.p_w_compositing_label.setText("")
        self.p_w_compositing_label.setObjectName("p_w_compositing_label")
        self.gridLayout_3.addWidget(self.p_w_compositing_label, 6, 0, 1, 1)
        self.p_w_camera_label = QtWidgets.QLabel(self.frame_5)
        self.p_w_camera_label.setMinimumSize(QtCore.QSize(28, 28))
        self.p_w_camera_label.setMaximumSize(QtCore.QSize(28, 28))
        self.p_w_camera_label.setText("")
        self.p_w_camera_label.setObjectName("p_w_camera_label")
        self.gridLayout_3.addWidget(self.p_w_camera_label, 7, 0, 1, 1)
        self.verticalLayout_7.addLayout(self.gridLayout_3)
        self.verticalLayout_5.addWidget(self.frame_5)
        self.tabWidget.addTab(self.sequences_tab, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setMinimumSize(QtCore.QSize(100, 40))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addWidget(self.frame_2)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "Rigging"))
        self.label_5.setText(_translate("Form", "Grooming"))
        self.label_9.setText(_translate("Form", "Shading"))
        self.label_7.setText(_translate("Form", "Texturing"))
        self.label_2.setText(_translate("Form", "Modeling"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.assets_tab), _translate("Form", "Assets"))
        self.label_19.setText(_translate("Form", "Video"))
        self.label_6.setText(_translate("Form", "Cyclo"))
        self.label_12.setText(_translate("Form", "Lut"))
        self.label_18.setText(_translate("Form", "Stockshots"))
        self.label_8.setText(_translate("Form", "Fx Setup"))
        self.label_17.setText(_translate("Form", "Sounds"))
        self.label_4.setText(_translate("Form", "Camera Rig"))
        self.label_15.setText(_translate("Form", "Render Pass"))
        self.label_11.setText(_translate("Form", "Light Rig"))
        self.label.setText(_translate("Form", "Autorig"))
        self.label_16.setText(_translate("Form", "Scripts"))
        self.label_14.setText(_translate("Form", "Render Graph"))
        self.label_10.setText(_translate("Form", "Gizmo"))
        self.label_13.setText(_translate("Form", "Material"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.libraries_tab), _translate("Form", "Libraries"))
        self.label_20.setText(_translate("Form", "Concept"))
        self.label_21.setText(_translate("Form", "Layout"))
        self.label_25.setText(_translate("Form", "Fx"))
        self.label_22.setText(_translate("Form", "Animation"))
        self.label_24.setText(_translate("Form", "Cfx"))
        self.label_26.setText(_translate("Form", "Compositing"))
        self.label_23.setText(_translate("Form", "Lighting"))
        self.label_27.setText(_translate("Form", "Camera"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.sequences_tab), _translate("Form", "Sequences"))
        self.pushButton.setText(_translate("Form", "Apply"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
