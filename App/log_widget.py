# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtCore, QtGui
from gui.log_widget import Ui_log_widget
from wizard.tools import log
from wizard.vars import defaults
from wizard.prefs.main import prefs
import traceback
import dialog_report
from gui import build

import sys
from io import StringIO

logger = log.pipe_log()
prefs = prefs()


class Main(QtWidgets.QWidget):

    def __init__(self):
        super(Main, self).__init__()
        # Build the ui from ui converted file
        self.ui = Ui_log_widget()
        self.ui.setupUi(self)
        self.ui.log_py_plainTextEdit = script_editor_plainTextEdit()
        self.ui.horizontalLayout_py_script.addWidget(self.ui.log_py_plainTextEdit)
        self.init_buttons()
        self.connect_functions()

    def connect_functions(self):
        self.ui.log_clear_pushButton.clicked.connect(self.ui.log_textEdit.clear)
        self.ui.log_report_pushButton.clicked.connect(self.launch_report_dialog)
        execute_shortcut = QtWidgets.QShortcut(QtGui.QKeySequence('Ctrl+Return'), self)
        execute_shortcut.activated.connect(self.run_py)
        self.ui.log_execute_pushButton.clicked.connect(lambda: self.run_py(all=1))
        self.ui.log_py_plainTextEdit.textChanged.connect(self.update_lines)
        self.py_scroll = self.ui.log_py_plainTextEdit.verticalScrollBar()
        self.lines_scroll = self.ui.log_lines_plainTextEdit.verticalScrollBar()
        self.py_scroll.valueChanged.connect(self.update_lines_scroll)
        self.py_scroll.rangeChanged.connect(self.update_lines_scroll)
        self.ui.log_py_plainTextEdit.textChanged.connect(self.update_lines_scroll)

    def closeEvent(self, event):
        event.ignore()
        self.hide()

    def init_buttons(self):
        self.ui.log_report_pushButton.setIcon(QtGui.QIcon(defaults._email_flat_icon_))
        self.ui.log_clear_pushButton.setIcon(QtGui.QIcon(defaults._clear_icon_))
        self.ui.log_execute_pushButton.setIcon(QtGui.QIcon(defaults._execute_icon_))
        self.ui.log_report_pushButton.setIconSize(QtCore.QSize(22, 22))
        self.ui.log_clear_pushButton.setIconSize(QtCore.QSize(15, 15))
        self.ui.log_execute_pushButton.setIconSize(QtCore.QSize(13, 13))

    def update_lines_scroll(self):
        self.lines_scroll.setValue(self.py_scroll.value())

    def update_lines(self):
        self.ui.log_lines_plainTextEdit.clear()
        lines = self.ui.log_py_plainTextEdit.blockCount()
        text = '1'
        for line in range(2, lines + 1):
            text += '\n' + str(line)
        self.ui.log_lines_plainTextEdit.setPlainText(text)

    def launch_report_dialog(self):
        try:
            error = self.ui.log_textEdit.toHtml()
            self.dialog_report = dialog_report.Main(error)
            build.launch_dialog_as_child(self.dialog_report)
        except:
            logger.error(str(traceback.format_exc()))

    def run_py(self, all=None):
        if all:
            py_script = self.ui.log_py_plainTextEdit.toPlainText()
        else:
            py_script = self.ui.log_py_plainTextEdit.textCursor().selection().toPlainText()
        if py_script != '' and py_script:
            logger.info(py_script)
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


class script_editor_plainTextEdit(QtWidgets.QPlainTextEdit):
    def __init__(self):
        super(script_editor_plainTextEdit, self).__init__()
        self.setPlainText(prefs.script_cache)
        self.connect_functions()

    def dragEnterEvent(self, event):
        self.setStyleSheet('border : 2px solid white;')
        data = event.mimeData()
        urls = data.urls()
        if urls and urls[0].scheme() == 'file':
            event.acceptProposedAction()

    def dragMoveEvent(self, event):
        data = event.mimeData()
        urls = data.urls()
        if urls and urls[0].scheme() == 'file':
            event.acceptProposedAction()

    def dropEvent(self, event):
        data = event.mimeData()
        urls = data.urls()
        if urls and urls[0].scheme() == 'file':
            filepath = str(urls[0].path())[1:]
            if filepath:
                self.read_file(filepath)

    def read_file(self, filepath):
        self.setStyleSheet('border:none;')
        extension = filepath.split('.')[-1]
        if extension == 'py' or extension == 'pyw':
            with open(filepath) as f:
                text = f.read()
            if text:
                self.setPlainText(text)
        else:
            logger.warning('Reader accept only ".log" or ".wd"')

    def save_cache(self):
        script_cache = self.toPlainText()
        prefs.set_script_cache(script_cache)

    def connect_functions(self):
        self.textChanged.connect(self.save_cache)
