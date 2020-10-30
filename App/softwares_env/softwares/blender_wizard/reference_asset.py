from wizard.asset import main as asset_core
from wizard.prefs.main import prefs
from wizard.tools import log
from wizard.vars import defaults
from wizard.asset.reference import references
from wizard.prefs import project as project_prefs
# from softwares.maya_wizard import create_ai_surface

import os

import bpy

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


def duplicate_reference():
    pass


def delete_asset():
    pass


def unhide_reference():
    pass


def switch_proxy(proxy = 1):
    pass


def hide_ref():
    pass


def hide_locator(namespace):
    pass


def show_locator(namespace):
    pass


def setRGBColor(ctrl, color = (1,1,1)):
    pass


def import_all():
    import_geo()
    import_anim()
    import_camera()
    import_rig()
    import_autoRig()
    import_camRig()
    import_layout()
    import_hair()


def import_geo():
    asset_list = get_asset_list()

    # check ig 'GEO' collection exists
    if bpy.data.collections.get('GEO') is None:
        # create 'GEO' collection
        geo_collection = bpy.data.collections.new('GEO')
        bpy.context.scene.collection.children.link(geo_collection)

    # link references
    for asset in asset_list:
        # check stage and proceed if 'geo'
        if asset[0].stage == defaults._geo_:
            # check if ref already linked
            if bpy.data.objects.get('geo_GRP') is None:
                # import file
                geo_GRP = bpy.data.collections.new('geo_GRP')
                bpy.context.scene.collection.children.link(geo_GRP)
                # deselect all
                bpy.ops.object.select_all(action='DESELECT')
                ############## select collection
                bpy.data.collections[geo_GRP].select = True #### don't work
                # import alembic
                bpy.ops.wm.alembic_import(filepath=asset[2])
                # bpy.data.objects['geo_GRP'].parent = bpy.data.collections.get('geo_GRP')
                # replace empty 'geo_GRP' by collection
                delete_object('geo_GRP')
                # parent ref under GEO collection
                # if bpy.data.objects.get(asset[0].export_asset) is not None:
                #     bpy.data.objects['geo_GRP'].parent = bpy.data.collections.get('GEO')

def delete_object(object):
    # deselect all
    bpy.ops.object.select_all(action='DESELECT')
    # selection
    bpy.data.objects[object].select = True
    # remove it
    bpy.ops.object.delete()


def import_anim(namespace = None):
    pass


def import_camera(namespace = None):
    pass


def import_textures(namespace = None):
    pass


def lock_node(node):
    pass


def create_set_locator(grp, replace = 0):
    pass


def import_layout():
    pass


def refresh_all():
    pass


def refresh_references():
    pass

def get_scene_references():
    pass


def import_rig():
    import_ma(defaults._rig_)


def import_autoRig():
    import_ma(defaults._autorig_)


def import_camRig():
    import_ma(defaults._cam_rig_)


def import_hair():
    import_ma(defaults._hair_)


def import_ma(stage):
    pass
