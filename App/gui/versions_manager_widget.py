# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\conta\Documents\script\Wizard\App\ui_files\versions_manager_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1000, 774)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.exports_main_frame = QtWidgets.QFrame(Form)
        self.exports_main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.exports_main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.exports_main_frame.setObjectName("exports_main_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.exports_main_frame)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(8)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.exports_manager_header_Frame = QtWidgets.QFrame(self.exports_main_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exports_manager_header_Frame.sizePolicy().hasHeightForWidth())
        self.exports_manager_header_Frame.setSizePolicy(sizePolicy)
        self.exports_manager_header_Frame.setObjectName("exports_manager_header_Frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.exports_manager_header_Frame)
        self.horizontalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.exports_manager_label = QtWidgets.QLabel(self.exports_manager_header_Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exports_manager_label.sizePolicy().hasHeightForWidth())
        self.exports_manager_label.setSizePolicy(sizePolicy)
        self.exports_manager_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.exports_manager_label.setObjectName("exports_manager_label")
        self.horizontalLayout_3.addWidget(self.exports_manager_label)
        self.show_more_horizontalFrame = QtWidgets.QFrame(self.exports_manager_header_Frame)
        self.show_more_horizontalFrame.setObjectName("show_more_horizontalFrame")
        self.show_more_layout = QtWidgets.QHBoxLayout(self.show_more_horizontalFrame)
        self.show_more_layout.setContentsMargins(0, 0, 4, 0)
        self.show_more_layout.setSpacing(4)
        self.show_more_layout.setObjectName("show_more_layout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.show_more_layout.addItem(spacerItem)
        self.exports_number_label = QtWidgets.QLabel(self.show_more_horizontalFrame)
        self.exports_number_label.setText("")
        self.exports_number_label.setObjectName("exports_number_label")
        self.show_more_layout.addWidget(self.exports_number_label)
        self.show_more_pushButton = QtWidgets.QPushButton(self.show_more_horizontalFrame)
        self.show_more_pushButton.setMinimumSize(QtCore.QSize(28, 28))
        self.show_more_pushButton.setMaximumSize(QtCore.QSize(28, 28))
        self.show_more_pushButton.setObjectName("show_more_pushButton")
        self.show_more_layout.addWidget(self.show_more_pushButton)
        self.show_less_pushButton = QtWidgets.QPushButton(self.show_more_horizontalFrame)
        self.show_less_pushButton.setMinimumSize(QtCore.QSize(28, 28))
        self.show_less_pushButton.setMaximumSize(QtCore.QSize(28, 28))
        self.show_less_pushButton.setObjectName("show_less_pushButton")
        self.show_more_layout.addWidget(self.show_less_pushButton)
        self.display_pushButton = QtWidgets.QPushButton(self.show_more_horizontalFrame)
        self.display_pushButton.setMinimumSize(QtCore.QSize(28, 28))
        self.display_pushButton.setMaximumSize(QtCore.QSize(28, 28))
        self.display_pushButton.setText("")
        self.display_pushButton.setObjectName("display_pushButton")
        self.show_more_layout.addWidget(self.display_pushButton)
        self.horizontalLayout_3.addWidget(self.show_more_horizontalFrame)
        self.sanity_exports_pushButton = QtWidgets.QPushButton(self.exports_manager_header_Frame)
        self.sanity_exports_pushButton.setMinimumSize(QtCore.QSize(120, 28))
        self.sanity_exports_pushButton.setMaximumSize(QtCore.QSize(120, 28))
        self.sanity_exports_pushButton.setCheckable(True)
        self.sanity_exports_pushButton.setChecked(True)
        self.sanity_exports_pushButton.setObjectName("sanity_exports_pushButton")
        self.horizontalLayout_3.addWidget(self.sanity_exports_pushButton)
        self.show_all_exports_pushButton = QtWidgets.QPushButton(self.exports_manager_header_Frame)
        self.show_all_exports_pushButton.setMinimumSize(QtCore.QSize(100, 28))
        self.show_all_exports_pushButton.setMaximumSize(QtCore.QSize(120, 28))
        self.show_all_exports_pushButton.setCheckable(True)
        self.show_all_exports_pushButton.setObjectName("show_all_exports_pushButton")
        self.horizontalLayout_3.addWidget(self.show_all_exports_pushButton)
        self.verticalLayout_2.addWidget(self.exports_manager_header_Frame)
        self.versions_number_label = QtWidgets.QLabel(self.exports_main_frame)
        self.versions_number_label.setObjectName("versions_number_label")
        self.verticalLayout_2.addWidget(self.versions_number_label)
        self.reference_list_listWidget = QtWidgets.QListWidget(self.exports_main_frame)
        self.reference_list_listWidget.setObjectName("reference_list_listWidget")
        self.verticalLayout_2.addWidget(self.reference_list_listWidget)
        self.manual_publish_horizontalFrame = QtWidgets.QFrame(self.exports_main_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.manual_publish_horizontalFrame.sizePolicy().hasHeightForWidth())
        self.manual_publish_horizontalFrame.setSizePolicy(sizePolicy)
        self.manual_publish_horizontalFrame.setObjectName("manual_publish_horizontalFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.manual_publish_horizontalFrame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.add_empty_file_pushButton = QtWidgets.QPushButton(self.manual_publish_horizontalFrame)
        self.add_empty_file_pushButton.setMinimumSize(QtCore.QSize(150, 48))
        self.add_empty_file_pushButton.setMaximumSize(QtCore.QSize(150, 48))
        self.add_empty_file_pushButton.setObjectName("add_empty_file_pushButton")
        self.horizontalLayout.addWidget(self.add_empty_file_pushButton)
        self.verticalLayout_2.addWidget(self.manual_publish_horizontalFrame)
        self.verticalLayout.addWidget(self.exports_main_frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.exports_manager_label.setText(_translate("Form", "Versions manager"))
        self.show_more_pushButton.setText(_translate("Form", "+3"))
        self.show_less_pushButton.setText(_translate("Form", "-3"))
        self.sanity_exports_pushButton.setText(_translate("Form", "Check sanity"))
        self.show_all_exports_pushButton.setText(_translate("Form", "Show all"))
        self.versions_number_label.setText(_translate("Form", "( 0/0 )"))
        self.add_empty_file_pushButton.setText(_translate("Form", "Add empty file"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
