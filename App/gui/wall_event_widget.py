# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\leo\Documents\Script\Wizard\App\gui\ui_files\wall_event_widget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(257, 69)
        Form.setMinimumSize(QtCore.QSize(0, 69))
        Form.setMaximumSize(QtCore.QSize(16777215, 69))
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, 0, -1, 0)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.wall_event_frame = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wall_event_frame.sizePolicy().hasHeightForWidth())
        self.wall_event_frame.setSizePolicy(sizePolicy)
        self.wall_event_frame.setMinimumSize(QtCore.QSize(0, 67))
        self.wall_event_frame.setMaximumSize(QtCore.QSize(16777215, 120))
        self.wall_event_frame.setStyleSheet("")
        self.wall_event_frame.setObjectName("wall_event_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.wall_event_frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.color_id_frame = QtWidgets.QFrame(self.wall_event_frame)
        self.color_id_frame.setMinimumSize(QtCore.QSize(5, 0))
        self.color_id_frame.setMaximumSize(QtCore.QSize(5, 16777215))
        self.color_id_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.color_id_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.color_id_frame.setObjectName("color_id_frame")
        self.horizontalLayout.addWidget(self.color_id_frame)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(10, 6, 10, 6)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.wall_event_user_label = QtWidgets.QLabel(self.wall_event_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wall_event_user_label.sizePolicy().hasHeightForWidth())
        self.wall_event_user_label.setSizePolicy(sizePolicy)
        self.wall_event_user_label.setMinimumSize(QtCore.QSize(0, 18))
        self.wall_event_user_label.setStyleSheet("")
        self.wall_event_user_label.setObjectName("wall_event_user_label")
        self.verticalLayout_3.addWidget(self.wall_event_user_label)
        self.wall_event_message_label = QtWidgets.QLabel(self.wall_event_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wall_event_message_label.sizePolicy().hasHeightForWidth())
        self.wall_event_message_label.setSizePolicy(sizePolicy)
        self.wall_event_message_label.setWordWrap(True)
        self.wall_event_message_label.setObjectName("wall_event_message_label")
        self.verticalLayout_3.addWidget(self.wall_event_message_label)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout.addWidget(self.wall_event_frame)
        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.wall_event_user_label.setText(_translate("Form", "user"))
        self.wall_event_message_label.setText(_translate("Form", "message"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

