from PySide2 import QtWidgets, QtCore, QtGui
import substance_painter.ui
import substance_painter.project as project

import os
import sys
path = os.path.abspath('softwares_env/')
sys.path.append(path)

import plugin

import importlib
importlib.reload(plugin)

from wizard.tools import log
logger = log.pipe_log()
from wizard.prefs.main import prefs
from wizard.vars import defaults
from wizard.asset import main as asset_core

plugin_widgets = []
"""Keep track of added ui elements for cleanup"""

def start_plugin():
    """This method is called when the plugin is started."""
    # Store added widget for proper cleanup when stopping the plugin
    pass

def close_plugin():
    """This method is called when the plugin is stopped."""
    # We need to remove all added widgets from the UI.
    pass

print('lolllll')

def open_project():
    asset = asset_core.string_to_asset(os.environ[defaults._asset_var_])
    file = asset.file
    mesh = get_mesh(asset).replace('\\', '/')
    print(mesh)
    #template_file = get_template(asset)
    #if template_file:
    #    substance_painter.project.create(mesh_file_path=mesh,
    #                                 template_file_path=template_file)
    #else:
    project.create(mesh_file_path=mesh)
    print('lol')

def get_mesh(asset):
    references_list = prefs().asset(asset).software.references
    geo_asset_file = None
    for namespace in list(references_list.keys()):
        imported_asset = asset_core.string_to_asset(references_list[namespace][defaults._asset_key_])
        if imported_asset.stage == defaults._geo_:
            folder = prefs().asset(imported_asset).export.version_folder
            file = prefs().asset(imported_asset).export.file
            geo_asset_file = os.path.join(folder, file)
            break
    return geo_asset_file

def get_template(asset):
    references_list = prefs().asset(asset).software.references
    template_asset_file = None
    for namespace in list(references_list.keys()):
        imported_asset = asset_core.string_to_asset(references_list[namespace][defaults._asset_key_])
        if imported_asset.stage == defaults._painter_template_:
            folder = prefs().asset(imported_asset).export.version_folder
            file = prefs().asset(imported_asset).export.file
            template_asset_file = os.path.join(folder, file)
            break
    return template_asset_file

open_project()