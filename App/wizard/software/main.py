# coding: utf-8

# Defaults Python modules
import os
import subprocess
import time
import traceback

from watchdog.events import FileSystemEventHandler
# Pip Python modules
from watchdog.observers import Observer

from wizard.asset.folder import folder
# Wizard prefs modules
from wizard.prefs.main import prefs
from wizard.prefs.stats import stats
from wizard.tools import build_g_conf
# Wizard tools modules
from wizard.tools import log
from wizard.tools import utility as utils
from wizard.tools import screen_tools
# Wizard variables modules
from wizard.vars import defaults
from wizard.vars import softwares
#from wizard.asset import main as asset_core
from wizard.prefs import software as software_prefs
from wizard.signal import send_signal

import pyautogui

from PyQt5 import QtWidgets

# Creates the main logger
logger = log.pipe_log(__name__)

prefs = prefs()

try:
    from PyQt5.QtCore import QThread, pyqtSignal, QObject
except ImportError:
    logger.info('Cannot import PyQt5')

class launch():

    def __init__(self, asset, reference = None):
        # Init the " asset " and software preferences before
        # launching it
        self.asset = asset
        self.path = os.path.dirname(self.asset.work)
        self.executable = prefs.software(self.asset.software).path
        #self.sct = sct
        self.reference = reference
        env = prefs.software(self.asset.software).env

    def open(self):
        # Launch the " asset " object with the corresponding software
        if not self.executable:
            logger.warning('{} not found or not setted'.format(self.asset.software))
            return 0
        elif not self.asset.work or not os.path.isfile(self.asset.work):
            logger.error('No work file found')
            return 0
        else:
            self.command = softwares.get_cmd(self.asset.software, self.asset.work, self.reference)
            self.earThread_process = earThread(self.asset, self.path)
            self.earThread_process.start()
            self.software_process = subThread(self.command, self.earThread_process, self.asset.software, self.asset)
            self.software_process.start()
            return 1

def convert_env(env):
    if env:
        env = env.splitlines()
        return env
    else:
        return None


class ear_handler(FileSystemEventHandler, QObject):

    def __init__(self, asset):
        super(ear_handler, self).__init__()
        self.asset = asset
        #self.sct = sct

    def on_created(self, event):
        pass
        '''
        filename = os.path.basename(event.src_path)
        filename = filename.split('.')[0]
        if filename == folder(self.asset).work_name_template:
            version = folder(self.asset).version_from_file(event.src_path)
            if version.isdigit():
                self.asset.version = prefs.asset(self.asset).software.new_version(version=version)
                time.sleep(1)
                try:
                    im_file = prefs.asset(self.asset).software.image
                    screen_tools.screen_shot_current_screen(im_file)
                except:
                    logger.critical(str(traceback.format_exc()))

                # Try refreshing the ui
                try:
                    send_signal.refresh_signal()
                    logger.info('{} saved ({})'.format(event.src_path, self.asset.software))
                    send_signal.save_signal()
                    stats().add_xp(2)
                    stats().add_version(self.asset)
                except:
                    pass
        '''

