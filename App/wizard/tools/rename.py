# coding: utf-8
import os
from wizard.tools import log
import time

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
				file_name = "{}_{}".format(self.conform_string(self.prefix, index), file_name)

			if self.suffix != '':
				file_name = "{}_{}".format(file_name, self.conform_string(self.suffix, index))

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
		if contains_duplicates:
			logger.warning("The new files list contains duplicates")
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

		return string

	def apply(self):
		if not self.is_duplicates():
			for file in self.files_list:
				try:
					old_file = os.path.join(self.folder, file)
					new_file = os.path.join(self.folder, self.modified_list[self.files_list.index(file)])
					logger.info("Renaming {} > {}".format(old_file, new_file))
					os.rename(old_file, new_file)
				except FileNotFoundError:
					logger.warning("<{}> not found".format(old_file))
