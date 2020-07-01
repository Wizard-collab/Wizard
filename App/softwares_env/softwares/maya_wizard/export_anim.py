import sys
if sys.platform == "win32":
    import ctypes
    ctypes.windll.kernel32.SetDllDirectoryA(None)

import maya.cmds as cmds
import maya.standalone
maya.standalone.initialize()

from wizard.tools import log
from wizard.asset import main as asset_core
from wizard.asset import checker
from wizard.asset import builder
from wizard.vars import defaults
from wizard.prefs.main import prefs
from wizard.project import wall
import traceback
import logging

#cmds.loadPlugin( allPlugins=True )
cmds.loadPlugin( 'AbcImport.mll' )
cmds.loadPlugin( 'AbcExport.mll' )

logger = log.pipe_log()

class export_anim():

    def __init__(self, string_asset, file, nspace_list, frange, comment = None, set_done = 1):
        self.asset = asset_core.string_to_asset(string_asset)
        self.file = file
        self.nspace_list = nspace_list
        self.range = frange
        self.references_list = prefs().asset(self.asset).variant.references
        self.comment = comment
        self.set_done = set_done
        self.camera = None

    def export_anim(self):

        percent_step = 100.0/len(self.nspace_list)
        percent = 0.0
        logging.info('status:Starting...')
        logging.info('percent:'+str(percent))
        file = None

        for nspace in self.nspace_list:

            logging.info('status:Working...')

            logging.info('current_task:Exporting {}'.format(nspace))
            cmds.file(self.file, o=True, f=True)
            percent += percent_step

            self.rig_asset = asset_core.string_to_asset(self.references_list[nspace][defaults._asset_key_])
            self.count = nspace.split('_')[-1]

            if self.camera:
                self.shapes_list = self.get_cam_shapes_from_namespace(nspace)
            else:
                self.shapes_list = self.get_shapes_from_namespace(nspace)
            logging.info(self.shapes_list)

            if self.shapes_list != []:
                self.export_shapes()

            logging.info('percent:'+str(percent))

        if self.set_done:
            logging.info('status:Done !')
        wall.wall().publish_event(self.asset)

    def export_cam(self):
        self.camera = 1
        self.export_anim()

    def export_shapes(self):

        cmds.select(self.shapes_list, replace = 1)
        export_variant = '{}_{}_{}'.format(self.rig_asset.name, self.rig_asset.variant, self.count)
        if self.camera and self.asset.domain == defaults._sequences_:
            self.asset.stage = defaults._camera_
            if not checker.check_stage_existence(self.asset):
                builder.create_stage(self.asset)
                builder.create_variant(self.asset)

        export_file = self.asset.export(export_variant, self.comment)

        self.export_abc(export_file, self.shapes_list)

    def get_shapes_from_namespace(self, namespace):

        set_name = '{}:{}'.format(namespace, defaults._rig_export_set_)

        if cmds.objExists(set_name):

            cmds.select( set_name, replace = 1 )
            shapes_list = cmds.ls( selection=True )
            return shapes_list

        else:
            logger.warning('{} not found'.format(set_name))
            return []

    def get_cam_shapes_from_namespace(self, namespace):

        set_name = '{}:{}'.format(namespace, defaults._camrig_export_set_)

        if cmds.objExists(set_name):

            cmds.select( set_name, replace = 1 )
            shapes_list = cmds.ls( selection=True )
            return shapes_list

        else:
            logger.warning('{} not found'.format(set_name))
            return []

    def export_abc(self, file, shapes_list):

        start = str(self.range[0])
        end = str(self.range[1])

        percent_step = 100.0/(int(end)-int(start))
        script = "import maya.cmds as cmds\\n"
        script += "import time\\n"
        script += "current_frame = cmds.currentTime( query=True )\\n"
        script += "percent = (current_frame - {})*{}\\n".format(int(start), round(percent_step, 1))
        script += "print('percent:'+str(percent))\\n"
        script += "time.sleep(0.01)"

        command = "-frameRange "
        command += start
        command += " "
        command += end
        command += " -step 1"
        command += " -frameRelativeSample -0.2 -frameRelativeSample 0 -frameRelativeSample 0.2 -attr GuerillaTags -uvWrite -worldSpace "
        for shape in shapes_list:
            command += '-root {} '.format(shape)
        command += '-pythonPerFrameCallback "{}"'.format(script)
        command += " -dataFormat ogawa -file "
        command += file
        logging.info(command)
        cmds.AbcExport(j=command)

