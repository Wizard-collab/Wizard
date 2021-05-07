# Defaults Python modules
import os
import pickle
from pynput import keyboard

# Wizard tools modules
from wizard.tools import log
from wizard.tools import utility as util
# Wizard variables modules
from wizard.vars import defaults

# Create the main logger
logger = log.pipe_log(__name__)
# Write the pref_path in console (debug level)

class shortcuts_prefs():
	def __init__(self):
		self.shortcuts_prefs_file = defaults._shortcuts_prefs_file_
		self.read_prefs()

	def read_prefs(self):
		if os.path.isfile(self.shortcuts_prefs_file):
			with open(self.shortcuts_prefs_file, 'rb') as f:
				self.shortcuts_dic = pickle.load(f)
		else:
			self.shortcuts_dic = dict()
			self.shortcuts_dic[defaults._screen_record_] = {keyboard.Key.f3}
			self.write_prefs()

	def write_prefs(self):
		with open(self.shortcuts_prefs_file, 'wb') as f:
			pickle.dump(self.shortcuts_dic, f)
