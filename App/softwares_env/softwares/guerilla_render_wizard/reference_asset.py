from wizard.asset import main as asset_core
from wizard.prefs.main import prefs
from wizard.tools import log
from wizard.vars import defaults
from guerilla import Document, Modifier, pynode, Node, Plug
import traceback

import os

reload(asset_core)

logger = log.pipe_log()


def get_asset_list():
    asset = asset_core.string_to_asset(os.environ[defaults._asset_var_])
    references_list = prefs().asset(asset).software.references
    asset_list = []
    for namespace in list(references_list.keys()):
        imported_asset = asset_core.string_to_asset(references_list[namespace][defaults._asset_key_])
        folder = prefs().asset(imported_asset).export.version_folder
        from_software = prefs().asset(imported_asset).export.version_software
        imported_asset.software = from_software
        file = prefs().asset(imported_asset).export.file
        full_path = os.path.join(folder, file)
        asset_list.append([imported_asset, namespace, full_path])
    return asset_list


def import_geo(reload=0):
    asset_list = get_asset_list()
    for imported_asset in asset_list:
        if imported_asset[0].stage == defaults._geo_:
            if imported_asset[1] not in get_all_nodes() and not reload:
                with Modifier() as mod:
                    geo_GRP = add_GRP('GEOMETRY')
                    refNode, topNodes = mod.createref(imported_asset[1], imported_asset[2], geo_GRP)
            elif imported_asset[1] in get_all_nodes() and reload:
                refNode = get_node_from_name(imported_asset[1])
                refNode.ReferenceFileName.set(imported_asset[2])

def import_grooming(reload=0):

    asset_list = get_asset_list()
    grooming_GRP = add_GRP('GROOMING')

    for imported_asset in asset_list:
        if imported_asset[0].stage == defaults._hair_:

            nodes_list = []

            folder = os.path.split(imported_asset[2])[0]
            for file in os.listdir(folder):
                if file.endswith('.fur'):
                    node_tuple = [file.split('.')[-2], os.path.join(folder, file)]
                    nodes_list.append(node_tuple)

            if imported_asset[1] not in get_all_nodes() and not reload:
                for node_tuple in nodes_list:
                        with Modifier() as mod:
                            nspace_GRP = add_GRP(imported_asset[1], grooming_GRP)
                            node_name = '{}:{}'.format(imported_asset[1], node_tuple[0])
                            yeti_node = mod.createnode(node_name, "Yeti", nspace_GRP)
                            yeti_node.File.set(node_tuple[1])
                            yeti_node.HierarchyMode.set(2)
                            yeti_node.Membership.set(node_tuple[0])

            elif imported_asset[1] in get_all_nodes() and reload:
                for node_tuple in nodes_list:
                    nspace_GRP = add_GRP(imported_asset[1], grooming_GRP)
                    node_name = '{}:{}'.format(imported_asset[1], node_tuple[0])
                    yeti_node = get_node_from_name(node_name)
                    yeti_node.File.set(node_tuple[1])

def import_cfx(reload=0):

    asset_list = get_asset_list()
    grooming_GRP = add_GRP('CFX')

    for imported_asset in asset_list:
        if imported_asset[0].stage == defaults._cfx_:

            nodes_list = []

            folder = os.path.split(imported_asset[2])[0]
            for file in os.listdir(folder):
                if file.endswith('.fur'):
                    file = file.replace(file.split('.')[-2], '%04d')
                    node_tuple = [file.split('.')[-3], os.path.join(folder, file)]
                    if node_tuple not in nodes_list:
                        nodes_list.append(node_tuple)


            if imported_asset[1] not in get_all_nodes() and not reload:
                for node_tuple in nodes_list:
                    with Modifier() as mod:

                        nspace_GRP = add_GRP(imported_asset[1], grooming_GRP)

                        node_name = '{}:{}'.format(imported_asset[1], node_tuple[0])

                        yeti_node = mod.createnode(node_name, "Yeti", nspace_GRP)
                        yeti_node.File.set(node_tuple[1])
                        yeti_node.HierarchyMode.set(2)
                        yeti_node.Membership.set(node_tuple[0])

            elif imported_asset[1] in get_all_nodes() and reload:
                for node_tuple in nodes_list:

                    nspace_GRP = add_GRP(imported_asset[1], grooming_GRP)

                    node_name = '{}:{}'.format(imported_asset[1], node_tuple[0])

                    yeti_node = get_node_from_name(node_name)
                    yeti_node.File.set(node_tuple[1])

