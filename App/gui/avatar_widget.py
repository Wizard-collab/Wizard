import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget, QCheckBox, QSystemTrayIcon, \
    QSpacerItem, QSizePolicy, QMenu, QAction, QStyle, qApp
from PyQt5.QtCore import QSize, QPoint
import os
from wizard.tools import log

logger = log.pipe_log()


def build_avatar(self, image):
    self.ui.avatar_main_Frame = QtWidgets.QFrame(self.ui.scrollAreaWidgetContents)
    self.ui.avatar_main_Frame.setObjectName("avatar_main_Frame")
    self.ui.avatar_main_Frame.setMinimumSize(QtCore.QSize(202, 237))
    self.ui.avatar_main_Frame.setMaximumSize(QtCore.QSize(202, 237))
    self.ui.verticalLayout_2 = QtWidgets.QVBoxLayout(self.ui.avatar_main_Frame)
    self.ui.verticalLayout_2.setObjectName("verticalLayout_2")
    self.ui.avatar_image_frame = QtWidgets.QFrame(self.ui.avatar_main_Frame)
    self.ui.avatar_image_frame.setMinimumSize(QtCore.QSize(200, 200))
    self.ui.avatar_image_frame.setMaximumSize(QtCore.QSize(200, 200))
    self.ui.avatar_image_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
    self.ui.avatar_image_frame.setFrameShadow(QtWidgets.QFrame.Raised)
    self.ui.avatar_image_frame.setObjectName("avatar_image_frame")
    self.ui.verticalLayout_2.addWidget(self.ui.avatar_image_frame)
    self.ui.avatar_main_pushButton = QtWidgets.QPushButton(self.ui.avatar_main_Frame)
    self.ui.avatar_main_pushButton.setObjectName("avatar_main_pushButton")
    self.ui.verticalLayout_2.addWidget(self.ui.avatar_main_pushButton)
    self.ui.horizontalLayout_2.addWidget(self.ui.avatar_main_Frame)
    self.ui.verticalLayout_3 = QtWidgets.QVBoxLayout(self.ui.avatar_image_frame)
    self.ui.verticalLayout_3.setObjectName("verticalLayout_3")
    self.ui.avatar_name = QtWidgets.QLabel(self.ui.avatar_image_frame)
    sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
    sizePolicy.setHorizontalStretch(0)
    sizePolicy.setVerticalStretch(0)
    sizePolicy.setHeightForWidth(self.ui.avatar_name.sizePolicy().hasHeightForWidth())
    self.ui.avatar_name.setSizePolicy(sizePolicy)
    self.ui.avatar_name.setObjectName("avatar_name")

    avatar_name = os.path.basename(image).split('.')[0]

    self.ui.avatar_name.setText(avatar_name)
    self.ui.verticalLayout_3.addWidget(self.ui.avatar_name)
    self.ui.image_label = QtWidgets.QLabel(self.ui.avatar_image_frame)
    self.ui.image_label.setText("")
    self.ui.image_label.setObjectName("image_label")
    self.ui.verticalLayout_3.addWidget(self.ui.image_label)
    self.ui.image_label.setPixmap(QtGui.QPixmap(image).scaled(160,160, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
    self.ui.avatar_main_pushButton.setText("Select")

    self.ui.avatar_main_pushButton.clicked.connect(lambda: select_avatar(self, avatar_name))

def select_avatar(self, avatar_name):
    self.avatar = avatar_name
    self.accept()
   