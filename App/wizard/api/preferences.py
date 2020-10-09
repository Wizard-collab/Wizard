# coding: utf-8

""" This module is the user API of Wizard. 
	It gives access to the wizard functions in a simple way

	Author : BRUNEL Leo """

from wizard.vars import defaults # The wizard defaults module, contains all wizard constants
from wizard.tools import utility # Some wizard tools
from wizard.prefs.main import prefs # The access to all the prefs files
from wizard.asset import main as asset_core # The wizard asset core module
from wizard.tools import log # The wizard main logger
from wizard.asset import main as asset_core # Import the asset main module to manipulate assets
from wizard.asset.reference import references # Import the asset reference module to create references
import os

prefs = prefs()
logger = log.pipe_log(__name__)


def get_site_path():
	'''This function return the wizard site path'''
	return os.environ[defaults._wizard_site_]

def get_current_user():
	'''This function return current logged wizard user'''
	return prefs.user

def get_all_users():
	'''This function return all the site users'''
	return list(prefs.site.users.keys())

def get_user_email(user=None):
	'''This function return the email of the requested user
		'user' : the user as string
		If the user doesn't exists, wizard return 'None' 
		If no user is given, wizard return the current user email'''
	if not user:
		user = prefs.user
	if user in get_all_users():
		return prefs.get_email_from_user(user)
	else:
		return None

def get_user_admin(user=None):
	'''This function check if the user is 'administrator' and return a boolean 
		'user' : the user as string
		If no user is given, wizard return the current user admin status'''
	if not user:
		user = prefs.user
	return prefs.admin_from_user(user)

def get_user_full_name(user=None):
	'''This function return the full name of the requested user 
		'user' : the user as string
		If the user doesn't exists, wizard return 'None'
		If no user is given, wizard return the current user full name'''
	if not user:
		user = prefs.user
	if user in get_all_users():
		return prefs.get_full_name_from_user(user)
	else:
		return None

def get_current_project():
	'''This function return current wizard project name of the current user'''
	return prefs.project_name

def get_all_projects():
	'''This function return all the site projects'''
	return list(prefs.site.projects.keys())

def get_project_path(project_name=None):
	'''This function return the project path of the requested project
		'project_name' : the project name as string
		If the project doesn't exists, wizard return 'None'
		If no project name is given, wizard return the current project path'''
	if not project_name:
		project_name = prefs.project_name
	if project_name in get_all_projects():
		return prefs.get_path_from_project(project_name)
	else:
		return None

def get_project_format():
	'''This function return the format of the current project'''
	return prefs.format

def get_project_frame_rate():
	'''This function return the frame rate of the current project'''
	return prefs.frame_rate