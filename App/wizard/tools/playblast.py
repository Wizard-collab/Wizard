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

prefs = prefs()

class playblast():

    def __init__(self, string_asset, frange):
        self.string_asset = string_asset
        self.frange = frange
        self.asset = asset_core.string_to_asset(string_asset)

    def playblast(self, cam_namespace, ornaments, show_playblast):

        self.temp_directory = utils.temp_dir()
        print(self.temp_directory)

        pb_command = 'from softwares.maya_wizard.do_playblast import do_playblast\n'
        pb_command += 'do_playblast("{}", "{}", "{}", {}).do_playblast("{}")'.format(self.string_asset,
                                                                                        self.asset.file.replace('\\', '/'),
                                                                                        self.temp_directory.replace('\\', '/'),
                                                                                        self.frange,
                                                                                        cam_namespace)

        file = utils.temp_file_from_command(pb_command)

        print('status:Starting...')
        print('status:Working...')
        print('current_task:Playblasting...')

        mayapy = prefs.software(defaults._mayapy_).path
        
        env = software.get_env(defaults._mayapy_, 1)

        self.process = subprocess.Popen([mayapy, "-u", file], env = env)
        self.process.wait()

        print('percent:33')

        print('current_task:Conforming frames...')

        if ornaments:
            self.conform_playblast()

        print('percent:66')
        print('current_task:Creating movie file...')

        pbfile = self.create_video()

        print('status:Done !')
        print('percent:100')

        wall().playblast_event(self.asset)

        if show_playblast:
            os.startfile(pbfile)

    def conform_playblast(self):
        f = 0
        frange = prefs.asset(self.asset).name.range
        user = prefs.user
        for file in os.listdir(self.temp_directory):
            file = os.path.join(self.temp_directory, file)
            string = 'project: {} | scene: {}-{}-{}-{}-{} | user: {} | frame range: {}-{} | frame: {}'.format(self.asset.project, self.asset.category,
                                                                                self.asset.name,
                                                                                self.asset.stage,
                                                                                self.asset.variant,
                                                                                self.asset.version,
                                                                                user,
                                                                                frange[0],
                                                                                frange[-1],
                                                                                str(f+frange[0]))
            convert_playblast.convert_image(file, string)
            f+=1

    def create_video(self):
        files_list = []
        for file in os.listdir(self.temp_directory):
            files_list.append(os.path.join(self.temp_directory, file))

        pbfile = self.asset.playblast()
        frame_rate = prefs.frame_rate
        #size = defaults._formats_dic_[prefs.format]

        create_video.make_video(files_list, pbfile)

        return pbfile
