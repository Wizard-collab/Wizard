# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\conta\Documents\script\Wizard\App\ui_files\log_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_log_widget(object):
    def setupUi(self, log_widget):
        log_widget.setObjectName("log_widget")
        log_widget.resize(1108, 855)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(log_widget.sizePolicy().hasHeightForWidth())
        log_widget.setSizePolicy(sizePolicy)
        log_widget.setMinimumSize(QtCore.QSize(0, 0))
        self.verticalLayout = QtWidgets.QVBoxLayout(log_widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_4 = QtWidgets.QFrame(log_widget)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.log_clear_pushButton = QtWidgets.QPushButton(self.frame_4)
        self.log_clear_pushButton.setMinimumSize(QtCore.QSize(28, 28))
        self.log_clear_pushButton.setMaximumSize(QtCore.QSize(28, 28))
        self.log_clear_pushButton.setText("")
        self.log_clear_pushButton.setObjectName("log_clear_pushButton")
        self.horizontalLayout_3.addWidget(self.log_clear_pushButton)
        self.log_report_pushButton = QtWidgets.QPushButton(self.frame_4)
        self.log_report_pushButton.setMinimumSize(QtCore.QSize(28, 28))
        self.log_report_pushButton.setMaximumSize(QtCore.QSize(28, 28))
        self.log_report_pushButton.setText("")
        self.log_report_pushButton.setObjectName("log_report_pushButton")
        self.horizontalLayout_3.addWidget(self.log_report_pushButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addWidget(self.frame_4)
        self.widget = QtWidgets.QWidget(log_widget)
        self.widget.setObjectName("widget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.splitter = QtWidgets.QSplitter(self.widget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setChildrenCollapsible(True)
        self.splitter.setObjectName("splitter")
        self.frame = QtWidgets.QFrame(self.splitter)
        self.frame.setMinimumSize(QtCore.QSize(0, 50))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.log_textEdit = QtWidgets.QTextEdit(self.frame)
        self.log_textEdit.setReadOnly(True)
        self.log_textEdit.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.log_textEdit.setObjectName("log_textEdit")
        self.verticalLayout_2.addWidget(self.log_textEdit)
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_5 = QtWidgets.QFrame(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setMaximumSize(QtCore.QSize(200, 16777215))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setContentsMargins(0, 0, 1, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.frame_5)
        self.label.setMinimumSize(QtCore.QSize(0, 28))
        self.label.setMaximumSize(QtCore.QSize(16777215, 28))
        self.label.setStyleSheet("color:gray")
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.log_widget_scripts_listWidget = QtWidgets.QListWidget(self.frame_5)
        self.log_widget_scripts_listWidget.setMaximumSize(QtCore.QSize(200, 16777215))
        self.log_widget_scripts_listWidget.setObjectName("log_widget_scripts_listWidget")
        self.verticalLayout_4.addWidget(self.log_widget_scripts_listWidget)
        self.horizontalLayout_4.addWidget(self.frame_5)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_2 = QtWidgets.QFrame(self.layoutWidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.log_execute_pushButton = QtWidgets.QPushButton(self.frame_2)
        self.log_execute_pushButton.setMinimumSize(QtCore.QSize(28, 28))
        self.log_execute_pushButton.setMaximumSize(QtCore.QSize(28, 28))
        self.log_execute_pushButton.setText("")
        self.log_execute_pushButton.setObjectName("log_execute_pushButton")
        self.horizontalLayout.addWidget(self.log_execute_pushButton)
        self.log_execute_sub_pushButton = QtWidgets.QPushButton(self.frame_2)
        self.log_execute_sub_pushButton.setMinimumSize(QtCore.QSize(28, 28))
        self.log_execute_sub_pushButton.setMaximumSize(QtCore.QSize(28, 28))
        self.log_execute_sub_pushButton.setText("")
        self.log_execute_sub_pushButton.setObjectName("log_execute_sub_pushButton")
        self.horizontalLayout.addWidget(self.log_execute_sub_pushButton)
        self.log_widget_save_pushButton = QtWidgets.QPushButton(self.frame_2)
        self.log_widget_save_pushButton.setMinimumSize(QtCore.QSize(28, 28))
        self.log_widget_save_pushButton.setMaximumSize(QtCore.QSize(28, 28))
        self.log_widget_save_pushButton.setText("")
        self.log_widget_save_pushButton.setObjectName("log_widget_save_pushButton")
        self.horizontalLayout.addWidget(self.log_widget_save_pushButton)
        self.log_widget_add_script_pushButton = QtWidgets.QPushButton(self.frame_2)
        self.log_widget_add_script_pushButton.setMinimumSize(QtCore.QSize(28, 28))
        self.log_widget_add_script_pushButton.setMaximumSize(QtCore.QSize(28, 28))
        self.log_widget_add_script_pushButton.setText("")
        self.log_widget_add_script_pushButton.setObjectName("log_widget_add_script_pushButton")
        self.horizontalLayout.addWidget(self.log_widget_add_script_pushButton)
        self.log_widget_create_shelf_tool_pushButton = QtWidgets.QPushButton(self.frame_2)
        self.log_widget_create_shelf_tool_pushButton.setMinimumSize(QtCore.QSize(28, 28))
        self.log_widget_create_shelf_tool_pushButton.setMaximumSize(QtCore.QSize(28, 28))
        self.log_widget_create_shelf_tool_pushButton.setText("")
        self.log_widget_create_shelf_tool_pushButton.setObjectName("log_widget_create_shelf_tool_pushButton")
        self.horizontalLayout.addWidget(self.log_widget_create_shelf_tool_pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 3, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_5.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.tabWidget = QtWidgets.QTabWidget(self.frame_3)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.python_0 = QtWidgets.QWidget()
        self.python_0.setObjectName("python_0")
        self.script_editor_layout = QtWidgets.QVBoxLayout(self.python_0)
        self.script_editor_layout.setContentsMargins(0, 0, 0, 0)
        self.script_editor_layout.setSpacing(0)
        self.script_editor_layout.setObjectName("script_editor_layout")
        self.tabWidget.addTab(self.python_0, "")
        self.horizontalLayout_5.addWidget(self.tabWidget)
        self.verticalLayout_5.addWidget(self.frame_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout_6.addWidget(self.splitter)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(log_widget)
        self.tabWidget.setCurrentIndex(0)
        log_widget.destroyed.connect(log_widget.hide)
        QtCore.QMetaObject.connectSlotsByName(log_widget)

    def retranslateUi(self, log_widget):
        _translate = QtCore.QCoreApplication.translate
        log_widget.setWindowTitle(_translate("log_widget", "Form"))
        self.label.setText(_translate("log_widget", "/Documents/Wizard/Scripts/"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.python_0), _translate("log_widget", "Default"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    log_widget = QtWidgets.QWidget()
    ui = Ui_log_widget()
    ui.setupUi(log_widget)
    log_widget.show()
    sys.exit(app.exec_())
