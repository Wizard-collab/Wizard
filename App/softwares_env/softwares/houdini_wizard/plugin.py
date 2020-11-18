import hou
from wizard.prefs.main import prefs
from wizard.vars import defaults
from wizard.tools import log
from wizard.asset import main as asset_core
from softwares.houdini_wizard.tools import *
from wizard.tools import utility as utils
import os
import traceback
import shutil
from wizard.project import wall
import sys

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

def export(batch=None, frange=None):
    asset = asset_core.string_to_asset(os.environ[defaults._asset_var_])
    if asset.extension == "hipnc":
        export_hipfile()
    elif asset.extension == "abc":
        export_abc(batch=batch, frange=frange)
    elif asset.extension == "vdb":
        export_vdb(batch=batch, frange=frange)

def prepare_export():
    asset = asset_core.string_to_asset(os.environ[defaults._asset_var_])
    if asset.extension == "abc":
        export_abc(prepare = 1)
    elif asset.extension == "vdb":
        export_vdb(prepare = 1)

def export_hipfile():
    asset = asset_core.string_to_asset(os.environ[defaults._asset_var_])
    export_file = asset.export("{}_{}".format(asset.name, asset.variant), from_asset=asset)

    hou.hipFile.save()
    current_file = hou.hipFile.path()
    shutil.copyfile(current_file, export_file)
    wall.wall().publish_event(asset)

def export_abc(batch=None, prepare=None, frange=None):

    asset = asset_core.string_to_asset(os.environ[defaults._asset_var_])
    
    if not batch:
        abc_export_null = create_export_null_on_last_node('abc')
    else:
        abc_export_null = look_for_export_null('abc')

    if abc_export_null:

        wizard_exports_node = get_wizard_export_node()
        abc_object_merge_node = create_node_without_duplicate('object_merge', 'abc_exports_object_merge', wizard_exports_node)

        abc_object_merge_node.parm('objpath1').set(abc_export_null.path())

        rop_alembic_node = create_node_without_duplicate('rop_alembic', 'exports_alembic', wizard_exports_node)
        rop_alembic_node.setInput(0, abc_object_merge_node)
        wizard_exports_node.layoutChildren()

        rop_alembic_node.parm("trange").set('normal')

        if frange:
            hou.playbar.setFrameRange(frange[0], frange[1])
            
        rop_alembic_node.parm("f1").setExpression('$FSTART')
        rop_alembic_node.parm("f2").setExpression('$FEND')

        rop_alembic_node.parm("motionBlur").set(1)
        rop_alembic_node.parm("shutter1").set(-0.2)
        rop_alembic_node.parm("shutter2").set(0.2)
        if batch:
            rop_alembic_node.parm('lpostframe').set("python")
            rop_alembic_node.parm('postframe').set(by_frame_script_to_file(80))

        if not prepare:
            export_file = asset.export("{}_{}".format(asset.name, asset.variant), from_asset=asset)
            rop_alembic_node.parm("filename").set(export_file)
            rop_alembic_node.parm("execute").pressButton()
            wall.wall().publish_event(asset)

    else:
        logger.warning("No abc out node")

def export_vdb(batch=None, prepare=None, frange=None):
    asset = asset_core.string_to_asset(os.environ[defaults._asset_var_])

    if not batch:
        vdb_export_null = create_export_null_on_last_node('vdb')
    else:
        vdb_export_null = look_for_export_null('vdb')

    if vdb_export_null:

        wizard_exports_node = get_wizard_export_node()
        vdb_object_merge_node = create_node_without_duplicate('object_merge', 'vdb_exports_object_merge', wizard_exports_node)

        vdb_object_merge_node.parm('objpath1').set(vdb_export_null.path())

        rop_geometry_node = create_node_without_duplicate('rop_geometry', 'exports_vdb', wizard_exports_node)
        rop_geometry_node.setInput(0, vdb_object_merge_node)

        wizard_exports_node.layoutChildren()

        temp_dir = utils.temp_dir()
        export_path = os.path.join(temp_dir, "file.$F4.vdb")

        if batch:
            rop_geometry_node.parm('lpostframe').set("python")
            rop_geometry_node.parm('postframe').set(by_frame_script_to_file(80))

        rop_geometry_node.parm('sopoutput').set(export_path)
        rop_geometry_node.parm("trange").set('normal')

        if frange:
            hou.playbar.setFrameRange(frange[0], frange[1])

        rop_geometry_node.parm("f1").setExpression('$FSTART')
        rop_geometry_node.parm("f2").setExpression('$FEND')


        if not prepare:
            rop_geometry_node.parm("execute").pressButton()

            files_list = []

            for file in os.listdir(temp_dir):
                files_list.append(os.path.join(temp_dir, file))

            publish_files_name = asset.export_multiple('{}_{}'.format(asset.name, asset.variant), files_list)

            if batch:
                print("current_task:copying output files")
                sys.stdout.flush()

            for file in files_list:
                shutil.copyfile(file, publish_files_name[files_list.index(file)])

            wall.wall().publish_event(asset)

    else:
        logger.warning("No vdb out node")

