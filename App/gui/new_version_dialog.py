# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\conta\Documents\script\Wizard\App\work\ui_files\new_version_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(529, 186)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.version_label = QtWidgets.QLabel(self.frame_2)
        self.version_label.setText("")
        self.version_label.setObjectName("version_label")
        self.verticalLayout_2.addWidget(self.version_label)
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout.addWidget(self.frame_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.never_pushButton = QtWidgets.QPushButton(Dialog)
        self.never_pushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.never_pushButton.setObjectName("never_pushButton")
        self.horizontalLayout_2.addWidget(self.never_pushButton)
        self.later_pushButton = QtWidgets.QPushButton(Dialog)
        self.later_pushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.later_pushButton.setObjectName("later_pushButton")
        self.horizontalLayout_2.addWidget(self.later_pushButton)
        self.download_pushButton = QtWidgets.QPushButton(Dialog)
        self.download_pushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.download_pushButton.setDefault(True)
        self.download_pushButton.setObjectName("download_pushButton")
        self.horizontalLayout_2.addWidget(self.download_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "New wizard version available !"))
        self.label_2.setText(_translate("Dialog", "Warning : You will need to uninstall the current version and install the new one."))
        self.never_pushButton.setText(_translate("Dialog", "Don\'t show me this again"))
        self.later_pushButton.setText(_translate("Dialog", "Remind me later"))
        self.download_pushButton.setText(_translate("Dialog", "Download"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
