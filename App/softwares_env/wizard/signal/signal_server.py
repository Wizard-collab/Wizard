import socket
import sys
from threading import *
import time
import traceback
from wizard.tools import log
from PyQt5.QtCore import QThread, pyqtSignal

logger = log.pipe_log(__name__)

class signal_server(QThread):

    signal_received = pyqtSignal(str)

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
                    self.signal_received.emit("")
            except:
                logger.error(str(traceback.format_exc()))
                continue