class subThread(QThread):

    def __init__(self, command, earThread, software, asset):
        super(subThread, self).__init__()
        self.asset = asset
        self.command = command
        self.earThread = earThread
        self.software = software

    def run(self):
        lock = prefs.asset(self.asset).software.get_lock
        if not lock or lock == prefs.user:
            logger.info('Launching {}...'.format(self.asset.software))
            #prefs.asset(self.asset).software.set_running(0)
            os.environ[defaults._current_assets_list_]+=':'+utils.short_asset_to_string(self.asset)

            wizard_path = os.path.abspath('')
            python_path = os.path.abspath('ressources\\python27')
            python37_path = os.path.abspath('ressources\\python37')
            ocio_path = os.path.abspath('ressources\\plugins\\color_managment\\aces_1.0.3\\config.ocio')

            rel_site_script_path = os.path.join(defaults._softwares_scripts_path_)
            abs_site_script_path = os.path.abspath(rel_site_script_path)

            env = os.environ.copy()

            if self.asset.software != defaults._guerilla_ and self.asset.software != defaults._designer_:
                env[defaults._script_software_env_dic_[self.asset.software]] = abs_site_script_path
                env[defaults._script_software_env_dic_[self.asset.software]] += os.pathsep + wizard_path + '\\softwares_env'
                env[defaults._script_software_env_dic_[self.asset.software]] += os.pathsep + python_path + '\\Lib\\site-packages'


            if self.asset.software == defaults._houdini_ or self.asset.software == defaults._nuke_:
                env[defaults._script_software_env_dic_[self.asset.software]] = wizard_path + '\\softwares_env'
                env[defaults._script_software_env_dic_[self.asset.software]] += os.pathsep + python_path + '\\Lib\\site-packages'
            '''
            if self.asset.software == defaults._houdini_:
                env[defaults._script_software_env_dic_[self.asset.software]] += os.pathsep + wizard_path + '\\softwares_env\\softwares\\houdini_wizard'
            '''
            env_paths = software_prefs.software(self.asset.software).get_env_paths()
            scripts_paths = software_prefs.software(self.asset.software).get_env()

            if scripts_paths:
                for path in scripts_paths.splitlines():
                    env[defaults._script_software_env_dic_[self.asset.software]] += os.pathsep + path
            if env_paths:
                for user_env in env_paths.splitlines():
                    user_env.replace(' ', '')
                    if '=' in user_env:
                        key = user_env.split('=')[0]
                        path = user_env.split('=')[-1]
                        env[key]=path
                    else:
                        pass

            if self.asset.software == defaults._maya_ or self.asset.software == defaults._maya_yeti_:
                if defaults._maya_icon_path_ in env.keys():
                    env[defaults._maya_icon_path_] += os.pathsep + os.path.abspath(defaults._icon_path_)
                else:
                    env[defaults._maya_icon_path_] = os.path.abspath(defaults._icon_path_)


            if self.asset.software == defaults._nuke_:
                env[defaults._script_software_env_dic_[self.asset.software]] += os.pathsep + abs_site_script_path
                env[defaults._script_software_env_dic_[self.asset.software]] += os.pathsep + os.path.join(abs_site_script_path, 'nuke_wizard')
                env[defaults._script_software_env_dic_[self.asset.software]] += os.pathsep + os.path.abspath(defaults._icon_path_)

            if self.asset.software == defaults._painter_:
                env[defaults._script_software_env_dic_[self.asset.software]] += os.pathsep + os.path.join(abs_site_script_path, 'painter_wizard')

            if self.asset.software == defaults._designer_:
                env[defaults._script_software_env_dic_[self.asset.software]] = os.pathsep + python37_path + '\\Lib\\site-packages'
                env[defaults._script_software_env_dic_[self.asset.software]] += os.pathsep + wizard_path + '\\softwares_env'
                env[defaults._script_software_env_dic_[self.asset.software]] += os.pathsep + os.path.join(abs_site_script_path, 'designer_wizard')

            if self.asset.software == defaults._blender_:
                env[defaults._script_software_env_dic_[self.asset.software]] = os.pathsep + python37_path + '\\Lib\\site-packages'
                env[defaults._script_software_env_dic_[self.asset.software]] += os.pathsep + wizard_path + '\\softwares_env'
                env[defaults._script_software_env_dic_[self.asset.software]] += os.pathsep + os.path.join(abs_site_script_path, 'blender_wizard')

            env[defaults._site_var_] = os.environ[defaults._site_var_]
            env[defaults._asset_var_] = utils.asset_to_string(self.asset)

            logger.info(self.command)

            
            if self.asset.software == defaults._painter_ or self.asset.software == defaults._nuke_:
                self.process = subprocess.Popen(self.command, env=env, cwd=wizard_path + '\\softwares_env')
            elif self.asset.software == defaults._houdini_:
                self.process = subprocess.Popen(self.command, env=env, cwd=wizard_path + '\\softwares_env\\softwares\\houdini_wizard')
            else:
                self.process = subprocess.Popen(self.command, env=env)
            self.process.wait()

            self.earThread.observer.stop()
            self.earThread.observer.join()

            string_asset = utils.short_asset_to_string(self.asset)
            running_assets_list = os.environ[defaults._current_assets_list_].split(':')
            if string_asset in running_assets_list:

                running_assets_list.remove(string_asset)
                running_assets_list_string = (':').join(running_assets_list)
                os.environ[defaults._current_assets_list_] = running_assets_list_string

            send_signal.refresh_launcher_signal()
            logger.info('{} closed'.format(self.software))
            

        else:
            message = '{} - '.format(self.asset.category)
            message += '{} - '.format(self.asset.name)
            message += '{} - '.format(self.asset.stage)
            message += '{} - '.format(self.asset.variant)
            message += '{} '.format(self.asset.software)
            message += 'is locked by {}...'.format(prefs.asset(self.asset).software.get_lock)
            logger.warning(message)


class earThread(QThread):

    def __init__(self, asset, path):
        super(earThread, self).__init__()
        self.asset = asset
        self.path = path
        self.event_handler = ear_handler(asset=self.asset)

    def run(self):
        self.observer = Observer()
        self.observer.schedule(self.event_handler, self.path, recursive=True)
        self.observer.start()

def get_env(software, level=0):

    env = os.environ.copy()

    if level == 0:
        env_path = os.path.abspath('softwares_env')
        python_path = os.path.abspath('ressources\\python27\\Lib\\site-packages')
    elif level == 1:
        env_path = os.path.abspath('')
        python_path = os.path.abspath('..\\ressources\\python27\\Lib\\site-packages')

    script_path = os.path.join(env_path, 'softwares')

    env[defaults._script_software_env_dic_[software]] = script_path
    env[defaults._script_software_env_dic_[software]] += os.pathsep + env_path
    env[defaults._script_software_env_dic_[software]] += os.pathsep + python_path
    env['PATH'] = ''

    env_paths = software_prefs.software(software).get_env_paths()

    if env_paths:
        for user_env in env_paths.splitlines():
            user_env.replace(' ', '')
            if '=' in user_env:
                key = user_env.split('=')[0]
                path = user_env.split('=')[-1]
                env[key]=path
            else:
                pass

    return env
