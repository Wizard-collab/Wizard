from wizard.prefs.main import prefs
import wizard.asset.main as asset_core
from wizard.vars import defaults
from wizard.tools import log
from guerilla import Document, Modifier
import os


logger = log.pipe_log(__name__)

def setup_guerilla():
	set_format()
	set_range()
	set_frame_rate()
	create_main_node()
	
def set_format(half = None):
	format = prefs().format

	if not half:
		width = format[0]
		height = format[1]
	else:
		width = int(format[0])/2
		height = int(format[1])/2

	Document().ProjectWidth.set(width)
	Document().ProjectHeight.set(height)
	Document().ProjectAspectRatio.set(1)

def set_range():
	asset = asset_core.string_to_asset(os.environ[defaults._asset_var_])
	range = prefs().asset(asset).name.range
	start = int(range[0])
	end = int(range[-1])
	Document().FirstFrame.set(start)
	Document().LastFrame.set(end)

def set_frame_rate():
	frame_rate = prefs().frame_rate
	Document().Preferences.FrameRate.set(frame_rate)

def create_main_node():
	asset = asset_core.string_to_asset(os.environ[defaults._asset_var_])
	grp_name = defaults._stage_export_grp_dic_[asset.stage]
	if grp_name and grp_name not in get_all_nodes():
		create_GRP(grp_name)

def create_GRP(grp_name):
	with Modifier() as mod:
		mod.createnode(grp_name)

def get_all_nodes():
	nodes_list = []
	for node in Document().children(recursive=True):
		nodes_list.append(node.getname())
	return nodes_list
	