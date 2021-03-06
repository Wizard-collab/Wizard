import hou
import os
from softwares.houdini_wizard.tools import *
from softwares.houdini_wizard import reference_asset
from wizard.vars import defaults

def do_flipbook(string_asset, namespace, frange, temp_path, scene_file, refresh_asset):
    file_path = os.path.join(temp_path, "temp.$F.png")
    open_file(scene_file, string_asset)

    reference_asset.import_all()
    if refresh_asset:
        reference_asset.refresh_all()

    opengl_node = create_rop_network()
    cam_path = get_cam_path(namespace)
    opengl_node.parm('lpostframe').set("python")
    opengl_node.parm('postframe').set(by_frame_script_to_file(33))
    opengl_node.parm('camera').set(cam_path)
    opengl_node.parm('trange').set("normal")
    opengl_node.parm('f1').set(frange[0])
    opengl_node.parm('f2').set(frange[1])
    opengl_node.parm('scenepath').set('/obj')
    opengl_node.parm('picture').set(file_path)
    opengl_node.parm('execute').pressButton()

def open_file(file, string_asset):
    os.environ[defaults._asset_var_] = string_asset
    hou.hipFile.load(file)

def create_rop_network():
    obj_node = hou.node("/obj")
    rop_network = obj_node.createNode("ropnet", "wizard_rop_flipbook")
    opengl_node = rop_network.createNode("opengl", "wizard_opengl_flipbook")
    return opengl_node

def get_cam_path(namespace):
    obj_node = hou.node("/obj")
    node_path = "{}/{}".format(obj_node.path(), namespace)
    cam_main_node = hou.node(node_path)
    if cam_main_node:
        node_path ="{}/{}".format(cam_main_node.path(), namespace+'_xform')
        abc_xform_node = hou.node(node_path)
        if abc_xform_node:
            node_path = "{}/{}".format(abc_xform_node.path(), namespace+'_hou_cam')
            hou_camera_node = hou.node(node_path)
            if hou_camera_node:
                return hou_camera_node.path()
            else:
                print("Given camera doesn't exists in scene") 
                return None
        else:
           print("Given camera doesn't exists in scene") 
           return None
    else:
        print("Given camera doesn't exists in scene")
        return None
