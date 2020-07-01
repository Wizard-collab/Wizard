# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\conta\Documents\script\Wizard\App\work\ui_files\updates.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(761, 629)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.maj_layout = QtWidgets.QVBoxLayout(self.frame)
        self.maj_layout.setContentsMargins(1, 1, 1, 1)
        self.maj_layout.setObjectName("maj_layout")
        self.update_scrollArea = QtWidgets.QScrollArea(self.frame)
        self.update_scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.update_scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.update_scrollArea.setWidgetResizable(True)
        self.update_scrollArea.setObjectName("update_scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 732, 529))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widgets_verticalLayout = QtWidgets.QVBoxLayout()
        self.widgets_verticalLayout.setSpacing(10)
        self.widgets_verticalLayout.setObjectName("widgets_verticalLayout")
        self.verticalLayout_3.addLayout(self.widgets_verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.update_scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.maj_layout.addWidget(self.update_scrollArea)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.show_startup_checkBox = QtWidgets.QCheckBox(self.frame_3)
        self.show_startup_checkBox.setChecked(True)
        self.show_startup_checkBox.setObjectName("show_startup_checkBox")
        self.horizontalLayout_2.addWidget(self.show_startup_checkBox)
        self.maj_layout.addWidget(self.frame_3)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Wizard updates"))
        self.show_startup_checkBox.setText(_translate("Form", "Show this at startup"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
