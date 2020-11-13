import hou
import os
from wizard.asset import main as asset_core
from wizard.prefs.main import prefs
from wizard.tools import log
from wizard.vars import defaults
from wizard.asset.reference import references
from wizard.prefs import project as project_prefs

logger = log.pipe_log(__name__)


def get_asset_list():
    asset = asset_core.string_to_asset(os.environ[defaults._asset_var_])
    references_list = prefs().asset(asset).software.references
    asset_list = []
    for namespace in list(references_list.keys()):
        imported_asset = asset_core.string_to_asset(references_list[namespace][defaults._asset_key_])
        proxy = references_list[namespace][defaults._proxy_]

        folder = prefs().asset(imported_asset).export.version_folder
        from_software = prefs().asset(imported_asset).export.version_software
        imported_asset.software = from_software
        if proxy:
            file = prefs().asset(imported_asset).export.proxy
        else:
            file = prefs().asset(imported_asset).export.file
        full_path = os.path.join(folder, file)
        asset_list.append([imported_asset, namespace, full_path])
    return asset_list

def import_geo():
    asset_list = get_asset_list()

    for imported_asset in asset_list:
	    asset = imported_asset[0]
	    namespace = imported_asset[1]
	    file_path = imported_asset[2]
	    create_abc_ref(namespace, file_path)

def get_wizard_ref_node():
    wizard_ref_node_name = "wizard_references"
    obj_node = hou.node("/obj")
    wizard_ref_node = hou.node("/obj/" + wizard_ref_node_name)
    if wizard_ref_node not in obj_node.children():
         obj_node.createNode("geo", node_name = wizard_ref_node_name)
         wizard_ref_node = hou.node("/obj/" + wizard_ref_node_name)
    return wizard_ref_node

def create_node_without_duplicate(parent, type, name):
	node_path = "{}/{}".format(parent.path(), name)
	node = hou.node(node_path)
	if node not in parent.children():
		node = parent.createNode(type, node_name = name)
		node = hou.node(node_path)
	return node

def create_abc_ref(namespace, file):
    wizard_ref_node = get_wizard_ref_node()
    abc_node = create_node_without_duplicate(wizard_ref_node, 'alembic', namespace)
    abc_node.parm("fileName").set(file)
    convert_node = create_node_without_duplicate(wizard_ref_node, 'convert', namespace+"_convert")
    convert_node.setInput(0, abc_node)
    null_node = create_node_without_duplicate(wizard_ref_node, 'null', namespace+"_null")
    null_node.setInput(0, convert_node)
    wizard_ref_node.layoutChildren()