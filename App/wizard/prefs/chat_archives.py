from wizard.prefs.main import prefs
from wizard.tools import log
from wizard.vars import defaults
from wizard.tools import utility as utils

import importlib
importlib.reload(defaults)

import yaml
import os
import shutil

import sys

prefs = prefs()
logger = log.pipe_log(__name__)

class chat_archives():
    def __init__(self):

        self.database = utils.database()
        self.init_shared_folder()
        self.users = prefs.project_users

        if self.is_file():
            self.read()
        else:
            self.init_settings()

    def init_settings(self):
        self.archives_dic = dict()
        self.archives_dic[defaults._chat_messages_] = dict()
        self.archives_dic[defaults._chat_rooms_] = dict()
        self.archives_dic[defaults._chat_rooms_messages_] = dict()
        self.write()

    def add_message(self, message_key, msg_dic):
        self.read()
        self.archives_dic[defaults._chat_messages_][message_key] = msg_dic

        self.add_msg_id_to_room(message_key, msg_dic)

        self.write()

    def add_msg_id_to_room(self, msg_id, msg_dic):
        if msg_dic[defaults._chat_destination_] in self.users:
            key = self.get_user_couple_key(msg_dic[defaults._chat_destination_])
        else:
            key = msg_dic[defaults._chat_destination_]
        if key not in self.archives_dic[defaults._chat_rooms_messages_].keys():
            self.archives_dic[defaults._chat_rooms_messages_][key] = list()
        self.archives_dic[defaults._chat_rooms_messages_][key].append(msg_id)

    def get_user_couple_key(self, user):
        user_couple = [user, prefs.user]
        user_couple.sort()
        user_couple_key = '|'.join(user_couple)
        return user_couple_key

    def create_room(self, room_name):
        self.read()
        if room_name not in self.archives_dic[defaults._chat_rooms_]:
            self.archives_dic[defaults._chat_rooms_][room_name] = dict()
            self.archives_dic[defaults._chat_rooms_][room_name][defaults._users_list_key_] = []
            self.write()
            return 1
        else:
            logger.warning("Room already exists")
            return None

    def init_shared_folder(self):
        self.shared_folder = os.path.join(prefs.project_path, defaults._shared_folder_)
        if not os.path.isdir(self.shared_folder):
            os.makedirs(self.shared_folder)

    def add_file_to_shared(self, file):
        if os.path.isfile(file):
            filename = os.path.basename(file)
            #filename, extension = os.path.splitext(filename)
            #new_filename = "{}{}".format(utils.random_string(), extension)
            new_file = utils.get_filename_without_override(os.path.join(self.shared_folder, filename))
            print(new_file)
            shutil.copyfile(file, new_file)
            return new_file
        else:
            logger.warning("The file doesn't exists")
            return None

    def get_messages(self):
        if self.read():
            return self.archives_dic[defaults._chat_messages_]
        else:
            return None

    def get_room_last_ids(self, room, number=10):
        if room not in self.users:
            key = room
        else:
            key = self.get_user_couple_key(room)
        if key in self.archives_dic[defaults._chat_rooms_messages_].keys():
            return self.archives_dic[defaults._chat_rooms_messages_][key][-number:]
        else:
            return []

    def get_rooms(self):
        if self.read():
            return list(self.archives_dic[defaults._chat_rooms_].keys())
        else:
            return None

    def get_current_project_chat_archives_file(self):
        # Get the pref file from the current project
        # (from user prefs)
        project_path = prefs.project_path
        if project_path:
            file = os.path.join(project_path, defaults._chat_archives_)
            # Write the pref_path in console (debug level)
            logger.debug(file)
            return file
        else:
            return 0

    def write(self):
        self.database.write(0, self.file, self.archives_dic)

    def read(self):
        if self.is_file():
            self.archives_dic = self.database.read(0, self.file)
            return 1
        else:
            logger.warning("Prefs file doesn't exist : {}".format(os.path.abspath(self.file)))
            return None

    def is_file(self):
        self.file = self.get_current_project_chat_archives_file()
        # Check the pref_file presence
        if self.database.isfile(2, self.file):
            return 1
        else:
            logger.warning("Can't find chat archives")
            return 0


