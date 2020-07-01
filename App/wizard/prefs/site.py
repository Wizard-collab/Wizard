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
# Wizard tools modules
from wizard.tools import log
from wizard.tools import password as pw
from wizard.tools import utility as util
# Wizard variables modules
from wizard.vars import defaults

# Create the main logger
logger = log.pipe_log(__name__)
# Write the pref_path in console (debug level)

class site:

    def __init__(self):
        self.database = util.database()
        if not self.is_prefs():
            # Create a basic settings dict
            self.settings = dict()
            self.settings[defaults._users_list_key_] = dict()
            self.settings[defaults._projects_list_key_] = dict()
            # Create the preferences file
            self.write_pref_file(new=1)
            self.create_user(add_user_name='admin', promotion=defaults._staff_, email='contact@leobrunel.com',
                             password='administrator', admin=1, full_name='Administrator')
            logger.debug('site.prefs file created')
        else:
            self.open_pref_file()

    def create_user(self, add_user_name=None, promotion='Staff', email=None, password=None, admin=0, full_name=None):
        # Read the setting file
        # settings = open_pref_file()
        self.open_pref_file()
        # Check if a user_name was given
        if not add_user_name:
            logger.warning('Please enter a name')
            return 0
        elif add_user_name == '':
            logger.warning('Please enter a valid name')
            return 0
        # Check if user_name already exists
        elif add_user_name in self.settings[defaults._users_list_key_]:
            logger.warning('User "{}" already exists'.format(add_user_name))
            return 0
        # Check if password is legal
        elif not util.check_illegal(password) and password != '':
            logger.warning('Illegal password, only use a-z, A-Z, 1-9')
            return 0
        elif not full_name or full_name == '':
            logger.warning('Please enter your full name')
            return 0
        elif not email:
            logger.warning('Please enter a valid email')
        else:
            # create new user_dic
            user_dic = dict()
            user_dic[defaults._user_name_key_] = add_user_name
            user_dic[defaults._promotion_key_] = promotion
            user_dic[defaults._user_email_key_] = email
            user_dic[defaults._password_key_] = pw.encrypt(password)
            user_dic[defaults._admin_key_] = admin
            user_dic[defaults._full_name_key_] = full_name
            # Append user to the list of users
            self.settings[defaults._users_list_key_][add_user_name] = user_dic
            # Write the setting file
            self.write_pref_file()
            
            logger.info('User "{}" created'.format(add_user_name))
            logger.debug('  Users names : {}'.format(self.settings[defaults._users_list_key_]))
            return 1

    def change_user_password(self, user, password):
        if user in self.get_users_list():
            # settings = open_pref_file()
            self.open_pref_file()
            self.settings[defaults._users_list_key_][user][defaults._password_key_] = password
            self.write_pref_file()
        else:
            logger.error("User {} doesn't exists".format(user))

    def add_project(self, project_name=None, project_path=None, password=None):
        # settings = open_pref_file()
        self.open_pref_file()
        if project_name in self.settings[defaults._projects_list_key_]:
            logger.warning('Project "{}" already exists'.format(project_name))
            return 0
        else:
            new_project_dic = dict()
            new_project_dic[defaults._project_name_key_] = project_name
            new_project_dic[defaults._project_path_key_] = project_path
            new_project_dic[defaults._password_key_] = pw.encrypt(password)
            # Check the password concordance
            self.settings[defaults._projects_list_key_][project_name] = new_project_dic
            logger.debug('   Projects : {}'.format(self.settings[defaults._projects_list_key_]))
            self.write_pref_file()
            return 1

    def get_users_list(self):
        # Read the site_prefs file to get all users list
        # Read the setting file
        # settings = open_pref_file()
        self.open_pref_file()
        if self.settings:
            value = self.settings[defaults._users_list_key_]
            return value
        else:
            return None

    def get_projects_list(self):
        # settings = open_pref_file()
        self.open_pref_file()
        if self.settings:
            value = self.settings[defaults._projects_list_key_]
            return value
        else:
            return None

    def clean_projects(self):
        pass
        '''
        for project in self.get_projects_list():
            project_path = self.get_project_path_from_name(project)
            if not os.path.isdir(project_path):
                logger.warning("Removing unfound project : {}".format(project))
                self.remove_project(project)
        '''

    def remove_project(self, project_name):
        self.open_pref_file()
        if self.settings:
            projects_list = self.settings[defaults._projects_list_key_]
            if project_name in projects_list:
                del self.settings[defaults._projects_list_key_][project_name]
            self.write_pref_file()

    def get_project_path_from_name(self, project_name):
        projects = self.get_projects_list()
        self.open_pref_file()
        if projects and (project_name in projects):
            # settings = open_pref_file()
            project_path = self.settings[defaults._projects_list_key_] \
                [project_name] \
                [defaults._project_path_key_]
            return project_path
        else:
            return None

    def get_email_from_user(self, user):
        # settings = open_pref_file()
        self.open_pref_file()
        users_list = self.settings[defaults._users_list_key_]
        if user in users_list:
            email = self.settings[defaults._users_list_key_][user][defaults._user_email_key_]
            return email
        else:
            logger.warning("User {} doesn't exists...".format(user))

    def get_user_promotion(self, user):
        # settings = open_pref_file()
        self.open_pref_file()
        users_list = self.settings[defaults._users_list_key_]
        if user in users_list:
            promotion = self.settings[defaults._users_list_key_][user][defaults._promotion_key_]
            return promotion
        else:
            logger.warning("User {} doesn't exists...".format(user))

    def get_user_admin(self, user):
        # settings = open_pref_file()
        self.open_pref_file()
        users_list = self.settings[defaults._users_list_key_]
        if user in users_list:
            admin = self.settings[defaults._users_list_key_][user][defaults._admin_key_]
            return admin
        else:
            logger.warning("User {} doesn't exists...".format(user))

    def get_user_full_name(self, user):
        # settings = open_pref_file()
        self.open_pref_file()
        users_list = self.settings[defaults._users_list_key_]
        if user in users_list:
            if defaults._full_name_key_ in self.settings[defaults._users_list_key_][user].keys():
                full_name = self.settings[defaults._users_list_key_][user][defaults._full_name_key_]
            else:
                self.settings[defaults._users_list_key_][user][defaults._full_name_key_] = 'No name'
                self.write_pref_file()
                full_name = 'No name'
            return full_name
        else:
            logger.warning("User {} doesn't exists...".format(user))

    def password_check(self, user_name, password):
        # Read the site_prefs to get a password from a user
        # Read the setting file
        # settings = open_pref_file()
        self.open_pref_file()
        # Check if the password is right using the "password.py" module
        if not user_name or user_name == '':
            logger.info(defaults._missing_user_)
        else:
            value = self.settings[defaults._users_list_key_][user_name][defaults._password_key_]
            if pw.decrypt(value, password):
                logger.info('Logged !')
                return True
            else:
                logger.error('Wrong password')
                return False

    def project_password_check(self, project_name, password):
        # Read the site_prefs to get a password from a user
        # Read the setting file
        # settings = open_pref_file()
        self.open_pref_file()
        # Check if the password is right using the "password.py" module
        value = self.settings[defaults._projects_list_key_][project_name][defaults._password_key_]
        if pw.decrypt(value, password):
            logger.info('Access granted !')
            return True
        else:
            logger.error('Wrong password')
            return False

    def write_pref_file(self, new=0):
        self.database.write(0, self.get_site_file(), self.settings)

    def open_pref_file(self):
        if self.is_prefs():
            site_file = self.get_site_file()
            self.settings = self.database.read(0, site_file)
        else:
            logger.warning("Prefs file doesn't exist : {}".format(self.get_site_file()))

    def is_prefs(self):
        # Check the pref_file presence
        if not self.database.isfile(0, os.environ[defaults._site_var_]):
            return 0
        else:
            return 1

    def get_site_file(self):
        return os.environ[defaults._site_var_]
