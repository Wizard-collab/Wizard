# coding: utf8

import maya.cmds as cmds
import maya.standalone
maya.standalone.initialize()

cmds.loadPlugin( 'AbcImport.mll' )
cmds.loadPlugin( 'AbcExport.mll' )

from maya_wizard import plugin
from wizard.asset import main as asset_core
from wizard.tools import log
from wizard.vars import defaults
import os

import sys

logger = log.pipe_log(__name__)

def batch_export():
	asset = asset_core.string_to_asset(os.environ[defaults._asset_var_])

	print('current_task:exporting {}-{}-{}...'.format(asset.category, asset.name, asset.stage))
	print('status:starting...')
	print('percent:0')
	sys.stdout.flush()

	file = asset.file
	print('current_task:openning file {}'.format(file))
	sys.stdout.flush()
	cmds.file(file, o=True, f=True)
	print('percent:20')
	sys.stdout.flush()


	print('current_task:exporting asset')
	print('percent:25')
	sys.stdout.flush()
	plugin.export()

	print('status:Done !')
	print('percent:100')
	sys.stdout.flush()
