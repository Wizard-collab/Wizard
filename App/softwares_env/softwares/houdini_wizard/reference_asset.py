import hou
import os
from wizard.asset import main as asset_core
from wizard.prefs.main import prefs
from wizard.tools import log
from wizard.vars import defaults
from wizard.asset.reference import references
from wizard.prefs import project as project_prefs
from softwares.houdini_wizard.tools import *

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

def import_all():
    import_geo()
    import_cam()

def refresh_all():
    import_geo(1)
    import_cam(1)

def import_geo(reload=0):
    asset_list = get_asset_list()
    for imported_asset in asset_list:

        asset = imported_asset[0]
        namespace = imported_asset[1]
        file_path = imported_asset[2]

        if asset.stage == defaults._geo_ or asset.stage == defaults._animation_:
            wizard_ref_node = get_wizard_ref_node()
            if node_exists(namespace, wizard_ref_node) and not reload:
                pass
            else:
                create_abc_ref(namespace, file_path)

def import_cam(reload=0):
    asset_list = get_asset_list()
    for imported_asset in asset_list:

        asset = imported_asset[0]
        namespace = imported_asset[1]
        file_path = imported_asset[2]

        if asset.stage == defaults._camera_:
            wizard_ref_node = get_wizard_ref_node()
            if node_exists(namespace) and not reload:
                pass
            else:
                create_cam_ref(namespace, file_path)

def create_abc_ref(namespace, file):
    wizard_ref_node = get_wizard_ref_node()
    abc_node = create_node_without_duplicate('alembic', namespace, wizard_ref_node)
    abc_node.parm("fileName").set(file)
    convert_node = create_node_without_duplicate('convert', namespace+"_convert", wizard_ref_node)
    convert_node.setInput(0, abc_node)
    null_node = create_node_without_duplicate('null', namespace+"_null", wizard_ref_node)
    null_node.setInput(0, convert_node)
    wizard_ref_node.layoutChildren()

def create_cam_ref(namespace, file):
    cam_main_node = create_node_without_duplicate("alembicarchive", namespace)
    abc_xform_node = create_node_without_duplicate("alembicxform", namespace+'_xform', cam_main_node)
    abc_xform_node.parm("fileName").set(file)
    connect_to_input_item(abc_xform_node, cam_main_node, 1)
    arg = abc_xform_node.parm("objectPath").menuLabels()[1]
    abc_xform_node.parm("objectPath").set(arg)
    abc_xform_node.parm("frame").setExpression("$F")
    hou_camera_node = create_node_without_duplicate("cam", namespace+'_hou_cam', abc_xform_node)
    connect_to_input_item(hou_camera_node, abc_xform_node, 1)
    cam_main_node.layoutChildren()
    abc_xform_node.layoutChildren()