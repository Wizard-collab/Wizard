from PyQt5 import QtWidgets
from PyQt5.QtCore import QPoint

from gui.add_variant_dialog import Ui_Dialog


class Main(QtWidgets.QDialog):

    def __init__(self):
        super(Main, self).__init__()
        # Build the ui from ui converted file
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.connect_functions()

    def add_variant(self):
        variant_name = self.ui.variant_name_lineEdit.text()
        self.variant_name = variant_name
        self.accept()

    def connect_functions(self):
        self.ui.create_variant_pushButton.clicked.connect(self.add_variant)
