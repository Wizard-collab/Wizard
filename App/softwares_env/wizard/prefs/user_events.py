# coding: utf-8

'''
This module is used to manage the local preferences of the user
It permits to set and get the user name and the current project

'''
# Defaults Python modules
import os
import sys
# Wizard tools modules
from wizard.tools import log
from wizard.tools import utility as util
# Wizard variables modules
from wizard.vars import defaults

# Create the main logger
logger = log.pipe_log(__name__)

# Write the user prefs file to the log
logger.debug(os.path.abspath(defaults._user_))


class user_events:

    def __init__(self, project_path, user):

        self.database = util.database()
        self.user = user
        self.project_path = project_path

        if project_path:
            self.file = os.path.join(project_path, self.user + '.prefs')
            if not self.is_file():
                # Create settings dictionnary
                settings = dict()
                settings[defaults._events_] = []
                settings[defaults._locks_] = []
                # Write the .manager file as YAML with setting dict
                logger.info('{} file created'.format(self.user + '.prefs'))
                self.write_file(settings, new=1)
        else:
            self.file = None

    def resolve_lock_missing(self):
        if self.is_file():
            settings = self.open_file()
            if defaults._locks_ not in settings.keys():
                settings[defaults._locks_] = []
            self.write_file(settings)

    def get_events(self):
        if self.is_file():
            settings = self.open_file()
            keys_list = settings[defaults._events_]
            if keys_list and type(keys_list) == list:
                return keys_list
            else:
                return list()

    def add_event(self, id):
        if self.is_file():
            settings = self.open_file()
            settings[defaults._events_].append(id)
            self.write_file(settings)

    def get_locks(self):
        self.resolve_lock_missing()
        if self.is_file():
            settings = self.open_file()
            string_assets_list = settings[defaults._locks_]
            if string_assets_list and type(string_assets_list) == list:
                return string_assets_list
            else:
                return list()

    def add_lock(self, string_asset):
        self.resolve_lock_missing()
        if self.is_file():
            settings = self.open_file()
            settings[defaults._locks_].append(string_asset)
            self.write_file(settings)

    def remove_lock(self, string_asset):
        self.resolve_lock_missing()
        if self.is_file():
            settings = self.open_file()
            string_assets_list = settings[defaults._locks_]
            if string_asset in string_assets_list:
                settings[defaults._locks_].remove(string_asset)
                self.write_file(settings)

    def open_file(self):
        try:
            if self.is_file():
                settings = util.database().read(2, self.file)
                return settings
            else:
                logger.warning("{} file doesn't exist...".format(self.user + '.prefs'))

        except:
            logger.error(sys.exc_info()[1])

    def write_file(self, settings, new=0):
        try:
            util.database().write(2, self.file, settings)
            if not new:
                logger.debug('{} file updated'.format(self.user + '.prefs'))
        except:
            logger.error(sys.exc_info()[1])

    def is_file(self):
        if self.file:
            return util.database().isfile(2, self.file)
        else:
            return None
