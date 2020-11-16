from wizard.tools import utility
import subprocess
from wizard.asset import main as asset_core
from wizard.tools import utility as utils
from wizard.tools import convert_playblast
from wizard.tools import create_video
from wizard.prefs.main import prefs
from wizard.vars import defaults
from wizard.project.wall import wall
import wizard.prefs.software as software_prefs
from wizard.software import main as software
import os
import sys
import shutil
import traceback

prefs = prefs()

class playblast():

    def __init__(self, string_asset, frange, refresh_assets, is_preroll = None):
        self.string_asset = string_asset
        self.frange = frange
        self.asset = asset_core.string_to_asset(string_asset)
        self.refresh_assets = refresh_assets
        self.is_preroll = is_preroll

    def playblast(self, cam_namespace, ornaments, show_playblast):

        self.temp_directory = utils.temp_dir()

        if self.asset.software == defaults._maya_:
            pb_command = 'from softwares.maya_wizard.do_playblast import do_playblast\n'
            pb_command += 'do_playblast("{}", "{}", "{}", {}, {}).do_playblast("{}")'.format(self.string_asset,
                                                                                            self.asset.file.replace('\\', '/'),
                                                                                            self.temp_directory.replace('\\', '/'),
                                                                                            self.frange,
                                                                                            self.refresh_assets,
                                                                                            cam_namespace)

            file = utils.temp_file_from_command(pb_command)
            print('status:Starting...')
            print('status:Working...')
            print('current_task:Playblasting...')
            sys.stdout.flush()
            mayapy = prefs.software(defaults._mayapy_).path
            env = software.get_env(defaults._mayapy_, 1)
            self.process = subprocess.Popen([mayapy, "-u", file], env = env)
            self.process.wait()

        elif self.asset.software == defaults._houdini_:
            pb_command = "from softwares.houdini_wizard import flipbook\n"
            pb_command += 'flipbook.do_flipbook("{}", {}, "{}", "{}")'.format(cam_namespace, 
                                                                  self.frange,
                                                                  self.temp_directory.replace('\\', '/'),
                                                                  self.asset.file.replace('\\', '/')
                                                                  )

            file = utils.temp_file_from_command(pb_command)

            print('status:Starting...')
            print('status:Working...')
            print('current_task:Playblasting...')
            sys.stdout.flush()

            hbatch = prefs.software(defaults._houdini_).path
            env = software.get_env(defaults._houdini_, 1)
            self.process = subprocess.Popen([hbatch, "-u", file], env = env)
            self.process.wait()

        print('percent:33')

        print('current_task:Conforming frames...')
        sys.stdout.flush()


        focal_file = os.path.join(self.temp_directory, 'focal.txt')
        self.focal = 'none'
        if os.path.isfile(focal_file):
            with open(focal_file, 'r') as f:
                self.focal = f.readlines()[0]
            os.remove(focal_file)

        if ornaments:
            self.conform_playblast()

        print('percent:66')
        print('current_task:Creating movie file...')
        sys.stdout.flush()

        pbfile = self.create_video()
        wall().playblast_event(self.asset)

        print('status:Done !')
        print('percent:100')
        sys.stdout.flush()


        if show_playblast:
            os.startfile(pbfile)

    def conform_playblast(self):
        f = 0
        frange = prefs.asset(self.asset).name.range
        preroll = prefs.asset(self.asset).name.preroll
        percent_step = 33.0/int(frange[-1])
        percent = 33
        user = prefs.user

        for file in os.listdir(self.temp_directory):
            file = os.path.join(self.temp_directory, file)

            current_frame = f+frange[0]
            if self.is_preroll:
                current_frame= current_frame-int(preroll)

            string = 'project: {} | scene: {}-{}-{}-{}-{} | user: {} | frame range: {}-{} | frame: {} | focal: {}'.format(self.asset.project, self.asset.category,
                                                                                self.asset.name,
                                                                                self.asset.stage,
                                                                                self.asset.variant,
                                                                                self.asset.version,
                                                                                user,
                                                                                frange[0],
                                                                                frange[-1],
                                                                                str(current_frame),
                                                                                str(self.focal))
            convert_playblast.convert_image(file, string)
            f+=1
            percent += percent_step
            print('percent:{}'.format(int(percent)))
            sys.stdout.flush()

    def create_video(self):
        files_list = []
        for file in os.listdir(self.temp_directory):
            files_list.append(os.path.join(self.temp_directory, file))

        pb_version = prefs.asset(self.asset).playblast.get_new_version()
        pbfile = self.asset.playblast(pb_version)
        
        pb_image = prefs.asset(self.asset).playblast.version_image(pb_version)
        shutil.copyfile(files_list[0], pb_image)

        frame_rate = prefs.frame_rate

        create_video.make_video(files_list, pbfile)

        return pbfile
