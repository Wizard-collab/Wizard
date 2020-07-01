from PyQt5 import QtWidgets, QtGui

from gui.export_asset_widget import Ui_Form
from wizard.vars import defaults
from wizard.tools import log
from wizard.tools import utility as utils

logger = log.pipe_log()


class Main(QtWidgets.QWidget):

    def __init__(self, asset):
        super(Main, self).__init__()
        # Build the ui from ui converted file
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.asset = asset
        self.string_asset = utils.asset_to_string(asset)
        self.widgets_list = []
        self.init_ui()
        self.connect_functions()
        self.hidden = 0

    def init_ui(self):
        self.ui.export_asset_widget_label.setText(self.asset.export_asset)
        self.ui.export_asset_widget_pushButton.setIcon(QtGui.QIcon(defaults._folder_icon_))

    def connect_functions(self):
        self.ui.export_asset_widget_pushButton.clicked.connect(self.hide)

    def hide(self):
        for widget in self.widgets_list:
            widget.setVisible(self.hidden)
        self.hidden = 1 - self.hidden

    def closeEvent(self, event):
        event.ignore()
        self.hide()
