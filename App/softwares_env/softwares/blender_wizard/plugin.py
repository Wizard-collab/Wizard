from wizard.asset import main as asset_core
from wizard.prefs.main import prefs
from wizard.prefs import project as project_prefs
from wizard.tools import log
from wizard.vars import defaults
from wizard.project.wall import wall
from wizard.tools import utility as utils
import tools
import os

import bpy

logger = log.pipe_log(__name__)

prefs = prefs()

global error_message

def save():
    '''Save file in an incremental version.'''
    asset = asset_core.string_to_asset(os.environ[defaults._asset_var_])
    asset.version = prefs.asset(asset).software.get_new_version()
    bpy.ops.wm.save_as_mainfile(filepath=asset.file)
    logger.info('File saved.')
    os.environ[defaults._asset_var_] = utils.asset_to_string(asset)


def export():
    asset = asset_core.string_to_asset(os.environ[defaults._asset_var_])
    stage = asset.stage
    category = asset.category
    if stage == defaults._geo_:
        if asset.category == defaults._set_dress_:
            export_set_dress()
        elif asset.category == defaults._sets_:
            export_sets()
        else:
            export_geo()
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


def export_geo():
    '''Takes 'geo_GRP' and export all meshes.'''
    if sanity(defaults._stage_export_grp_dic_[defaults._geo_]):
        save()
        geo_GRP = bpy.data.collections[defaults._stage_export_grp_dic_[defaults._geo_]]
        # unselect all
        bpy.ops.object.select_all(action='DESELECT')
        # select geo_GRP to convert collection to Maya grp (Empty type objects)
        geo_GRP = tools.replace_blender_collection_by_maya_grp(geo_GRP)
        # add guerilla tags to mesh object - NOT SUPPORTED BY BLENDER YET

        for mesh in tools.list_objects(geo_GRP):
            # if it's a mesh or an empty (= Maya groups) add it to selection
            if mesh.type == 'MESH' or mesh.type == 'PLAIN_AXES':
                # auto_tag.tagGuerillaAuto()
                mesh.select_set(True)

        asset = asset_core.string_to_asset(os.environ[defaults._asset_var_])
        file = asset.export("{}_{}".format(asset.name, asset.variant), from_asset = asset) ### < J'ai rajouté ça
        # time_range = prefs.asset(asset).name.range
        time_range = [1,1]
        export_abc(time_range, file, selected=True)
        wall().publish_event(asset)
        logger.info('Geo exported.')
        # reload Blender file to retrieve collection hierarchy
        bpy.ops.wm.open_mainfile(filepath=asset.file)


def export_set_dress():
    pass
def export_sets():
    pass
def export_rig():
    '''Export 'rig_GRP' content as publish.'''
    if sanity_rig():
        export_blend(defaults._stage_export_grp_dic_[defaults._rig_])
def export_autoRig():
    pass
def export_camRig():
    pass
def export_hair():
    pass
def export_layout():
    pass
def export_cyclo():
    pass

def create_export_GRP():
    '''Create 'export_GRP' based on the asset current stage.'''
    stage = asset_core.string_to_asset(os.environ[defaults._asset_var_]).stage

    if stage == defaults._geo_:
        grp_name = 'geo_GRP'
    elif stage == defaults._rig_:
        grp_name = 'rig_GRP'

    # obj_list = bpy.context.selected_objects

    # create export_Grp collection if not exist
    if bpy.data.collections.get(grp_name) is None:
        grp_name_collection = bpy.data.collections.new(grp_name)
        bpy.context.scene.collection.children.link(grp_name_collection)
    # add selected object to new grp
    # for obj in obj_list:
    #     try:
    #         old_obj_collection = obj.users_collection
    #         bpy.data.collections[grp_name].objects.link(obj)
    #         for old_coll in old_obj_collection:
    #             old_coll.objects.unlink(obj)
    #     except:
    #         continue
    logger.info('{} created.'.format(grp_name))


