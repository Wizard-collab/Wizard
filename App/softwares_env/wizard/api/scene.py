# coding: utf-8

""" This module is the user API of Wizard. 
	It gives access to the wizard functions in a simple way

	Author : BRUNEL Leo """

from wizard.vars import defaults # The wizard defaults module, contains all wizard constants
from wizard.tools import utility # Some wizard tools
from wizard.prefs.main import prefs # The access to all the prefs files
from wizard.asset import main as asset_core # The wizard asset core module
from wizard.tools import log # The wizard main logger
from wizard.asset import main as asset_core # Import the asset main module to manipulate assets
from wizard.asset.reference import references # Import the asset reference module to create references
from wizard.signal import send_signal

import os

prefs = prefs()
logger = log.pipe_log(__name__)



def set_current_asset(asset):
	string_asset = asset_core.asset_to_string(asset)
	os.environ[defaults._scene_current_asset_] = string_asset

def current_asset():
	return asset_core.string_to_asset(os.environ[defaults._scene_current_asset_])

def refresh_ui():
	send_signal.refresh_signal()

def update_main_progress_bar(percent):
	send_signal.task_signal(percent)

def reference_asset_in_current_scene(string_asset):
	# Convert this ASSET_STRING string to a wizard asset object
	asset = asset_core.string_to_asset(string_asset)
	# Get the default export asset of the reference asset
	if not asset.export_asset or asset.export_asset == "None":
		asset.export_asset = prefs.asset(asset).export_root.default_export_asset
	# Get the last export version of the reference asset
	if not asset.export_version or asset.export_version == "None":
		asset.set_export_version()
	# Create the reference
	references(current_asset()).add_reference(asset, 0, 1)
	# Refresh the ui
	refresh_ui()