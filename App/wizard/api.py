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
import scene # Import the scene module to interact with the UI
import os

prefs = prefs()
logger = log.pipe_log(__name__)


# Wizard assets constants

# Domain constants
_assets_ = defaults._assets_
_library_ = defaults._library_
_sequences_ = defaults._sequences_
_editing_ = defaults._editing_
_domain_list_ = [_assets_,
				_library_,
				_sequences_,
				_editing_]

# Assets categories constants
_characters_ = defaults._characters_
_props_ = defaults._props_
_sets_ = defaults._sets_
_set_dress_ = defaults._set_dress_
_vehicles_ = defaults._vehicles_
_assets_categories_list_ = [_characters_,
							_props_,
							_sets_,
							_set_dress_,
							_vehicles_]

# Assets stages constants
_design_ = defaults._design_
_geo_ = defaults._geo_
_rig_ = defaults._rig_
_hair_ = defaults._hair_
_texturing_ = defaults._texturing_
_shading_ = defaults._shading_
_assets_stages_list_ = [_design_,
						_geo_,
						_rig_,
						_hair_,
						_texturing_,
						_shading_]

# Library categories constants
_autorig_ = defaults._autorig_
_cam_rig_ = defaults._cam_rig_
_gizmo_ = defaults._gizmo_
_light_rig_ = defaults._light_rig_
_lut_ = defaults._lut_
_render_graph_ = defaults._render_graph_
_render_pass_ = defaults._render_pass_
_scripts_ = defaults._scripts_
_sons_ = defaults._sons_
_stockshot_ = defaults._stockshot_
_video_ = defaults._video_
_cyclo_ = defaults._cyclo_
_fx_setup_ = defaults._fx_setup_
_library_categories_list_ = [_autorig_,
							_cam_rig_,
							_gizmo_,
							_light_rig_,
							_lut_,
							_render_graph_,
							_render_pass_,
							_scripts_,
							_sons_,
							_stockshot_,
							_video_,
							_cyclo_,
							_fx_setup_]

# Sequences stages constants
_concept_ = defaults._concept_
_layout_ = defaults._layout_
_animation_ = defaults._animation_
_lighting_ = defaults._lighting_
_cfx_ = defaults._cfx_
_fx_ = defaults._fx_
_compositing_ = defaults._compositing_
_camera_ = defaults._camera_
_sequences_stages_list_ = [_concept_,
							_layout_,
							_animation_,
							_lighting_,
							_cfx_,
							_fx_,
							_compositing_,
							_camera_]

# Editing categories constants
_video_edit_ = defaults._video_edit_
_sound_edit_ = defaults._sound_edit_
_editing_categories_list_ = [_video_edit_,
							_sound_edit_]


def get_site_path():
	'''This function return the wizard site path'''
	return os.environ[defaults._wizard_site_]

def get_current_user():
	'''This function return current logged wizard user'''
	return prefs.user

def get_all_users():
	'''This function return all the site users'''
	return list(prefs.site.users.keys())

def get_user_email(user=None):
	'''This function return the email of the requested user
		'user' : the user as string
		If the user doesn't exists, wizard return 'None' 
		If no user is given, wizard return the current user email'''
	if not user:
		user = prefs.user
	if user in get_all_users():
		return prefs.get_email_from_user(user)
	else:
		return None

def get_user_admin(user=None):
	'''This function check if the user is 'administrator' and return a boolean 
		'user' : the user as string
		If no user is given, wizard return the current user admin status'''
	if not user:
		user = prefs.user
	return prefs.admin_from_user(user)

def get_user_full_name(user=None):
	'''This function return the full name of the requested user 
		'user' : the user as string
		If the user doesn't exists, wizard return 'None'
		If no user is given, wizard return the current user full name'''
	if not user:
		user = prefs.user
	if user in get_all_users():
		return prefs.get_full_name_from_user(user)
	else:
		return None

def get_current_project():
	'''This function return current wizard project name of the current user'''
	return prefs.project_name

def get_all_projects():
	'''This function return all the site projects'''
	return list(prefs.site.projects.keys())

def get_project_path(project_name=None):
	'''This function return the project path of the requested project
		'project_name' : the project name as string
		If the project doesn't exists, wizard return 'None'
		If no project name is given, wizard return the current project path'''
	if not project_name:
		project_name = prefs.project_name
	if project_name in get_all_projects():
		return prefs.get_path_from_project(project_name)
	else:
		return None

def get_project_format():
	'''This function return the format of the current project'''
	return prefs.format

def get_project_frame_rate():
	'''This function return the frame rate of the current project'''
	return prefs.frame_rate

def create_character(name):
	'''Create a character with the given name'''
	asset = asset_core.asset(_assets_, _characters_, name)
	asset.create()

def create_prop(name):
	'''Create a prop with the given name'''
	asset = asset_core.asset(_assets_, _props_, name)
	asset.create()

def create_set(name):
	'''Create a set with the given name'''
	asset = asset_core.asset(_assets_, _sets_, name)
	asset.create()

