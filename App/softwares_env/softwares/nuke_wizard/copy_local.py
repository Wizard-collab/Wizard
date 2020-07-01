import time
import nuke
import os
import shutil
from wizard.prefs.main import prefs

prefs = prefs()

def copy_local(ref_path, files_list):
	t = nuke.ProgressTask("Copying files to local drive")

	project_path = prefs.project_path
	local_project_path = prefs.local_project_path

	percent = 0.0
	percent_step = 100/len(files_list)

	for file in files_list:
		if local_project_path != '':
			project_file = os.path.join(project_path, ref_path, file)
			local_file = os.path.join(local_project_path, ref_path, file)
			percent += percent_step
			t.setProgress(int(percent))
			t.setMessage("Copying {} to local drive".format(file))
			local_dir = os.path.split(local_file)[0]
			if not os.path.isdir(local_dir):
				os.makedirs(local_dir)
			shutil.copyfile(project_file, local_file)
