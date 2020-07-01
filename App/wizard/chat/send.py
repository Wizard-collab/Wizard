from socket import *
import time
from wizard.prefs import project
import traceback
from wizard.tools import log

logger = log.pipe_log()


def send_message(message):
    try:
        host_name = project.get_server_ip()
        server = socket(AF_INET, SOCK_STREAM)
        server.connect((host_name, 5000))
        server.send('temp_conn'.encode('utf-8'))
        time.sleep(0.5)
        server.send(message)
    except TimeoutError:
        pass
    except ConnectionRefusedError:
        logger.warning('No server started for this project, no event will be saved...')
    except:
        logger.critical(str(traceback.format_exc()))

def send_message_chat(message):
    try:
        host_name = project.get_server_ip()
        server = socket(AF_INET, SOCK_STREAM)
        server.connect((host_name, 5000))
        server.send('temp_conn_chat'.encode('utf-8'))
        time.sleep(0.5)
        server.send(message)
    except TimeoutError:
        pass
    except ConnectionRefusedError:
        logger.warning('No server started for this project, no message can be sent...')
    except:
        logger.critical(str(traceback.format_exc()))
