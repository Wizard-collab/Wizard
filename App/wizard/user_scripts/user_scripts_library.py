import_asset_script = '''# coding: utf8

# Import asset in current scene template

# This template allows you to import the "ASSET_STRING" asset in the current scene
# Just replace "ASSET_STRING" to a valid string asset

import wizard.api as wapi

# Reference the given asset in the current scene
wapi.scene.reference_asset_in_current_scene("ASSET_STRING")
'''

create_shots_script = '''# coding: utf8

# Create shots template

# This templates allows you to create a bunch of shot in subprocess
# Just replace "MY_SEQUENCE" and the number of shots you want

import wizard.api as wapi

SEQUENCE = "MY_SEQUENCE" # The sequence name
HOW_MANY_SHOTS = 5 # The number of shots you want to create

wapi.assets.create_sequence(SEQUENCE) # Create the sequence

for shot in range(HOW_MANY_SHOTS):

	SHOT = str(shot).zfill(4) # Convert "1" to "0001"
	wapi.assets.create_shot(SEQUENCE, SHOT) # Create the shot
	
	wapi.assets.create_concept_stage(SEQUENCE, SHOT) # Create the concept stage
	wapi.assets.create_animation_stage(SEQUENCE, SHOT) # Create the animation stage
	wapi.assets.create_layout_stage(SEQUENCE, SHOT) # Create the layout stage
	wapi.assets.create_lighting_stage(SEQUENCE, SHOT) # Create the lighting stage
	wapi.assets.create_cfx_stage(SEQUENCE, SHOT) # Create the cfx stage
	wapi.assets.create_fx_stage(SEQUENCE, SHOT) # Create the fx stage
	wapi.assets.create_compositing_stage(SEQUENCE, SHOT) # Create the compositing stage
	wapi.assets.create_camera_stage(SEQUENCE, SHOT) # Create the camera stage
	'''

refresh_ui_script = '''# coding: utf8

# Refresh ui template
# This template allows you to refresh your ui

import wizard.api as wapi
# This refresh the ui
wapi.scene.refresh_ui()
'''

refresh_team_ui_script = '''# coding: utf8

# Refresh team ui template
# This template allows you to refresh the ui of all your team

import wizard.api as wapi
# This refresh the team ui
wapi.scene.refresh_team_ui()
'''

open_url = '''# coding: utf8

# Open url template
# This template allows you to open an url with your default web browser

import webbrowser

URL = "www.google.com" # The url to modify
webbrowser.open(URL, new=0, autoraise=True) # Openning the browser with the given url
'''

open_software = '''# coding: utf8

# Open file template
# This template allows you to open a file or a software

import os
DEST = "C:\\Program Files\\PureRef\\PureRef.exe" # The path of your file or software

os.startfile(DEST)
'''

scripts_dic = dict()
scripts_dic["create shots"] = create_shots_script
scripts_dic["import asset"] = import_asset_script
scripts_dic["refresh ui"] = refresh_ui_script
scripts_dic["refresh team ui"] = refresh_team_ui_script
scripts_dic["open url"] = open_url
scripts_dic["open software"] = open_software