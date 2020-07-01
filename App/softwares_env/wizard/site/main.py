import os
from wizard.vars import defaults
from wizard.tools import log
import subprocess

logger = log.pipe_log(__name__)

def is_site():
	keys_list = os.environ.keys()
	logger.info(keys_list)
	if defaults._wizard_site_ in keys_list:
		if os.environ[defaults._wizard_site_] == 'null':
			return 0
		else:
			if os.path.isdir(os.environ[defaults._wizard_site_]):
				return 1
			else:
				return 0
	else:
		return 0

def modify_site(site_path):

	if os.path.isdir(site_path):

		site_path = os.path.join(site_path, 'wizard_site')
		if not os.path.isdir(site_path):
			os.makedirs(site_path)

		data_path = os.path.join(site_path, 'Data')
		logger.info(data_path)
		if not os.path.isdir(data_path):
			os.makedirs(data_path)

		avatars_path = os.path.join(data_path, 'avatars')
		logger.info(avatars_path)
		if not os.path.isdir(avatars_path):
			os.makedirs(avatars_path)

		os.environ[defaults._wizard_site_] = site_path
		subprocess.Popen('setx {} {}'.format(defaults._wizard_site_, site_path))

	else:
		logger.warning("{} doesn't exists".format(site_path))
