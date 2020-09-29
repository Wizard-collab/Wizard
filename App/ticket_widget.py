from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import pyqtSignal
from gui.ticket_widget import Ui_Form
from wizard.vars import defaults
from wizard.tools import log
from wizard.prefs.main import prefs
from wizard.tools import utility as utils
from wizard.asset.tickets import tickets
from time import strftime
import dialog_close_ticket
from gui import build

logger = log.pipe_log(__name__)

prefs = prefs()

class Main(QtWidgets.QWidget):

    close_signal = pyqtSignal(int)

    def __init__(self, user, adress, date, message, state, id, close_date, comment, close_user, tickets_obj):
        super(Main, self).__init__()
        # Build the ui from ui converted file
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.user = user
        self.adress = adress
        self.date = date
        self.message = message
        self.state = state
        self.id = id
        self.close_date = close_date
        self.comment = comment
        self.tickets_obj = tickets_obj
        self.close_user = close_user

        self.setup_ui()
        self.connect_functions()
        #self.add_icon()

        self.shadow = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(5)
        self.shadow.setColor(QtGui.QColor(0, 0, 0, 180))
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.setGraphicsEffect(self.shadow)

    def add_icon(self, closed = None):
        if closed:
            icon = defaults._ticket_icon_
        else:
            icon = defaults._red_ticket_icon_

        self.ui.ticket_icon_label.setPixmap(
                    QtGui.QPixmap(icon).scaled(24, 24, QtCore.Qt.KeepAspectRatio,
                                                                              QtCore.Qt.SmoothTransformation))

    def connect_functions(self):
        self.ui.change_ticket_state_pushButton.clicked.connect(self.change_state)
        self.ui.delete_ticket_pushButton.clicked.connect(self.delete_ticket)
        if self.user == prefs.user:
            self.ui.delete_ticket_pushButton.setIcon(QtGui.QIcon(defaults._trash_icon_))
        else:
            self.ui.delete_ticket_pushButton.setVisible(0)

    def delete_ticket(self):
        self.tickets_obj.delete_ticket(self.id)
        self.close()

    def change_state(self):
        if self.state == defaults._ticket_open_:
            self.dialog_close_ticket = dialog_close_ticket.Main()
            if build.launch_dialog_as_child(self.dialog_close_ticket):
                self.state = defaults._ticket_close_
                self.tickets_obj.close_ticket(self.id, self.dialog_close_ticket.comment)
                self.close_date = self.tickets_obj.get_ticket_close_date(self.id)
                self.close_signal.emit(1)
        else:
            self.state = defaults._ticket_open_
            self.tickets_obj.open_ticket(self.id)
            self.close_date = self.tickets_obj.get_ticket_close_date(self.id)
        self.setup_ui()

    def setup_ui(self):

        date = strftime("%m/%d/%Y, %H:%M:%S", self.date)

        self.ui.ticket_user_label.setText(self.user)
        self.ui.ticket_adress_label.setText(self.adress)

        self.ui.ticket_date_label.setText(date)
        self.ui.ticket_message_label.setText(self.message)
        self.ui.ticket_state_label.setText(self.state)
        if self.close_date:
            close_date = strftime("%m/%d/%Y, %H:%M:%S", self.close_date)
            self.ui.close_date_label.setText(close_date)
        else:
            self.ui.close_date_label.setText('')


        if self.state == defaults._ticket_open_:
            self.add_icon()
            self.ui.change_ticket_state_pushButton.setText('Close')
        else:
            self.ui.change_ticket_state_pushButton.setText('Open again')
            self.add_icon(1)

        if self.comment:
            self.ui.ticket_comment_label.setVisible(1)
            self.ui.ticket_comment_label.setText(self.comment)
        else:
            self.ui.ticket_comment_label.setVisible(0)
            self.ui.ticket_comment_label.setText('')

        if self.close_user:
            self.ui.ticket_close_user_label.setText('by {}'.format(self.close_user))
        else:
            self.ui.ticket_close_user_label.setText(''.format(self.close_user))

