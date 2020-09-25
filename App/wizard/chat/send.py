from socket import *
import time
from wizard.prefs import project
import traceback
from wizard.tools import log
import yaml
from wizard.prefs.main import prefs

logger = log.pipe_log()
prefs = prefs()

def send_message(message):
    try:
        host_name = prefs.server_ip
        if host_name:
            server = socket(AF_INET, SOCK_STREAM)
            server.connect((host_name, 5033))
            message_dic = dict()
            message_dic['target'] = 'project'
            message_dic['project'] = prefs.project_name
            message_dic['message'] = message
            message_dic['user'] = prefs.user
            server.send(bytes(yaml.dump(message_dic), 'utf8'))
            time.sleep(0.5)
            server.close()
        else:
            logger.warning("No server ip defined, can't connect to any server")
    except TimeoutError:
        pass
    except ConnectionRefusedError:
        logger.warning('No server started for this project, no event will be saved...')
    except:
        logger.critical(str(traceback.format_exc()))
