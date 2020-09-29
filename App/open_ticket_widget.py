from PyQt5 import QtWidgets, QtCore, QtGui
from gui.open_ticket_widget import Ui_Form
from wizard.vars import defaults
from wizard.tools import log
from wizard.prefs.main import prefs
from wizard.tools import utility as utils
from wizard.asset.tickets import tickets

import ticket_widget

logger = log.pipe_log(__name__)

prefs = prefs()

class Main(QtWidgets.QWidget):

    def __init__(self, asset):
        super(Main, self).__init__()
        # Build the ui from ui converted file
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.connect_functions()
        self.asset = asset
        self.setup_ui()
        self.fill_users_combo()

    def connect_functions(self):
        self.ui.open_ticket_widget_open_pushButton.clicked.connect(self.open_ticket)
        self.ui.open_ticket_widget_cancel_pushButton.clicked.connect(self.close)

    def fill_users_combo(self):
        users = prefs.site.users
        for user in users:
            self.ui.ticket_adress_comboBox.addItem(user)

    def setup_ui(self):
        self.ui.ticket_icon_label.setPixmap(
                    QtGui.QPixmap(defaults._red_ticket_icon_).scaled(24, 24, QtCore.Qt.KeepAspectRatio,
                                                                              QtCore.Qt.SmoothTransformation))
        string_asset = utils.variant_asset_to_string(self.asset)
        self.ui.open_ticket_asset_label.setText(string_asset.replace('.', ' - '))

    def closeEvent(self, event):
        event.ignore()
        self.hide()

    def open_ticket(self):
        message = self.ui.open_ticket_plainTextEdit.toPlainText()
        adress = self.ui.ticket_adress_comboBox.currentText()
        if message and message != '':
            tickets().create_ticket(self.asset, message, adress)
            self.close()
        else:
            logger.info("Please enter some retakes needs or bug informations")