import sd
from sd.api.sbs.sdsbsarexporter import *
import os
from wizard.asset import main as asset_core
from wizard.tools import log
from wizard.prefs.main import prefs
from wizard.vars import defaults
from wizard.project import wall

logger = log.pipe_log()
prefs = prefs()

asset = asset_core.string_to_asset(os.environ[defaults._asset_var_])
ctx = sd.getContext()

def save():

	pkgMgr, pkg = get_wizard_pkg()
	
	asset.version = prefs.asset(asset).software.get_new_version()
	pkgMgr.savePackageAs(pkg, asset.file)

def export_sbsar():

	exporterInstance = None
	exporterInstance = SDSBSARExporter(ctx, exporterInstance)
	e = exporterInstance.sNew()

	pkgMgr, pkg = get_wizard_pkg()

	file = asset.export('{}_{}'.format(asset.name, asset.variant))

	e.exportPackageToSBSAR(pkg, file)

	wall.wall().publish_event(asset)
	#sd.tools.export.exportSDGraphOutputs(aSDGraph, aOutputDir='', aFileExt='png')

def get_wizard_pkg():
	
	file_template = os.path.split(asset.file)[-1].split('.')[0]
	# Get the application and UI manager object.
	
	app = ctx.getSDApplication()
	# Get the current graph.
	pkgMgr = app.getPackageMgr()
	all_pkgs = pkgMgr.getPackages()
	pkgs_size = all_pkgs.getSize()
	for index in range(pkgs_size):
		pkg = all_pkgs.getItem(index)
		if file_template in pkg.getFilePath():
			break
	return pkgMgr, pkg