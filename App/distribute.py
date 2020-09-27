import subprocess
import os
import shutil
from playsound import playsound


if os.path.isdir('dist'):
	shutil.rmtree('dist')

if os.path.isdir('build'):
	shutil.rmtree('build')

command_line = "PyInstaller wizard_site.spec"
p = subprocess.Popen(command_line)
p.wait()

folders_list = ['ressources', 'PIL', 'cv2', 'numpy']

for folder in folders_list:
	destination = os.path.join('dist/wizard', folder)
	shutil.copytree(folder, destination)

destination = 'dist/wizard/softwares_env/wizard'
shutil.copytree('wizard', destination)

destination = 'dist/wizard/softwares_env/softwares'
shutil.copytree('softwares_env/softwares', destination)

command_line = "PyInstaller wizard_site_debug.spec"
p = subprocess.Popen(command_line)
p.wait()

file = 'dist/wizard_console/wizard_console.exe'
dest = 'dist/wizard/wizard_console.exe'
shutil.copyfile(file, dest)
shutil.rmtree('dist/wizard_console')

command_line = "PyInstaller pywizard.spec"
p = subprocess.Popen(command_line)
p.wait()

file = 'dist/pywizard/pywizard.exe'
dest = 'dist/wizard/pywizard.exe'
shutil.copyfile(file, dest)
shutil.rmtree('dist/pywizard')

command_line = "PyInstaller file_viewer.spec"
p = subprocess.Popen(command_line)
p.wait()

file = 'dist/file_viewer/file_viewer.exe'
dest = 'dist/wizard/file_viewer.exe'
shutil.copyfile(file, dest)
shutil.rmtree('dist/file_viewer')

file = 'updater.exe'
dest = 'dist/wizard/updater.exe'
shutil.copyfile(file, dest)


dist_path = os.path.abspath('dist/wizard/')

playsound('1631.wav')

os.startfile(dist_path)

