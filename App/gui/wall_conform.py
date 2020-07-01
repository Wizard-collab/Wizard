import os
import time

# from wizard.project.wall import wall
from wizard.prefs.main import prefs
# Wizard tools modules
from wizard.tools import log
from wizard.vars import defaults

# Creates the main logger
logger = log.pipe_log(__name__)
try:
    from PyQt5.QtCore import QThread, pyqtSignal
except ImportError:
    logger.info('Cannot import PyQt5')


class wallThread(QThread):
    signal = pyqtSignal(str)

    def __init__(self, main_ui):
        super(wallThread, self).__init__(main_ui)
        self.main_ui = main_ui
        self.prefs = prefs()

    def run(self):

        self.watcher = watcher(os.path.join(self.prefs.project_path, defaults._wall_))
        while 1:
            if self.watcher.check():
                self.signal.emit('wall_event')
            time.sleep(1)


class watcher():
    def __init__(self, file_name):
        self._cached_stamp = 0
        self.file_name = file_name

    def check(self):
        stamp = os.stat(self.file_name).st_mtime
        if stamp != self._cached_stamp:
            self._cached_stamp = stamp
            return 1
        else:
            return 0
