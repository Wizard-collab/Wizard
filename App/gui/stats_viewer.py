# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\conta\Documents\script\wizard_devellop\App\gui\ui_files\stats_viewer.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(407, 208)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.stats_main_frame = QtWidgets.QFrame(Form)
        self.stats_main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.stats_main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.stats_main_frame.setObjectName("stats_main_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.stats_main_frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName("gridLayout")
        self.design_publish_label = QtWidgets.QLabel(self.stats_main_frame)
        self.design_publish_label.setObjectName("design_publish_label")
        self.gridLayout.addWidget(self.design_publish_label, 0, 3, 1, 1)
        self.rig_publish_label = QtWidgets.QLabel(self.stats_main_frame)
        self.rig_publish_label.setObjectName("rig_publish_label")
        self.gridLayout.addWidget(self.rig_publish_label, 2, 3, 1, 1)
        self.texturing_publish_label = QtWidgets.QLabel(self.stats_main_frame)
        self.texturing_publish_label.setObjectName("texturing_publish_label")
        self.gridLayout.addWidget(self.texturing_publish_label, 3, 3, 1, 1)
        self.geo_publish_label = QtWidgets.QLabel(self.stats_main_frame)
        self.geo_publish_label.setObjectName("geo_publish_label")
        self.gridLayout.addWidget(self.geo_publish_label, 1, 3, 1, 1)
        self.hair_publish_label = QtWidgets.QLabel(self.stats_main_frame)
        self.hair_publish_label.setObjectName("hair_publish_label")
        self.gridLayout.addWidget(self.hair_publish_label, 4, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.stats_main_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(60, 0))
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.stats_main_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(60, 0))
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)
        self.rig_stats_progressBar = QtWidgets.QProgressBar(self.stats_main_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rig_stats_progressBar.sizePolicy().hasHeightForWidth())
        self.rig_stats_progressBar.setSizePolicy(sizePolicy)
        self.rig_stats_progressBar.setMinimumSize(QtCore.QSize(0, 12))
        self.rig_stats_progressBar.setMaximumSize(QtCore.QSize(16777215, 12))
        self.rig_stats_progressBar.setProperty("value", 24)
        self.rig_stats_progressBar.setTextVisible(True)
        self.rig_stats_progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.rig_stats_progressBar.setObjectName("rig_stats_progressBar")
        self.gridLayout.addWidget(self.rig_stats_progressBar, 2, 2, 1, 1)
        self.hair_image_label = QtWidgets.QLabel(self.stats_main_frame)
        self.hair_image_label.setMinimumSize(QtCore.QSize(25, 25))
        self.hair_image_label.setMaximumSize(QtCore.QSize(25, 25))
        self.hair_image_label.setText("")
        self.hair_image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.hair_image_label.setObjectName("hair_image_label")
        self.gridLayout.addWidget(self.hair_image_label, 4, 0, 1, 1)
        self.design_stats_progressBar = QtWidgets.QProgressBar(self.stats_main_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.design_stats_progressBar.sizePolicy().hasHeightForWidth())
        self.design_stats_progressBar.setSizePolicy(sizePolicy)
        self.design_stats_progressBar.setMinimumSize(QtCore.QSize(0, 12))
        self.design_stats_progressBar.setMaximumSize(QtCore.QSize(16777215, 12))
        self.design_stats_progressBar.setProperty("value", 24)
        self.design_stats_progressBar.setTextVisible(True)
        self.design_stats_progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.design_stats_progressBar.setObjectName("design_stats_progressBar")
        self.gridLayout.addWidget(self.design_stats_progressBar, 0, 2, 1, 1)
        self.geo_image_label = QtWidgets.QLabel(self.stats_main_frame)
        self.geo_image_label.setMinimumSize(QtCore.QSize(25, 25))
        self.geo_image_label.setMaximumSize(QtCore.QSize(25, 25))
        self.geo_image_label.setText("")
        self.geo_image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.geo_image_label.setObjectName("geo_image_label")
        self.gridLayout.addWidget(self.geo_image_label, 1, 0, 1, 1)
        self.texturing_image_label = QtWidgets.QLabel(self.stats_main_frame)
        self.texturing_image_label.setMinimumSize(QtCore.QSize(25, 25))
        self.texturing_image_label.setMaximumSize(QtCore.QSize(25, 25))
        self.texturing_image_label.setText("")
        self.texturing_image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.texturing_image_label.setObjectName("texturing_image_label")
        self.gridLayout.addWidget(self.texturing_image_label, 3, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.stats_main_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(60, 0))
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 1, 1, 1)
        self.design_image_label = QtWidgets.QLabel(self.stats_main_frame)
        self.design_image_label.setMinimumSize(QtCore.QSize(25, 25))
        self.design_image_label.setMaximumSize(QtCore.QSize(25, 25))
        self.design_image_label.setText("")
        self.design_image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.design_image_label.setObjectName("design_image_label")
        self.gridLayout.addWidget(self.design_image_label, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.stats_main_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(60, 0))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.stats_main_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QtCore.QSize(60, 0))
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 1, 1, 1)
        self.texturing_stats_progressBar = QtWidgets.QProgressBar(self.stats_main_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.texturing_stats_progressBar.sizePolicy().hasHeightForWidth())
        self.texturing_stats_progressBar.setSizePolicy(sizePolicy)
        self.texturing_stats_progressBar.setMinimumSize(QtCore.QSize(0, 12))
        self.texturing_stats_progressBar.setMaximumSize(QtCore.QSize(16777215, 12))
        self.texturing_stats_progressBar.setProperty("value", 24)
        self.texturing_stats_progressBar.setTextVisible(True)
        self.texturing_stats_progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.texturing_stats_progressBar.setObjectName("texturing_stats_progressBar")
        self.gridLayout.addWidget(self.texturing_stats_progressBar, 3, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.stats_main_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(60, 0))
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 1, 1, 1)
        self.rig_image_label = QtWidgets.QLabel(self.stats_main_frame)
        self.rig_image_label.setMinimumSize(QtCore.QSize(25, 25))
        self.rig_image_label.setMaximumSize(QtCore.QSize(25, 25))
        self.rig_image_label.setText("")
        self.rig_image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.rig_image_label.setObjectName("rig_image_label")
        self.gridLayout.addWidget(self.rig_image_label, 2, 0, 1, 1)
        self.shading_image_label = QtWidgets.QLabel(self.stats_main_frame)
        self.shading_image_label.setMinimumSize(QtCore.QSize(25, 25))
        self.shading_image_label.setMaximumSize(QtCore.QSize(25, 25))
        self.shading_image_label.setText("")
        self.shading_image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.shading_image_label.setObjectName("shading_image_label")
        self.gridLayout.addWidget(self.shading_image_label, 5, 0, 1, 1)
        self.hair_stats_progressBar = QtWidgets.QProgressBar(self.stats_main_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hair_stats_progressBar.sizePolicy().hasHeightForWidth())
        self.hair_stats_progressBar.setSizePolicy(sizePolicy)
        self.hair_stats_progressBar.setMinimumSize(QtCore.QSize(0, 12))
        self.hair_stats_progressBar.setMaximumSize(QtCore.QSize(16777215, 12))
        self.hair_stats_progressBar.setProperty("value", 24)
        self.hair_stats_progressBar.setTextVisible(True)
        self.hair_stats_progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.hair_stats_progressBar.setObjectName("hair_stats_progressBar")
        self.gridLayout.addWidget(self.hair_stats_progressBar, 4, 2, 1, 1)
        self.shading_stats_progressBar = QtWidgets.QProgressBar(self.stats_main_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shading_stats_progressBar.sizePolicy().hasHeightForWidth())
        self.shading_stats_progressBar.setSizePolicy(sizePolicy)
        self.shading_stats_progressBar.setMinimumSize(QtCore.QSize(0, 12))
        self.shading_stats_progressBar.setMaximumSize(QtCore.QSize(16777215, 12))
        self.shading_stats_progressBar.setProperty("value", 24)
        self.shading_stats_progressBar.setTextVisible(True)
        self.shading_stats_progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.shading_stats_progressBar.setObjectName("shading_stats_progressBar")
        self.gridLayout.addWidget(self.shading_stats_progressBar, 5, 2, 1, 1)
        self.geo_stats_progressBar = QtWidgets.QProgressBar(self.stats_main_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.geo_stats_progressBar.sizePolicy().hasHeightForWidth())
        self.geo_stats_progressBar.setSizePolicy(sizePolicy)
        self.geo_stats_progressBar.setMinimumSize(QtCore.QSize(0, 12))
        self.geo_stats_progressBar.setMaximumSize(QtCore.QSize(16777215, 12))
        self.geo_stats_progressBar.setProperty("value", 24)
        self.geo_stats_progressBar.setTextVisible(True)
        self.geo_stats_progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.geo_stats_progressBar.setObjectName("geo_stats_progressBar")
        self.gridLayout.addWidget(self.geo_stats_progressBar, 1, 2, 1, 1)
        self.shading_publish_label = QtWidgets.QLabel(self.stats_main_frame)
        self.shading_publish_label.setObjectName("shading_publish_label")
        self.gridLayout.addWidget(self.shading_publish_label, 5, 3, 1, 1)
        self.design_work_label = QtWidgets.QLabel(self.stats_main_frame)
        self.design_work_label.setObjectName("design_work_label")
        self.gridLayout.addWidget(self.design_work_label, 0, 4, 1, 1)
        self.geo_work_label = QtWidgets.QLabel(self.stats_main_frame)
        self.geo_work_label.setObjectName("geo_work_label")
        self.gridLayout.addWidget(self.geo_work_label, 1, 4, 1, 1)
        self.rig_work_label = QtWidgets.QLabel(self.stats_main_frame)
        self.rig_work_label.setObjectName("rig_work_label")
        self.gridLayout.addWidget(self.rig_work_label, 2, 4, 1, 1)
        self.texturing_work_label = QtWidgets.QLabel(self.stats_main_frame)
        self.texturing_work_label.setObjectName("texturing_work_label")
        self.gridLayout.addWidget(self.texturing_work_label, 3, 4, 1, 1)
        self.hair_work_label = QtWidgets.QLabel(self.stats_main_frame)
        self.hair_work_label.setObjectName("hair_work_label")
        self.gridLayout.addWidget(self.hair_work_label, 4, 4, 1, 1)
        self.shading_work_label = QtWidgets.QLabel(self.stats_main_frame)
        self.shading_work_label.setObjectName("shading_work_label")
        self.gridLayout.addWidget(self.shading_work_label, 5, 4, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.verticalLayout_8.addWidget(self.stats_main_frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.design_publish_label.setText(_translate("Form", "TextLabel"))
        self.rig_publish_label.setText(_translate("Form", "TextLabel"))
        self.texturing_publish_label.setText(_translate("Form", "TextLabel"))
        self.geo_publish_label.setText(_translate("Form", "TextLabel"))
        self.hair_publish_label.setText(_translate("Form", "TextLabel"))
        self.label_2.setText(_translate("Form", "Geo"))
        self.label_3.setText(_translate("Form", "Rig"))
        self.label_4.setText(_translate("Form", "Texturing"))
        self.label.setText(_translate("Form", "Design"))
        self.label_6.setText(_translate("Form", "Hair"))
        self.label_5.setText(_translate("Form", "Shading"))
        self.shading_publish_label.setText(_translate("Form", "TextLabel"))
        self.design_work_label.setText(_translate("Form", "TextLabel"))
        self.geo_work_label.setText(_translate("Form", "TextLabel"))
        self.rig_work_label.setText(_translate("Form", "TextLabel"))
        self.texturing_work_label.setText(_translate("Form", "TextLabel"))
        self.hair_work_label.setText(_translate("Form", "TextLabel"))
        self.shading_work_label.setText(_translate("Form", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
