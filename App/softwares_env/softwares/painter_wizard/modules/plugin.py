from wizard.prefs.main import prefs
from wizard.vars import defaults
from wizard.asset import main as asset_core
import os
import substance_painter.project
import substance_painter.export
import substance_painter.textureset
import json
from wizard.project import wall
import export_config

import importlib
importlib.reload(export_config)

from wizard.tools import log

prefs = prefs()
logger = log.pipe_log()



def save():
    # Check if a project is already opened:
    if substance_painter.project.is_open():
        # Check if the project needs to be saved at all:
        if substance_painter.project.needs_saving():
            asset = asset_core.string_to_asset(os.environ[defaults._asset_var_])
            asset.version = prefs.asset(asset).software.get_new_version()
            substance_painter.project.save_as(asset.file,
                                              substance_painter.project.ProjectSaveMode.Full)
        else:
            logger.info("There is nothing to save!")
    else:
        logger.info("No painter project openned!")

def export():
    asset = asset_core.string_to_asset(os.environ[defaults._asset_var_])
    print(asset.extension)
    if asset.extension == 'spt':
        export_template()
    else:
        export_maps()

def export_maps():

    asset = asset_core.string_to_asset(os.environ[defaults._asset_var_])
    file = asset.export('{}_{}'.format(asset.name, asset.variant))
    filename = os.path.splitext(os.path.split(file)[-1])[0]
    ext = os.path.splitext(os.path.split(file)[-1])[-1].split('.')[-1]

    export_config.json_config['exportPath'] = os.path.split(file)[0]
    export_config.json_config["exportPresets"][0]['maps'][0]['fileName'] = "{}_baseColor.$textureSet".format(filename)
    export_config.json_config["exportPresets"][0]['maps'][1]['fileName'] = "{}_roughness.$textureSet".format(filename)
    export_config.json_config["exportPresets"][0]['maps'][2]['fileName'] = "{}_metallic.$textureSet".format(filename)
    export_config.json_config["exportPresets"][0]['maps'][3]['fileName'] = "{}_normal.$textureSet".format(filename)
    export_config.json_config["exportPresets"][0]['maps'][4]['fileName'] = "{}_height.$textureSet".format(filename)
    export_config.json_config["exportPresets"][0]['maps'][5]['fileName'] = "{}_sss.$textureSet".format(filename)
    export_config.json_config['exportParameters'][0]['parameters']['fileFormat'] = ext

    export_list = []
    for set in substance_painter.textureset.all_texture_sets():
        set_name = set.name()
        dict = {}
        dict['rootPath'] = set_name
        export_list.append(dict)
    export_config.json_config['exportList']=export_list

    substance_painter.export.export_project_textures(export_config.json_config)

def export_template():
    asset = asset_core.string_to_asset(os.environ[defaults._asset_var_])
    file = asset.export('{}_{}'.format(asset.name, asset.variant))
    substance_painter.project.save_as_template(file, substance_painter.textureset.get_active_stack().material().name())
    wall.wall().publish_event(asset)
