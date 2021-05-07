import maya.cmds as cmds
from wizard.prefs.main import prefs
from wizard.tools import utility as utils
from wizard.tools import log
import os


logger = log.pipe_log()

def quick_pb():
	format=prefs().format
	project_path = prefs().project_path
	local_project_path = prefs().local_project_path
	start = cmds.playbackOptions( q=True,min=True )
	end  = cmds.playbackOptions( q=True,max=True )

	if local_project_path and local_project_path != '':
		quickpb_path = utils.convert_local_path(os.path.join(os.path.dirname(cmds.file(q=True, sn=True)), 'quick_playblasts'), project_path, local_project_path)
		quick_file = utils.get_filename_without_override(os.path.join(quickpb_path, 'quick_playblast_0001.avi'))
		cmds.playblast(st=start, et=end, p= 100, f=quick_file, wh=format, qlt= 70, fp= 4, fmt= 'movie', fo=1, v=1)
		logger.info("Playblast saved as {}".format(quick_file))
	else:
		logger.warning('Please set a local project path in wizard before')