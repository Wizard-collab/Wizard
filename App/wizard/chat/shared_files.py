from wizard.prefs.main import prefs
from wizard.vars import defaults
from wizard.tools import log
from wizard.tools import utility as utils
import os
import shutil

logger = log.pipe_log(__name__)


class shared_files():
	def __init__(self):
		self.create_folder()

	def create_folder(self):
		shared_folder = os.path.join(prefs().project_path, defaults._shared_folder_)
		if not os.path.isdir(shared_folder):
			os.mkdir(shared_folder)
		self.shared_folder = shared_folder

	def add_file(self, base_file):
		extension = os.path.splitext(base_file)[1]
		file = '{}{}'.format(utils.id_based_time(), extension)
		file_name = os.path.join(self.shared_folder, file)
		shutil.copy(base_file, file_name)
		return file_name


