from wizard.prefs.main import prefs
from wizard.tools import log
from wizard.vars import defaults
from wizard.tools import utility as utils
import shutil

import importlib
importlib.reload(defaults)

import yaml
import os

import sys

prefs = prefs()
logger = log.pipe_log(__name__)

class user_scripts():
	def __init__(self):
		self.file = defaults._user_scripts_file_
		if prefs.project_path:
			self.project_file = os.path.join(prefs.project_path, defaults._project_script_file_)
		else:
			self.project_file = None
		self.init_scripts_paths()
		self.read_file()
		self.read_project_file()

	def init_scripts_paths(self):
		if not os.path.exists(defaults._user_custom_scripts_path_):
			os.makedirs(defaults._user_custom_scripts_path_)
		sys.path.append(defaults._user_custom_scripts_path_.replace('\\', '/'))

		if prefs.project_path:
			project_custom_scripts_path = os.path.join(prefs.project_path, defaults._project_custom_scripts_path_)
			if not os.path.exists(project_custom_scripts_path):
				os.makedirs(project_custom_scripts_path)
			sys.path.append(project_custom_scripts_path.replace('\\', '/'))

	def create_user_script(self, name, image, script, only_subprocess, project=None):

		local_image_path = image
		shared_folder = os.path.join(prefs.project_path, defaults._shared_folder_)
		if not os.path.isdir(shared_folder):
			os.makedirs(shared_folder)
		shared_image_path_raw = os.path.join(shared_folder, os.path.basename(image))
		shared_image_path = utils.get_filename_without_override(shared_image_path_raw)
		shutil.copyfile(local_image_path, shared_image_path)

		script_dic = dict()
		script_dic[defaults._user_script_image_] = shared_image_path
		script_dic[defaults._user_script_name_] = name
		script_dic[defaults._user_script_] = script
		script_dic[defaults._subprocess_] = only_subprocess
		script_dic[defaults._project_] = project
		if not project:
			self.main_dic[defaults._user_scripts_][name] = script_dic
			self.write_script_file()
		else:
			self.project_dic[defaults._user_scripts_][name] = script_dic
			self.write_project_script_file()

	def init_file(self):
		self.main_dic = dict()
		self.main_dic[defaults._user_scripts_] = dict()
		self.write_script_file()

	def init_project_file(self):
		self.project_dic = dict()
		self.project_dic[defaults._user_scripts_] = dict()
		self.write_project_script_file()

	def write_script_file(self):
		with open(self.file, 'w') as f:
			f.write(yaml.dump(self.main_dic))

	def write_project_script_file(self):
		if self.project_file:
			with open(self.project_file, 'w') as f:
				f.write(yaml.dump(self.project_dic))

	def delete_script(self, key):
		self.read_file()
		self.read_project_file()
		if key in self.main_dic[defaults._user_scripts_].keys():
			del self.main_dic[defaults._user_scripts_][key]
			self.write_script_file()
		if key in self.project_dic[defaults._user_scripts_].keys():
			del self.project_dic[defaults._user_scripts_][key]
			self.write_project_script_file()

	def read_file(self):
		if self.is_file():
			with open(self.file, 'r') as f:
				self.main_dic = yaml.load(f.read(), Loader = yaml.Loader)
		else:
			self.init_file()

	def read_project_file(self):
		if self.is_project_file():
			with open(self.project_file, 'r') as f:
				self.project_dic = yaml.load(f.read(), Loader = yaml.Loader)
		else:
			self.init_project_file()

	def get_scripts_as_dic(self):
		self.read_file()
		return self.main_dic

	def get_project_scripts_as_dic(self):
		self.read_project_file()
		return self.project_dic

	def is_file(self):
		return os.path.isfile(self.file)

	def is_project_file(self):
		if self.project_file:
			return os.path.isfile(self.project_file)
		else:
			return None


