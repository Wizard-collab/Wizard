from wizard.asset import main as asset_core
from wizard.prefs.main import prefs
from wizard.tools import log
from wizard.vars import defaults
from wizard.asset.reference import references
from wizard.prefs import project as project_prefs
from softwares.maya_wizard import create_ai_surface

import os

reload(asset_core)
reload(create_ai_surface)

import maya.cmds as cmds
import maya.mel as mel

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
    sel = cmds.ls(sl=1, long=1)
    if len(sel) == 1:
        namespace = None
        relatives = cmds.listRelatives(sel[0], allDescendents = 1 )
        for relative in relatives:
            if cmds.referenceQuery( relative, isNodeReferenced=True ):
                namespace = relative.split(':')[0]
                break
        if namespace:
            scene_asset = asset_core.string_to_asset(os.environ[defaults._asset_var_])
            references_list = prefs().asset(scene_asset).variant.references
            if namespace in references_list.keys():

                asset = asset_core.string_to_asset(references_list[namespace][defaults._asset_key_])
                count = references(scene_asset).add_reference(asset, 1, 1)
                new_namespace = namespace.replace(namespace.split('_')[-1], count)
                import_geo(new_namespace)

            else:
                logger.warning('This reference was not found in wizard')
    else:
        logger.warning('Please select only one asset')

def delete_asset():
    selection = cmds.ls(sl=1, long=1)
    namespaces_list = []

    for sel in selection:
        namespace = None
        relatives = cmds.listRelatives(sel, allDescendents = 1 )
        for relative in relatives:
            if cmds.referenceQuery( relative, isNodeReferenced=True ):
                namespace = relative.split(':')[0]
                refFile = cmds.referenceQuery(relative, filename=True)
                break
        if [namespace, refFile] not in namespaces_list:
            namespaces_list.append([namespace, refFile])

    for namespace in namespaces_list:
        cmds.file( namespace[-1], removeReference=True )
        locator_name = namespace[0]+'_CTRL'
        if cmds.objExists(locator_name):
            cmds.delete( locator_name )
            if cmds.namespace( exists=namespace[0] ):
                cmds.namespace( rm=namespace[0] )

def unhide_reference():
    selection = cmds.ls(sl=1, long=1)
    namespaces_list = []

    for sel in selection:
        if cmds.objectType(sel) == 'reference':
            cmds.file( loadReference=sel )
            namespace = cmds.referenceQuery( sel, namespace=True )
            logger.info(namespace)
            show_locator(namespace)

def switch_proxy(proxy = 1):

    asset = asset_core.string_to_asset(os.environ[defaults._asset_var_])
    references_list = prefs().asset(asset).software.references

    selection = cmds.ls(sl=1, long=1)

    namespaces_list = []

    for sel in selection:

        if not cmds.referenceQuery( sel, isNodeReferenced=True ):
            sel = cmds.listRelatives(sel)[1]

        if cmds.referenceQuery( sel, isNodeReferenced=True ):
            namespace = sel.split(':')[0]
            if namespace not in namespaces_list:
                namespaces_list.append([namespace, sel])

    for namespace in namespaces_list:
        if namespace[0] in references_list.keys():
            asset = asset_core.string_to_asset(references_list[namespace[0]][defaults._asset_key_])
            from_software = prefs().asset(asset).export.version_software
            asset.software = software
            if proxy:
                file = prefs().asset(asset).export.full_proxy
            else:
                file = prefs().asset(asset).export.full_file
            ref_node = cmds.referenceQuery(namespace[1], referenceNode=True)
            nodes = cmds.file(file, loadReference = ref_node, returnNewNodes=1)
            if cmds.objectType(nodes[0]) == 'reference':
                nodes.pop(0)
            grp = nodes[0]
            if nodes[0].endswith('GRP'):
                nodes.pop(0)
            for node in nodes:
                lock_node(node)
            if grp.endswith('GRP'):
                create_set_locator(grp, 1)

    cmds.select(selection, replace = 1)


def hide_ref():

    asset = asset_core.string_to_asset(os.environ[defaults._asset_var_])
    references_list = prefs().asset(asset).software.references
    selection = cmds.ls(sl=1)

    namespaces_list = []

    for sel in selection:
        if not cmds.referenceQuery( sel, isNodeReferenced=True ):
            sel = cmds.listRelatives(sel)[1]

        if cmds.referenceQuery( sel, isNodeReferenced=True ):
            namespace = sel.split(':')[0]
            if namespace not in namespaces_list:
                namespaces_list.append([namespace, sel])

    for namespace in namespaces_list:
        if namespace[0] in references_list.keys():
            asset = asset_core.string_to_asset(references_list[namespace[0]][defaults._asset_key_])
            file = cmds.referenceQuery(namespace[1], filename=True)
            cmds.file( file, unloadReference=True )

            hide_locator(namespace[0])

