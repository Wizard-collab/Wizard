from socket import *
import time
from wizard.prefs import project
import traceback
from wizard.tools import log
from wizard.prefs.main import prefs

logger = log.pipe_log()
prefs = prefs()

def send_signal():
    try:
        host_name = 'localhost'
        if host_name:
            server = socket(AF_INET, SOCK_STREAM)
            server.connect((host_name, 5034))
            server.send(bytes('0', 'utf8'))
            time.sleep(0.1)
            server.close()
    except:
        pass