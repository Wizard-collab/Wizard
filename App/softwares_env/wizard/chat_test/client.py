from wizard.tools import utility as utils
utils.init_wizard_env()

from wizard.tools import log
from wizard.prefs.main import prefs
from wizard.prefs import project
import importlib
from wizard.vars import defaults
importlib.reload(defaults)

from PyQt5.QtCore import pyqtSignal, QThread
import traceback
import time
from socket import *
import yaml

logger = log.pipe_log(__name__)

prefs = prefs()

class chat_client(QThread):

    msg_recv = pyqtSignal(dict)

    def __init__(self):
        super(chat_client, self).__init__()
        self.init_connection()
        self.running = True

    def init_connection(self):
        self.server = socket(AF_INET, SOCK_STREAM)
        try:
            host_name = prefs.server_ip
            if host_name:
                self.server.connect((host_name, 5034))
                self.is_server = 1
            else:
                logger.warning("No server ip defined, can't connect to any server")
                self.is_server = 0
        except:
            self.is_server = 0

    def run(self):
        try:
            while self.is_server and self.running:
                try:
                    message_bytes = self.server.recv(1024)
                    message_dic = yaml.load(message_bytes.decode('utf8'), Loader = yaml.Loader)
                    self.msg_recv.emit(message_dic)
                except ConnectionResetError:
                    self.is_server = 0
                except:
                    logger.critical(str(traceback.format_exc()))
        except:
            logger.critical(str(traceback.format_exc()))

    def send_message(self, message, message_key, asset=None, file=None, quote=None, message_type = defaults._chat_conversation_, destination = defaults._chat_general_, user = prefs.user):
        if self.is_server and self.running:
            message_dic = dict()
            message_dic[defaults._chat_type_] = message_type
            message_dic[defaults._chat_user_] = user
            message_dic[defaults._chat_project_] = prefs.project_name
            message_dic[defaults._chat_message_] = message
            message_dic[defaults._chat_date_] = utils.id_based_time()
            message_dic[defaults._chat_destination_] = destination
            message_dic[defaults._chat_asset_] = asset
            message_dic[defaults._chat_file_] = file
            message_dic[defaults._chat_key_] = message_key
            message_dic[defaults._chat_quote_] = quote
            message_bytes = yaml.dump(message_dic).encode('utf8')
            self.server.send(message_bytes)
            return message_dic
        else:
            return None

    def send_seen(self, message_key, user = prefs.user, destination = defaults._chat_general_):
        if self.is_server and self.running:
            message_dic = dict()
            message_dic[defaults._chat_type_] = defaults._chat_seen_
            message_dic[defaults._chat_project_] = prefs.project_name
            message_dic[defaults._chat_user_] = user
            message_dic[defaults._chat_destination_] = destination
            message_dic[defaults._chat_key_] = message_key
            message_bytes = yaml.dump(message_dic).encode('utf8')
            self.server.send(message_bytes)
            return message_dic
        else:
            return None

    def send_info(self, message, message_key, user = prefs.user, destination = defaults._chat_general_):
        if self.is_server and self.running:
            message_dic = dict()
            message_dic[defaults._chat_type_] = defaults._chat_info_
            message_dic[defaults._chat_user_] = user
            message_dic[defaults._chat_project_] = prefs.project_name
            message_dic[defaults._chat_message_] = message
            message_dic[defaults._chat_date_] = utils.id_based_time()
            message_dic[defaults._chat_destination_] = destination
            message_dic[defaults._chat_key_] = message_key
            message_bytes = yaml.dump(message_dic).encode('utf8')
            self.server.send(message_bytes)
            return message_dic
        else:
            return None

    def new_room_signal(self, room_name):
        if self.is_server and self.running:
            message_dic = dict()
            message_dic[defaults._chat_type_] = defaults._chat_room_signal_
            message_dic[defaults._chat_room_] = room_name
            message_bytes = yaml.dump(message_dic).encode('utf8')
            self.server.send(message_bytes)
            return message_dic
        else:
            return None

    def send_remove(self, message_key):
        if self.is_server and self.running:
            message_dic = dict()
            message_dic[defaults._chat_type_] = defaults._chat_remove_message_
            message_dic[defaults._chat_key_] = message_key
            message_bytes = yaml.dump(message_dic).encode('utf8')
            self.server.send(message_bytes)
            return message_dic
        else:
            return None

    def stop(self):
        self.running = False

thread = chat_client()
thread.start()
time.sleep(0.1)
thread.stop()