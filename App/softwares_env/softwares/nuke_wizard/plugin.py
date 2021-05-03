from wizard.asset import main as asset_core
from wizard.vars import defaults
from wizard.prefs.main import prefs
from wizard.asset.folder import folder
from nuke_wizard import reference_asset
from wizard.signal import send_signal
from wizard.tools import utility as utils
reload(reference_asset)
import nuke
import os

prefs = prefs()

def save():

    asset = asset_core.string_to_asset(os.environ[defaults._asset_var_])
    asset.version = prefs.asset(asset).software.get_new_version()
    if os.path.isfile(asset.file):
        asset.version = str(int(asset.version) + 1).zfill(4)

    nuke.scriptSaveAs(asset.file)

    string_asset = utils.asset_to_string(asset)
    os.environ[defaults._asset_var_] = string_asset
    send_signal.save_request_signal(asset.file, string_asset)

def set_f_range():
    asset = asset_core.string_to_asset(os.environ[defaults._asset_var_])
    f_range = prefs.asset(asset).name.range
    for n in nuke.allNodes('Read'):
        n['first'].setValue(f_range[0])
        n['last'].setValue(f_range[1])
        n['origfirst'].setValue(f_range[0])
        n['origlast'].setValue(f_range[1])
    nuke.knob("root.first_frame", str(f_range[0]))
    nuke.knob("root.last_frame", str(f_range[1]))

def set_format():
    format = ' '.join([str(prefs.format[0]), str(prefs.format[1])])
    format_name = prefs.project_name + '_format'
    project_format = '{} {}'.format(format, format_name)
    nuke.addFormat( project_format )
    nuke.root().knob('format').setValue(format_name)

def set_f_rate():
    f_rate = prefs.frame_rate
    nuke.knob("root.fps", str(f_rate))

def prepare_export():
    asset = asset_core.string_to_asset(os.environ[defaults._asset_var_])
    node_name = 'Export (wizard)'
    if node_name not in reference_asset.get_all_nodes_names():
        write_node = nuke.createNode('Write')
        write_node['name'].setValue(node_name)
    else:
        write_node = nuke.toNode(node_name)

    base_file = folder(asset).export_file
    extension = os.path.splitext(base_file)[-1]
    file = base_file.replace(extension, '.%05d')+extension
    path = os.path.split(asset.export('{}{}{}'.format(asset.category, asset.name, asset.variant)))[0]
    full_file = os.path.join(path, file)

    write_node['file'].setValue(full_file.replace('\\', '/'))
