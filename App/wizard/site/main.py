import os
from wizard.vars import defaults
from wizard.tools import log
import subprocess
from wizard.tools import utility as utils

logger = log.pipe_log(__name__)

def is_site():
	site_file = os.path.join(defaults._user_path_, 'site.wd')
	if os.path.isfile(site_file):
		site = utils.database().read(0, site_file)
		if site == 'null':
			return 0
		else:
			if os.path.isdir(site):
				return 1
			else:
				return 0
	else:
		return 0

def modify_site(site_path):
	logger.info(site_path)
	site_path = site_path.replace('\\', '/')
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

		site_file = os.path.join(defaults._user_path_, 'site.wd')
		utils.database().write(0, site_file, site_path)

		#subprocess.Popen('setx {} {}'.format(defaults._wizard_site_, site_path))

	else:
		logger.warning("{} doesn't exists".format(site_path))
