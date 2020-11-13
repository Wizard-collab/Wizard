import hou
import os

SAVE_COMMAND = "from softwares.houdini_wizard import plugin\n"
SAVE_COMMAND += "plugin.save()"
SAVE_ICON = os.path.abspath("save.png")

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
		save_tool = hou.shelves.newTool(name="wizard_save", label="Save")
	save_tool.setScript(SAVE_COMMAND)
	
	save_tool.setIcon(SAVE_ICON)
	shelf.setTools([save_tool])