def hide_locator(namespace):
    locator = namespace+'_CTRL'
    if cmds.objExists(locator):
        cmds.select(locator, replace = 1)
        mel.eval('doHideInOutliner 1;')
        cmds.hide()

def show_locator(namespace):
    locator = namespace+'_CTRL'
    if cmds.objExists(locator):
        cmds.select(locator, replace = 1)
        mel.eval('doHideInOutliner 0;')
        cmds.showHidden( locator )

def setRGBColor(ctrl, color = (1,1,1)):

    rgb = ("R","G","B")

    cmds.setAttr(ctrl + ".overrideEnabled",1)
    cmds.setAttr(ctrl + ".overrideRGBColors",1)

    for channel, color in zip(rgb, color):

        cmds.setAttr(ctrl + ".overrideColor%s" %channel, color)

def import_all():
    import_geo()
    import_anim()
    import_camera()
    import_rig()
    import_autoRig()
    import_camRig()
    import_layout()
    import_hair()
    import_fx()

def import_geo(namespace = None):
    asset_list = get_asset_list()

    for imported_asset in asset_list:
        if namespace and imported_asset[1] == namespace:
            run = 1
        elif not namespace:
            run = 1
        else:
            run = 0
        if imported_asset[0].stage == defaults._geo_ and run:
            if not cmds.namespace(exists=imported_asset[1]):
                old_namespace = cmds.namespaceInfo( currentNamespace=True )
                cmds.file(imported_asset[2], r=True, ignoreVersion=True, namespace=imported_asset[1])
                if cmds.objExists(imported_asset[0].export_asset):
                    if not cmds.objExists('GEO'):
                        cmds.group( em=True, name='GEO' )
                    cmds.parent(imported_asset[0].export_asset, 'GEO', a=1)

def import_anim(namespace = None):
    asset_list = get_asset_list()

    for imported_asset in asset_list:
        if namespace and imported_asset[1] == namespace:
            run = 1
        elif not namespace:
            run = 1
        else:
            run = 0
        if imported_asset[0].stage == defaults._animation_ and run:
            if not cmds.namespace(exists=imported_asset[1]):
                group_name = '{}_{}'.format(imported_asset[0].export_asset, imported_asset[0].stage)
                cmds.file(imported_asset[2], r=True, ignoreVersion=True, namespace=imported_asset[1], groupReference=1, groupName=group_name)
                if cmds.objExists(group_name):
                    if not cmds.objExists('ANIMATION'):
                        cmds.group( em=True, name='ANIMATION' )
                    cmds.parent(group_name, 'ANIMATION', a=1)

def import_fx(namespace = None):
    asset_list = get_asset_list()

    for imported_asset in asset_list:
        if namespace and imported_asset[1] == namespace:
            run = 1
        elif not namespace:
            run = 1
        else:
            run = 0
        if imported_asset[0].stage == defaults._fx_ and run:
            if not cmds.namespace(exists=imported_asset[1]):
                group_name = '{}_{}'.format(imported_asset[0].export_asset, imported_asset[0].stage)
                cmds.file(imported_asset[2], r=True, ignoreVersion=True, namespace=imported_asset[1], groupReference=1, groupName=group_name)
                if cmds.objExists(group_name):
                    if not cmds.objExists('FX'):
                        cmds.group( em=True, name='FX' )
                    cmds.parent(group_name, 'FX', a=1)

def import_camera(namespace = None):
    asset_list = get_asset_list()


    for imported_asset in asset_list:
        if namespace and imported_asset[1] == namespace:
            run = 1
        elif not namespace:
            run = 1
        else:
            run = 0
        if imported_asset[0].stage == defaults._camera_ and run:
            if not cmds.namespace(exists=imported_asset[1]):
                cmds.file(imported_asset[2], r=True, ignoreVersion=True, namespace=imported_asset[1], groupReference=1, groupName=imported_asset[0].export_asset)
                if cmds.objExists(imported_asset[0].export_asset):
                    if not cmds.objExists('CAMERA'):
                        cmds.group( em=True, name='CAMERA' )
                    cmds.parent(imported_asset[0].export_asset, 'CAMERA', a=1)

