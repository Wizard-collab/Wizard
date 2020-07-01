from wizard.prefs.main import prefs
from wizard.tools import log

# Creates the main logger
logger = log.pipe_log(__name__)


def asset_to_id(asset):
    id = (prefs().project_name).upper()
    id += asset.domain.upper()[0]

    if asset.variant:
        id += asset.category.upper()[:2]
        id += asset.name.upper()
        id += asset.stage.upper()[:2]
        id += asset.variant.upper()

    return id
