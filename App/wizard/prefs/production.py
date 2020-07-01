# coding: utf-8

'''
This module is used to manage the site preferences of the studio/school

-init_site_prefs()
	init the site_prefs if don't exist

-create_user(<user_name>, <password>)
	add a user to all the users of the site

-get_users_list()
	return all the users of the site in a user list

-password_check(<user_name>, <password>)
	check if the given <password> match 
	the user password in the site for this <user>

'''
# Defaults Python modules
import os
from shutil import copyfile

from wizard.prefs.user import user
from wizard.project import wall
from wizard.prefs.site import site
from wizard.prefs.user import user
# Wizard tools modules
from wizard.tools import log
from wizard.tools import utility as util
# Wizard variables modules
from wizard.vars import defaults

# Create the main logger
logger = log.pipe_log(__name__)
# Write the pref_path in console (debug level)


class production:
    def __init__(self):
        self.database = util.database()
        project_name = user().get_current_project_name()
        if project_name:
            project_path = site().get_project_path_from_name(project_name)
        else:
            project_path = None
        if project_path:
            self.production_file = os.path.join(project_path, defaults._production_)
            if not self.is_file():
                self.init_settings()
            else:
                self.read()
        else:
            self.production_file = None

    def init_settings(self):
        self.settings = dict()
        self.settings[defaults._assets_] = dict()
        self.settings[defaults._assets_][defaults._characters_] = dict()
        self.settings[defaults._assets_][defaults._props_] = dict()
        self.settings[defaults._assets_][defaults._sets_] = dict()
        self.settings[defaults._assets_][defaults._set_dress_] = dict()
        self.settings[defaults._assets_][defaults._vehicles_] = dict()
        self.write()

    def add_name(self, asset):
        if asset.name not in self.settings[defaults._assets_][asset.category].keys():
            self.settings[defaults._assets_][asset.category][asset.name] = dict()
            self.write()

    def add_category(self, asset):
        if asset.category not in self.settings[defaults._assets_].keys():
            self.settings[defaults._assets_][asset.category] = dict()
            self.write()

    def add_asset(self, asset):
        asset_string = util.asset_to_string(asset)
        asset_dic = dict()
        asset_dic[defaults._asset_state_] = defaults._todo_
        asset_dic[defaults._assigned_user_] = None
        if asset.variant not in self.settings[defaults._assets_][asset.category][asset.name].keys():
            self.settings[defaults._assets_][asset.category][asset.name][asset.variant] = dict()
        self.settings[defaults._assets_][asset.category][asset.name][asset.variant][asset.stage] = asset_dic
        self.write()

    def get_dic(self):
        return self.settings

    def change_state(self, domain, category, name, variant, stage, state):
        self.settings[domain][category][name][variant][stage][defaults._asset_state_] = state
        self.write()

    def write(self):
        self.database.write(0, self.production_file, self.settings)

    def read(self):
        if self.is_file():
            self.settings = self.database.read(0, self.production_file)
        else:
            logger.warning("Prefs file doesn't exist : {}".format(os.path.abspath(self.production_file)))
            return None

    def is_file(self):
        return self.database.isfile(0, self.production_file)
