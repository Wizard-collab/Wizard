import os
import shutil
from wizard.vars import defaults
from wizard.tools import log

logger = log.pipe_log()

def setup_painter():

	plugin_folder = os.path.abspath(defaults._substance_plugin_)

	#if not os.path.isdir(defaults._substance_plugin_path_):
	try:
		if not os.path.isdir(defaults._substance_plugin_path_):
			os.mkdir(defaults._substance_plugin_path_)
		for file in os.listdir(plugin_folder):
			shutil.copy(os.path.join(plugin_folder, file), os.path.join(defaults._substance_plugin_path_, file))

	except PermissionError:
		logger.warning("You don't have the permission to access the Substance plugin folder")