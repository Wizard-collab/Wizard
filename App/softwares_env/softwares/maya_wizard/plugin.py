from wizard.asset import main as asset_core
from wizard.prefs.main import prefs
from wizard.prefs import project as project_prefs
from wizard.tools import log
from wizard.vars import defaults
from wizard.project import wall
from maya_wizard import auto_tag
import os

reload(asset_core)
reload(auto_tag)

import maya.cmds as cmds

logger = log.pipe_log(__name__)

prefs = prefs()

def save():
    asset = asset_core.string_to_asset(os.environ[defaults._asset_var_])
    asset.version = prefs.asset(asset).software.get_new_version()
    cmds.file(rename=asset.file)
    cmds.file(save=True, type='mayaAscii')


def export():
    asset = asset_core.string_to_asset(os.environ[defaults._asset_var_])
    stage = asset.stage
    category = asset.category
    if stage == defaults._geo_ and asset.category != defaults._set_dress_:
        export_geo()
    elif stage == defaults._geo_ and asset.category == defaults._set_dress_:
        export_set_dress()
    elif stage == defaults._rig_:
        export_rig()
    elif stage == defaults._autorig_:
        export_autoRig()
    elif stage == defaults._cam_rig_:
        export_camRig()
    elif stage == defaults._hair_:
        export_hair()
    elif stage == defaults._layout_:
        export_layout()
    elif stage == defaults._cyclo_:
        export_cyclo()
    else:
        logger.warning('Unknown stage...')


def sanity(grp):
    grp_existence = 0
    grp_childs = 0
    if cmds.objExists(grp):
        grp_existence = 1
    else:
        logger.warning("{} missing".format(grp))
    if grp_existence and cmds.listRelatives(grp) >= 1:
        grp_childs = 1
    else:
        logger.warning("{} has no childs".format(grp))
    if grp_existence and grp_childs:
        return 1
    else:
        return 0


def export_geo():
    if sanity(defaults._stage_export_grp_dic_[defaults._geo_]):

        save()

        for mesh in cmds.listRelatives(defaults._stage_export_grp_dic_[defaults._geo_], ad=1):
            cmds.select(clear=1)
            cmds.select(mesh)
            relatives = cmds.listRelatives(mesh)
            if relatives:
                if cmds.objectType(relatives[0]) == 'mesh':
                    auto_tag.tagGuerillaAuto()

        cmds.select(clear=1)
        cmds.select('geo_GRP')

        asset = asset_core.string_to_asset(os.environ[defaults._asset_var_])
        file = asset.export('{}_{}'.format(asset.name, asset.variant))
        export_abc([0, 1], file, defaults._stage_export_grp_dic_[defaults._geo_])
        wall.wall().publish_event(asset)

def export_set_dress():
    if sanity(defaults._stage_export_grp_dic_[defaults._set_dress_]):

        save()

        for mesh in cmds.listRelatives(defaults._stage_export_grp_dic_[defaults._set_dress_], ad=1):
            cmds.select(clear=1)
            cmds.select(mesh)
            relatives = cmds.listRelatives(mesh)
            if relatives:
                if cmds.objectType(relatives[0]) == 'mesh':
                    auto_tag.tagGuerillaAuto()

        cmds.select(clear=1)
        cmds.select('set_dress_GRP')

        asset = asset_core.string_to_asset(os.environ[defaults._asset_var_])
        file = asset.export('{}_{}'.format(asset.name, asset.variant))
        export_abc([0, 1], file, defaults._stage_export_grp_dic_[defaults._set_dress_])
        wall.wall().publish_event(asset)

def export_cyclo():
    if sanity(defaults._stage_export_grp_dic_[defaults._cyclo_]):

        save()

        for mesh in cmds.listRelatives(defaults._stage_export_grp_dic_[defaults._cyclo_], ad=1):
            cmds.select(clear=1)
            cmds.select(mesh)
            relatives = cmds.listRelatives(mesh)
            if relatives:
                if cmds.objectType(relatives[0]) == 'mesh':
                    auto_tag.tagGuerillaAuto()

        cmds.select(clear=1)
        cmds.select(defaults._stage_export_grp_dic_[defaults._cyclo_])

        asset = asset_core.string_to_asset(os.environ[defaults._asset_var_])
        file = asset.export('{}_{}'.format(asset.name, asset.variant))
        export_abc([0, 1], file, defaults._stage_export_grp_dic_[defaults._cyclo_])
        wall.wall().publish_event(asset)

def sanity_rig():

    if cmds.objExists(defaults._rig_export_set_):
        if cmds.sets( defaults._rig_export_set_, q=True ) != []:
            return 1
        else:
            logger.warning('"export_set" selection set is empty...')
            return 0
    else:
        logger.warning('"export_set" selection set missing...')
        return 0

def sanity_cam_rig():

    if cmds.objExists(defaults._camrig_export_set_):
        shapes_list = cmds.sets( defaults._camrig_export_set_, q=True )
        if shapes_list != []:
            if len(shapes_list) == 1:
                return 1
            else:
                logger.warning('Please put only 1 camera in "{}"'.format(defaults._camrig_export_set_))
                return 0
        else:
            logger.warning('"{}" selection set is empty...'.format(defaults._camrig_export_set_))
            return 0
    else:
        logger.warning('"{}" selection set missing...'.format(defaults._camrig_export_set_))
        return 0

