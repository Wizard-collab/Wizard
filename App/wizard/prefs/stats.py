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
# Wizard tools modules
from wizard.tools import log
from wizard.tools import utility as util
# Wizard variables modules
from wizard.vars import defaults

# Create the main logger
logger = log.pipe_log(__name__)
# Write the pref_path in console (debug level)


class stats:
    def __init__(self, user_name=None):
        self.database = util.database()
        if not user_name:
            self.user_name = user().get_user()
        else:
            self.user_name = user_name
        if self.user_name:
            self.stats_file = os.path.join(os.environ[defaults._stats_var_], (self.user_name + '.prefs'))
            if not self.is_file():
                self.create_user()
            else:
                self.read()

    def create_user(self, avatar=defaults._default_profile_image_):
        # create new user_dic
        if self.add_avatar(avatar):
            logger.debug("Profile image added !")
        else:
            logger.error("Can't add profile image !")
        self.settings = dict()
        self.settings[defaults._user_level_] = 1
        self.settings[defaults._user_xp_] = 0
        self.settings[defaults._user_life_] = 100
        self.settings[defaults._work_count_] = dict()
        for stage in defaults._assets_stages_:
            self.settings[defaults._work_count_][stage] = 0
        # Append user to the list of users
        # Write the setting file
        self.write()
        logger.debug('{}.prefs created !'.format(self.user_name))
        return 1

    def reset_versions_count(self):
        if self.is_file():
            if defaults._work_count_ not in self.settings.keys():
                self.settings[defaults._work_count_] = dict()
                for stage in defaults._assets_stages_:
                    self.settings[defaults._work_count_][stage] = 0
            self.write()

    def is_version_count(self):
        if self.is_file():
            return defaults._work_count_ in self.settings.keys()

    def add_version(self, asset):
        if self.is_file():
            self.settings[defaults._work_count_][asset.stage] += 1
            self.write()

    def get_versions(self):
        if self.is_file():
            return self.settings[defaults._work_count_]

    def add_avatar(self, avatar):
        if os.path.isfile(avatar):
            extension = os.path.splitext(avatar)[-1]
            path = os.path.join(os.environ[defaults._wizard_site_], defaults._avatar_images_path_) + self.user_name + extension
            if os.path.isfile(path.replace(extension,'.png')):
                os.remove(path.replace(extension,'.png'))
            if os.path.isfile(path.replace(extension,'.jpg')):
                os.remove(path.replace(extension,'.jpg'))
            if os.path.isfile(path.replace(extension,'.jpeg')):
                os.remove(path.replace(extension,'.jpeg'))
            copyfile(avatar, path)
            if os.path.isfile(path):
                return 1
            else:
                return 0
        else:
            return 0

    def get_avatar(self):
        avatar_path = os.path.join(os.environ[defaults._wizard_site_], defaults._avatar_images_path_) + self.user_name + '.png'
        if not os.path.isfile(avatar_path):
            avatar_path = avatar_path.replace('.png', '.jpg')
        if not os.path.isfile(avatar_path):
            avatar_path = avatar_path.replace('.jpg', '.jpeg')
        if os.path.isfile(avatar_path):
            return avatar_path
        else:
            logger.error("No avatar found...")
            return 0

    def get_xp(self):
        if self.is_file():
            return str(self.settings[defaults._user_xp_])
        else:
            logger.warning('User {} has no game prefs...'.format(self.user_name))

    def get_level(self):
        if self.is_file():
            return str(self.settings[defaults._user_level_])
        else:
            logger.warning('User {} has no game prefs...'.format(self.user_name))

    def get_life(self):
        if self.is_file():
            return str(self.settings[defaults._user_life_])
        else:
            logger.warning('User {} has no game prefs...'.format(self.user_name))

    def add_xp(self, number):
        if self.is_file():
            xp = int(self.settings[defaults._user_xp_])
            xp += int(number)
            if xp >= 100:
                xp = 0
                level = int(self.settings[defaults._user_level_])
                level += 1
                wall.wall().xp_event(level)
                self.settings[defaults._user_level_] = level
            self.settings[defaults._user_xp_] = xp
            self.write()
        else:
            logger.warning('User {} has no prefs...'.format(self.user_name))

    def write(self):
        self.database.write(0, self.stats_file, self.settings)

    def read(self):
        if self.is_file():
            self.settings = self.database.read(0, self.stats_file)
        else:
            logger.warning("Prefs file doesn't exist : {}".format(os.path.abspath(self.stats_file)))
            return None

    def is_file(self):
        return self.database.isfile(0, self.stats_file)
