import hou
import os

SAVE_COMMAND = "from softwares.houdini_wizard import plugin\n"
SAVE_COMMAND += "plugin.save()"

EXPORT_COMMAND = "from softwares.houdini_wizard import plugin\n"
EXPORT_COMMAND += "plugin.export()"

PEXPORT_COMMAND = "from softwares.houdini_wizard import plugin\n"
PEXPORT_COMMAND += "plugin.prepare_export()"

IMPORT_COMMAND = "from softwares.houdini_wizard import reference_asset\n"
IMPORT_COMMAND += "reference_asset.import_all()"

REFRESH_COMMAND = "from softwares.houdini_wizard import reference_asset\n"
REFRESH_COMMAND += "reference_asset.refresh_all()"

FRANGE_COMMAND = "from softwares.houdini_wizard import plugin\n"
FRANGE_COMMAND += "plugin.set_f_range()"

SAVE_ICON = os.path.abspath("save.png")
IMPORT_ICON = os.path.abspath("import.png")
REFRESH_ICON = os.path.abspath("refresh.png")
EXPORT_ICON = os.path.abspath("export.png")
PEXPORT_ICON = os.path.abspath("prepare_export.png")
FRANGE_ICON = os.path.abspath("frange.png")

def build_shelf():
	wizard_shelf_name = "wizard_shelf"
	
	shelves_dic = hou.shelves.shelves()
	
	if wizard_shelf_name not in shelves_dic.keys():
		shelf = hou.shelves.newShelf(name=wizard_shelf_name, label="wizard")
	else:
		shelf = shelves_dic[wizard_shelf_name]
	
	wizard_save_tool_name = "wizard_save"
	tools_dic = hou.shelves.tools()
	if wizard_save_tool_name in tools_dic.keys():
		save_tool = tools_dic[wizard_save_tool_name]
	else:
		save_tool = hou.shelves.newTool(name=wizard_save_tool_name, label="Save")
	save_tool.setScript(SAVE_COMMAND)
	save_tool.setIcon(SAVE_ICON)

	wizard_import_tool_name = "wizard_import"
	if wizard_import_tool_name in tools_dic.keys():
		import_tool = tools_dic[wizard_import_tool_name]
	else:
		import_tool = hou.shelves.newTool(name=wizard_import_tool_name, label="Import All")
	import_tool.setScript(IMPORT_COMMAND)
	import_tool.setIcon(IMPORT_ICON)

	wizard_refresh_tool_name = "wizard_refresh"
	if wizard_refresh_tool_name in tools_dic.keys():
		refresh_tool = tools_dic[wizard_refresh_tool_name]
	else:
		refresh_tool = hou.shelves.newTool(name=wizard_refresh_tool_name, label="Refresh All")
	refresh_tool.setScript(REFRESH_COMMAND)
	refresh_tool.setIcon(REFRESH_ICON)

	wizard_export_tool_name = "wizard_export"
	if wizard_export_tool_name in tools_dic.keys():
		export_tool = tools_dic[wizard_export_tool_name]
	else:
		export_tool = hou.shelves.newTool(name=wizard_export_tool_name, label="Export")
	export_tool.setScript(EXPORT_COMMAND)
	export_tool.setIcon(EXPORT_ICON)

	wizard_p_export_tool_name = "wizard_prepare_export"
	if wizard_p_export_tool_name in tools_dic.keys():
		pexport_tool = tools_dic[wizard_p_export_tool_name]
	else:
		pexport_tool = hou.shelves.newTool(name=wizard_p_export_tool_name, label="Prepare export")
	pexport_tool.setScript(PEXPORT_COMMAND)
	pexport_tool.setIcon(PEXPORT_ICON)

	wizard_frange_tool_name = "wizard_frange"
	if wizard_frange_tool_name in tools_dic.keys():
		frange_tool = tools_dic[wizard_frange_tool_name]
	else:
		frange_tool = hou.shelves.newTool(name=wizard_frange_tool_name, label="Set frame range")
	frange_tool.setScript(FRANGE_COMMAND)
	frange_tool.setIcon(FRANGE_ICON)


	shelf.setTools([save_tool, import_tool, refresh_tool, pexport_tool, export_tool, frange_tool])
