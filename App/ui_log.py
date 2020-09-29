from PyQt5 import QtWidgets, QtCore, QtGui

from gui.log import Ui_log
from gui import build
from wizard.vars import defaults
from wizard.tools import log
import traceback
import dialog_report

logger = log.pipe_log(__name__)


class Main(QtWidgets.QWidget):

    def __init__(self, parent):
        super(Main, self).__init__()
        # Build the ui from ui converted file
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_log()
        self.ui.setupUi(self)
        self.connect_scrollBar()
        self.init_report_button()

    def init_report_button(self):
        self.ui.report_error_pushButton.setIcon(QtGui.QIcon(defaults._email_icon_))
        self.ui.report_error_pushButton.setIconSize(QtCore.QSize(38, 38))

    def launch_report_dialog(self):
        try:
            error = self.ui.log_textEdit.toPlainText()
            self.dialog_report = dialog_report.Main(error)
            build.launch_dialog_as_child(self.dialog_report)
        except:
            logger.error(str(traceback.format_exc()))

    def connect_scrollBar(self):
        # self.ui.log_textEdit.verticalScrollBar().setValue(self.ui.log_textEdit.verticalScrollBar().maximum())
        scroll_bar = self.ui.log_textEdit.verticalScrollBar()
        scroll_bar.rangeChanged.connect(lambda: scroll_bar.setValue(scroll_bar.maximum()))
        close_shortCut = QtWidgets.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_F1), self)
        close_shortCut.activated.connect(self.close)
        self.ui.report_error_pushButton.clicked.connect(self.launch_report_dialog)
