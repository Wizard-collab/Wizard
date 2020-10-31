# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtCore, QtGui
from gui.log_widget import Ui_log_widget
from wizard.tools import log
from wizard.vars import defaults
from wizard.prefs.main import prefs
import traceback
import dialog_report
from gui import build
import script_editor
from wizard.tools import utility as utils

import sys
import os
from io import StringIO
import create_user_script_widget
import ui_subprocess_manager

logger = log.pipe_log(__name__)
prefs = prefs()


class Main(QtWidgets.QWidget):

    def __init__(self):
        super(Main, self).__init__()
        # Build the ui from ui converted file
        self.ui = Ui_log_widget()
        self.ui.setupUi(self)
        self.ui.log_py_plainTextEdit = script_editor.SimplePythonEditor()
        self.ui.log_py_plainTextEdit.setStyleSheet(build.load_stylesheet())
        self.ui.script_editor_layout.addWidget(self.ui.log_py_plainTextEdit)
        self.tabs_dict = dict()
        try:
            self.set_script_cache()
        except:
            logger.critical(str(traceback.format_exc()))
        self.init_buttons()
        self.connect_functions()
        self.refresh_scripts_files_tree()

    def refresh_scripts_files_tree(self):
        self.ui.log_widget_scripts_listWidget.clear()
        self.get_files_list()
        for key in self.files_dic.keys():
            self.ui.log_widget_scripts_listWidget.addItem(key)

    def get_files_list(self):
        folder = defaults._user_custom_scripts_path_
        self.files_dic = dict()
        for file in os.listdir(folder):
            file_name = os.path.splitext(file)[0]
            file_ext = os.path.splitext(file)[-1]
            if file_ext == '.py':
                self.files_dic[file] = os.path.join(folder, file)

    def create_shelf_tool_from_script(self):
        script_data = self.get_script_data()
        self.create_user_script_widget = create_user_script_widget.Main(new_script=script_data)
        build.launch_normal_as_child(self.create_user_script_widget)

    def open_script_from_item(self, item):
        script_name = item.text()
        script_file = self.files_dic[script_name]
        if os.path.isfile(script_file):
            with open(script_file, 'r') as f:
                script_data = f.read()
            #self.ui.log_py_plainTextEdit.setText(script_data)
            self.add_tab(script_name, script_file, script_data)
        else:
            row = self.ui.log_widget_scripts_listWidget.currentRow()
            self.ui.log_widget_scripts_listWidget.takeItem(row)

    def add_tab(self, name, file, data):
        already_exists = 0
        index = None

        if name in self.tabs_dict.keys():
            already_exists = 1
            index = self.tabs_dict[name][defaults._index_key_]

        if not already_exists:
            self.script_editor = script_editor.SimplePythonEditor()
            self.script_editor.setText(data)
            self.script_editor.textChanged.connect(self.tab_text_changed)
            index = self.ui.tabWidget.addTab(self.script_editor, QtGui.QIcon(defaults._python_blue_icon_), name)


            self.tabs_dict[name] = dict()
            self.tabs_dict[name][defaults._file_key_] = file
            self.tabs_dict[name][defaults._widget_key_] = self.script_editor
            self.tabs_dict[name][defaults._index_key_] = index

        if index:
            self.ui.tabWidget.setCurrentIndex(index)

    def get_script_data(self, index=None):
        name = self.get_script_name(index)
        if name != "Default":
            
            full_path = self.tabs_dict[name][defaults._file_key_]
            editor_widget = self.tabs_dict[name][defaults._widget_key_]
            index = self.tabs_dict[name][defaults._index_key_]
            script_data = editor_widget.text().decode('utf-8')
        else:
            script_data = self.ui.log_py_plainTextEdit.text().decode('utf-8')
        return script_data

    def save_script(self):
        name = self.get_script_name()
        if name != "Default":
            
            full_path = self.tabs_dict[name][defaults._file_key_]
            editor_widget = self.tabs_dict[name][defaults._widget_key_]
            index = self.tabs_dict[name][defaults._index_key_]
            script_data = editor_widget.text().decode('utf-8')
            with open(full_path, 'w') as f:
                f.write(script_data)
            tab_name = self.ui.tabWidget.tabText(index)
            if tab_name.endswith(' *'):
                tab_name = tab_name[:-2]
                self.ui.tabWidget.setTabText(index, tab_name)

        self.refresh_scripts_files_tree()

    def close_tab(self, index):

        name = self.get_script_name(index)
        if name != 'Default' and index != 0:
            self.ui.tabWidget.removeTab(index)
            if name in self.tabs_dict.keys():
                del self.tabs_dict[name]

        for tab_index in range(1, self.ui.tabWidget.count()):
            name = self.get_script_name(tab_index)
            if name != "Default":
                if name in self.tabs_dict.keys():
                    self.tabs_dict[name][defaults._index_key_] = tab_index

    def tab_text_changed(self):
        current_tab_name = self.get_script_name()
        if not current_tab_name.endswith(" *"):
            current_tab_name+=" *"
            self.ui.tabWidget.setTabText(self.ui.tabWidget.currentIndex(), current_tab_name)

    def get_script_name(self, index=None):
        if not index:
            index = self.ui.tabWidget.currentIndex()
        current_tab_name = self.ui.tabWidget.tabText(index)
        if current_tab_name.endswith(' *'):
            current_tab_name = current_tab_name[:-2]
        return current_tab_name

    def set_script_cache(self):
        script_cache = prefs.script_cache
        self.ui.log_py_plainTextEdit.setText(script_cache)

    def connect_functions(self):
        self.ui.log_clear_pushButton.clicked.connect(self.ui.log_textEdit.clear)
        self.ui.log_report_pushButton.clicked.connect(self.launch_report_dialog)
        self.ui.log_widget_save_pushButton.clicked.connect(self.save_script)
        execute_shortcut = QtWidgets.QShortcut(QtGui.QKeySequence('Ctrl+Return'), self)
        execute_shortcut.activated.connect(self.run_py)
        save_shortcut = QtWidgets.QShortcut(QtGui.QKeySequence('Ctrl+S'), self)
        save_shortcut.activated.connect(self.save_script)
        self.ui.log_execute_pushButton.clicked.connect(lambda: self.run_py(all=1))
        self.ui.log_py_plainTextEdit.textChanged.connect(self.save_cache)
        self.ui.tabWidget.tabCloseRequested.connect(self.close_tab)
        self.ui.log_widget_scripts_listWidget.itemDoubleClicked.connect(self.open_script_from_item)
        self.ui.log_widget_create_shelf_tool_pushButton.clicked.connect(self.create_shelf_tool_from_script)
        self.ui.log_execute_sub_pushButton.clicked.connect(self.execute_as_subprocess)

    def closeEvent(self, event):
        event.ignore()
        self.hide()

    def init_buttons(self):
        self.ui.log_report_pushButton.setIcon(QtGui.QIcon(defaults._email_flat_icon_))
        self.ui.log_clear_pushButton.setIcon(QtGui.QIcon(defaults._clear_icon_))
        self.ui.log_execute_pushButton.setIcon(QtGui.QIcon(defaults._execute_icon_))
        self.ui.log_widget_save_pushButton.setIcon(QtGui.QIcon(defaults._save_icon_))
        self.ui.log_widget_add_script_pushButton.setIcon(QtGui.QIcon(defaults._add_icon_))
        self.ui.log_execute_sub_pushButton.setIcon(QtGui.QIcon(defaults._execute_sub_icon_))
        self.ui.tabWidget.setTabIcon(0, QtGui.QIcon(defaults._python_blue_icon_))  # <---
        self.ui.log_report_pushButton.setIconSize(QtCore.QSize(22, 22))
        self.ui.log_clear_pushButton.setIconSize(QtCore.QSize(15, 15))
        self.ui.log_widget_save_pushButton.setIconSize(QtCore.QSize(13, 13))
        self.ui.log_execute_pushButton.setIconSize(QtCore.QSize(13, 13))
        self.ui.tabWidget.setIconSize(QtCore.QSize(18, 18))

    def launch_report_dialog(self):
        try:
            error = self.ui.log_textEdit.toHtml()
            self.dialog_report = dialog_report.Main(error)
            build.launch_dialog_as_child(self.dialog_report)
        except:
            logger.error(str(traceback.format_exc()))

    def save_cache(self):
        script_cache = self.get_code()
        prefs.set_script_cache(script_cache)

    def get_code(self):
        name = self.get_script_name()
        if name != "Default":
            full_path = self.tabs_dict[name][defaults._file_key_]
            editor_widget = self.tabs_dict[name][defaults._widget_key_]
            index = self.tabs_dict[name][defaults._index_key_]
            script_data = editor_widget.text().decode('utf-8')
        else:
            script_data = self.ui.log_py_plainTextEdit.text()
            script_data = script_data.decode('utf-8')
        return script_data

    def execute_as_subprocess(self):

        file = utils.temp_file_from_command(self.get_code())
        env = os.environ.copy()
        self.ui_subprocess_manager = ui_subprocess_manager.Main(f"python {file}", env, cwd=os.path.abspath(''))
        build.launch_normal_as_child(self.ui_subprocess_manager, minimized = 0)

    def run_py(self, all=None):
        py_script = self.get_code()
        if py_script != '' and py_script:
            try:
                # create file-like string to capture output
                codeOut = StringIO()
                # capture output and errors
                sys.stdout = codeOut

                exec(py_script)

                # restore stdout and stderr
                sys.stdout = sys.__stdout__
                s = codeOut.getvalue()
                if str(s).rstrip() != '' and s:
                    logger.info(str(s).rstrip())
                codeOut.close()

            except:
                logger.error(str(traceback.format_exc()))
