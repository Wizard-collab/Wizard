# coding: utf-8

# Defaults Python modules
from time import strftime, localtime
import time
from datetime import datetime
from datetime import timedelta
import re
import yaml
import base64
import ctypes
import os
from wizard.tools import log
import tempfile
import zipfile
import math
import os
from wizard.vars import defaults
import subprocess
import string
import random

logger = log.pipe_log(__name__)

import traceback

def init_wizard_env():
    site_path = os.path.join(os.environ[defaults._wizard_site_], defaults._site_)
    stats_path = os.path.join(os.environ[defaults._wizard_site_], defaults._stats_)

    os.environ[defaults._site_var_] = site_path
    os.environ[defaults._abs_site_path_] = os.path.abspath('')
    os.environ[defaults._stats_var_] = stats_path

def get_time():
    time = strftime("%Y-%m-%d - %H:%M", localtime())
    time = strftime("%Y-%m-%d - %H:%M", localtime())
    return time

def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

def get_gmtime():
    time = localtime()
    return time


def get_hour():
    time = strftime("%H:%M", localtime())
    return time

def random_string(len=8):
    all_chars = list(string.digits + string.ascii_letters)
    random.shuffle(all_chars)
    return ''.join(all_chars[:len])

def random_number(len=8):
    all_chars = list(string.digits)
    random.shuffle(all_chars)
    return ''.join(all_chars[:len])

def id_based_time():
    now = datetime.now()
    try:
        timestamp = datetime.timestamp(now)
    except AttributeError:
        timestamp = time.time()
    return str(timestamp)

def timestamp():
    now = datetime.now()
    try:
        timestamp = datetime.timestamp(now)
    except AttributeError:
        timestamp = time.time()
    return timestamp


def check_illegal(string):
    check_re = re.match("^[A-Za-z0-9_-]*$", string)
    # check_underscore = '_' not in string
    if check_re:
        return string
    else:
        return None

def temp_file_from_command(command):

    tempdir = tempfile.mkdtemp()

    temporary_python_file = os.path.join(tempdir, 'wizard_temp_script.py')

    full_command = command

    with open(temporary_python_file, 'w') as f:
        f.write(full_command)
    return temporary_python_file

def session_file_from_command(command):
    full_command = command
    with open(defaults._session_file_, 'w') as f:
        f.write(command)

def temp_dir():
    tempdir = tempfile.mkdtemp()
    return tempdir

class database:
    def __init__(self):
        pass
        # self.database = sq.db_wrap()

    def refresh_database(self):
        pass
        # self.database = sq.db_wrap()

    def write(self, env, file, data, is_yaml=0):
        ctypes.windll.kernel32.SetFileAttributesW(file, 128)
        file = os.path.abspath(file)
        if not is_yaml:
            bytes_data = str.encode(yaml.dump(data))
        else:
            bytes_data = str.encode(data)
        encoded_data = base64.b64encode(bytes_data)
        file = os.path.abspath(file).replace('\\', '/')

        try:
            with open(file, 'wb') as f:
                f.write(encoded_data)
        except IOError:
            logger.error("Can't write {}...".format(file))

        # ctypes.windll.kernel32.SetFileAttributesW(file, 2)

    def read(self, env, file, keep_yaml=0):
        ctypes.windll.kernel32.SetFileAttributesW(file, 128)
        file = file.replace('\\', '/')
        file = os.path.abspath(file)
        # data = self.database.read_data(0, file)

        with open(file, 'rb') as f:
            data = f.read()

        # ctypes.windll.kernel32.SetFileAttributesW(file, 2)

        if data:
            bytes_data = base64.b64decode(data)
            if not keep_yaml:
                data = yaml.load(bytes_data, Loader=yaml.Loader)
            else:
                data = bytes_data
            return data

    def isfile(self, env, file):
        file = file.replace('\\', '/')
        file = os.path.abspath(file)
        if os.path.isfile(file):
            return 1
        else:
            return None
        # check = self.database.is_key(0, file)
        # return check


def encode_message(message_dic):
    message_bytes = (yaml.dump(message_dic)).encode('utf-8')
    return message_bytes


def decode_message(message_bytes):
    decoded_string = message_bytes.decode('utf-8')
    message_dic = yaml.load(decoded_string, Loader=yaml.Loader)
    return message_dic


def asset_to_string(asset):
    string_asset = "{}".format(asset.domain)
    string_asset += "/{}".format(asset.category)
    string_asset += "/{}".format(asset.name)
    string_asset += "/{}".format(asset.stage)
    string_asset += "/{}".format(asset.variant)
    string_asset += "/{}".format(asset.software)
    string_asset += "/{}".format(asset.version)
    string_asset += "/{}".format(asset.export_asset)
    string_asset += "/{}".format(asset.export_version)
    return string_asset

def short_asset_to_string(asset):
    string_asset = "{}".format(asset.domain)
    string_asset += "/{}".format(asset.category)
    string_asset += "/{}".format(asset.name)
    string_asset += "/{}".format(asset.stage)
    string_asset += "/{}".format(asset.variant)
    string_asset += "/{}".format(asset.software)
    return string_asset

def variant_asset_to_string(asset):
    string_asset = "{}".format(asset.domain)
    string_asset += "/{}".format(asset.category)
    string_asset += "/{}".format(asset.name)
    string_asset += "/{}".format(asset.stage)
    string_asset += "/{}".format(asset.variant)
    return string_asset

def version_asset_to_string(asset):
    string_asset = "{}".format(asset.domain)
    string_asset += "/{}".format(asset.category)
    string_asset += "/{}".format(asset.name)
    string_asset += "/{}".format(asset.stage)
    string_asset += "/{}".format(asset.variant)
    string_asset += "/{}".format(asset.software)
    string_asset += "/{}".format(asset.version)
    return string_asset


def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))


def zip_folder(file, folder):
    zipf = zipfile.ZipFile(file, 'w', zipfile.ZIP_DEFLATED)
    zipdir(folder, zipf)
    zipf.close()


def zipfiles(files_list, file):
    curr_dir = os.getcwd()
    zip_file = zipfile.ZipFile(file, mode='w')
    for file in files_list:
        add_zip_flat(zip_file, file)
    zip_file.close()
    os.chdir(curr_dir)


def add_zip_flat(zip_file, filename):
    dir, base_filename = os.path.split(filename)
    os.chdir(dir)
    zip_file.write(base_filename)

def get_filename_without_override(file):

    folder = os.path.dirname(file)
    basename = os.path.basename(file)
    extension = os.path.splitext(basename)[-1]
    filename = os.path.splitext(basename)[0]
    index = 1

    while os.path.isfile(file):
        new_filename = "{}_{}{}".format(filename, index, extension)
        file = os.path.join(folder, new_filename)
        index+=1

    return file

def increment_folder(folder_name):

    num=1

    folder = "{}_{}".format(folder_name, str(num).zfill(4))

    while os.path.isdir(folder):
        num+=1
        folder = "{}_{}".format(folder_name, str(num).zfill(4))

    os.makedirs(folder)

    return folder
