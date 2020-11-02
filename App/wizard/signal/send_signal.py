from socket import *
import time
import traceback
from wizard.tools import log
from wizard.vars import defaults
import yaml

logger = log.pipe_log(__name__)

def send_signal(signal_as_str):
    try:
        host_name = 'localhost'
        if host_name:
            server = socket(AF_INET, SOCK_STREAM)
            server.connect((host_name, 5034))
            server.send(bytes(signal_as_str, 'utf8'))
            server.close()
    except:
        pass

def log_line(value):
    signal_dic = dict()
    signal_dic[defaults._signal_type_key_] = defaults._log_signal_
    signal_dic[defaults._log_line_] = value
    signal_as_str = yaml.dump(signal_dic)
    send_signal(signal_as_str)

def refresh_signal():
    signal_dic = dict()
    signal_dic[defaults._signal_type_key_] = defaults._refresh_signal_
    signal_as_str = yaml.dump(signal_dic)
    send_signal(signal_as_str)

def save_signal():
    signal_dic = dict()
    signal_dic[defaults._signal_type_key_] = defaults._save_signal_
    signal_as_str = yaml.dump(signal_dic)
    send_signal(signal_as_str)

def task_signal(value):
    signal_dic = dict()
    signal_dic[defaults._signal_type_key_] = defaults._task_signal_
    signal_dic[defaults._task_value_] = value
    signal_as_str = yaml.dump(signal_dic)
    send_signal(signal_as_str)

def task_name_signal(name):
    signal_dic = dict()
    signal_dic[defaults._signal_type_key_] = defaults._task_name_signal_
    signal_dic[defaults._task_name_] = name
    signal_as_str = yaml.dump(signal_dic)
    send_signal(signal_as_str)

def focus_signal():
    signal_dic = dict()
    signal_dic[defaults._signal_type_key_] = defaults._focus_signal_
    signal_as_str = yaml.dump(signal_dic)
    send_signal(signal_as_str)