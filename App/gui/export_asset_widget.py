# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\leo\Documents\Script\Wizard\App\gui\ui_files\export_asset_widget.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1059, 39)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.line_7 = QtWidgets.QFrame(Form)
        self.line_7.setMaximumSize(QtCore.QSize(16777215, 1))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.verticalLayout.addWidget(self.line_7)
        self.list_export_widget_frame = QtWidgets.QFrame(Form)
        self.list_export_widget_frame.setMaximumSize(QtCore.QSize(16777215, 38))
        self.list_export_widget_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.list_export_widget_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.list_export_widget_frame.setObjectName("list_export_widget_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.list_export_widget_frame)
        self.horizontalLayout.setContentsMargins(11, 5, 5, 5)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.export_asset_widget_pushButton = QtWidgets.QPushButton(self.list_export_widget_frame)
        self.export_asset_widget_pushButton.setMinimumSize(QtCore.QSize(28, 28))
        self.export_asset_widget_pushButton.setMaximumSize(QtCore.QSize(28, 28))
        self.export_asset_widget_pushButton.setText("")
        self.export_asset_widget_pushButton.setIconSize(QtCore.QSize(16, 16))
        self.export_asset_widget_pushButton.setObjectName("export_asset_widget_pushButton")
        self.horizontalLayout.addWidget(self.export_asset_widget_pushButton)
        self.export_asset_widget_label = QtWidgets.QLabel(self.list_export_widget_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.export_asset_widget_label.sizePolicy().hasHeightForWidth())
        self.export_asset_widget_label.setSizePolicy(sizePolicy)
        self.export_asset_widget_label.setObjectName("export_asset_widget_label")
        self.horizontalLayout.addWidget(self.export_asset_widget_label)
        self.line = QtWidgets.QFrame(self.list_export_widget_frame)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.export_asset_widget_number_label = QtWidgets.QLabel(self.list_export_widget_frame)
        self.export_asset_widget_number_label.setObjectName("export_asset_widget_number_label")
        self.horizontalLayout.addWidget(self.export_asset_widget_number_label)
        self.verticalLayout.addWidget(self.list_export_widget_frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.export_asset_widget_label.setText(_translate("Form", "Asset"))
        self.export_asset_widget_number_label.setText(_translate("Form", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
