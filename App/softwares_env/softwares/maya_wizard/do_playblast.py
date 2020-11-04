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
from maya_wizard import reference_asset
from maya_wizard import plugin
import os

cmds.loadPlugin( 'AbcImport.mll' )
cmds.loadPlugin( 'AbcExport.mll' )

class do_playblast():
    def __init__(self, string_asset, file, temp_dir, frange, refresh_assets=0):

        self.asset = asset_core.string_to_asset(string_asset)
        self.file = file
        self.range = frange
        self.format = prefs().format
        self.temp_dir = temp_dir
        self.refresh_assets = refresh_assets

    def do_playblast(self, cam_namespace):

        cmds.file(self.file, o=True, f=True)

        if self.refresh_assets:
            reference_asset.refresh_all()

        temp_file = os.path.join(self.temp_dir, 'temp_blast')

        reference_asset.import_camera()

        camera = self.select_cam(cam_namespace)
        # get camera focal length and write it to a file. File is later deleted in 'tools/playblast.py'
        camera_focal = cmds.getAttr(camera + '.focalLength')
        camera_focal = str(round(camera_focal, 1))
        with open('{}/focal.txt'.format(self.temp_dir), 'w') as f:
            f.write(camera_focal)

        cmds.playblast(st=self.range[0], et=self.range[-1], p= 100, f= temp_file, wh= self.format, qlt= 100, fp= 4, fmt= 'image', compression='png', fo=1, v=False)

    def select_cam(self, cam_namespace):
        camera_shape = self.list_cam(cam_namespace)
        if camera_shape:
            cams = cmds.ls(type='camera')
            for cam in cams:
                cmds.setAttr(cam + '.rnd', 0)
            cmds.setAttr(camera_shape + '.rnd', 1)
            return camera_shape

    def list_cam(self, cam_namespace):
        set_name = '{}:{}'.format(cam_namespace, defaults._camrig_export_set_)

        if cmds.objExists(set_name):

            cmds.select( set_name, replace = 1 )
            shapes_list = cmds.ls( selection=True )
            camera = shapes_list[0]
            camera_shape = cmds.listRelatives(camera, shapes = 1)

            return camera_shape[0]

        else:

            if cmds.namespaceInfo(cur=1) != cam_namespace:
                cmds.namespace( set = cam_namespace)
            shapes_list = cmds.namespaceInfo( listNamespace=True)
            cam = None
            for shape in shapes_list:
                if cmds.objectType(shape) == 'camera':
                    cam = shape
                    break
            if cam:
                return cam
            else:
                print('camera or {} not found'.format(set_name))
                return None