def sanity_hair():

    sanity = 1

    if cmds.objExists(defaults._stage_export_grp_dic_[defaults._hair_]):

        if cmds.objExists(defaults._scalp_export_set_):
            if cmds.sets( defaults._scalp_export_set_, q=True ) == []:
                logger.warning('"scalp_export_set" selection set is empty...')
                sanity = 0
            else:
                cmds.select( defaults._scalp_export_set_, replace = 1 )
                scalps_list = cmds.ls( selection=True )
                for scalp in scalps_list:
                    shape = cmds.listRelatives(scalp, shapes=1)
                    connections_list = cmds.listConnections( shape, d=False, s=True, plugs=True )
                    if connections_list:
                        for conn in connections_list:
                            if '.message' in conn:
                                tex_ref = 1
                                break
                            else:
                                tex_ref = 0
                    else:
                        tex_ref = 0
                    if not tex_ref:
                        sanity = 0
                        logger.warning('No texture reference for this scalp : {}'.format(scalp))

        else:
            logger.warning('"scalp_export_set" selection set missing...')
            sanity = 0

        if cmds.objExists(defaults._yeti_export_set_):
            if cmds.sets( defaults._yeti_export_set_, q=True ) == []:
                logger.warning('"yeti_export_set" selection set is empty...')
                sanity = 0
        else:
            logger.warning('"yeti_export_set" selection set missing...')
            sanity = 0

    return sanity

def export_rig():

    if sanity_rig():
        export_ma(defaults._stage_export_grp_dic_[defaults._rig_])

def export_layout():
    if sanity(defaults._stage_export_grp_dic_[defaults._layout_]):

        save()

        for mesh in cmds.listRelatives(defaults._stage_export_grp_dic_[defaults._layout_], ad=1):
            cmds.select(clear=1)
            cmds.select(mesh)
            logger.info(cmds.objectType(mesh))
            relatives = cmds.listRelatives(mesh)
            if relatives:
                if cmds.objectType(relatives[0]) == 'mesh':
                    auto_tag.tagGuerillaAuto()

        cmds.select(clear=1)
        cmds.select(defaults._stage_export_grp_dic_[defaults._layout_])

        asset = asset_core.string_to_asset(os.environ[defaults._asset_var_])
        file = asset.export('{}_{}'.format(asset.name, asset.variant))
        export_abc([0, 1], file, defaults._stage_export_grp_dic_[defaults._layout_])
        wall.wall().publish_event(asset)

def export_autoRig():
    export_ma(defaults._stage_export_grp_dic_[defaults._autorig_])

def export_camRig():
    if sanity_cam_rig():
        export_ma(defaults._stage_export_grp_dic_[defaults._cam_rig_])

def export_hair():
    if sanity_hair():
        file = export_ma(defaults._stage_export_grp_dic_[defaults._cam_rig_])
        if file:
            export_fur(file)

def export_fur(file):
    nodes_list = cmds.sets( defaults._yeti_export_set_, q=True )
    for node in nodes_list:
        fur_file = file.replace('.' + file.split('.')[-1], '.{}.fur'.format(node))
        cmds.pgYetiCommand(node, writeCache=fur_file, range=(0,0), samples=1)

def export_ma(grp):
    if cmds.objExists(grp):
        asset = asset_core.string_to_asset(os.environ[defaults._asset_var_])
        file = asset.export('{}_{}'.format(asset.name, asset.variant))
        if grp == defaults._stage_export_grp_dic_[defaults._rig_]:
            export_list = [grp, defaults._rig_export_set_]
        elif grp == defaults._stage_export_grp_dic_[defaults._hair_]:
            export_list = [grp, defaults._scalp_export_set_, defaults._yeti_export_set_]
        elif grp == defaults._stage_export_grp_dic_[defaults._cam_rig_]:
            export_list = [grp, defaults._camrig_export_set_]
        else:
            export_list = [grp]
        export_grp(export_list, file)
        wall.wall().publish_event(asset)
        return file
    else:
        logger.warning("{} missing".format(grp))
        return None

def create_export_GRP():
    stage = asset_core.string_to_asset(os.environ[defaults._asset_var_]).stage
    grp_name = defaults._stage_export_grp_dic_[stage]
    if not cmds.objExists(grp_name):
        cmds.group( em=True, name=grp_name )

def copy_team(selection = True):

    file = prefs.copy_file()

    if selection :
        obj_list = cmds.ls(sl=True)
        cmds.file(file, exportSelected=1, type='mayaAscii', pr=0, f=1)
    else:
        cmds.file(file, exportAll=1, type='mayaAscii', pr=1, f=1)

def paste_team():
    file = prefs.copy_file()
    if os.path.isfile(file):
        cmds.file(file, i=True, f=True)

def export_grp(grp_list, file):
    cmds.select(clear=1)
    for obj in grp_list:
        cmds.select(grp_list, add=1, replace=1, ne=1)
    cmds.file(file, exportSelected=1, type='mayaAscii', pr=0)


def export_abc(range, file, grp):
    start = str(range[0])
    end = str(range[1])
    command = "-frameRange "
    command += start
    command += " "
    command += end
    command += " -step 1"
    command += " -frameRelativeSample -0.2 -frameRelativeSample 0 -frameRelativeSample 0.2 -attr GuerillaTags -uvWrite -worldSpace -root "
    command += grp
    command += " -dataFormat ogawa -file "
    command += file
    cmds.AbcExport(j=command)
