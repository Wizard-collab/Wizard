import sys
if sys.platform == "win32":
    import ctypes
    ctypes.windll.kernel32.SetDllDirectoryA(None)

import maya.standalone
maya.standalone.initialize()
import maya.cmds as cmds

from wizard.asset import main as asset_core
from wizard.prefs.main import prefs
from wizard.tools import utility as utils
from wizard.vars import defaults
import os

class do_playblast():
    def __init__(self, string_asset, file, temp_dir, frange):

        self.asset = asset_core.string_to_asset(string_asset)
        self.file = file
        self.range = frange
        self.format = prefs().format
        self.temp_dir = temp_dir

    def do_playblast(self, cam_namespace):

        
        cmds.file(self.file, o=True, f=True)
        temp_file = os.path.join(self.temp_dir, 'temp_blast')

        self.select_cam(cam_namespace)

        cmds.playblast(st=self.range[0], et=self.range[-1], p= 100, f= temp_file, wh= self.format, qlt= 100, fp= 4, fmt= 'image', compression='png', fo=1, v=False)

    def select_cam(self, cam_namespace):
        camera_shape = self.list_cam(cam_namespace)
        if camera_shape:
            cams = cmds.ls(type='camera')
            for cam in cams:
                cmds.setAttr(cam + '.rnd', 0)
            cmds.setAttr(camera_shape + '.rnd', 1)

    def list_cam(self, cam_namespace):
        set_name = '{}:{}'.format(cam_namespace, defaults._camrig_export_set_)

        if cmds.objExists(set_name):

            cmds.select( set_name, replace = 1 )
            shapes_list = cmds.ls( selection=True )
            camera = shapes_list[0]
            camera_shape = cmds.listRelatives(camera, shapes = 1)

            return camera_shape[0]

        else:
            print('{} not found'.format(set_name))
            return None