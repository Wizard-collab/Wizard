# coding: utf8

# Import PyQt5 libraries
from PyQt5.QtWidgets import *

class Main(QWidget):
	def __init__(self):
		super(Main, self).__init__()
		layout = QVBoxLayout()
		layout.setContentsMargins(0,0,0,0)
		self.progress_bar_widget = QProgressBar()
		layout.addWidget(self.progress_bar_widget)
		self.setLayout(layout)
		self.progress_bar_widget.setValue(0)
		self.setMaximumHeight(1)
		self.progress_bar_widget.setMaximumHeight(1)
		self.progress_bar_widget.setTextVisible(0)
		self.progress_bar_widget.setStyleSheet('''::chunk{
													background-color: #7785de;
													margin:0px;
													padding:0px;
													border-radius: 0px;
												}''')
	def set_progress(self, value):
		self.progress_bar_widget.setValue(value)
