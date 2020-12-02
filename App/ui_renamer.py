# coding: utf8

# Import PyQt6 libraries
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QFileDialog

from gui.renamer import Ui_Form
from gui import build
from wizard.tools import log
from wizard.vars import defaults

from wizard.tools import rename
import dialog_accept

import sys

# Init main logger
logger = log.pipe_log(__name__)

class Main(QtWidgets.QWidget):

    def __init__(self, folder=None):
        super(Main, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.renamer = rename.renamer()
        self.update_source_list()
        self.modify_file_name()
        self.setup_ui()
        self.connect_functions()

    def setup_ui(self):
        self.ui.renamer_folder_pushButton.setIcon(QtGui.QIcon(defaults._folder_icon_))
        self.ui.renamer_apply_pushButton.setIcon(QtGui.QIcon(defaults._export_list_icon_))

    def open_folder(self):
        site_path = QtWidgets.QFileDialog.getExistingDirectory(None, 'Choose a destination folder',
                                                         'c://', QtWidgets.QFileDialog.ShowDirsOnly)
        self.ui.renamer_folder_lineEdit.setText(site_path)

    def update_source_list(self):
        self.ui.renamer_source_listWidget.clear()
        for file in self.renamer.files_list:
            self.ui.renamer_source_listWidget.addItem(file)

    def update_destination_list(self):
        self.ui.renamer_destination_listWidget.clear()
        for file in self.renamer.modified_list:
            self.ui.renamer_destination_listWidget.addItem(file)

    def connect_functions(self):
        self.ui.renamer_prefix_lineEdit.textChanged.connect(self.modify_file_name)
        self.ui.renamer_suffix_lineEdit.textChanged.connect(self.modify_file_name)
        self.ui.renamer_override_lineEdit.textChanged.connect(self.modify_file_name)
        self.ui.renamer_extension_lineEdit.textChanged.connect(self.modify_file_name)
        self.ui.renamer_find_lineEdit.textChanged.connect(self.modify_file_name)
        self.ui.renamer_replace_lineEdit.textChanged.connect(self.modify_file_name)
        self.ui.renamer_start_at_spinBox.valueChanged.connect(self.modify_file_name)
        self.ui.renamer_start_crop_spinBox.valueChanged.connect(self.modify_file_name)
        self.ui.renamer_end_crop_spinBox.valueChanged.connect(self.modify_file_name)
        self.ui.renamer_selection_only_pushButton.clicked.connect(self.apply_selection)
        self.ui.renamer_folder_pushButton.clicked.connect(self.open_folder)
        self.ui.renamer_refresh_pushButton.clicked.connect(self.refresh_all)
        self.ui.renamer_folder_lineEdit.textChanged.connect(self.refresh_all)
        self.ui.renamer_uppercase_checkBox.stateChanged.connect(self.modify_file_name)
        self.ui.renamer_lowercase_checkBox.stateChanged.connect(self.modify_file_name)
        self.ui.renamer_apply_pushButton.clicked.connect(self.apply)

    def apply(self):
        self.dialog_accept = dialog_accept.Main("Are you sure ?", "Please confirm that you want to rename these files")
        if build.launch_dialog_as_child(self.dialog_accept):
            self.renamer.apply()
            self.clear_all()
            self.refresh_all()

    def clear_all(self):
        self.ui.renamer_prefix_lineEdit.clear()
        self.ui.renamer_suffix_lineEdit.clear()
        self.ui.renamer_override_lineEdit.clear()
        self.ui.renamer_extension_lineEdit.clear()
        self.ui.renamer_find_lineEdit.clear()
        self.ui.renamer_replace_lineEdit.clear()
        self.ui.renamer_start_at_spinBox.setValue(0)
        self.ui.renamer_start_crop_spinBox.setValue(0)
        self.ui.renamer_end_crop_spinBox.setValue(0)
        self.ui.renamer_uppercase_checkBox.setCheckState(0)
        self.ui.renamer_lowercase_checkBox.setCheckState(0)

    def apply_selection(self):
        files_list = []
        items_list = self.ui.renamer_source_listWidget.selectedItems()
        for item in items_list:
            files_list.append(item.text())
        self.renamer.files_list = files_list
        self.update_source_list()
        self.modify_file_name()
        self.update_destination_list()

    def refresh_all(self):
        path = self.ui.renamer_folder_lineEdit.text()
        self.renamer.set_folder(path)
        self.update_source_list()
        self.modify_file_name()

    def modify_file_name(self):
        prefix = self.ui.renamer_prefix_lineEdit.text()
        suffix = self.ui.renamer_suffix_lineEdit.text()
        override = self.ui.renamer_override_lineEdit.text()
        override_extension = self.ui.renamer_extension_lineEdit.text()
        find = self.ui.renamer_find_lineEdit.text()
        replace = self.ui.renamer_replace_lineEdit.text()
        start_at = self.ui.renamer_start_at_spinBox.value()
        start_crop = self.ui.renamer_start_crop_spinBox.value()
        end_crop = self.ui.renamer_end_crop_spinBox.value()
        uppercase = self.ui.renamer_uppercase_checkBox.isChecked()
        lowercase = self.ui.renamer_lowercase_checkBox.isChecked()
        self.renamer.prefix = prefix
        self.renamer.suffix = suffix
        self.renamer.override = override
        self.renamer.override_extension = override_extension
        self.renamer.find_and_replace = [find, replace]
        self.renamer.start_at = start_at
        self.renamer.uppercase = uppercase
        self.renamer.lowercase = lowercase
        self.renamer.start_crop = start_crop
        self.renamer.end_crop = end_crop
        self.renamer.modify_file_name()
        self.update_destination_list()

       
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(defaults._wizard_ico_))
    build.launch_normal(Main())