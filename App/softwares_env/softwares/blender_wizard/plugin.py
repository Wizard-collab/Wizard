from wizard.asset import main as asset_core
from wizard.prefs.main import prefs
from wizard.prefs import project as project_prefs
from wizard.tools import log
from wizard.vars import defaults
from wizard.project import wall
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
        # add guerilla tags to mesh object - NOT SUPPORTED
        for mesh in geo_GRP.objects:
            if mesh.type == 'MESH':
                # auto_tag.tagGuerillaAuto()
                # it's a mesh so add it to selection
                mesh.select_set(True)
                pass

        asset = asset_core.string_to_asset(os.environ[defaults._asset_var_])
        ## ERROR next line - waiting for answers
        file = asset.export('{}_{}'.format(asset.name, asset.variant))
        time_range = prefs.asset(asset).name.range
        export_abc(time_range, file, selected=True)
        wall.wall().publish_event(asset)
        logger.info('Geo exported.')

def export_set_dress():
    pass
def export_sets():
    pass
def export_rig():
    pass
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
    grp_name = defaults._stage_export_grp_dic_[stage]
    obj_list = bpy.context.selected_objects
    # create export_Grp collection if not exist
    if bpy.data.collections.get(grp_name) is None:
        print('Creating export_GRP...')
        grp_name_collection = bpy.data.collections.new(grp_name)
        bpy.context.scene.collection.children.link(grp_name_collection)
    for obj in obj_list:
        try:
            old_obj_collection = obj.users_collection
            bpy.data.collections[grp_name].objects.link(obj)
            for old_coll in old_obj_collection:
                old_coll.objects.unlink(obj)
        except:
            continue
    logger.info('{} created.'.format(grp_name))


def error_popup(self, context):
    '''Builds popup window. Displays the text of the global error_message var.'''
    global error_message
    self.layout.label(text=error_message)
def raise_error(message):
    '''Takes message and call a popup window with it.'''
    global error_message
    error_message = message
    bpy.context.window_manager.popup_menu(error_popup, title="Wizard Error", icon='ERROR')


def sanity(grp):
    '''Check if export_GRP exists and if it's not empty.'''
    grp_existence = 0
    grp_childs = 0

    if bpy.data.collections.get(grp) is not None:
        grp_existence = 1
    else:
        raise_error('{} missing'.format(grp))
        logger.warning('{} missing'.format(grp))
        return 0
    if grp_existence and len(bpy.data.collections[grp].objects) >= 1:
        grp_childs = 1
    else:
        raise_error('{} has no childs'.format(grp))
        logger.warning('{} has no childs'.format(grp))
        return 0
    if grp_existence and grp_childs:
        return 1
    else:
        raise_error('{} is not clean.'.format(grp))
        logger.warning('{} is not clean.'.format(grp))
        return 0


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
                            flatten=True,
                            uvs=True,
                            export_hair=True,
                            export_particles=True)
                            ###### ADD CUSTOM ATTRIBUTE - only supported in Blender 2.91
                            ###### "GuerillaTags"
