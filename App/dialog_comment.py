from PyQt5 import QtWidgets, QtCore, QtGui

from gui.comment_dialog import Ui_Dialog
from wizard.vars import defaults
from wizard.tools import log
from wizard.tools import utility as utils
from wizard.prefs.main import prefs

logger = log.pipe_log(__name__)

prefs = prefs()

class Main(QtWidgets.QDialog):

    def __init__(self, asset, is_export = 1, playblast_version = None):
        super(Main, self).__init__()
        # Build the ui from ui converted file
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.asset = asset
        self.is_export = is_export
        self.playblast_version = playblast_version
        self.ui.comment_asset_label.setText(utils.asset_to_string(self.asset))
        self.ui.comment_dialog_pushButton.setIcon(QtGui.QIcon(defaults._comment_icon_))
        self.connect_functions()

    def connect_functions(self):
        self.ui.comment_dialog_pushButton.clicked.connect(self.submit)

    def submit(self):
        self.comment = self.ui.comment_dialog_plainTextEdit.toPlainText()
        if self.is_export:
            prefs.asset(self.asset).export.set_version_comment(self.comment)
        elif self.playblast_version:
            prefs.asset(self.asset).playblast.set_version_comment(self.comment, self.playblast_version)
        else:
            prefs.asset(self.asset).software.set_version_comment(self.comment)

        self.accept()

    def closeEvent(self, event):
        event.ignore()
        self.hide()