def create_set_GRP():
    '''Create 'set_GRP' based on the asset current stage.'''
    stage = asset_core.string_to_asset(os.environ[defaults._asset_var_]).stage
    grp_name = 'export_set'

    # obj_list = bpy.context.selected_objects

    # create export_Grp collection if not exist
    if bpy.data.collections.get(grp_name) is None:
        grp_name_collection = bpy.data.collections.new(grp_name)
        bpy.context.scene.collection.children.link(grp_name_collection)
    # add selected object to new grp
    # for obj in obj_list:
    #     try:
    #         old_obj_collection = obj.users_collection
    #         bpy.data.collections[grp_name].objects.link(obj)
    #         # for old_coll in old_obj_collection:
    #         #     old_coll.objects.unlink(obj)
    #     except:
    #         continue
    logger.info('{} created.'.format(grp_name))


def sanity(grp):
    '''Check if export_GRP exists and if it's not empty.'''
    grp_existence = 0
    grp_childs = 0

    if bpy.data.collections.get(grp) is not None:
        grp_existence = 1
    else:
        tools.raise_error('{} missing'.format(grp))
        logger.warning('{} missing'.format(grp))
        return 0
    if grp_existence and len(bpy.data.collections[grp].objects) or grp_existence and len(bpy.data.collections[grp].children)>= 1:
        grp_childs = 1
    else:
        tools.raise_error('{} has no childs'.format(grp))
        logger.warning('{} has no childs'.format(grp))
        return 0
    if grp_existence and grp_childs:
        return 1
    else:
        tools.raise_error('{} is not clean.'.format(grp))
        logger.warning('{} is not clean.'.format(grp))
        return 0


def sanity_rig():
    if bpy.data.collections.get(defaults._rig_export_set_) is not None:
        # select export_set content
        bpy.ops.object.select_all(action='DESELECT')
        for obj in bpy.data.collections[defaults._rig_export_set_].objects:
            obj.select_set(True)

        if bpy.context.selected_objects != []:
            return 1
        else:
            tools.raise_error('"export_set" is empty...')
            logger.warning('"export_set" is empty...')
            return 0
    else:
        tools.raise_error('"export_set" selection set missing...')
        logger.warning('"export_set" selection set missing...')
        return 0


def export_blend(grp):
    if bpy.data.collections.get(grp) is not None:
        asset = asset_core.string_to_asset(os.environ[defaults._asset_var_])
        file = asset.export(f'{asset.name}_{asset.variant}', from_asset=asset)

        if grp == defaults._stage_export_grp_dic_[defaults._rig_]:
            export_list = [grp, defaults._rig_export_set_]
        else:
            export_list = [grp]

        save()
        export_grp(export_list, file)
        # reload Blender file to retrieve collection hierarchy
        bpy.ops.wm.open_mainfile(filepath=asset.file)
        # send notif to wall
        wall().publish_event(asset)
        return file
    else:
        logger.warning(f'{grp} missing')
        return None


def export_grp(grp_list, file):
    all_scene_coll =  list(bpy.context.scene.collection.children)
    all_scene_obj = list(bpy.context.scene.collection.objects)

    # erase all collections and objects in Main scene
    for coll in all_scene_coll:
        if bpy.data.collections[grp_list[0]] == coll or bpy.data.collections[grp_list[1]] == coll:
            continue
        tools.delete_collection(coll)
    for obj in all_scene_obj:
        tools.delete_object(obj)

    # erase blend file cache
    bpy.data.orphans_purge() # /!\ THIS COMMAND WILL DELETE ALL UNSAVED DATA-BLOCKS /!\
    bpy.ops.wm.save_as_mainfile(filepath=file)


def export_abc(time_range, file, selected=False):
    '''Export object(s) in alembic file.'''
    start = time_range[0]
    end = time_range[1]
    bpy.ops.wm.alembic_export(filepath=file,
                            start=start,
                            end=end,
                            sh_open=-0.2,
                            sh_close=0.2,
                            selected=selected,
                            flatten=False,
                            uvs=True,
                            export_hair=True,
                            export_particles=True)
                            ###### ADD CUSTOM ATTRIBUTE - only supported in Blender 2.91
                            ###### "GuerillaTags"
