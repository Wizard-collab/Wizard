# coding: utf-8

'''
This module is used to manage the local preferences of the user
It permits to set and get the user name and the current project

'''
# Defaults Python modules
import os
import sys
import pickle
# Pip Python modules
import yaml
# Wizard tools modules
from wizard.tools import log
from wizard.tools import utility as util
from wizard.tools import password as pw
# Wizard prefs modules
# Wizard variables modules
from wizard.vars import defaults


# Create the main logger
logger = log.pipe_log(__name__)

# Write the user prefs file to the log
logger.debug(os.path.abspath(defaults._user_))

class user:
    def __init__(self, user_name=None, current_project=None):
        self.database = util.database()
        if not self.is_prefs():
            # Create pref path if doesn't exists
            if not os.path.exists(defaults._user_path_):
                os.makedirs(defaults._user_path_)
            # Create settings dictionnary
            self.settings = dict()
            self.settings[defaults._user_name_key_] = user_name
            self.settings[defaults._asset_context_] = None
            self.settings[defaults._popup_prefs_key_] = dict()
            self.settings[defaults._popup_prefs_key_][defaults._popup_enable_key_] = 1
            self.settings[defaults._popup_prefs_key_][defaults._popup_sound_key_] = 1
            self.settings[defaults._popup_prefs_key_][defaults._popup_sound_file_key_] = defaults._woo_key_
            self.settings[defaults._popup_prefs_key_][defaults._popup_duration_key_] = 3
            self.settings[defaults._popup_prefs_key_][defaults._popup_creation_key_] = 1
            self.settings[defaults._popup_prefs_key_][defaults._popup_publish_key_] = 1
            self.settings[defaults._popup_prefs_key_][defaults._popup_playblast_key_] = 1
            self.settings[defaults._popup_prefs_key_][defaults._popup_save_key_] = 1
            self.settings[defaults._popup_prefs_key_][defaults._popup_message_key_] = 1
            self.settings[defaults._popup_prefs_key_][defaults._popup_position_key_] = defaults._bt_r_key_
            self.settings[defaults._current_project_key_] = current_project
            self.settings[defaults._user_theme_key_] = defaults._dark_theme_key_
            self.settings[defaults._user_chat_theme_key_] = defaults._purple_color_
            self.settings[defaults._user_screen_index_key_] = 0
            self.settings[defaults._windows_quit_key_] = 0
            self.settings[defaults._show_updates_] = 1
            self.settings[defaults._last_updates_] = "0.9.1"
            self.settings[defaults._script_cache_] = ""
            self.settings[defaults._show_new_version_] = 1
            self.settings[defaults._show_error_handler_] = 0
            self.settings[defaults._local_project_path_] = ''
            # Write the .manager file as YAML with setting dict
            logger.debug('user.prefs file created')
            self.write_pref_file(new=1)
        else:
            self.open_pref_file()

    def get_last_update(self):
        self.open_pref_file()
        if defaults._last_updates_ in self.settings.keys():
            return self.settings[defaults._last_updates_]
        else:
            self.settings[defaults._last_updates_] = "0.9.1"
            self.write_pref_file()
            return self.settings[defaults._last_updates_]

    def set_last_update(self, last_update = "0.9.1"):
        self.open_pref_file()
        self.settings[defaults._last_updates_] = last_update
        # Write the file
        self.write_pref_file()

    def get_show_updates(self):
        self.open_pref_file()
        if defaults._show_updates_ in self.settings.keys():
            return self.settings[defaults._show_updates_]
        else:
            self.settings[defaults._show_updates_] = 1
            self.write_pref_file()
            return 1

    def get_show_new_version(self):
        self.open_pref_file()
        if defaults._show_new_version_ in self.settings.keys():
            return self.settings[defaults._show_new_version_]
        else:
            self.settings[defaults._show_new_version_] = 1
            self.write_pref_file()
            return 1

    def get_show_error_handler(self):
        self.open_pref_file()
        if defaults._show_error_handler_ in self.settings.keys():
            self.set_show_error_handler()
            return self.settings[defaults._show_error_handler_]
        else:
            self.settings[defaults._show_error_handler_] = 1
            self.write_pref_file()
            return 1

    def get_local_project_path(self):
        self.open_pref_file()
        if defaults._local_project_path_ in self.settings.keys():
            return self.settings[defaults._local_project_path_]
        else:
            self.settings[defaults._local_project_path_] = ''
            self.write_pref_file()
            return 1

    def set_local_project_path(self, local_project_path):
        self.open_pref_file()
        self.settings[defaults._local_project_path_] = local_project_path
        # Write the file
        self.write_pref_file()

    def set_show_updates(self, show_updates = 1):
        self.open_pref_file()
        self.settings[defaults._show_updates_] = show_updates
        # Write the file
        self.write_pref_file()

    def set_show_new_version(self, show_new_version = 1):
        self.open_pref_file()
        self.settings[defaults._show_new_version_] = show_new_version
        # Write the file
        self.write_pref_file()

    def set_show_error_handler(self, show_error_handler = 0):
        self.open_pref_file()
        self.settings[defaults._show_error_handler_] = 1
        # Write the file
        self.write_pref_file()

    def set_script_cache(self, script):
        self.open_pref_file()
        self.settings[defaults._script_cache_] = script
        # Write the file
        self.write_pref_file()

    def get_script_cache(self):
        self.open_pref_file()
        if defaults._script_cache_ in self.settings.keys():
            return self.settings[defaults._script_cache_]
        else:
            self.settings[defaults._script_cache_] = ""
            self.write_pref_file()
            return self.settings[defaults._script_cache_]

    def get_user(self):
        self.open_pref_file()
        return self.settings[defaults._user_name_key_]

    def get_popup_prefs(self):
        self.open_pref_file()
        if defaults._popup_playblast_key_ not in self.settings[defaults._popup_prefs_key_].keys():
            self.settings[defaults._popup_prefs_key_][defaults._popup_playblast_key_] = 1
            self.write_pref_file()
        return self.settings[defaults._popup_prefs_key_]

    def get_theme(self):
        self.open_pref_file()
        return self.settings[defaults._user_theme_key_]

    def get_screen(self):
        self.open_pref_file()
        return self.settings[defaults._user_screen_index_key_]

    def set_screen(self, index):
        self.open_pref_file()
        #settings = open_pref_file()
        self.settings[defaults._user_screen_index_key_] = index
        # Write the file
        self.write_pref_file()

    def get_chat_theme(self):
        self.open_pref_file()
        return self.settings[defaults._user_chat_theme_key_]

    def set_theme(self, theme):
        self.open_pref_file()
        self.settings[defaults._user_theme_key_] = theme
        # Write the file
        self.write_pref_file()

    def set_chat_theme(self, theme):
        self.open_pref_file()
        self.settings[defaults._user_chat_theme_key_] = theme
        # Write the file
        self.write_pref_file()

    def get_quit_on_close(self):
        self.open_pref_file()
        return self.settings[defaults._windows_quit_key_]

    def set_quit_on_close(self, boolean):
        self.open_pref_file()
        self.settings[defaults._windows_quit_key_] = boolean
        # Write the file
        self.write_pref_file()

    def set_popup_prefs(self, popup_dict):
        self.open_pref_file()
        self.settings[defaults._popup_prefs_key_] = popup_dict
        # Write the file
        self.write_pref_file()

    def get_current_project_name(self):
        self.open_pref_file()
        current_project_dic = self.settings[defaults._current_project_key_]
        if current_project_dic:
            current_project_name = self.settings[defaults._current_project_key_]
            return current_project_name
        else:
            return 0

    def set_user(self, user_name):
        self.open_pref_file()
        # Read the setting file
        self.settings[defaults._user_name_key_] = user_name
        # Write the file
        self.write_pref_file()

    def change_project(self, current_project):
        self.open_pref_file()
        # Check the password concordance
        self.settings[defaults._current_project_key_] = current_project
        logger.debug('   Current project : {}'.format(self.settings[defaults._current_project_key_]))
        self.write_pref_file()
        logger.info('Project {} loaded...'.format(self.settings[defaults._current_project_key_]))
        return 1

    def set_context(self, asset):
        self.open_pref_file()
        # Check the password concordance
        self.settings[defaults._asset_context_] = pickle.dumps(asset, 0).decode('utf-8')
        logger.info('Asset context saved !')
        self.write_pref_file()

    def get_context(self):
        self.open_pref_file()
        if self.settings[defaults._asset_context_]:
            asset = pickle.loads(self.settings[defaults._asset_context_].encode('utf-8'))
            return asset
        else:
            return None

    def get_pref_path(self):
        return defaults._user_path_


    def is_prefs(self):
        return util.database().isfile(1, defaults._user_)


    def open_pref_file(self):
        try:
            if self.is_prefs():
                self.settings = util.database().read(1, defaults._user_)
            else:
                logger.warning("Prefs file doesn't exist : {}, creating it..."
                               .format(defaults._user_))
        except:
            logger.error(sys.exc_info()[1])


    def write_pref_file(self, new=0):
        try:
            util.database().write(1, defaults._user_, self.settings)
            logger.debug('user.prefs file updated')
        except:
            logger.error(sys.exc_info()[1])
