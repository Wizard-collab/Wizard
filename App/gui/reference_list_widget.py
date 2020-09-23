# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\conta\Documents\script\Wizard\App\work\ui_files\reference_list_widget.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(934, 668)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.reference_list_frame = QtWidgets.QFrame(Form)
        self.reference_list_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.reference_list_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.reference_list_frame.setObjectName("reference_list_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.reference_list_frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.reference_list_label = QtWidgets.QLabel(self.reference_list_frame)
        self.reference_list_label.setObjectName("reference_list_label")
        self.verticalLayout.addWidget(self.reference_list_label)
        self.reference_list_listWidget = QtWidgets.QListWidget(self.reference_list_frame)
        self.reference_list_listWidget.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.reference_list_listWidget.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.reference_list_listWidget.setSelectionMode(QtWidgets.QAbstractItemView.ContiguousSelection)
        self.reference_list_listWidget.setObjectName("reference_list_listWidget")
        self.verticalLayout.addWidget(self.reference_list_listWidget)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.references_number_frame = QtWidgets.QFrame(self.reference_list_frame)
        self.references_number_frame.setMinimumSize(QtCore.QSize(20, 0))
        self.references_number_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.references_number_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.references_number_frame.setObjectName("references_number_frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.references_number_frame)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.references_number_label = QtWidgets.QLabel(self.references_number_frame)
        self.references_number_label.setObjectName("references_number_label")
        self.horizontalLayout_5.addWidget(self.references_number_label)
        self.horizontalLayout_4.addWidget(self.references_number_frame)
        self.node_editor_buttons_frame = QtWidgets.QFrame(self.reference_list_frame)
        self.node_editor_buttons_frame.setMinimumSize(QtCore.QSize(0, 20))
        self.node_editor_buttons_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.node_editor_buttons_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.node_editor_buttons_frame.setObjectName("node_editor_buttons_frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.node_editor_buttons_frame)
        self.horizontalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.update_all_pushButton = QtWidgets.QPushButton(self.node_editor_buttons_frame)
        self.update_all_pushButton.setMinimumSize(QtCore.QSize(28, 28))
        self.update_all_pushButton.setMaximumSize(QtCore.QSize(28, 28))
        self.update_all_pushButton.setText("")
        self.update_all_pushButton.setObjectName("update_all_pushButton")
        self.horizontalLayout_3.addWidget(self.update_all_pushButton)
        self.trash_pushButton = QtWidgets.QPushButton(self.node_editor_buttons_frame)
        self.trash_pushButton.setMinimumSize(QtCore.QSize(28, 28))
        self.trash_pushButton.setMaximumSize(QtCore.QSize(28, 28))
        self.trash_pushButton.setText("")
        self.trash_pushButton.setObjectName("trash_pushButton")
        self.horizontalLayout_3.addWidget(self.trash_pushButton)
        self.horizontalLayout_4.addWidget(self.node_editor_buttons_frame)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.addWidget(self.reference_list_frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.reference_list_label.setText(_translate("Form", "Reference list"))
        self.references_number_label.setText(_translate("Form", "0 references"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
