from socket import *
import time
from wizard.prefs import project
import traceback
from wizard.tools import log
from wizard.prefs.main import prefs
from wizard.vars import defaults
import yaml

logger = log.pipe_log(__name__)
prefs = prefs()

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

def refresh_signal():
    signal_dic = dict()
    signal_dic[defaults._signal_type_key_] = defaults._refresh_signal_
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