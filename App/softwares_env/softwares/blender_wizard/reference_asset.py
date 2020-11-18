from wizard.asset import main as asset_core
from wizard.prefs.main import prefs
from wizard.tools import log
from wizard.vars import defaults
from wizard.asset.reference import references
from wizard.prefs import project as project_prefs
# from softwares.maya_wizard import create_ai_surface

import tools

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


def import_all(asset_list=[]):
    import_geo(asset_list)
    import_anim(asset_list)
    import_camera(asset_list)
    import_rig(asset_list)
    import_autoRig(asset_list)
    import_camRig(asset_list)
    import_layout(asset_list)
    import_hair(asset_list)


def import_geo(asset_list=[]):
    '''
    Import publish .abc from eference data set in Wizard app.
        args:
            - asset_list = [] list of assets to import. If empty get assets list
                              from Wizard. Allows to import specific asset in scene.
    '''
    if not asset_list:
        asset_list = get_asset_list()
    # check if 'GEO' collection exists
    if bpy.data.collections.get('GEO') is None:
        # create 'GEO' collection
        geo_collection = bpy.data.collections.new('GEO')
        bpy.context.scene.collection.children.link(geo_collection)

    for asset in asset_list:
        # check stage and proceed if 'geo'
        if asset[0].stage == defaults._geo_:
            asset_group = 'geo_GRP'
            asset_path = asset[2]
            # if already in scene skip
            if bpy.data.collections.get(f'{asset[0].name}_{asset_group}') is not None:
                logger.info(f'{asset[0].name} already imported. Skipped.')
                continue

            # if has already a geo_GRP object in scene stop loop (because will fail the import process)
            if bpy.data.objects.get(asset_group) is not None:
                tools.raise_error(f'A \'geo_GRP\' object already exists, can\'t import {asset[0].name}. Please rename or delete the existing object.')
                logger.warning(f'A \'geo_GRP\' object already exists, can\'t import {asset[0].name}. Please rename or delete the existing object.')
                continue

            # set active object as Master scene collection to not have to unparent each grp
            scene_collection = bpy.context.view_layer.layer_collection
            bpy.context.view_layer.active_layer_collection = scene_collection
            # import modeling asset file
            import_alembic(asset_path)
            # add namespace
            asset_version = asset[2].rpartition('\\')[0].rpartition('\\')[2]
            geo_root = tools.add_namespace(bpy.data.objects[asset_group], asset[0].name, asset_version)
            # convert Maya groups to collections
            tools.replace_maya_grp_by_collection(geo_root)

            logger.info(f'{asset[0].name} imported.')


def import_alembic(filepath):
    # import alembic
    bpy.ops.wm.alembic_import(filepath=filepath)


def import_anim(asset_list=[], namespace = None):
    pass


def import_camera(asset_list=[], namespace = None):
    pass


def import_textures(namespace = None):
    pass


def lock_node(node):
    pass


def create_set_locator(grp, replace = 0):
    pass


def import_layout(asset_list=[]):
    pass



def refresh_all():
    for imported_asset in get_asset_list():
        asset_name = imported_asset[0].name

        # declare group name to look for based on asset's stage
        if imported_asset[0].stage == defaults._geo_:
            asset_grp = f'{asset_name}_geo_GRP'
        elif imported_asset[0].stage == defaults._rig_:
            asset_grp = f'{asset_name}_rig_GRP'

        # check if already in scene
        if bpy.data.collections.get(asset_grp) is not None:
            stage_GRP = bpy.data.collections[asset_grp]

            # get asset's current version
            asset_current_version = bpy.context.scene[f'{asset_name}_version']
            new_asset_version = imported_asset[0].export_version

            # check version
            if asset_current_version == new_asset_version:
                logger.info(f'{asset_name} is up to date ! Skipped.')
                continue
            else:
                # remove current
                collections_to_delete = []
                for c in tools.list_collections(stage_GRP):
                    collections_to_delete.append(c)
                for col in collections_to_delete:
                    tools.delete_collection(col)
                tools.delete_collection(stage_GRP)

                logger.info(f'Replacing {asset_name} with version {new_asset_version}')
                # erase blend file cache
                bpy.data.orphans_purge() # /!\ THIS COMMAND WILL DELETE ALL UNSAVED DATA-BLOCKS /!\
                # import latest
                new_asset_version
                import_all([imported_asset])
                # erase blend file cache
                bpy.data.orphans_purge() # /!\ THIS COMMAND WILL DELETE ALL UNSAVED DATA-BLOCKS /!\
                continue


def import_rig(asset_list=[]):
    import_ma(defaults._rig_)


def import_autoRig(asset_list=[]):
    import_ma(defaults._autorig_)


def import_camRig(asset_list=[]):
    import_ma(defaults._cam_rig_)


def import_hair(asset_list=[]):
    import_ma(defaults._hair_)


def import_ma(stage):
    pass
