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
import os

prefs = prefs()
logger = log.pipe_log(__name__)

def create_character(name):
	'''Create a character with the given name'''
	asset = asset_core.asset(defaults._assets_, defaults._characters_, name)
	asset.create()

def create_prop(name):
	'''Create a prop with the given name'''
	asset = asset_core.asset(defaults._assets_, defaults._props_, name)
	asset.create()

def create_set(name):
	'''Create a set with the given name'''
	asset = asset_core.asset(defaults._assets_, defaults._sets_, name)
	asset.create()

def create_set_dress(name):
	'''Create a set_dress with the given name'''
	asset = asset_core.asset(defaults._assets_, defaults._set_dress_, name)
	asset.create()

def create_vehicle(name):
	'''Create a vehicle with the given name'''
	asset = asset_core.asset(defaults._assets_, defaults._vehicle_, name)
	asset.create()

def create_auto_rig(name):
	'''Create an autorig with the given name'''
	asset = asset_core.asset(defaults._library_, defaults._autorig_, name)
	asset.create()
	asset = asset_core.asset(defaults._library_, defaults._autorig_, name, defaults._autorig_)
	asset.create()

def create_camera_rig(name):
	'''Create a camera rig with the given name'''
	asset = asset_core.asset(defaults._library_, defaults._cam_rig_, name)
	asset.create()
	asset = asset_core.asset(defaults._library_, defaults._cam_rig_, name, defaults._cam_rig_)
	asset.create()

def create_gizmo(name):
	'''Create a gizmo with the given name'''
	asset = asset_core.asset(defaults._library_, defaults._gizmo_, name)
	asset.create()
	asset = asset_core.asset(defaults._library_, defaults._gizmo_, name, defaults._gizmo_)
	asset.create()

def create_light_rig(name):
	'''Create a light rig with the given name'''
	asset = asset_core.asset(defaults._library_, defaults._light_rig_, name)
	asset.create()
	asset = asset_core.asset(defaults._library_, defaults._light_rig_, name, defaults._light_rig_)
	asset.create()

def create_lut(name):
	'''Create a lut with the given name'''
	asset = asset_core.asset(defaults._library_, defaults._lut_, name)
	asset.create()
	asset = asset_core.asset(defaults._library_, defaults._lut_, name, defaults._lut_)
	asset.create()

def create_painter_template(name):
	'''Create a painter template with the given name'''
	asset = asset_core.asset(defaults._library_, defaults._painter_template_, name)
	asset.create()
	asset = asset_core.asset(defaults._library_, defaults._painter_template_, name, defaults._painter_template_)
	asset.create()

def create_render_graph(name):
	'''Create a render graph with the given name'''
	asset = asset_core.asset(defaults._library_, defaults._render_graph_, name)
	asset.create()
	asset = asset_core.asset(defaults._library_, defaults._render_graph_, name, defaults._render_graph_)
	asset.create()

def create_render_pass(name):
	'''Create a render pass with the given name'''
	asset = asset_core.asset(defaults._library_, defaults._render_pass_, name)
	asset.create()
	asset = asset_core.asset(defaults._library_, defaults._render_pass_, name, defaults._render_pass_)
	asset.create()

def create_script(name):
	'''Create a script with the given name'''
	asset = asset_core.asset(defaults._library_, defaults._scripts_, name)
	asset.create()
	asset = asset_core.asset(defaults._library_, defaults._scripts_, name, defaults._scripts_)
	asset.create()

def create_sound(name):
	'''Create a sound with the given name'''
	asset = asset_core.asset(defaults._library_, defaults._sons_, name)
	asset.create()
	asset = asset_core.asset(defaults._library_, defaults._sons_, name, defaults._sons_)
	asset.create()

def create_stockshot(name):
	'''Create a stockshot with the given name'''
	asset = asset_core.asset(defaults._library_, defaults._stockshot_, name)
	asset.create()
	asset = asset_core.asset(defaults._library_, defaults._stockshot_, name, defaults._stockshot_)
	asset.create()

def create_video(name):
	'''Create a video with the given name'''
	asset = asset_core.asset(defaults._library_, defaults._video_, name)
	asset.create()
	asset = asset_core.asset(defaults._library_, defaults._video_, name, defaults._video_)
	asset.create()

def create_cyclo(name):
	'''Create a cyclo with the given name'''
	asset = asset_core.asset(defaults._library_, defaults._cyclo_, name)
	asset.create()
	asset = asset_core.asset(defaults._library_, defaults._cyclo_, name, defaults._cyclo_)
	asset.create()

def create_fx_setup(name):
	'''Create a fx setup with the given name'''
	asset = asset_core.asset(defaults._library_, defaults._fx_setup_, name)
	asset.create()
	asset = asset_core.asset(defaults._library_, defaults._fx_setup_, name, defaults._fx_setup_)
	asset.create()

def create_variant(asset, variant):
	'''Create the given asset
		'asset' : wizard asset object
		'variant' : the wizard asset variant as string'''
	asset.variant = variant
	asset.create()

def create_sequence(sequence):
	'''Create the given sequence'''
	asset = asset_core.asset(defaults._sequences_, sequence)
	asset.create()

def create_shot(sequence, shot):
	'''Create the given shot'''
	asset = asset_core.asset(defaults._sequences_, sequence, shot)
	asset.create()

def create_animation_stage(sequence, shot):
	'''Create animation for the given shot'''
	asset = asset_core.asset(defaults._sequences_, sequence, shot, defaults._animation_)
	asset.create()

def create_lighting_stage(sequence, shot):
	'''Create lighting for the given shot'''
	asset = asset_core.asset(defaults._sequences_, sequence, shot, defaults._lighting_)
	asset.create()

def create_fx_stage(sequence, shot):
	'''Create fx for the given shot'''
	asset = asset_core.asset(defaults._sequences_, sequence, shot, defaults._fx_)
	asset.create()

def create_camera_stage(sequence, shot):
	'''Create camera for the given shot'''
	asset = asset_core.asset(defaults._sequences_, sequence, shot, defaults._camera_)
	asset.create()

def create_concept_stage(sequence, shot):
	'''Create concept for the given shot'''
	asset = asset_core.asset(defaults._sequences_, sequence, shot, defaults._concept_)
	asset.create()

def create_layout_stage(sequence, shot):
	'''Create layout for the given shot'''
	asset = asset_core.asset(defaults._sequences_, sequence, shot, defaults._layout_)
	asset.create()

def create_compositing_stage(sequence, shot):
	'''Create compositing for the given shot'''
	asset = asset_core.asset(defaults._sequences_, sequence, shot, defaults._compositing_)
	asset.create()

def create_cfx_stage(sequence, shot):
	'''Create cfx for the given shot'''
	asset = asset_core.asset(defaults._sequences_, sequence, shot, defaults._cfx_)
	asset.create()

def asset_to_string(asset):
	'''Convert an asset object to a string'''
	string_asset = asset_core.asset_to_string(asset)
	return string_asset

def string_to_asset(string_asset):
	'''Convert a string object to an asset'''
	asset = asset_core.asset_to_string(string_asset)
	return asset
