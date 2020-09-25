import os
from wizard.asset import main as asset_core
from wizard.vars import defaults
from wizard.signal.send_signal import send_signal

def set_current_asset(asset):
	string_asset = asset_core.asset_to_string(asset)
	os.environ[defaults._scene_current_asset_] = string_asset

def current_asset():
	return asset_core.string_to_asset(os.environ[defaults._scene_current_asset_])

def refresh_ui():
	send_signal()