def create_set_dress(name):
	'''Create a set_dress with the given name'''
	asset = asset_core.asset(_assets_, _set_dress_, name)
	asset.create()

def create_vehicle(name):
	'''Create a vehicle with the given name'''
	asset = asset_core.asset(_assets_, _vehicle_, name)
	asset.create()

def create_auto_rig(name):
	'''Create an autorig with the given name'''
	asset = asset_core.asset(_library_, _autorig_, name)
	asset.create()
	asset = asset_core.asset(_library_, _autorig_, name, _autorig_)
	asset.create()

def create_camera_rig(name):
	'''Create a camera rig with the given name'''
	asset = asset_core.asset(_library_, _cam_rig_, name)
	asset.create()
	asset = asset_core.asset(_library_, _cam_rig_, name, _cam_rig_)
	asset.create()

def create_gizmo(name):
	'''Create a gizmo with the given name'''
	asset = asset_core.asset(_library_, _gizmo_, name)
	asset.create()
	asset = asset_core.asset(_library_, _gizmo_, name, _gizmo_)
	asset.create()

def create_light_rig(name):
	'''Create a light rig with the given name'''
	asset = asset_core.asset(_library_, _light_rig_, name)
	asset.create()
	asset = asset_core.asset(_library_, _light_rig_, name, _light_rig_)
	asset.create()

def create_lut(name):
	'''Create a lut with the given name'''
	asset = asset_core.asset(_library_, _lut_, name)
	asset.create()
	asset = asset_core.asset(_library_, _lut_, name, _lut_)
	asset.create()

def create_render_graph(name):
	'''Create a render graph with the given name'''
	asset = asset_core.asset(_library_, _render_graph_, name)
	asset.create()
	asset = asset_core.asset(_library_, _render_graph_, name, _render_graph_)
	asset.create()

def create_render_pass(name):
	'''Create a render pass with the given name'''
	asset = asset_core.asset(_library_, _render_pass_, name)
	asset.create()
	asset = asset_core.asset(_library_, _render_pass_, name, _render_pass_)
	asset.create()

def create_script(name):
	'''Create a script with the given name'''
	asset = asset_core.asset(_library_, _scripts_, name)
	asset.create()
	asset = asset_core.asset(_library_, _scripts_, name, _scripts_)
	asset.create()

def create_sound(name):
	'''Create a sound with the given name'''
	asset = asset_core.asset(_library_, _sons_, name)
	asset.create()
	asset = asset_core.asset(_library_, _sons_, name, _sons_)
	asset.create()

def create_stockshot(name):
	'''Create a stockshot with the given name'''
	asset = asset_core.asset(_library_, _stockshot_, name)
	asset.create()
	asset = asset_core.asset(_library_, _stockshot_, name, _stockshot_)
	asset.create()

def create_video(name):
	'''Create a video with the given name'''
	asset = asset_core.asset(_library_, _video_, name)
	asset.create()
	asset = asset_core.asset(_library_, _video_, name, _video_)
	asset.create()

def create_cyclo(name):
	'''Create a cyclo with the given name'''
	asset = asset_core.asset(_library_, _cyclo_, name)
	asset.create()
	asset = asset_core.asset(_library_, _cyclo_, name, _cyclo_)
	asset.create()

def create_fx_setup(name):
	'''Create a fx setup with the given name'''
	asset = asset_core.asset(_library_, _fx_setup_, name)
	asset.create()
	asset = asset_core.asset(_library_, _fx_setup_, name, _fx_setup_)
	asset.create()

def create_variant(asset, variant):
	'''Create the given asset
		'asset' : wizard asset object
		'variant' : the wizard asset variant as string'''
	asset.variant = variant
	asset.create()

def create_sequence(sequence):
	'''Create the given sequence'''
	asset = asset_core.asset(_sequences_, sequence)
	asset.create()

def create_shot(sequence, shot):
	'''Create the given shot'''
	asset = asset_core.asset(_sequences_, sequence, shot)
	asset.create()

def create_animation_stage(sequence, shot):
	'''Create animation for the given shot'''
	asset = asset_core.asset(_sequences_, sequence, shot, _animation_)
	asset.create()

def asset_to_string(asset):
	'''Convert an asset object to a string'''
	string_asset = asset_core.asset_to_string(asset)
	return string_asset

def string_to_asset(string_asset):
	'''Convert a string object to an asset'''
	asset = asset_core.asset_to_string(string_asset)
	return asset

def reference_asset_in_current_scene(string_asset):
	# Get the current asset using the "scene" module
	current_asset = scene.current_asset()
	# Convert this ASSET_STRING string to a wizard asset object
	asset = asset_core.string_to_asset(string_asset)
	# Get the default export asset of the reference asset
	if not asset.export_asset or asset.export_asset == "None":
		asset.export_asset = prefs.asset(asset).export_root.default_export_asset
	# Get the last export version of the reference asset
	if not asset.export_version or asset.export_version == "None":
		asset.set_export_version()
	# Create the reference
	references(current_asset).add_reference(asset, 0, 1)
	# Refresh the ui
	scene.refresh_ui()