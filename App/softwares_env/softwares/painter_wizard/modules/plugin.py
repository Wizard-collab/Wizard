from wizard.prefs.main import prefs
from wizard.vars import defaults
from wizard.asset import main as asset_core
import os
import substance_painter.project


from wizard.tools import log

prefs = prefs()
logger = log.pipe_log(__name__)

def save():
    # Check if a project is already opened:
    if substance_painter.project.is_open():
        # Check if the project needs to be saved at all:
        if substance_painter.project.needs_saving():
            asset = asset_core.string_to_asset(os.environ[defaults._asset_var_])
            asset.version = prefs.asset(asset).software.get_new_version()
            substance_painter.project.save_as(asset.file,
                                              substance_painter.project.ProjectSaveMode.Full)
        else:
            logger.info("There is nothing to save!")
    else:
        logger.info("No painter project openned!")