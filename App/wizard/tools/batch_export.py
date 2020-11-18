from wizard.vars import defaults
import ui_subprocess_manager
from wizard.tools import utility as utils
from wizard.tools import log
from wizard.prefs.main import prefs
import os
from wizard.software import main as software
from gui import build

prefs = prefs()
logger = log.pipe_log()

class batch_export():

    def __init__(self, asset):
        self.asset = asset
        
        if asset.software == defaults._maya_:
            self.batch_export_maya()

    def batch_export_maya(self):

        command =  'from softwares.maya_wizard.batch_export import batch_export\n'
        command += 'batch_export()'

        file = utils.temp_file_from_command(command)
        mayapy = prefs.software(defaults._mayapy_).path
        env = software.get_env(defaults._mayapy_, 0)
        env[defaults._asset_var_] = utils.asset_to_string(self.asset)

        self.ui_subprocess_manager = ui_subprocess_manager.Main([mayapy, "-u", file], env)
        build.launch_normal_as_child(self.ui_subprocess_manager, minimized = 1)
        

def sequence(asset, nspace_list, cam_nspace_list, out_range, refresh_assets, auto_hair):
    if asset.software == defaults._maya_:
        maya_sequence(asset, nspace_list, cam_nspace_list, out_range, refresh_assets, auto_hair)
    elif asset.software == defaults._houdini_:
        houdini_sequence(asset, out_range, refresh_assets)

class houdini_sequence():
    def __init__(self, asset, out_range, refresh_assets):
        self.asset = asset
        self.out_range = out_range
        self.refresh_assets = refresh_assets
        self.command = ''

        self.fx_export()
        self.execute()

    def fx_export(self):
        self.command += 'from softwares.houdini_wizard.batch_export import batch_export\n'
        self.command += 'batch_export({}, {})'.format(self.refresh_assets, self.out_range)

    def execute(self):
        file = utils.temp_file_from_command(self.command)
        hython = prefs.software(defaults._hython_).path
        env = software.get_env(defaults._hython_, 0)
        env[defaults._asset_var_] = utils.asset_to_string(self.asset)

        self.ui_subprocess_manager = ui_subprocess_manager.Main([hython, "-u", file], env)
        build.launch_normal_as_child(self.ui_subprocess_manager, minimized = 1)

class maya_sequence():
    def __init__(self, asset, nspace_list, cam_nspace_list, out_range, refresh_assets, auto_hair):
        self.asset = asset
        self.nspace_list = nspace_list
        self.cam_nspace_list = cam_nspace_list
        self.out_range = out_range
        self.refresh_assets = refresh_assets
        self.set_done = 1
        self.command = ''

        if self.nspace_list != []:

            if self.cam_nspace_list != []:
                self.set_done = 0

            if self.asset.stage == defaults._animation_ and auto_hair:
                self.auto_hair()
            elif self.asset.stage == defaults._animation_ and not auto_hair:
                self.animation()
            elif self.asset.stage == defaults._cfx_:
                self.fur()

        else:
            if self.cam_nspace_list != []:
                pass
            else:
                logger.info("Nothing to export")

        if self.cam_nspace_list != []:
            self.camera()

        self.execute()

        


    def auto_hair(self):
        self.command += 'from softwares.maya_wizard.auto_hair import auto_hair\n'
        self.command += 'auto_hair("{}", "{}", {}, frange = {}, set_done = {}, refresh_assets = {}).auto_hair()'.format(utils.asset_to_string(self.asset),
                                                                                self.asset.file.replace('\\', '/'),
                                                                                self.nspace_list,
                                                                                self.out_range,
                                                                                self.set_done,
                                                                                self.refresh_assets)

    def animation(self):
        self.command += 'from softwares.maya_wizard.export_anim import export_anim\n'
        self.command += 'export_anim("{}", "{}", {}, frange = {}, set_done = {}, refresh_assets = {}).export_anim()'.format(utils.asset_to_string(self.asset),
                                                                                self.asset.file.replace('\\', '/'),
                                                                                self.nspace_list,
                                                                                self.out_range,
                                                                                self.set_done,
                                                                                self.refresh_assets)

    def fur(self):
        self.command += 'from softwares.maya_wizard.export_fur import export_fur\n'
        self.command +='export_fur("{}", "{}", {}, {}, refresh_assets = {}).export_fur()'.format(utils.asset_to_string(self.asset),
                                                                                self.asset.file.replace('\\', '/'),
                                                                                self.nspace_list,
                                                                                self.out_range,
                                                                                self.refresh_assets)

    def camera(self):
        self.command += '\nfrom softwares.maya_wizard.export_anim import export_anim\n'
        self.command += 'export_anim("{}", "{}", {}, frange = {}, refresh_assets = {}).export_cam()'.format(utils.asset_to_string(self.asset),
                                                                                self.asset.file.replace('\\', '/'),
                                                                                self.cam_nspace_list,
                                                                                self.out_range,
                                                                                self.refresh_assets)

    def execute(self):
        if self.command != '':
            file = utils.temp_file_from_command(self.command)
            mayapy = prefs.software(defaults._mayapy_).path
            env = software.get_env(defaults._mayapy_, 0)
            env[defaults._asset_var_] = utils.asset_to_string(self.asset)
            self.ui_subprocess_manager = ui_subprocess_manager.Main([mayapy, "-u", file], env)
            build.launch_normal_as_child(self.ui_subprocess_manager, minimized = 1)
        else:
            logger.warning('Nothing to export !')