# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\conta\Documents\script\Wizard\App\work\ui_files\tickets_widget.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(472, 559)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.exports_main_frame = QtWidgets.QFrame(Form)
        self.exports_main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.exports_main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.exports_main_frame.setObjectName("exports_main_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.exports_main_frame)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(7)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.only_openned_tickets_pushButton = QtWidgets.QPushButton(self.exports_main_frame)
        self.only_openned_tickets_pushButton.setMinimumSize(QtCore.QSize(140, 28))
        self.only_openned_tickets_pushButton.setMaximumSize(QtCore.QSize(200, 16777215))
        self.only_openned_tickets_pushButton.setCheckable(True)
        self.only_openned_tickets_pushButton.setChecked(True)
        self.only_openned_tickets_pushButton.setObjectName("only_openned_tickets_pushButton")
        self.horizontalLayout_3.addWidget(self.only_openned_tickets_pushButton)
        self.ticket_adressed_to_me_pushButton = QtWidgets.QPushButton(self.exports_main_frame)
        self.ticket_adressed_to_me_pushButton.setMinimumSize(QtCore.QSize(120, 28))
        self.ticket_adressed_to_me_pushButton.setCheckable(True)
        self.ticket_adressed_to_me_pushButton.setObjectName("ticket_adressed_to_me_pushButton")
        self.horizontalLayout_3.addWidget(self.ticket_adressed_to_me_pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.tickets_scrollArea = QtWidgets.QScrollArea(self.exports_main_frame)
        self.tickets_scrollArea.setWidgetResizable(True)
        self.tickets_scrollArea.setObjectName("tickets_scrollArea")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 446, 439))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tickets_layout = QtWidgets.QVBoxLayout()
        self.tickets_layout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.tickets_layout.setSpacing(1)
        self.tickets_layout.setObjectName("tickets_layout")
        self.verticalLayout_3.addLayout(self.tickets_layout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.tickets_scrollArea.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout_2.addWidget(self.tickets_scrollArea)
        self.ticket_toolbar_frame = QtWidgets.QFrame(self.exports_main_frame)
        self.ticket_toolbar_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.ticket_toolbar_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.ticket_toolbar_frame.setObjectName("ticket_toolbar_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.ticket_toolbar_frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.open_ticket_pushButton = QtWidgets.QPushButton(self.ticket_toolbar_frame)
        self.open_ticket_pushButton.setMinimumSize(QtCore.QSize(160, 48))
        self.open_ticket_pushButton.setMaximumSize(QtCore.QSize(160, 48))
        self.open_ticket_pushButton.setObjectName("open_ticket_pushButton")
        self.horizontalLayout_2.addWidget(self.open_ticket_pushButton)
        self.verticalLayout_2.addWidget(self.ticket_toolbar_frame)
        self.verticalLayout.addWidget(self.exports_main_frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.only_openned_tickets_pushButton.setText(_translate("Form", "openned tickets"))
        self.ticket_adressed_to_me_pushButton.setText(_translate("Form", "my tickets"))
        self.open_ticket_pushButton.setText(_translate("Form", "Open new ticket"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
