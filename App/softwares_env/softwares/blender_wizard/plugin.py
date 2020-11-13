from wizard.asset import main as asset_core
from wizard.prefs.main import prefs
from wizard.prefs import project as project_prefs
from wizard.tools import log
from wizard.vars import defaults
from wizard.project.wall import wall
import os

import bpy

logger = log.pipe_log(__name__)

prefs = prefs()

def save():
    asset = asset_core.string_to_asset(os.environ[defaults._asset_var_])
    asset.version = prefs.asset(asset).software.get_new_version()
    bpy.ops.wm.save_as_mainfile(filepath=asset.file)

def export():
	# Check the asset stage
	if asset.stage == defaults._geo_:
		# Publishing GEO as ABC ( for the moment )
		asset = asset_core.string_to_asset(os.environ[defaults._asset_var_])
		### > export_file_path = asset.export("{}_{}".format(asset.name, asset.variant))
		### > *blender_command_to_export_abc.(file = export_file_path)*
		### > wall().publish_event(asset)
