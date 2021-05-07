from pynput import keyboard
from wizard.prefs.shortcuts import shortcuts_prefs
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal
from wizard.vars import defaults
from wizard.tools import log
logger = log.pipe_log(__name__)

class shortcuts_listener(QtCore.QThread):

    screen_record_signal = pyqtSignal(str)

    def __init__(self):
        super(shortcuts_listener, self).__init__()
        self.shortcuts_dic = shortcuts_prefs().shortcuts_dic
        self.listener = None
        self.current = set()

    def on_press(self, key):
        self.current.add(key)

    def on_release(self, key):
        self.analyse(self.current)
        self.current.clear()

    def analyse(self, current):
        for shortcut_target in self.shortcuts_dic.keys():
            if self.shortcuts_dic[shortcut_target] == current: 
                self.execute(shortcut_target)
                break

    def execute(self, shortcut_target):
        if shortcut_target == defaults._screen_record_:
            self.screen_record_signal.emit('')

    def run(self):
        with keyboard.Listener(on_press=self.on_press, on_release=self.on_release) as self.listener:
            self.listener.join()

    def stop_thread(self):
        if self.listener:
            self.listener.stop()