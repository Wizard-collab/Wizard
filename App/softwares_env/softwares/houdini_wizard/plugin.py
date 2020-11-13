import hou
from wizard.prefs.main import prefs
from wizard.vars import defaults
from wizard.tools import log
from wizard.asset import main as asset_core
import os

logger = log.pipe_log()
prefs = prefs()

def save():
    asset = asset_core.string_to_asset(os.environ[defaults._asset_var_])
    asset.version = prefs.asset(asset).software.get_new_version()
    hou.hipFile.save(file_name=asset.file)