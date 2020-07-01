import subprocess
import os
import shutil

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

command_line = "PyInstaller wizard_server.spec"
p = subprocess.Popen(command_line)
p.wait()

file = 'dist/wizard server/wizard server.exe'
dest = 'dist/wizard/wizard server.exe'
shutil.copyfile(file, dest)
shutil.rmtree('dist/wizard server')

command_line = "PyInstaller wizard_site_debug.spec"
p = subprocess.Popen(command_line)
p.wait()

file = 'dist/wizard console/wizard console.exe'
dest = 'dist/wizard/wizard console.exe'
shutil.copyfile(file, dest)
shutil.rmtree('dist/wizard console')

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

file = 'dist/file viewer/file viewer.exe'
dest = 'dist/wizard/file viewer.exe'
shutil.copyfile(file, dest)
shutil.rmtree('dist/file viewer')

file = 'updater.exe'
dest = 'dist/wizard/updater.exe'
shutil.copyfile(file, dest)
