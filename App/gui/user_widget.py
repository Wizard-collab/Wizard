# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(294, 167)
        Form.setMaximumSize(QtCore.QSize(294, 16777215))
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.user_frame = QtWidgets.QFrame(Form)
        self.user_frame.setMinimumSize(QtCore.QSize(125, 130))
        self.user_frame.setMaximumSize(QtCore.QSize(125, 10000))
        self.user_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.user_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.user_frame.setObjectName("user_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.user_frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.user_image_pushButton = QtWidgets.QPushButton(self.user_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.user_image_pushButton.sizePolicy().hasHeightForWidth())
        self.user_image_pushButton.setSizePolicy(sizePolicy)
        self.user_image_pushButton.setMinimumSize(QtCore.QSize(70, 70))
        self.user_image_pushButton.setMaximumSize(QtCore.QSize(70, 70))
        self.user_image_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.user_image_pushButton.setText("")
        self.user_image_pushButton.setIconSize(QtCore.QSize(70, 70))
        self.user_image_pushButton.setObjectName("user_image_pushButton")
        self.horizontalLayout_2.addWidget(self.user_image_pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.user_name_label = QtWidgets.QLabel(self.user_frame)
        self.user_name_label.setText("")
        self.user_name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.user_name_label.setObjectName("user_name_label")
        self.verticalLayout_2.addWidget(self.user_name_label)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.admin_image_label = QtWidgets.QLabel(self.user_frame)
        self.admin_image_label.setMinimumSize(QtCore.QSize(20, 20))
        self.admin_image_label.setMaximumSize(QtCore.QSize(20, 20))
        self.admin_image_label.setText("")
        self.admin_image_label.setObjectName("admin_image_label")
        self.horizontalLayout_5.addWidget(self.admin_image_label)
        self.promotion_label = QtWidgets.QLabel(self.user_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.promotion_label.sizePolicy().hasHeightForWidth())
        self.promotion_label.setSizePolicy(sizePolicy)
        self.promotion_label.setText("")
        self.promotion_label.setAlignment(QtCore.Qt.AlignCenter)
        self.promotion_label.setObjectName("promotion_label")
        self.horizontalLayout_5.addWidget(self.promotion_label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout.addWidget(self.user_frame)
        self.game_stats_frame = QtWidgets.QFrame(Form)
        self.game_stats_frame.setMaximumSize(QtCore.QSize(168, 10000))
        self.game_stats_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.game_stats_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.game_stats_frame.setObjectName("game_stats_frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.game_stats_frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setHorizontalSpacing(1)
        self.formLayout.setVerticalSpacing(0)
        self.formLayout.setObjectName("formLayout")
        self.level_label = QtWidgets.QLabel(self.game_stats_frame)
        self.level_label.setMinimumSize(QtCore.QSize(25, 25))
        self.level_label.setMaximumSize(QtCore.QSize(25, 25))
        self.level_label.setText("")
        self.level_label.setObjectName("level_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.level_label)
        self.level_label_number = QtWidgets.QLabel(self.game_stats_frame)
        self.level_label_number.setObjectName("level_label_number")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.level_label_number)
        self.xp_label = QtWidgets.QLabel(self.game_stats_frame)
        self.xp_label.setMinimumSize(QtCore.QSize(25, 25))
        self.xp_label.setMaximumSize(QtCore.QSize(25, 25))
        self.xp_label.setText("")
        self.xp_label.setObjectName("xp_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.xp_label)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        spacerItem3 = QtWidgets.QSpacerItem(20, 6, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_6.addItem(spacerItem3)
        self.xp_progressBar = QtWidgets.QProgressBar(self.game_stats_frame)
        self.xp_progressBar.setMinimumSize(QtCore.QSize(0, 12))
        self.xp_progressBar.setMaximumSize(QtCore.QSize(16777215, 12))
        self.xp_progressBar.setProperty("value", 24)
        self.xp_progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.xp_progressBar.setTextVisible(False)
        self.xp_progressBar.setObjectName("xp_progressBar")
        self.verticalLayout_6.addWidget(self.xp_progressBar)
        spacerItem4 = QtWidgets.QSpacerItem(20, 7, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_6.addItem(spacerItem4)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.verticalLayout_6)
        self.verticalLayout_4.addLayout(self.formLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.user_tickets_pushButton = QtWidgets.QPushButton(self.game_stats_frame)
        self.user_tickets_pushButton.setMinimumSize(QtCore.QSize(28, 28))
        self.user_tickets_pushButton.setMaximumSize(QtCore.QSize(28, 28))
        self.user_tickets_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.user_tickets_pushButton.setText("")
        self.user_tickets_pushButton.setObjectName("user_tickets_pushButton")
        self.horizontalLayout_3.addWidget(self.user_tickets_pushButton)
        self.stats_pushButton = QtWidgets.QPushButton(self.game_stats_frame)
        self.stats_pushButton.setMinimumSize(QtCore.QSize(28, 28))
        self.stats_pushButton.setMaximumSize(QtCore.QSize(28, 28))
        self.stats_pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.stats_pushButton.setText("")
        self.stats_pushButton.setObjectName("stats_pushButton")
        self.horizontalLayout_3.addWidget(self.stats_pushButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout.addWidget(self.game_stats_frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.level_label_number.setText(_translate("Form", "12"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
