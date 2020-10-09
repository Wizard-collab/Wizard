import sd
import os
from wizard.asset import main as asset_core
from wizard.tools import log
from wizard.prefs.main import prefs
from wizard.vars import defaults

logger = log.pipe_log()
prefs = prefs()

def save():

	asset = asset_core.string_to_asset(os.environ[defaults._asset_var_])
	file_template = os.path.split(asset.file)[-1].split('.')[0]
	# Get the application and UI manager object.
	ctx = sd.getContext()
	app = ctx.getSDApplication()
	uiMgr = app.getQtForPythonUIMgr()
	# Get the current graph.
	pkgMgr = app.getPackageMgr()
	all_pkgs = pkgMgr.getPackages()
	pkgs_size = all_pkgs.getSize()
	for index in range(pkgs_size):
		pkg = all_pkgs.getItem(index)
		if file_template in pkg.getFilePath():
			asset.version = prefs.asset(asset).software.get_new_version()
			pkgMgr.savePackageAs(pkg, asset.file)