from wizard.prefs.main import prefs
from wizard.tools import log
from wizard.vars import defaults

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
		self.custom_scripts_path = defaults._user_custom_scripts_path_
		self.init_scripts_path()
		self.read_file()

	def init_scripts_path(self):
		if not os.path.exists(self.custom_scripts_path):
			os.makedirs(self.custom_scripts_path)
		sys.path.append(self.custom_scripts_path)

	def create_user_script(self, name, image, script):

		script_dic = dict()
		script_dic[defaults._user_script_image_] = image
		script_dic[defaults._user_script_name_] = name
		script_dic[defaults._user_script_] = script
		self.main_dic[defaults._user_scripts_][name] = script_dic
		self.write_script_file()

	def init_file(self):
		self.main_dic = dict()
		self.main_dic[defaults._user_scripts_] = dict()
		self.write_script_file()

	def write_script_file(self):
		with open(self.file, 'w') as f:
			f.write(yaml.dump(self.main_dic))

	def delete_script(self, key):
		self.read_file()
		if key in self.main_dic[defaults._user_scripts_].keys():
			del self.main_dic[defaults._user_scripts_][key]
			self.write_script_file()

	def read_file(self):
		if self.is_file():
			with open(self.file, 'r') as f:
				self.main_dic = yaml.load(f.read(), Loader = yaml.Loader)
		else:
			self.init_file()

	def get_scripts_as_dic(self):
		self.read_file()
		return self.main_dic

	def is_file(self):
		return os.path.isfile(self.file)


