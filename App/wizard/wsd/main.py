import yaml

class wsd():
	
	def __init__(self, file, dict):
		self.file = file
		self.dict = dict

	def write_sd(self):
		with open(self.file, 'w') as f:
			f.write(yaml.dump(self.dict))