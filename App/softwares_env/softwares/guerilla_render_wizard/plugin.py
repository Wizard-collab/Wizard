from wizard.asset import main as asset_core
from wizard.prefs.main import prefs
from wizard.tools import log
from wizard.vars import defaults
from wizard.project import wall

from guerilla import Document, pynode
from softwares.guerilla_render_wizard.reference_asset import get_all_nodes


import os

logger = log.pipe_log(__name__)


def save():
    asset = asset_core.string_to_asset(os.environ[defaults._asset_var_])
    asset.version = prefs().asset(asset).software.get_new_version()
    Document().save(asset.file)

def export_cyclo(asset):
    file = asset.export('{}_{}'.format(asset.name, asset.variant))
    Document().save(file)
    save()
    wall.wall().publish_event(asset)

def export_shading(asset):
    file = asset.export('{}_{}'.format(asset.name, asset.variant))
    rg_name = 'shading_GRP'.format(asset.stage, asset.name)
    export_node(file, rg_name, asset)

def export_render_pass(asset):
    file = asset.export('{}_{}'.format(asset.name, asset.variant))
    rp_name = 'render_pass_GRP'
    export_node(file, rp_name, asset)

def export_render_graph(asset):
    file = asset.export('{}_{}'.format(asset.name, asset.variant))
    rg_name = 'render_graph_GRP'
    export_node(file, rg_name, asset)

def export_light_rig(asset):
    file = asset.export('{}_{}'.format(asset.name, asset.variant))
    rg_name = 'light_rig_GRP'
    export_node(file, rg_name, asset)

def export_all():
    asset = asset_core.string_to_asset(os.environ[defaults._asset_var_])
    if asset.stage == defaults._cyclo_:
        export_cyclo(asset)
    elif asset.stage == defaults._shading_:
        export_shading(asset)
    elif asset.stage == defaults._render_pass_:
        export_render_pass(asset)
    elif asset.stage == defaults._render_graph_:
        export_render_graph(asset)
    elif asset.stage == defaults._light_rig_:
        export_light_rig(asset)

def export_node(file, node_name, asset):
    if node_name in get_all_nodes():
        node = pynode(node_name)
        if type(node).__name__ == defaults._guerilla_node_type_:
            node.savefile(file)
            save()
            wall.wall().publish_event(asset)
        else:
            logger.warning('Node "{}" is missing'.format(node_name))
    else:
        logger.warning('Node "{}" is missing'.format(node_name))

def export_GRP(grp_name, file):
    if grp_name in get_all_nodes():
        node = pynode(grp_name)
        node.savefile(file)
        return 1
    else:
        logger.warning('Please create a node named "{}" with all the things you wants to export'.format(grp_name))
        return 0

def get_all_nodes():
    nodes_list = []
    for node in Document().children(recursive=True):
        nodes_list.append(node.getname())
    return nodes_list
