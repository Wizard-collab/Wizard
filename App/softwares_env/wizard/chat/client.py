from wizard.tools import log
from wizard.prefs.main import prefs
from wizard.prefs import project

from PyQt5.QtCore import pyqtSignal, QThread
import traceback
import time
from socket import *

logger = log.pipe_log()

prefs = prefs()

class client(QThread):
    receive = pyqtSignal(bytes)
    stopped = pyqtSignal(str)

    def __init__(self, chat=0):
        super(client, self).__init__()
        self.chat = chat
        self.init_connection()

    def init_connection(self):
        self.server = socket(AF_INET, SOCK_STREAM)
        try:
            host_name = project.get_server_ip()
            self.server.connect((host_name, 5000))
            user = prefs.user
            if self.chat:
                user = 'chat_user_' + prefs.user
            self.server.send(user.encode('utf-8'))
            self.is_server = 1
        except:
            self.is_server = 0

    def run(self):
        try:
            while self.is_server:
                try:
                    message = self.server.recv(1024)
                    if message != '':
                        self.receive.emit(message)
                except ConnectionResetError:
                    self.is_server = 0
                    self.stopped.emit('')
                except:
                    logger.critical(str(traceback.format_exc()))
        except:
            logger.critical(str(traceback.format_exc()))


class test_conn(QThread):
    is_running = pyqtSignal(int)

    def __init__(self):
        super(test_conn, self).__init__()

    def run(self):
        host_name = project.get_server_ip()
        while 1:
            try:
                server = socket(AF_INET, SOCK_STREAM)
                server.settimeout(1)
                server.connect((host_name, 5000))
                server.send('null_conn'.encode('utf-8'))
                server.close()
                self.is_running.emit(1)
                time.sleep(2)
            except:
                self.is_running.emit(0)
                time.sleep(10)


def test_conn_once():
    try:
        host_name = project.get_server_ip()
        server = socket(AF_INET, SOCK_STREAM)
        server.settimeout(1)
        server.connect((host_name, 5000))
        server.send('null_conn'.encode('utf-8'))
        server.close()
        return 1
    except:
        return 0