def import_anim(reload=0):
    asset_list = get_asset_list()
    for imported_asset in asset_list:
        if imported_asset[0].stage == defaults._animation_:
            if imported_asset[1] not in get_all_nodes() and not reload:
                with Modifier() as mod:
                    anim_GRP = add_GRP('ANIMATION')
                    refNode, topNodes = mod.createref(imported_asset[1], imported_asset[2], anim_GRP)
            elif imported_asset[1] in get_all_nodes() and reload:
                refNode = get_node_from_name(imported_asset[1])
                refNode.ReferenceFileName.set(imported_asset[2])

def import_camera(reload=0):
    asset_list = get_asset_list()
    for imported_asset in asset_list:
        if imported_asset[0].stage == defaults._camera_:
            if imported_asset[1] not in get_all_nodes() and not reload:
                with Modifier() as mod:
                    cam_GRP = add_GRP('CAMERA')
                    refNode, topNodes = mod.createref(imported_asset[1], imported_asset[2], cam_GRP)
            elif imported_asset[1] in get_all_nodes() and reload:
                refNode = get_node_from_name(imported_asset[1])
                refNode.ReferenceFileName.set(imported_asset[2])

def import_layout(reload=0):
    asset_list = get_asset_list()
    for imported_asset in asset_list:
        if imported_asset[0].stage == defaults._layout_:
            if imported_asset[1] not in get_all_nodes() and not reload:
                with Modifier() as mod:
                    layout_GRP = add_GRP('LAYOUT')
                    refNode, topNodes = mod.createref(imported_asset[1], imported_asset[2], layout_GRP)
            elif imported_asset[1] in get_all_nodes() and reload:
                refNode = get_node_from_name(imported_asset[1])
                refNode.ReferenceFileName.set(imported_asset[2])

def import_cyclo(reload=0):
    asset_list = get_asset_list()
    for imported_asset in asset_list:
        if imported_asset[0].stage == defaults._cyclo_:
            if imported_asset[1] not in get_all_nodes() and not reload:
                with Modifier() as mod:
                    cyclo_GRP = add_GRP('CYCLO')
                    refNode, topNodes = mod.createref(imported_asset[1], imported_asset[2], cyclo_GRP)
            elif imported_asset[1] in get_all_nodes() and reload:
                refNode = get_node_from_name(imported_asset[1])
                refNode.ReferenceFileName.set(imported_asset[2])

def import_shading(reload=0):
    asset_list = get_asset_list()
    for imported_asset in asset_list:
        if imported_asset[0].stage == defaults._shading_:
            if imported_asset[1] in get_all_nodes():
                if reload:
                    shading_GRP = add_GRP('SHADING')
                    shading_GRP.getchild(imported_asset[1]).delete()
                    rg_node = Document().loadfile(imported_asset[2])[0]
                    rg_node.move(shading_GRP)
                    rg_node.rename(imported_asset[1])
            else:
                if not reload:
                    shading_GRP = add_GRP('SHADING')
                    rg_node = Document().loadfile(imported_asset[2])[0]
                    rg_node.move(shading_GRP)
                    rg_node.rename(imported_asset[1])

