# coding: utf-8

"""
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

"""
# Defaults Python modules
import os

from wizard.prefs.site import site
from wizard.prefs.user import user
# Wizard tools modules
from wizard.tools import log
from wizard.tools import utility as util
# Wizard variables modules
from wizard.vars import defaults

# Create the main logger
logger = log.pipe_log(__name__)

database = util.database()


def get_current_project_prefs_file():
    # Get the pref file from the current project
    # (from user prefs)
    project_name = user().get_current_project_name()
    if project_name:
        project_path = site().get_project_path_from_name(project_name)
    else:
        project_path = None
    if project_path:
        project = os.path.join(project_path, defaults._project_)
        # Write the pref_path in console (debug level)
        logger.debug(project)
        return project
    else:
        return 0


def init_prefs(settings):
    write_pref_file(settings)


def open_pref_file():
    _project_ = get_current_project_prefs_file()
    if _project_:
        settings = database.read(2, _project_)
        return settings
    else:
        logger.warning("Prefs file doesn't exist : {}".format(_project_))
        return 0


def write_pref_file(settings):
    _project_ = get_current_project_prefs_file()
    if _project_:
        database.write(2, _project_, settings)
        logger.debug('project.wd file updated')


def get_abs_site():
    settings = open_pref_file()
    if settings:
        return settings[defaults._abs_site_]
    else:
        return None


def get_server_ip():
    settings = open_pref_file()
    if settings:
        return settings[defaults._server_ip_]
    else:
        return None

def set_server_ip(ip):
    settings = open_pref_file()
    settings[defaults._server_ip_] = ip
    write_pref_file(settings)

def add_user(user):
    settings = open_pref_file()
    if defaults._users_list_key_ not in settings.keys():
        settings[defaults._users_list_key_] = []
    if user not in settings[defaults._users_list_key_]:
        settings[defaults._users_list_key_].append(user)
    write_pref_file(settings)

def get_users():
    settings = open_pref_file()
    if defaults._users_list_key_ not in settings.keys():
        settings[defaults._users_list_key_] = []
    return settings[defaults._users_list_key_]

def init_extension_dic():
    settings = open_pref_file()
    if defaults._project_extension_dic_key_ not in settings.keys():
        settings[defaults._project_extension_dic_key_] = defaults._pub_ext_dic_
        write_pref_file(settings)

def add_camera_extension():
    init_extension_dic()
    settings = open_pref_file()
    if defaults._camera_ not in settings[defaults._project_extension_dic_key_].keys():
        settings[defaults._project_extension_dic_key_][defaults._camera_] = defaults._pub_ext_dic_[defaults._camera_]
        write_pref_file(settings)

def init_setdress_workflow():
    settings = open_pref_file()
    if defaults._project_setdress_workflow_ not in settings.keys():
        settings[defaults._project_setdress_workflow_] = defaults._abc_workflow_
        write_pref_file(settings)

def get_extension_dic():
    settings = open_pref_file()
    return settings[defaults._project_extension_dic_key_]

def set_extension_dic(extension_dic):
    settings = open_pref_file()
    settings[defaults._project_extension_dic_key_] = extension_dic
    write_pref_file(settings)

def set_setdress_workflow(workflow):
    settings = open_pref_file()
    settings[defaults._project_setdress_workflow_] = workflow
    write_pref_file(settings)

def get_setdress_workflow():
    settings = open_pref_file()
    return settings[defaults._project_setdress_workflow_]

def get_frame_rate():
    settings = open_pref_file()
    return settings[defaults._frame_rate_key_]

def get_format():
    settings = open_pref_file()
    format = settings[defaults._format_key_]
    if type(format[0]) == str:
        format[0] = int(format[0])
    if type(format[1]) == str:
        format[1] = int(format[1])
    return format
 
def set_format(format):
    settings = open_pref_file()
    settings[defaults._format_key_] = format
    write_pref_file(settings)

def set_frame_rate(f_rate):
    settings = open_pref_file()
    settings[defaults._frame_rate_key_] = f_rate
    write_pref_file(settings)

def get_color_managment():
    settings = open_pref_file()
    return settings[defaults._color_management_key_]

def is_prefs():
    # Check the pref_file presence
    project = get_current_project_prefs_file()
    if project and database.isfile(2, project):
        return project
    else:
        logger.warning("Your project exists but doesn't have preferences...")
        return 0
