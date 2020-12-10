# coding: utf8

# Import PyQt6 libraries
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QFileDialog

from wizard.tools import utility as utils
utils.init_wizard_env()

from gui.renamer import Ui_Form
from gui import build
from wizard.tools import log
from wizard.vars import defaults

from wizard.tools import rename
import dialog_accept

import sys
import os

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
        self.ui.renamer_undo_pushButton.setIcon(QtGui.QIcon(defaults._missing_file_export_list_icon_))
        self.ui.renamer_source_listWidget.setStyleSheet('''QListWidget::item{color:#99ff7a;}
                                                        QListWidget::item:selected{color:#99ff7a;}
                                                        ''')
        self.ui.renamer_destination_listWidget.setStyleSheet('''QListWidget::item{color:orange;}
                                                        QListWidget::item:selected{color:orange;}
                                                        ''')
        self.ui.renamer_undo_pushButton.setEnabled(0)

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
        self.ui.renamer_first_splitter_comboBox.currentIndexChanged.connect(self.modify_file_name)
        self.ui.renamer_second_splitter_comboBox.currentIndexChanged.connect(self.modify_file_name)
        self.ui.renamer_apply_pushButton.clicked.connect(self.apply)
        self.ui.renamer_show_folder_pushButton.clicked.connect(self.show_folder)
        self.ui.renamer_sort_pushButton.clicked.connect(self.sort_list)
        self.ui.renamer_invert_sort_pushButton.clicked.connect(lambda: self.sort_list(1))
        self.ui.renamer_undo_pushButton.clicked.connect(self.undo)
        self.ui.renamer_insert_lineEdit.textChanged.connect(self.modify_file_name)
        self.ui.renamer_insert_at_spinBox.valueChanged.connect(self.modify_file_name)

    def show_folder(self):
        if self.renamer.folder:
            if os.path.isdir(self.renamer.folder):
                os.startfile(self.renamer.folder)

    def apply(self):
        self.dialog_accept = dialog_accept.Main("Are you sure ?", "Please confirm that you want to rename these files", defaults._warning_)
        if build.launch_dialog_as_child(self.dialog_accept):
            self.renamer.apply()
            self.clear_all()
            self.refresh_all()

    def undo(self):
        self.dialog_accept = dialog_accept.Main("Are you sure ?", "Do you want to undo ?", defaults._warning_)
        if build.launch_dialog_as_child(self.dialog_accept):
            self.renamer.undo()
            self.clear_all()
            self.refresh_all()

    def sort_list(self, invert=0):

        if self.ui.renamer_sortby_comboBox.currentText() == 'Name':
            self.renamer.sort_files_list(invert)
        else:
            self.renamer.sort_by_time(invert)

        self.update_source_list()
        self.modify_file_name()
        self.update_destination_list()

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
        self.ui.renamer_insert_lineEdit.clear()
        self.ui.renamer_insert_at_spinBox.setValue(0)

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
        if self.renamer.undo_source == []:
            self.ui.renamer_undo_pushButton.setEnabled(0)
        else:
            self.ui.renamer_undo_pushButton.setEnabled(1)

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
        first_splitter = self.ui.renamer_first_splitter_comboBox.currentText()
        second_splitter = self.ui.renamer_second_splitter_comboBox.currentText()
        insert = self.ui.renamer_insert_lineEdit.text()
        insert_at = self.ui.renamer_insert_at_spinBox.value()
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
        self.renamer.first_splitter = first_splitter
        self.renamer.second_splitter = second_splitter
        self.renamer.insert = insert
        self.renamer.insert_at = insert_at
        self.renamer.modify_file_name()
        self.update_destination_list()

       
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(defaults._wizard_ico_))
    build.launch_normal(Main())