def import_texturing(reload=0):
    asset_list = get_asset_list()
    for imported_asset in asset_list:
        if imported_asset[0].stage == defaults._texturing_:



            asset = asset_core.string_to_asset(os.environ[defaults._asset_var_])

            shaders_GRP = add_GRP('SHADERS')

            if imported_asset[1] not in get_all_nodes():
                
                rg = Node.create(imported_asset[1], 'RenderGraph')
                rg.move(shaders_GRP)

                tag1 = rg.loadfile('$(LIBRARY)/rendergraph/tag.gnode')
                tag1[0].Tag.set(asset.name)
                tag1[0].rename(asset.name)

                at1 = rg.loadfile('$(LIBRARY)/rendergraph/attributes.gnode')
                at1[0].overrideinheritedattr('RaytraceSubdivLevel',2)
                at1[0].overrideinheritedattr('Subdiv', True)
                at1[0].Input1.Plug.connect(tag1[0].Output1.Plug)

                ds1 = rg.loadfile('$(LIBRARY)/rendergraph/shader.gnode') # Displacement Shader
                ds1[0].Shader.set('Displacement')
                ds1[0].Mode.set('displacement')
                ds1[0].rename('{}_displacement_shader'.format(asset.name))
                ds1[0].Input1.Plug.connect(at1[0].Output1.Plug)

                sh1 = rg.loadfile('$(LIBRARY)/rendergraph/shader.gnode') # Surface Shader
                sh1[0].Shader.set('Surface2')
                sh1[0].Mode.set('surface')
                sh1[0].rename('{}_main_shader'.format(asset.name))
                sh1[0].Input1.Plug.connect(ds1[0].Output1.Plug)

                out1 = rg.loadfile('$(LIBRARY)/rendergraph/output.gnode')
                out1[0].Input1.Plug.connect(sh1[0].Output1.Plug)
                replace = 0

            else:
                rg = get_node_from_name(imported_asset[1])
                surface_node = get_node_from_name('{}_main_shader'.format(asset.name))
                sh1 = []
                sh1.append(surface_node)
                replace = 1

            base_color_maps = []
            metalness_maps = []
            roughness_maps = []
            normal_maps = []
            sss_maps = []
            height_maps = []

            for texture_map in get_maps(imported_asset[2]):

                udim = texture_map.split('.')[-2]
                texture_map = texture_map.replace(udim, '%04d')

                if 'BASECOLOR' in texture_map.upper() and texture_map.endswith('.tex'):
                    base_color_maps.append(texture_map)
                if 'METALLIC' in texture_map.upper() and texture_map.endswith('.tex'):
                    metalness_maps.append(texture_map)
                if 'ROUGHNESS' in texture_map.upper() and texture_map.endswith('.tex'):
                    roughness_maps.append(texture_map)
                if 'NORMAL' in texture_map.upper() and texture_map.endswith('.tex'):
                    normal_maps.append(texture_map)
                if 'SSS' in texture_map.upper() and texture_map.endswith('.tex'):
                    sss_maps.append(texture_map)
                if 'HEIGHT' in texture_map.upper() and texture_map.endswith('.tex'):
                    height_maps.append(texture_map)

            with Modifier() as mod:

                try:
                    if base_color_maps != []:

                        if not replace:
                            attrSh1 = mod.createnode('DiffuseColor', type='AttributeShader', parent=sh1[0])
                            attrSh1.Shader.set('Texture')
                            p = attrSh1.createplug('File', 'user', 'texture', Plug.Dynamic)
                        else:
                            p = sh1[0].DiffuseColor.File
                        if replace and p.get() != '':
                            p.set(base_color_maps[0])
                        elif not replace:
                            p.set(base_color_maps[0])

                    else:
                        logger.warning("No DiffuseColor to load")
                except:
                    logger.error("Can't load DiffuseColor")

                try:
                    if base_color_maps != [] and metalness_maps != [] and roughness_maps != []:
                        
                        if not replace:
                            attrSh1 = mod.createnode('MetalColor', type='AttributeShader', parent=sh1[0])
                            attrSh1.Shader.set('Texture')
                            p = attrSh1.createplug('File', 'user', 'texture', Plug.Dynamic)
                        else:
                            p = sh1[0].MetalColor.File
                        
                        if replace and p.get() != '':
                            p.set(base_color_maps[0])
                        elif not replace:
                            p.set(base_color_maps[0])

                        if not replace:
                            attrSh1 = mod.createnode('Metal', type='AttributeShader', parent=sh1[0])
                            attrSh1.Shader.set('Texture')
                            attrSh1.overrideinheritedattr("Gamma","data")
                            p = attrSh1.createplug('File', 'user', 'texture', Plug.Dynamic)
                        else:
                            p = sh1[0].Metal.File

                        if replace and p.get() != '':
                            p.set(metalness_maps[0])
                        elif not replace:
                            p.set(metalness_maps[0])

                        if not replace:
                            attrSh1 = mod.createnode('MetalRoughness', type='AttributeShader', parent=sh1[0])
                            attrSh1.Shader.set('Texture')
                            attrSh1.overrideinheritedattr("Gamma","data")
                            p = attrSh1.createplug('File', 'user', 'texture', Plug.Dynamic)
                        else:
                            p = sh1[0].MetalRoughness.File

                        if replace and p.get() != '':
                            p.set(roughness_maps[0]) 
                        elif not replace:
                            p.set(roughness_maps[0]) 

                    else:
                        logger.warning("No Metallic to load")
                except:
                    logger.error("Can't load Metallic")

                try:
                    if roughness_maps != []:
                       
                        if not replace:
                            sh1[0].overrideinheritedattr('Spec1',1)
                            attrSh1 = mod.createnode('Spec1Roughness', type='AttributeShader', parent=sh1[0])
                            attrSh1.Shader.set('Texture')
                            attrSh1.overrideinheritedattr("Gamma","data")
                            p = attrSh1.createplug('File', 'user', 'texture', Plug.Dynamic)
                        else:
                            p = sh1[0].Spec1Roughness.File
                        
                        if replace and p.get() != '':
                            p.set(roughness_maps[0])
                        elif not replace:
                            p.set(roughness_maps[0])

                    else:
                        logger.warning("No Roughness to load")
                except:
                    logger.error("Can't load Roughness")
                
                try:
                    if normal_maps != []:

                        if not replace:
                            attrSh1 = mod.createnode('Normal', type='AttributeShader', parent=sh1[0])
                            attrSh1.Shader.set('NormalMap')
                            p = attrSh1.createplug('File', 'user', 'texture', Plug.Dynamic)
                        else:
                            p = sh1[0].Normal.File

                        if replace and p.get() != '':
                            p.set(normal_maps[0])
                        elif not replace:
                            p.set(normal_maps[0])

                    else:
                        logger.warning("No Normal to load")
                except:
                    logger.error("Can't load Normal")

                try:
                    if sss_maps != []:

                        if not replace:
                            attrSh1 = mod.createnode('SSS', type='AttributeShader', parent=sh1[0])
                            attrSh1.Shader.set('MaskTexture')
                            attrSh1.overrideinheritedattr("Gamma","data")
                            p = attrSh1.createplug('File', 'user', 'texture', Plug.Dynamic)
                        else:
                            p = sh1[0].Shader.File

                        if replace and p.get() != '':
                            p.set(sss_maps[0])
                        elif not replace:
                            p.set(sss_maps[0])

                    else:
                        logger.warning("No sss to load")
                except:
                    print(str(traceback.format_exc()))
                    logger.error("Can't load sss")

                try:
                    if height_maps != []:

                        if not replace:
                            attrDs1 = mod.createnode('Amount', type='AttributeShader', parent=ds1[0])
                            attrDs1.Shader.set('MaskTexture')
                            attrDs1.overrideinheritedattr("Gamma","data")
                            ds1[0].overrideinheritedattr('Normalization',"Affine")
                            ds1[0].overrideinheritedattr('Offset',0)
                            ds1[0].overrideinheritedattr("RaytraceDisplacement", 2)
                            ds1[0].overrideinheritedattr("DisplaceAmount", 1)
                            ds1[0].State.set("bypass")
                            p = attrDs1.createplug('File', 'user', 'texture', Plug.Dynamic)
                        else:
                            p = ds1[0].Shader.File

                        if replace and p.get() != '':
                            p.set(height_maps[0])
                        elif not replace:
                            p.set(height_maps[0])

                    else:
                        logger.warning("No height to load")
                except:
                    print(str(traceback.format_exc()))
                    logger.error("Can't load height")


