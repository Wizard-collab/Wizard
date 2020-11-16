import hou
from wizard.prefs.main import prefs
from wizard.vars import defaults
from wizard.tools import log
from wizard.asset import main as asset_core
from softwares.houdini_wizard.tools import *
import os
import traceback
import shutil
from wizard.project import wall

logger = log.pipe_log()
prefs = prefs()

def save():
    asset = asset_core.string_to_asset(os.environ[defaults._asset_var_])
    asset.version = prefs.asset(asset).software.get_new_version()
    hou.hipFile.save(file_name=asset.file)

def set_f_range(preroll=0):
    asset = asset_core.string_to_asset(os.environ[defaults._asset_var_])
    f_range = prefs.asset(asset).name.range
    
    if preroll:
        preroll = prefs.asset(asset).name.preroll
        postroll = prefs.asset(asset).name.postroll
        f_range[0] = f_range[0]-preroll
        f_range[1] = f_range[1]+postroll

    hou.playbar.setFrameRange(f_range[0], f_range[1])

def export():
    asset = asset_core.string_to_asset(os.environ[defaults._asset_var_])
    export_file = asset.export("{}_{}".format(asset.name, asset.variant))
    extension = os.path.splitext(export_file)[-1]

    if extension == ".hipnc":
        if export_hipfile(export_file):
            wall.wall().publish_event(asset)
    elif extension == ".abc":
        if export_abc(export_file):
            wall.wall().publish_event(asset)
    elif extension == ".vdb":
        if export_vdb(export_file):
            wall.wall().publish_event(asset)

def export_hipfile(file):

    hou.hipFile.save()
    current_file = hou.hipFile.path()
    shutil.copyfile(current_file, file)
    return 1

def export_abc(file):
    
    export_null = create_export_null_on_last_node()
    if export_null:

        wizard_exports_node = get_wizard_export_node()
        object_merge_node = create_node_without_duplicate('object_merge', 'exports_object_merge', wizard_exports_node)

        object_merge_node.parm('objpath1').set(export_null.path())

        rop_alembic_node = create_node_without_duplicate('rop_alembic', 'exports_alembic', wizard_exports_node)
        rop_alembic_node.setInput(0, object_merge_node)
        wizard_exports_node.layoutChildren()

        rop_alembic_node.parm("filename").set(file)

        rop_alembic_node.parm("trange").set('normal')
        rop_alembic_node.parm("f1").setExpression('$FSTART')
        rop_alembic_node.parm("f2").setExpression('$FEND')

        rop_alembic_node.parm("motionBlur").set(1)
        rop_alembic_node.parm("shutter1").set(-0.2)
        rop_alembic_node.parm("shutter2").set(0.2)

        rop_alembic_node.parm("execute").pressButton()
        return 1

    else:
        return None

def export_vdb(file):
    ### to do
    pass
    return 1

