import socket
import sys
from threading import *
import time
import traceback
from wizard.tools import log
from PyQt5.QtCore import QThread, pyqtSignal
import yaml
from wizard.vars import defaults

logger = log.pipe_log(__name__)

class signal_server(QThread):

    refresh_signal = pyqtSignal(str)
    focus_signal = pyqtSignal(str)
    save_signal = pyqtSignal(str)
    task_signal = pyqtSignal(int)
    task_name_signal = pyqtSignal(str)

    def __init__(self):

        super(signal_server, self).__init__()
        hostname = 'localhost'
        ## getting the IP address using socket.gethostbyname() method
        self.server_address = socket.gethostbyname(hostname)
        port = 5034
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind((hostname, port))
        self.server.listen(100) 

    def run(self):
        while True:
            try:
                conn, addr = self.server.accept()
                if addr[0] == self.server_address:
                    signal_as_str = conn.recv(2048).decode('utf8')
                    if signal_as_str:
                        self.analyse_signal(signal_as_str)
                        #time.sleep(0.05)
            except:
                logger.error(str(traceback.format_exc()))
                continue

    def analyse_signal(self, signal_as_str):
        signal_dic = yaml.load(signal_as_str, Loader = yaml.Loader)
        if signal_dic[defaults._signal_type_key_] == defaults._refresh_signal_:
            self.refresh_signal.emit(defaults._refresh_signal_)
        elif signal_dic[defaults._signal_type_key_] == defaults._save_signal_:
            self.save_signal.emit(defaults._save_signal_)
        elif signal_dic[defaults._signal_type_key_] == defaults._task_signal_:
            self.task_signal.emit(int(signal_dic[defaults._task_value_]))
        elif signal_dic[defaults._signal_type_key_] == defaults._task_name_signal_:
            self.task_name_signal.emit(signal_dic[defaults._task_name_])
        elif signal_dic[defaults._signal_type_key_] == defaults._focus_signal_:
            self.focus_signal.emit(defaults._focus_signal_)