def get_maps(path):
    path = os.path.split(path)[0]
    files_list = os.listdir(path)
    textures_files_list = []
    for file in files_list:
        texture_file = os.path.join(path, file)
        textures_files_list.append(texture_file)
    return textures_files_list

def import_render_pass(reload=0):
    asset_list = get_asset_list()
    for imported_asset in asset_list:
        if imported_asset[0].stage == defaults._render_pass_:
            if imported_asset[1] in get_all_nodes():
                if reload:
                    rp_GRP = add_GRP('RENDER_PASSES')
                    rp_GRP.getchild(imported_asset[1]).delete()
                    rg_node = Document().loadfile(imported_asset[2])[0]
                    rg_node.move(rp_GRP)
                    rg_node.rename(imported_asset[1])
            else:
                if not reload:
                    rp_GRP = add_GRP('RENDER_PASSES')
                    rg_node = Document().loadfile(imported_asset[2])[0]
                    rg_node.move(rp_GRP)
                    rg_node.rename(imported_asset[1])

def import_render_graph(reload=0):
    asset_list = get_asset_list()
    for imported_asset in asset_list:
        if imported_asset[0].stage == defaults._render_graph_:
            if imported_asset[1] in get_all_nodes():
                if reload:
                    rg_GRP = add_GRP('RENDER_GRAPHS')
                    rg_GRP.getchild(imported_asset[1]).delete()
                    rg_node = Document().loadfile(imported_asset[2])[0]
                    rg_node.move(rg_GRP)
                    rg_node.rename(imported_asset[1])
            else:
                if not reload:
                    rg_GRP = add_GRP('RENDER_GRAPHS')
                    rg_node = Document().loadfile(imported_asset[2])[0]
                    rg_node.move(rg_GRP)
                    rg_node.rename(imported_asset[1])

