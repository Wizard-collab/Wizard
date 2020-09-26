from wizard.asset import main as asset_core
from wizard.prefs.main import prefs
from wizard.tools import log
from wizard.vars import defaults
from nuke_wizard import copy_local
reload(copy_local)
from nuke_wizard.helios.lightingEngine import lightingEngine
reload(lightingEngine)
import os
import nuke
import nukescripts

logger = log.pipe_log()
prefs=prefs()

def set_project_path():
    project_path = prefs.project_path
    local_project_path = prefs.local_project_path
    if local_project_path != '' and os.path.isdir(local_project_path):
        nuke.thisRoot().knob("project_directory").setValue(local_project_path)
    else:
        nuke.thisRoot().knob("project_directory").setValue(project_path)

def resolve_local_paths():
    set_project_path()
    reload_all()

def get_asset_list():
    asset = asset_core.string_to_asset(os.environ[defaults._asset_var_])
    references_list = prefs.asset(asset).software.references
    asset_list = []
    for namespace in list(references_list.keys()):
        imported_asset = asset_core.string_to_asset(references_list[namespace][defaults._asset_key_])
        folder = prefs.asset(imported_asset).export.version_folder
        from_software = prefs.asset(imported_asset).export.version_software
        imported_asset.software = from_software
        file = prefs.asset(imported_asset).export.file
        full_path = os.path.join(folder, file)
        asset_list.append([imported_asset, namespace, full_path])
    return asset_list

def import_lighting(reload=0, helios=0):
    asset_list = get_asset_list()
    for imported_asset in asset_list:
        if imported_asset[0].stage == defaults._lighting_:

            ref_path = os.path.split(imported_asset[2])[0]

            relative_path = get_relative_path(ref_path)
            files = os.listdir(ref_path)
            files_list = []
            for file in files:
                digits = '.{}.'.format(file.split('.')[-2])
                digit_file = file.replace(digits, '.%05d.')
                if digit_file not in files_list:
                    files_list.append(digit_file)

            copy_local.copy_local(relative_path, files)

            reads_list = []

            namespaces_dic = get_all_namespaces()

            if imported_asset[1] not in namespaces_dic.keys() and not reload:

                
                
                for file in files_list:
                    full_file = os.path.join(relative_path, file).replace('\\', '/')
                    read = nuke.nodes.Read(file="%s" %(full_file), name = os.path.splitext(file)[0])
                    namespace_knob = nuke.String_Knob('wizard_namespace', 'wizard_namespace')
                    read.addKnob(namespace_knob)
                    read['wizard_namespace'].setValue(imported_asset[1])
                    read['wizard_namespace'].setEnabled(False)
                    reads_list.append(read)

                backdrop_nodes(reads_list, imported_asset[1])
                if helios:
                    lightingEngine.main(reads_list)

            elif imported_asset[1] in namespaces_dic.keys() and reload:

                reference_nodes = namespaces_dic[imported_asset[1]]
                for file in files_list:
                    for node in reference_nodes:
                        print(os.path.split(node['file'].value())[-1])
                        print(file)
                        if file == os.path.split(node['file'].value())[-1]:
                            full_file = os.path.join(relative_path, file).replace('\\', '/')
                            node['file'].setValue(full_file)

def import_lighting_helios():
    import_lighting(helios=1)

def reload_all():
    import_lighting(1)

def get_all_nodes_names():
    nodes_names_list = []
    for node in nuke.allNodes():
        nodes_names_list.append(node['name'].value())
    return nodes_names_list

def get_all_namespaces():

    namespaces_dic = dict()

    for n in nuke.allNodes('Read'):
        try:
            namespace = n['wizard_namespace'].value()
            if namespace not in namespaces_dic.keys():
                namespaces_dic[namespace] = []
            namespaces_dic[namespace].append(n)
        except NameError:
            pass

    return namespaces_dic

def unselect_all():
    for node in nuke.allNodes():
        node.setSelected(False)

def select_nodes(nodes_list):

    unselect_all()

    for node in nodes_list:
        node.setSelected(True)

def backdrop_nodes(nodes_list, name):

    select_nodes(nodes_list)
    backdrop = nukescripts.autoBackdrop()
    backdrop['name'].setValue(name)

def get_relative_path(ref_path):
    project_path = prefs.project_path
    if project_path in ref_path:
        relative_path = ref_path.replace(project_path, '')
    else:
        relative_path = ref_path
    if relative_path.startswith('/'):
        relative_path = relative_path[1:]
    if relative_path.startswith('\\'):
        relative_path = relative_path[1:]
    return relative_path
