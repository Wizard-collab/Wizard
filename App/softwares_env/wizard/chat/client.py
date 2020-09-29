from wizard.tools import log
from wizard.prefs.main import prefs
from wizard.prefs import project

from PyQt5.QtCore import pyqtSignal, QThread
import traceback
import time
from socket import *
import yaml

logger = log.pipe_log(__name__)

prefs = prefs()

class client(QThread):
    receive = pyqtSignal(str)
    stopped = pyqtSignal(str)

    def __init__(self):
        super(client, self).__init__()
        self.init_connection()

    def init_connection(self):
        self.server = socket(AF_INET, SOCK_STREAM)
        try:
            host_name = prefs.server_ip
            if host_name:
                self.server.connect((host_name, 5033))
                self.is_server = 1
            else:
                logger.warning("No server ip defined, can't connect to any server")
                self.is_server = 0
        except:
            self.is_server = 0

    def run(self):
        try:
            while self.is_server:
                try:
                    message_bytes = self.server.recv(1024)
                    message_dict = yaml.load(message_bytes.decode('utf8'), Loader = yaml.Loader)
                    message = message_dict['message']
                    target = message_dict['target']
                    project = message_dict['project']
                    user = message_dict['user']
                    if target == 'project' and project == prefs.project_name:
                        if message != '':
                            if isinstance(message, (bytes, bytearray)):
                                message = message.decode('utf8')
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
        host_name = prefs.server_ip
        while 1:
            try:
                if host_name:
                    server = socket(AF_INET, SOCK_STREAM)
                    server.settimeout(1)
                    server.connect((host_name, 5033))
                    server.close()
                    self.is_running.emit(1)
                    time.sleep(0.1)
                else:
                    logger.warning("No server ip defined, can't connect to any server")
                    self.is_running.emit(0)
                    time.sleep(0.1)
            except:
                self.is_running.emit(0)
                time.sleep(0.1)


def test_conn_once():
    try:
        host_name = prefs.server_ip
        if host_name:
            server = socket(AF_INET, SOCK_STREAM)
            server.settimeout(1)
            server.connect((host_name, 5033))
            #server.send('null_conn'.encode('utf-8'))
            server.close()
            return 1
        else:
            logger.warning("No server ip defined, can't connect to any server")
            return 0
    except:
        return 0