def import_light_rig(reload=0):
    asset_list = get_asset_list()
    for imported_asset in asset_list:
        if imported_asset[0].stage == defaults._light_rig_:
            if imported_asset[1] in get_all_nodes():
                if reload:
                    lr_GRP = add_GRP('LIGHT_RIGS')
                    lr_GRP.getchild(imported_asset[1]).delete()
                    rg_node = Document().loadfile(imported_asset[2])[0]
                    rg_node.move(lr_GRP)
                    rg_node.rename(imported_asset[1])
            else:
                if not reload:
                    lr_GRP = add_GRP('LIGHT_RIGS')
                    rg_node = Document().loadfile(imported_asset[2])[0]
                    rg_node.move(lr_GRP)
                    rg_node.rename(imported_asset[1])

def import_all(reload = None):
    try:
        import_shading(reload)
    except:
        logger.warning("Can't import shading")
    try:
        import_cyclo(reload)
    except:
        logger.warning("Can't import cyclo")
    try:
        import_geo(reload)
    except:
        logger.warning("Can't import geo")
    try:
        import_render_pass(reload)
    except:
        logger.warning("Can't import render pass")
    try:
        import_render_graph(reload)
    except:
        logger.warning("Can't import render graph")
    try:
        import_light_rig(reload)
    except:
        logger.warning("Can't import light rig")
    try:
        import_texturing(reload)
    except:
        logger.warning("Can't import texturing")
    try:
        import_anim(reload)
    except:
        logger.warning("Can't import animation")
    try:
        import_camera(reload)
    except:
        logger.warning("Can't import camera")
    try:
        import_grooming(reload)
    except:
        logger.warning("Can't import grooming")
    try:
        import_cfx(reload)
    except:
        logger.warning("Can't import cfx")
    try:
        import_layout(reload)
    except:
        logger.warning("Can't import layout")

def reload_all():
    import_all(1)

def add_GRP(grp_name, parent = None):
    if grp_name not in get_all_nodes():
        with Modifier() as mod:
            if parent:
                mod.createnode(grp_name, parent=parent)
            else:
                mod.createnode(grp_name)
    node = get_node_from_name(grp_name)
    return node


def get_all_nodes():
    nodes_list = []
    for node in Document().children(recursive=True):
        nodes_list.append(node.getname())
    return nodes_list

def get_node_from_name(name):
    nodes_list = []
    for node in Document().children(recursive=True):
        if node.getname() == name:
            break
    return node
