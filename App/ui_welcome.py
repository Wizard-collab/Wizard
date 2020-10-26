from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication
from gui.welcome import Ui_Dialog
from wizard.vars import defaults
import create_user_widget
import create_project_widget
import server_info_widget
from wizard.prefs.main import prefs
from wizard.chat.client import test_conn_once
import os

prefs = prefs()

class Main(QtWidgets.QDialog):

    def __init__(self):
        super(Main, self).__init__()
        # Build the ui from ui converted file
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.shadow = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(8)
        self.shadow.setColor(QtGui.QColor(0, 0, 0, 180))
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.setGraphicsEffect(self.shadow)
        self.create_user_widget = create_user_widget.Main()
        self.create_project_widget = create_project_widget.Main()
        self.server_info_widget = server_info_widget.Main()
        self.ui.welcome_main_widget_layout.addWidget(self.server_info_widget)
        self.server_info_widget.hide()
        self.server_info_widget.ui.ok_pushButton.clicked.connect(self.reject)
        self.ui.welcome_main_widget_layout.addWidget(self.create_project_widget)
        self.create_project_widget.project_openned.connect(self.add_server_info_widget)
        self.create_project_widget.hide()
        self.ui.welcome_main_widget_layout.addWidget(self.create_user_widget)
        self.create_user_widget.user_created.connect(self.add_project_widget)
        self.create_user_widget.hide()
        self.add_logos()
        self.need = 1
        self.init_prefs()

    def init_prefs(self):
        if not prefs.user:
            self.add_user_widget()
        else:
            if not prefs.project_name:
                self.add_project_widget()
            else:
                self.add_server_info_widget()

    def add_logos(self):
        self.ui.welcome_left_pushButton.setIcon(QtGui.QIcon(defaults._previous_icon_))
        self.ui.welcome_left_pushButton.hide()
        self.ui.welcome_right_pushButton.setIcon(QtGui.QIcon(defaults._next_icon_))
        self.ui.welcome_right_pushButton.hide()
        self.ui.welcome_image_label.setPixmap(
            QtGui.QPixmap(defaults._welcome_image_).scaled(200, 381, QtCore.Qt.KeepAspectRatio,
                                                           QtCore.Qt.SmoothTransformation))
        self.ui.welcome_wizard_logo_label.setPixmap(
            QtGui.QPixmap(defaults._wizard_icon_).scaled(45, 45, QtCore.Qt.KeepAspectRatio,
                                                                 QtCore.Qt.SmoothTransformation))
        self.ui.close_pushButton.setIcon(QtGui.QIcon(defaults._close_popup_icon_))

        self.ui.welcome_version_label.setText(defaults._wizard_version_)

    def add_project_widget(self):
        QApplication.processEvents()
        self.clear_layout()
        self.create_project_widget.show()
        QApplication.processEvents()

    def add_user_widget(self):
        QApplication.processEvents()
        self.clear_layout()
        self.create_user_widget.show()
        QApplication.processEvents()

    def add_server_info_widget(self):
        if not test_conn_once():
            '''
            QApplication.processEvents()
            self.clear_layout()
            self.server_info_widget.show()
            QApplication.processEvents()
            '''
            self.launch_server()
            self.need = 0
            self.accept()
        else:
            self.need = 0
            self.accept()

    def clear_layout(self):
        for i in reversed(range(self.ui.welcome_main_widget_layout.count())):
            self.ui.welcome_main_widget_layout.itemAt(i).widget().hide()

    def launch_server(self):
        pass
        #os.startfile('wizard server.exe')