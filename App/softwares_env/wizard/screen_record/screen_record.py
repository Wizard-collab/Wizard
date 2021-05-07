from PyQt5 import QtCore
import pyautogui
import cv2
import numpy as np
import time
from wizard.tools import utility as utils
import os
from wizard.vars import defaults

class screen_record(QtCore.QThread):
	def __init__(self):
		super(screen_record, self).__init__()
		self.running = False

	def run(self):

		filepath = defaults._screen_records_path_
		if not os.path.isdir(filepath):
			os.makedirs(filepath)
		filename = utils.get_filename_without_override(defaults._screen_records_file_)

		self.running = True
		# Specify resolution
		resolution = (1920, 1080)
		# Specify video codec
		codec = cv2.VideoWriter_fourcc(*'H264')
		# Specify frames rate. We can choose any 
		# value and experiment with it
		fps = 10.0
		# Creating a VideoWriter object
		out = cv2.VideoWriter(filename, codec, fps, resolution)
		  
		while self.running:
		    # Take screenshot using PyAutoGUI
		    img = pyautogui.screenshot()
		    # Convert the screenshot to a numpy array
		    frame = np.array(img)
		    # Convert it from BGR(Blue, Green, Red) to
		    # RGB(Red, Green, Blue)
		    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
		    # Write it to the output file
		    out.write(frame)
		    if cv2.waitKey(1) == ord('q'):
        		break
		  
		# Release the Video writer
		out.release()
		# Destroy all windows
		cv2.destroyAllWindows()

	def stop(self):
		self.running=False