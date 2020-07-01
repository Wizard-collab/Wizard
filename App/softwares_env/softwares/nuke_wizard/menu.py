import nuke
from nuke_wizard import plugin
reload(plugin)
from nuke_wizard import reference_asset
reload(reference_asset)
from wizard.vars import defaults
import sys
import os
import traceback

try:
	menubar = nuke.menu("Nuke")
	wizard_menu = menubar.addMenu('Wizard')
	wizard_menu.addCommand("Save", plugin.save, icon="nuke_save.png")
	wizard_menu.addCommand("Set frame range", plugin.set_f_range, icon="nuke_frame_range.png")
	wizard_menu.addCommand("Set format", plugin.set_format, icon="nuke_format.png")
	wizard_menu.addCommand("Set frame rate", plugin.set_f_rate, icon="nuke_frame_rate.png")
	wizard_menu.addCommand("Reload all", reference_asset.reload_all, icon="nuke_reload_all.png")
	wizard_menu.addCommand("Resolve missing files", reference_asset.resolve_local_paths, icon="nuke_resolve_local.png")
	wizard_menu.addCommand("Import lighting", reference_asset.import_lighting, icon="nuke_import_lighting.png")
	wizard_menu.addCommand("Import lighting helios", reference_asset.import_lighting_helios, icon="nuke_import_lighting_helios.png")

	t=nuke.toolbar("Wizard")
	t.addCommand("Save", plugin.save, icon="nuke_save.png")
	t.addCommand("Set frame range", plugin.set_f_range, icon="nuke_frame_range.png")
	t.addCommand("Set format", plugin.set_format, icon="nuke_format.png")
	t.addCommand("Set frame rate", plugin.set_f_rate, icon="nuke_frame_rate.png")
	t.addCommand("Reload all", reference_asset.reload_all, icon="nuke_reload_all.png")
	t.addCommand("Resolve missing files", reference_asset.resolve_local_paths, icon="nuke_resolve_local.png")
	t.addCommand("Import lighting", reference_asset.import_lighting, icon="nuke_import_lighting.png")
	t.addCommand("Import lighting helios", reference_asset.import_lighting_helios, icon="nuke_import_lighting_helios.png")


	from helios import menu
	reload(menu)
except:
	print(str(traceback.format_exc()))