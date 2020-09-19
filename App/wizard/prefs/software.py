# coding: utf-8

# Defaults Python modules
import os

from wizard.prefs.site import site
# Wizard prefs modules
from wizard.prefs.user import user
# Wizard tools modules
from wizard.tools import log
from wizard.tools import utility as util
# Wizard variables modules
from wizard.vars import defaults

# Create the main logger
logger = log.pipe_log(__name__)

'''
This module is used to define defaults settings for a defined software
The class software need one defaults software argument ( ex : 'Maya')
If you want init settings of this defaults software, it will need:
	
	- A valid executable path
	- Some env vars as needed
	- Additionals scripts paths as needed

The function is also used by the software launcher, to get :
	
	- the exe path
	- the env vars
	- the additionnals scripts path

'''


class software:

    def __init__(self,
                 software=None,
                 ):
        self.database = util.database()
        self.site = site()
        self.user = user()
        # Check if the given software is valid
        if not software or software not in defaults._softwares_list_:
            logger.warning('Please give a default software...')
        else:
            self.software = software
            # Read the software prefs
            self.settings = self.read_prefs()

    def get_settings_path(self):
        project_name = self.user.get_current_project_name()
        if project_name:
            project_folder = self.site.get_project_path_from_name(project_name)
        else:
            project_folder = None
        if project_folder:
            settings_path = os.path.join(project_folder, 'prefs', self.software)
            if not os.path.isdir(settings_path):
                os.makedirs(settings_path)
            return settings_path
        else:
            return None

    def get_settings_file(self):
        # Return the settings dictionary
        settings_path = self.get_settings_path()
        if settings_path:
            settings_file = os.path.join(settings_path, '{}.wd'.format(self.software))
            return settings_file
        else:
            return None

    def init_settings(
            self,
            software_path=None,
            env_paths=None,
            additionnal_scipt_path=None
    ):
        if not software_path or not os.path.isfile(software_path):
            logger.warning('Please give a valid {}.exe path'.format(self.software))
        else:
            self.settings = dict()
            self.settings[defaults._software_path_key_] = software_path
            self.settings[defaults._software_additionnal_env_key_] = env_paths
            self.settings[defaults._software_additionnal_script_key_] = additionnal_scipt_path
            self.write_prefs()
            logger.info('Prefs saved for {}'.format(self.software))

    def write_prefs(self):
        settings_file = self.get_settings_file()
        self.database.write(2, settings_file, self.settings)
        logger.debug('{} updated'.format(settings_file))

    def read_prefs(self):
        settings_file = self.get_settings_file()
        if self.database.isfile(2, settings_file):
            settings = self.database.read(2, settings_file)
            return settings
        else:
            logger.warning('No setup for this software : {}'.format(self.software))
            return None

    def get_path(self):
        if self.settings:
            return self.settings[defaults._software_path_key_]
        else:
            return None

    def get_env(self):
        if self.settings:
            return self.settings[defaults._software_additionnal_script_key_]
        else:
            return None

    def get_env_paths(self):
        if self.settings and defaults._software_additionnal_env_key_ in self.settings.keys():
            return self.settings[defaults._software_additionnal_env_key_]
        else:
            return None
