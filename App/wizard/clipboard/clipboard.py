from wizard.tools import log
from wizard.vars import defaults
from wizard.prefs.main import prefs
from wizard.tools import utility as utils
import wizard.asset.main as asset_core
import yaml
import os

logger = log.pipe_log()
prefs = prefs()

def copy_file(file_path):
	clipboard_data = get_clipboard_data()
	clipboard_data[defaults._clipboard_work_scene_path_] = file_path
	write_clipboard(clipboard_data)

def get_file():
	clipboard_data = get_clipboard_data()
	file = None
	if defaults._clipboard_work_scene_path_ in clipboard_data.keys():
		file = clipboard_data[defaults._clipboard_work_scene_path_]
	return file

def copy_references(references_list):
	clipboard_data = get_clipboard_data()
	string_refs_list = []
	for asset in references_list:
		string_refs_list.append(utils.asset_to_string(asset))
	clipboard_data[defaults._clipboard_reference_list_] = string_refs_list
	write_clipboard(clipboard_data)

def get_references():
	clipboard_data = get_clipboard_data()
	assets_list = []
	if defaults._clipboard_reference_list_ in clipboard_data.keys():
		assets_list = clipboard_data[defaults._clipboard_reference_list_]
	return assets_list

def get_clipboard_data():
	if os.path.isfile(defaults._clipboard_file_):
		with open(defaults._clipboard_file_, 'r') as f:
			clipboard_data = yaml.load(f, Loader=yaml.Loader)
	else:
		clipboard_data = dict()
		clipboard_data[defaults._clipboard_work_scene_path_] = ''
		clipboard_data[defaults._clipboard_reference_list_] = []
	logger.info(clipboard_data)
	return clipboard_data

def write_clipboard(clipboard_data):
	with open(defaults._clipboard_file_, 'w') as f:
		yaml.dump(clipboard_data, f)

