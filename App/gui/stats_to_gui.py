try:
	from PyQt5.QtCore import QThread, pyqtSignal
except ImportError:
	logger.info('Cannot import PyQt5')

import time
import psutil

class statThread(QThread):

	ram_signal = pyqtSignal(float)
	cpu_signal = pyqtSignal(float)

	def __init__(self, main_ui):
		super(statThread, self).__init__(main_ui)
		self.running=True

	def run(self):
		while self.running:
			ram = dict(psutil.virtual_memory()._asdict())['percent']
			self.ram_signal.emit(float(ram))
			self.cpu_signal.emit(float(psutil.cpu_percent()))
			time.sleep(0.5)

	def stop(self):
		self.running=False
