# coding: utf-8
import os
from wizard.tools import log
import time
from wizard.tools import utility as utils
from wizard.prefs.main import prefs

prefs = prefs()

logger = log.pipe_log(__name__)

class renamer:
	def __init__(self, folder = None):

		self.suffix = ''
		self.prefix = ''
		self.find_and_replace = ['', '']
		self.override = ''
		self.override_extension = ''
		self.start_at = 0
		self.uppercase = False
		self.lowercase = False
		self.start_crop = 0
		self.end_crop = 0
		self.first_splitter = '_'
		self.second_splitter = '_'

		self.undo_source = []
		self.undo_destination = []

		self.set_folder(folder)
		self.get_files_list()

	def set_folder(self, folder):

		if folder:
			if os.path.isdir(folder):
				self.folder = folder
				self.get_files_list()
			else:
				logger.warning("Folder <{}> doesn't exists or isn't accessible".format(folder))
				self.folder = None
				self.get_files_list()
		else:
			self.folder = folder

	def get_files_list(self):

		self.files_list = []
		if self.folder:
			for file in os.listdir(self.folder):
				if os.path.isfile(os.path.join(self.folder, file)):
					self.files_list.append(file)
		else:
			logger.warning("Please set a valid folder")
			self.files_list = []

	def sort_files_list(self, invert=0):
		self.files_list = sorted(self.files_list)
		if invert:
			self.files_list.reverse()

	def sort_by_time(self, invert=0):
		self.files_list.sort(key=lambda x: os.path.getmtime(os.path.join(self.folder, x)))
		if invert:
			self.files_list.reverse()

	def modify_file_name(self):

		self.modified_list = []
		if self.override_extension != "":
			logger.warning("Modifying extension can corrupt all your files")

		for file in self.files_list:

			index = self.files_list.index(file) + int(self.start_at)

			file_name = os.path.splitext(file)[0]
			extension = os.path.splitext(file)[-1]

			if self.find_and_replace[0] != '' and self.override == '':
				file_name = file_name.replace(self.find_and_replace[0], self.conform_string(self.find_and_replace[1], index))
			elif self.override != '':
				file_name = self.conform_string(self.override, index)

			if self.start_crop:
				file_name = file_name[self.start_crop:]
			if self.end_crop:
				file_name = file_name[:-self.end_crop]

			if self.prefix != '':
				file_name = "{}{}{}".format(self.conform_string(self.prefix, index), self.first_splitter, file_name)

			if self.suffix != '':
				file_name = "{}{}{}".format(file_name, self.second_splitter, self.conform_string(self.suffix, index))

			if self.override_extension != '':
				extension = ".{}".format(self.override_extension)

			if self.uppercase:
				file_name = file_name.upper()

			if self.lowercase:
				file_name = file_name.lower()

			file = file_name + extension

			self.modified_list.append(file)
			self.is_duplicates()

	def is_duplicates(self):
		contains_duplicates = any(self.modified_list.count(element) > 1 for element in self.modified_list)
		return contains_duplicates

	def conform_string(self, string, index=None):

		is_tag = "#" in string

		if is_tag and index!=None:
			tag_index = string.index("#")
			try:
				number = string[tag_index+1]
				int(number)
			except:
				number = None

			if number:
				string = string.replace("#{}".format(number), str(index).zfill(int(number)))
			else:
				string = string.replace("#", str(index))

		strings = time.strftime("%Y,%m,%d,%H,%M,%S")
		t = strings.split(',')

		string = string.replace("%YEAR", str(t[0]))
		string = string.replace("%MONTH", str(t[1]))
		string = string.replace("%DAY", str(t[2]))
		string = string.replace("%HOUR", str(t[3]))
		string = string.replace("%MINUT", str(t[4]))
		string = string.replace("%SECOND", str(t[5]))
		string = string.replace("%RANDOM", utils.random_string())
		string = string.replace("%RANDINT", utils.random_number())
		string = string.replace("%PROJECT", prefs.project_name)
		string = string.replace("%USER", prefs.user)

		return string

	def apply(self):
		if not self.is_duplicates():

			old_files_list = []
			temp_files_list = []
			new_files_list = []

			self.undo_source = []
			self.undo_destination = []

			for file in self.files_list:
				try:

					old_file = os.path.join(self.folder, file)
					old_files_list.append(old_file)
					self.undo_source.append(old_file)

					temp_file = os.path.join(self.folder, utils.random_string())
					temp_files_list.append(temp_file)

					new_file = os.path.join(self.folder, self.modified_list[self.files_list.index(file)])
					new_files_list.append(new_file)
					self.undo_destination.append(new_file)

					logger.info("Renaming {} > {}".format(old_file, new_file))
					os.rename(old_file, temp_file)

				except FileNotFoundError:
					logger.warning("<{}> not found".format(old_file))

			for temp_file in temp_files_list:
				os.rename(temp_file, new_files_list[temp_files_list.index(temp_file)])


		else:
			logger.warning("The new files list contains duplicates")

	def undo(self):
		old_files_list = []
		temp_files_list = []
		new_files_list = []

		print(self.undo_source)
		print(self.undo_destination)

		for file in self.undo_destination:
			try:

				old_file = os.path.join(self.folder, file)
				old_files_list.append(old_file)

				temp_file = os.path.join(self.folder, utils.random_string())
				temp_files_list.append(temp_file)

				new_file = os.path.join(self.folder, self.undo_source[self.undo_destination.index(file)])
				new_files_list.append(new_file)

				logger.info("Renaming {} > {}".format(old_file, new_file))
				os.rename(old_file, temp_file)

			except FileNotFoundError:
				logger.warning("<{}> not found".format(old_file))

		for temp_file in temp_files_list:
			os.rename(temp_file, new_files_list[temp_files_list.index(temp_file)])
