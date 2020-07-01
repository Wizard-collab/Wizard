# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
from gui.server_widget import Ui_Form
from wizard.tools import log
from wizard.prefs.main import prefs
import traceback
from gui import log_to_gui
from gui import build
from wizard.chat.server import server
import server_user_item_widget
import dialog_accept

logger = log.server_log()

prefs = prefs()

class Main(QtWidgets.QWidget):

    def __init__(self):
        super(Main, self).__init__()
        # Build the ui from ui converted file
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("Wizard server")

        self.init_log_ui()
        self.init_server()
        if self.server:
            self.setup_widget()
        self.connect_functions()

    def closeEvent(self, event):
        event.ignore()
        self.hide()

    def connect_functions(self):
        self.ui.server_reduce_pushButton.clicked.connect(self.hide)
        self.ui.server_quit_pushButton.clicked.connect(self.quit)

    def quit(self):
        if len(self.server.clients) != 0:
            self.dialog_accept = dialog_accept.Main('Warning', '{} users are connected to this server\nQuit anyway ?'.format(len(self.server.clients)))
            if build.launch_dialog_as_child(self.dialog_accept):
                QtWidgets.QApplication.quit()
        else:
            QtWidgets.QApplication.quit()

    def init_server(self):
        try:
            self.server = server()
            self.server.start()
            self.server.new_client_connection.connect(self.refresh_clients)
            self.refresh_clients()
        except:
            self.server = None
            logger.info("Can't run server")

    def refresh_clients(self):
        for i in reversed(range(self.ui.users_layout.count())):
            self.ui.users_layout.itemAt(i).widget().setParent(None)
        for client in self.server.clients:
            user_name = client[1].user
            addr = client[1].addr
            self.server_user_item_widget = server_user_item_widget.Main(user_name, addr)
            self.ui.users_layout.insertWidget(0, self.server_user_item_widget)
        if len(self.server.clients) > 1:
            plur = 's'
        else:
            plur = ''
        self.ui.server_connexions_label.setText("{} connexion{}".format(len(self.server.clients), plur))

    def setup_widget(self):
        self.ui.server_ip_label.setText('{} - Host - {}'.format(self.server.host_ip, prefs.user))
        self.ui.server_project_label.setText('Project - {}'.format(prefs.project_name))

    def init_log_ui(self):
        try:
            self.widget_handler = log_to_gui.log_widget_viewer(self)
            self.main_handler = log_to_gui.main_ui_log_viewer(self)
            logger.main_logger.addHandler(self.widget_handler)
            self.widget_handler.new_record.connect(self.ui.log_textEdit.append)
        except:
            logger.critical(str(traceback.format_exc()))