def import_textures(namespace = None):
    asset_list = get_asset_list()
    for imported_asset in asset_list:
        if namespace and imported_asset[1] == namespace:
            run = 1
        elif not namespace:
            run = 1
        else:
            run = 0
        if imported_asset[0].stage == defaults._texturing_ and run:

            if not cmds.namespace(exists=imported_asset[1]):

                shader_name = '{}:main_shader'.format(imported_asset[1])

                path = os.path.split(imported_asset[2])[0]
                all_textures = os.listdir(path)

                maps_extension = (project_prefs.get_custom_pub_ext_dic())[defaults._texturing_][imported_asset[0].software]
                textures_list = []

                if all_textures and all_textures != []:

                    for texture in all_textures:

                        full_path = os.path.join(path, texture)
                        extension = texture.split('.')[-1]

                        if extension == maps_extension:
                            textures_list.append(full_path)

                create_ai_surface.create_shader(shader_name, textures_list)

def lock_node(node):
    if cmds.objectType(node) != 'reference' and not node.endswith('GRP'):
        cmds.select(node, replace = 1)
        mel.eval('doHideInOutliner 1;')
        cmds.setAttr(node +'.overrideEnabled', 1)
        cmds.setAttr(node +'.overrideDisplayType', 2)

def create_set_locator(grp, replace = 0):
    locator_name = grp.replace(':'+grp.split(':')[-1], '_CTRL')
    if not replace:
        cmds.spaceLocator(name=locator_name)
        bbox = cmds.exactWorldBoundingBox(grp)
        cmds.setAttr(locator_name + '.translateY', bbox[-2]+2)
        cmds.makeIdentity( apply=True, t=1, r=1, s=1, n=2 )
        cmds.makeIdentity( apply=False, t=1, r=1, s=1, n=2 )
        setRGBColor(locator_name, (1,0,0))
    all_objects = cmds.ls(l=1)
    for obj in all_objects:
        if obj.endswith(locator_name):
            logger.info(locator_name)
            logger.info(obj)
            cmds.parent(grp, obj, relative=replace)
            break


def import_layout():
    asset_list = get_asset_list()

    for imported_asset in asset_list:
        if imported_asset[0].stage == defaults._layout_:
            if not cmds.namespace(exists=imported_asset[1]):
                cmds.file(imported_asset[2], r=True, ignoreVersion=True, namespace=imported_asset[1], groupReference=1, groupName=imported_asset[0].export_asset)
                if cmds.objExists(imported_asset[0].export_asset):
                    if not cmds.objExists('LAYOUT'):
                        cmds.group( em=True, name='LAYOUT' )
                    cmds.parent(imported_asset[0].export_asset, 'LAYOUT', a=1)


def refresh_all():
    for imported_asset in get_asset_list():
        if cmds.namespace(exists=imported_asset[1]):
            cmds.namespace(setNamespace=imported_asset[1])
            referenced_list = cmds.namespaceInfo(listNamespace=True)
            for obj in referenced_list:
                if cmds.objExists(obj):
                    if cmds.objectType(obj) == 'transform':
                        if cmds.referenceQuery(obj, isNodeReferenced=True):
                            referenced_obj = obj
                            break
                        else:
                            referenced_obj = None
            if referenced_obj:
                referenced_asset_path = cmds.referenceQuery(referenced_obj, filename=True)
                referenced_asset_node = cmds.referenceQuery(referenced_obj, referenceNode=True)
                referenced_asset_version = os.path.dirname(referenced_asset_path)[-4:]
                if referenced_asset_version != imported_asset[0].export_version:
                    logger.info('Replacing {} with version {}'.format(imported_asset[1], imported_asset[0].export_version))
                    cmds.file(imported_asset[2], loadReference=referenced_asset_node)
                else:
                    logger.info('{} is up to date !'.format(imported_asset[1]))
        cmds.namespace(setNamespace=':')


def refresh_references():
    assets_list = get_asset_list()
    for imported_asset in assets_list:
        version = asset.export_version

def get_scene_references():
    scene_references = cmds.ls(references=1)


def import_rig():
    import_ma(defaults._rig_)


def import_autoRig():
    import_ma(defaults._autorig_)


def import_camRig():
    import_ma(defaults._cam_rig_)


def import_hair():
    import_ma(defaults._hair_)


def import_ma(stage):
    asset_list = get_asset_list()
    for imported_asset in asset_list:
        if imported_asset[0].stage == stage:
            if not cmds.namespace(exists=imported_asset[1]):
                cmds.file(imported_asset[2], r=True, ignoreVersion=True, namespace=imported_asset[1])
