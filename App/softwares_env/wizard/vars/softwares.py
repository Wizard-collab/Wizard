from wizard.vars import defaults
from wizard.prefs.main import prefs
import os
from wizard.tools import log

logger = log.pipe_log(__name__)
prefs = prefs()


# Softwares commands
_executable_key_ = '[executable]'
_file_key_ = '[file]'
_script_key_ = '[startup_script]'
_reference_key_ = '[reference]'

_default_cmd_ = '"{}" "{}"'.format(_executable_key_, _file_key_)

_maya_cmd_ = '"{}" -file "{}" -script "{}"'.format(_executable_key_, _file_key_, _script_key_)

_painter_cmd_ = '"{}"'.format(_executable_key_)

_guerilla_cmd_ = '''"{}" "{}" --pycmd "execfile('{}')"'''.format(_executable_key_, _file_key_, _script_key_)

_nuke_cmd_ =  '"{}" --nukex "{}"'.format(_executable_key_, _file_key_)

_blender_cmd_ = '"{}" "{}" --python "{}"'.format(_executable_key_, _file_key_, _script_key_)

_houdini_cmd_ = '"{}" "{}" waitforui "{}" '.format(_executable_key_, _file_key_, _script_key_)

_hython_cmd_ = '"{}" "{}"'.format(_executable_key_, _file_key_)

_cmd_dic_ = dict()
_cmd_dic_[defaults._maya_] = _maya_cmd_
_cmd_dic_[defaults._maya_yeti_] = _maya_cmd_
_cmd_dic_[defaults._mayapy_] = _maya_cmd_
_cmd_dic_[defaults._photoshop_] = _default_cmd_
_cmd_dic_[defaults._krita_] = _default_cmd_
_cmd_dic_[defaults._zbrush_] = _default_cmd_
_cmd_dic_[defaults._blender_] = _blender_cmd_
_cmd_dic_[defaults._3dsmax_] = _default_cmd_
_cmd_dic_[defaults._marvelous_] = _default_cmd_
_cmd_dic_[defaults._painter_] = _painter_cmd_
_cmd_dic_[defaults._designer_] = _default_cmd_
_cmd_dic_[defaults._mari_] = _default_cmd_
_cmd_dic_[defaults._guerilla_] = _guerilla_cmd_
_cmd_dic_[defaults._houdini_] = _houdini_cmd_
_cmd_dic_[defaults._hython_] = _hython_cmd_
_cmd_dic_[defaults._nuke_] = _nuke_cmd_
_cmd_dic_[defaults._rumba_] = _default_cmd_
_cmd_dic_[defaults._resolve_] = _default_cmd_
_cmd_dic_[defaults._reaper_] = _default_cmd_
_cmd_dic_[defaults._folder_] = _default_cmd_

_scripts_dic_ = dict()

_scripts_dic_[defaults._maya_] = os.path.abspath(os.path.join(defaults._softwares_scripts_path_+defaults._mel_startup_))
_scripts_dic_[defaults._maya_yeti_] = os.path.abspath(os.path.join(defaults._softwares_scripts_path_+defaults._mel_startup_))
_scripts_dic_[defaults._mayapy_] = os.path.abspath(os.path.join(defaults._softwares_scripts_path_+defaults._mel_startup_))
_scripts_dic_[defaults._guerilla_] = os.path.abspath('').replace('\\', '/') + '/softwares_env/softwares/guerilla_render_wizard/startup.py'
_scripts_dic_[defaults._blender_] = os.path.abspath(os.path.join(defaults._softwares_scripts_path_+defaults._blender_startup_))
_scripts_dic_[defaults._houdini_] = os.path.abspath(os.path.join(defaults._softwares_scripts_path_+defaults._houdini_startup_))

def get_cmd(software, file, reference = None):

	cmd = _cmd_dic_[software]

	if software == defaults._painter_ and not reference:
		cmd = _default_cmd_

	executable = prefs.software(software).path
	cmd = cmd.replace(_executable_key_, executable)

	cmd = cmd.replace(_file_key_, file)

	if _script_key_ in cmd:
		cmd = cmd.replace(_script_key_, _scripts_dic_[software])

	if reference and _reference_key_ in cmd:
		cmd = cmd.replace(_reference_key_, reference)

	logger.debug(cmd)

	return cmd
