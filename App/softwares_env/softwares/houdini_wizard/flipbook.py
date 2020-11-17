import hou
import os

def do_flipbook(namespace, frange, temp_path, scene_file):


    #namespace = "sequences_Intro_1_camera_main_0001"
    #frange = [100, 220]
    #file_path = "C:/TEST_2/test.$F.png"
    #file = "C:/houdini/sequences/Intro/1/fx/main/Houdini/work_Intro_1_fx_main.0080.hipnc"

    print(namespace)
    print(frange)
    print(temp_path)
    print(scene_file)

    file_path = os.path.join(temp_path, "temp.$F.png")

    print(file_path)

    open_file(scene_file)

    opengl_node = create_rop_network()

    cam_path = get_cam_path(namespace)

    opengl_node.parm('camera').set(cam_path)
    opengl_node.parm('trange').set("normal")
    opengl_node.parm('f1').set(frange[0])
    opengl_node.parm('f2').set(frange[1])
    opengl_node.parm('scenepath').set('/obj')
    opengl_node.parm('picture').set(file_path)

    opengl_node.parm('execute').pressButton()

def open_file(file):

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
