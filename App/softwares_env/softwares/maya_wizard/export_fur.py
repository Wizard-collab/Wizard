import sys
if sys.platform == "win32":
    import ctypes
    ctypes.windll.kernel32.SetDllDirectoryA(None)

import maya.cmds as cmds
import maya.standalone
maya.standalone.initialize()

from wizard.tools import log
from wizard.asset import main as asset_core
from wizard.vars import defaults
from wizard.prefs.main import prefs
from wizard.project import wall
import shutil
import traceback
from wizard.tools import utility as utils
import os
import time

import maya.cmds as cmds
#cmds.loadPlugin( allPlugins=True )
try:
	cmds.loadPlugin( 'pgYetiMaya.mll' )

except:
	print(str(traceback.format_exc()))

cmds.loadPlugin( 'AbcImport.mll' )
cmds.loadPlugin( 'AbcExport.mll' )

logger = log.pipe_log(__name__)

class export_fur():

	def __init__(self, string_asset, file, nspace_list, frange, set_done=1):
		self.asset = asset_core.string_to_asset(string_asset)
		self.file = file
		self.nspace_list = nspace_list
		self.range = frange
		self.references_list = prefs().asset(self.asset).software.references
		self.set_done = set_done

	def export_fur(self):

		percent_step = 100.0/len(self.nspace_list)
		percent = 0.0
		print('status:Starting...')
		print('percent:'+str(percent))

		for nspace in self.nspace_list:

			print('status:Working...')

			print('current_task:Exporting {}'.format(nspace))
			cmds.file(self.file, o=True, f=True)

			self.fur_asset = asset_core.string_to_asset(self.references_list[nspace][defaults._asset_key_])
			self.count = nspace.split('_')[-1]

			self.yeti_nodes_list = self.get_yeti_nodes(nspace)

			if self.yeti_nodes_list != []:
				try:
					self.export_yeti_nodes(len(self.nspace_list), percent)
				except:
					print(str(traceback.format_exc()))

			percent += percent_step
			print('percent:'+str(percent))

		wall.wall().publish_event(self.asset)
		
		if self.set_done:
			print('status:Done !')

	def export_yeti_nodes(self, len_nspacelist, percent):

		directory = utils.temp_dir()

		for node in self.yeti_nodes_list:

			node_name = node.split(':')[-1]
			file = os.path.join(directory, '{}.%04d.fur'.format(node_name))
			cmds.pgYetiCommand(node, writeCache=file, range=(self.range[0], self.range[-1]), samples=3, sampleTimes= "-0.2 0.0 0.2")
			current_percent = float(percent) + (100.0/int(len_nspacelist))/2
			print('percent:{}'.format(current_percent))
		try:
			exported_files_list = os.listdir(directory)
			export_files = self.asset.export_multiple('{}_{}_{}'.format(self.fur_asset.name, self.fur_asset.variant, self.count), exported_files_list)

			percent_step = ((100.0/int(len_nspacelist))/2)/len(exported_files_list)
			percent = current_percent

			for file in exported_files_list:
				full_file = os.path.join(directory, file)
				print('current_task:Copying file {}'.format(full_file))
				print('percent:{}'.format(percent))
				time.sleep(0.01)
				index = exported_files_list.index(file)
				shutil.copyfile(full_file, export_files[index])
				percent+=percent_step
		except:
			print(str(traceback.format_exc()))


	def get_yeti_nodes(self, namespace):

		set_name = '{}:{}'.format(namespace, defaults._yeti_export_set_)

		if cmds.objExists(set_name):

			cmds.select( set_name, replace = 1 )
			yeti_nodes_list = cmds.ls( selection=True )
			return yeti_nodes_list

		else:
			logger.warning('{} not found'.format(set_name))
			return []
