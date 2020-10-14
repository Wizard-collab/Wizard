from PyQt5 import QtWidgets, QtCore, QtGui
from gui.tickets_widget import Ui_Form
from wizard.vars import defaults
from wizard.tools import log
from wizard.prefs.main import prefs
from wizard.tools import utility as utils
from wizard.asset.tickets import tickets
from wizard.signal import send_signal
import open_ticket_widget
from gui import build
from wizard.signal import send_signal
import wizard.api as api
import ticket_widget

logger = log.pipe_log(__name__)

prefs = prefs()

class Main(QtWidgets.QWidget):

    def __init__(self, user = None):
        super(Main, self).__init__()
        # Build the ui from ui converted file
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.connect_functions()
        self.asset = None
        self.tickets = tickets()
        self.show_only_open = True
        self.show_only_adress_to_me = False
        self.user = user
        if self.user:
            self.ui.ticket_toolbar_frame.setVisible(0)
            self.ui.ticket_adressed_to_me_pushButton.setVisible(0)
            self.ui.only_openned_tickets_pushButton.setStyleSheet('border-radius:14px')

    def connect_functions(self):
        area_scroll_bar = self.ui.tickets_scrollArea.verticalScrollBar()
        area_scroll_bar.rangeChanged.connect(lambda: area_scroll_bar.setValue(area_scroll_bar.maximum()))
        self.ui.open_ticket_pushButton.setIcon(QtGui.QIcon(defaults._open_ticket_icon_))
        self.ui.only_openned_tickets_pushButton.setIcon(QtGui.QIcon(defaults._red_ticket_icon_))
        self.ui.ticket_adressed_to_me_pushButton.setIcon(QtGui.QIcon(defaults._my_tickets_icon_))
        self.ui.only_openned_tickets_pushButton.clicked.connect(self.show_only_open_ticket)
        self.ui.ticket_adressed_to_me_pushButton.clicked.connect(self.show_only_adress_to_me_ticket)
        self.ui.open_ticket_pushButton.clicked.connect(self.open_ticket)

    def show_only_open_ticket(self):
        if self.ui.only_openned_tickets_pushButton.isChecked():
            self.show_only_open = True
        else:
            self.show_only_open = False
        self.refresh_visible()

    def show_only_adress_to_me_ticket(self):
        if self.ui.ticket_adressed_to_me_pushButton.isChecked():
            self.show_only_adress_to_me = True
        else:
            self.show_only_adress_to_me = False
        self.refresh_visible()

    def closeEvent(self, event):
        logger.info('Close tickets list')
        send_signal.refresh_signal()
        # api.scene.refresh_team_ui()
        event.ignore()
        self.hide()

    def refresh_visible(self):
        for i in reversed(range(self.ui.tickets_layout.count())):
            widget = self.ui.tickets_layout.itemAt(i).widget()
            if widget:

                if self.show_only_open and widget.state == defaults._ticket_close_:
                    only_open = 0
                else:
                    only_open = 1

                if self.show_only_adress_to_me and widget.adress != prefs.user:
                    adress_to_me = 0
                else:
                    adress_to_me = 1

            widget.setVisible(only_open*adress_to_me)

    def open_ticket(self):
        self.open_ticket_widget = open_ticket_widget.Main(self.asset)
        build.launch_normal_as_child(self.open_ticket_widget)

    def refresh_all(self, asset = None):
        self.clear_all()
        self.asset = asset
        self.tickets.open()
        if self.asset:
            tickets_ids = self.tickets.get_asset_tickets_ids(self.asset)
        else:
            tickets_ids = self.tickets.get_user_tickets_ids()

        for ticket_id in tickets_ids:
            self.build_ticket(ticket_id)
        self.refresh_visible()

    def clear_all(self):
        for i in reversed(range(self.ui.tickets_layout.count())):
            widget = self.ui.tickets_layout.itemAt(i).widget()
            if widget:
                widget.setParent(None)

    def build_ticket(self, ticket_id):
        user = self.tickets.get_ticket_user(ticket_id)
        date = self.tickets.get_ticket_date(ticket_id)
        message = self.tickets.get_ticket_message(ticket_id)
        state = self.tickets.get_ticket_state(ticket_id)
        close_date = self.tickets.get_ticket_close_date(ticket_id)
        adress = self.tickets.get_ticket_adress(ticket_id)
        comment = self.tickets.get_ticket_comment(ticket_id)
        close_user = self.tickets.get_ticket_close_user(ticket_id)

        new_ticket_widget = ticket_widget.Main(user, adress, date, message, state, ticket_id, close_date, comment, close_user, self.tickets)
        self.ui.tickets_layout.addWidget(new_ticket_widget)
        new_ticket_widget.close_signal.connect(self.refresh_visible)
