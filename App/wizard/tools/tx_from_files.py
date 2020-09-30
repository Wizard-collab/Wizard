import ui_subprocess_manager
from gui import build

from wizard.tools.maketx import maketx
from wizard.tools import log
from wizard.vars import defaults
from wizard.tools import utility as utils

import os

logger = log.pipe_log(__name__)

def tx_from_files(files_list, tex_creation='.tex'):
    command = "from wizard.tools.maketx import maketx"
    command += "\nmaketx({}, '{}').start()".format(files_list, tex_creation)

    temp_file = utils.temp_file_from_command(command)

    env = os.environ.copy()

    wizard_path = os.path.abspath('')

    rel_site_script_path = os.path.join(defaults._softwares_scripts_path_)
    abs_site_script_path = os.path.abspath(rel_site_script_path)

    env[defaults._script_software_env_dic_[defaults._mayapy_]] = abs_site_script_path
    env[defaults._script_software_env_dic_[defaults._mayapy_]] += os.pathsep + wizard_path + '\\softwares_env'

    cwd = os.path.abspath("")

    subprocess_manager = ui_subprocess_manager.Main('pywizard {}'.format(temp_file), env, cwd)
    build.launch_normal_as_child(subprocess_manager, minimized = 1)