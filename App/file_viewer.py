from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import pyqtSignal
from gui import build
from gui import log_to_gui

from gui.file_viewer import Ui_MainWindow
from wizard.vars import defaults
import os

site_path = os.path.join(os.environ[defaults._wizard_site_], defaults._site_)
stats_path = os.path.join(os.environ[defaults._wizard_site_], defaults._stats_)

os.environ[defaults._site_var_] = site_path
os.environ[defaults._abs_site_path_] = os.path.abspath('')
os.environ[defaults._stats_var_] = stats_path

from wizard.tools import log
from wizard.tools import utility as utils
from wizard.prefs.main import prefs
import traceback
import sys
import dialog_accept
import ui_about

logger = log.pipe_log()

prefs = prefs()

class Main(QtWidgets.QMainWindow):

    def __init__(self, do_close = 1):
        super(Main, self).__init__()
        # Build the ui from ui converted file
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.file_viewer_plainTextEdit = file_viewer_plainTextEdit()
        self.ui.file_viewer_plainTextEdit.import_signal.connect(self.update_file)
        self.ui.verticalLayout.addWidget(self.ui.file_viewer_plainTextEdit)
        self.file = None
        qtHandler = log_to_gui.log_viewer(self.ui)
        logger.main_logger.addHandler(qtHandler)
        self.connect_functions()
        self.modified=0
        try:
            file = sys.argv[1]
            if os.path.isfile(file):
                self.open_file(file)
        except:
            pass
        self.do_close = do_close


    def closeEvent(self, event):
        if not self.do_close:
            event.ignore()
            self.hide()
        else:
            event.accept()

    def new_file(self):
        try:
            if self.accept_dialog():
                self.file = None
                self.ui.file_viewer_plainTextEdit.clear()
                self.file_modified(modified=0)
                logger.info("New file *")
        except:
            logger.critical(str(traceback.format_exc()))

    def accept_dialog(self):
        run = 1
        if self.modified:
            self.dialog_accept = dialog_accept.Main("File not saved !", "File modified, continue ?")
            if build.launch_dialog_as_child(self.dialog_accept):
                run = 1
            else:
                run = 0
        return run

    def update_file(self):
        self.file = self.ui.file_viewer_plainTextEdit.file
        self.file_modified(modified=0)

    def save_file(self, save_as = None):
        try:
            extension = None
            if self.file:
                extension = self.file.split('.')[-1]
            if not save_as:
                if extension == "prefs":
                    if prefs.admin:
                        self.save(self.file)
                        logger.info("Saved - {}".format(self.file))
                    else:
                        logger.warning("You don't have the privilege to do that !")
                else:
                    self.save(self.file, 0)
                    logger.info("Saved - {}".format(self.file))

            else:
                data = self.ui.file_viewer_plainTextEdit.toPlainText()
                options = QFileDialog.Options()
                filename, _ = QFileDialog.getSaveFileName(self, 'Save prefs file', 'modified.prefs', "Prefs Files (*.prefs)", options=options)
                extension = filename.split('.')[-1]

                if extension == 'prefs':
                    if prefs.admin:
                        self.save(filename)
                        self.file = filename
                        logger.info("Saved - {}".format(self.file))
                    else:
                        logger.warning("You don't have the privilege to do that !")
                else:
                    self.save(filename, 0)
                    self.file = filename
                    logger.info("Saved - {}".format(self.file))
        except:
            logger.critical(str(traceback.format_exc()))

    def save(self, file, prefs = 1):
        data = self.ui.file_viewer_plainTextEdit.toPlainText()
        if prefs:
            utils.database().write(0, file, data, 1)
        else:
            with open(file, 'w') as f:
                f.write(data)
        self.file_modified(modified=0)

    def save_as(self):
        self.save_file(1)

    def file_modified(self, modified = 1):
        if modified:
            self.modified = 1
            self.setWindowTitle(str(self.file) + '*')
            QtWidgets.QApplication.processEvents()
        else:
            self.modified = 0
            self.setWindowTitle(self.file)
            QtWidgets.QApplication.processEvents()

    def open_file(self, file = None):
        if self.accept_dialog():
            if not file:
                options = QFileDialog.Options()
                fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                          "All Files (*);;Prefs Files (*.prefs)", options=options)
                if fileName:
                    self.ui.file_viewer_plainTextEdit.read_file(fileName)
                    self.file = fileName
                    self.file_modified(modified=0)
                    logger.info("Opened - {}".format(self.file))
            else:
                self.ui.file_viewer_plainTextEdit.read_file(file)
                self.file = file
                self.file_modified(modified=0)
                logger.info("Opened - {}".format(self.file))

        self.setWindowTitle(self.file)

    def show_about(self):
        try:
            self.ui_about = ui_about.Main()
            build.launch_normal_as_child(self.ui_about)
        except:
            logger.critical(str(traceback.format_exc()))

    def connect_functions(self):
        self.ui.actionNew.triggered.connect(self.new_file)
        self.ui.actionOpen.triggered.connect(self.open_file)
        self.ui.actionSave.triggered.connect(self.save_file)
        self.ui.actionSave_as.triggered.connect(self.save_as)
        self.ui.actionClose.triggered.connect(self.close)
        self.ui.actionAbout.triggered.connect(self.show_about)
        self.ui.file_viewer_plainTextEdit.textChanged.connect(self.file_modified)

class file_viewer_plainTextEdit(QtWidgets.QPlainTextEdit):
    import_signal = pyqtSignal(str)

    def __init__(self):
        super(file_viewer_plainTextEdit, self).__init__()
        self.file = None

    def dragEnterEvent(self, event):
        self.setStyleSheet('border : 1px solid white;')
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
        if extension == 'prefs':
            self.setPlainText(utils.database().read(0, filepath, 1).decode('utf-8'))
            self.file = filepath
            self.import_signal.emit('')
        else:
            with open(filepath, 'r') as f:
                data = f.read()
            self.setPlainText(data)
            self.file = filepath
            self.import_signal.emit('')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(defaults._file_viewer_ico_))
    file_viewer = Main()
    build.launch_file_viewer(file_viewer, title = file_viewer.file)