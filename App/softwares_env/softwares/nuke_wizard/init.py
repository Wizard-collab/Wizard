import nuke
from nuke_wizard import plugin
from wizard.vars import defaults
import sys
import os
from nuke_wizard import reference_asset
reload(reference_asset)

nuke.menu( 'Nuke' ).addCommand( 'Wizard/Save', plugin.save, icon='nuke_save.png')
reference_asset.set_project_path()
