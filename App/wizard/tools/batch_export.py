from wizard.vars import defaults
import ui_subprocess_manager
from wizard.tools import utility as utils
from wizard.prefs.main import prefs
import os
from wizard.software import main as software
from gui import build

class batch_export():

    def __init__(self, asset):
        self.asset = asset
        
        if asset.software == defaults._maya_:
            self.batch_export_maya()
        elif asset.software == defaults._houdini_:
            self.batch_export_houdini()

    def batch_export_maya(self):

        command =  'from softwares.maya_wizard.batch_export import batch_export\n'
        command += 'batch_export()'

        file = utils.temp_file_from_command(command)
        mayapy = prefs.software(defaults._mayapy_).path
        env = software.get_env(defaults._mayapy_, 0)
        env[defaults._asset_var_] = utils.asset_to_string(self.asset)

        self.ui_subprocess_manager = ui_subprocess_manager.Main([mayapy, "-u", file], env)
        build.launch_normal_as_child(self.ui_subprocess_manager, minimized = 1)

    def batch_export_houdini(self):

        command =  'from softwares.houdini_wizard.batch_export import batch_export\n'
        command += 'batch_export()'

        file = utils.temp_file_from_command(command)
        hython = prefs.software(defaults._hython_).path
        env = software.get_env(defaults._hython_, 0)
        env[defaults._asset_var_] = utils.asset_to_string(self.asset)

        self.ui_subprocess_manager = ui_subprocess_manager.Main([hython, "-u", file], env)
        build.launch_normal_as_child(self.ui_subprocess_manager, minimized = 1)