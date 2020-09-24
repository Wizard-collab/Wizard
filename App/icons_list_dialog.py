from PyQt5 import QtWidgets, QtCore, QtGui
from gui.icons_list_dialog import Ui_Dialog
from wizard.vars import defaults
from wizard.tools import log
from wizard.prefs.main import prefs
import traceback
import os

logger = log.pipe_log()

prefs = prefs()

class Main(QtWidgets.QDialog):

    def __init__(self):
        super(Main, self).__init__()
        # Build the ui from ui converted file
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.icon = None
        self.ui.icons_list_listWidget.setIconSize(QtCore.QSize(30, 30))
        self.connect_functions()
        self.init_list()

    def init_list(self):
        icons_list = os.listdir(defaults._icon_path_)
        for icon in icons_list:
            item = QtWidgets.QListWidgetItem()
            item.setIcon(QtGui.QIcon(defaults._icon_path_+icon))
            item.setSizeHint(QtCore.QSize(36,36))
            item.wizard_icon = icon
            self.ui.icons_list_listWidget.addItem(item)

    def connect_functions(self):
        self.ui.icon_apply_pushButton.clicked.connect(self.select_icon)

    def select_icon(self):
        selected_item = self.ui.icons_list_listWidget.selectedItems()[0]
        self.icon = selected_item.wizard_icon
        for x in range(self.ui.icons_list_listWidget.count()-1):
            item = self.ui.icons_list_listWidget.item(x)
            del item
        self.accept()