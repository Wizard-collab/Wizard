==========
Assets API
==========

The wizard "asset" are used everywhere in the pipeline
They can be used as Python objects or as strings ( Useful to store them in environments and files )

An asset object ( python class ) need 9 variables :

	- a <domain> variable that can be "assets", "library", "sequences" or "editing" ( Necessary )
		All thoses objects are from the same wizard "asset" class
	
	- a <category> variable ( Necessary )
		If the asset object domain variable is "Assets", the category can be

			- characters
			- props
			- sets
			- set_dress
			- vehicles
		
		If the asset object domain variable is "Sequences", the category is given by the user, example : Intro, Sequence_0001, Test...

		If the asset object domain variable is "Library", the category can be

			- autorig
			- camera_rig
			- gizmo
			- light_rig
			- lut
			- render_graph
			- render_pass
			- scripts
			- sons
			- stockshot
			- video
			- cyclo
			- fx_setup
		
		If the asset object domain variable is "Editing", the category can be

			- video_edit
			- sound_edit

	- a <name> variable ( Necessary )
		This variable is given by the user, example : John, shot_0001, main_cyclo

	- a <sage> variable ( Necessary )
		If the asset domain variable is "assets", the stage can be

			- design
			- modeling
			- rigging
			- texturing
			- shading
			- grooming

		If the asset domain variable is "library", the stage is the same as the category, example library - cyclo - myCyclo - cyclo

		If the asset domain variable is "sequences", the stage can be
		
			- concept
			- layout
			- animation
			- lighting
			- cfx
			- fx
			- compositing

		If the asset domain variable is "editing", the stage is the same as the category, example editing - video_edit - main_editing - video_edit

	- a <variant> variable ( Not necessary )
		This variable is given by the user, the default variant is "main"

	- a <software> variable ( Give nothing here, this variable is set by wizard when needed )
		pass

	- a <version> variable ( Give nothing here, this variable is set by wizard when needed )
		pass

	- a <export_asset> variable ( Give nothing here, this variable is set by wizard when needed )
		pass

	- a <export_version> variable ( Give nothing here, this variable is set by wizard when needed )
		pass


Create an asset
^^^^^^^^^^^^^^^

To create an asset, you need to have a project created, a current project setted and a current user.

First let's import the asset class ::

	from wizard.asset.main import asset

You can make sure to use the defaults strings by using the wizard "defaults" module::

	from wizard.vars import defaults

Then create an asset object using the "asset" class::

	my_new_asset = asset( domain = defaults._assets_, 
		category = defaults._characters_,
		name = "Stella",
		stage = defaults._geo_ )
	>> <wizard.asset.main.asset object at x0009098>

Notice that if you give only a category it will only create the domain object you asked::

	my_new_asset = asset( domain = defaults._sequences_, 
		category = "Intro")
	>> <wizard.asset.main.asset object at x0009098>

Since we have the asset object, let's build this asset in the pipeline::

	my_new_asset.create()
	>>1

If the asset already exists in the pipeline dictionnary or the asset folders already exists, the creation will fail returning an error::

	>>O

Remove an asset
^^^^^^^^^^^^^^^

You can only remove names and sequences categories::

	my_new_asset_to_remove = asset( domain = defaults._assets_, 
		category = defaults._characters_,
		name = "Stella")

	my_new_asset_to_remove.remove()

It will archive the asset folders and files into a '.zip' file located in the root of the project "myproject_root/archives/18982893.34.zip"

Notice that the .zip file name is given by the python "datetime" module::

    from datetime import datetime

    now = datetime.now()
    timestamp = datetime.timestamp(now)
    >>18982893.34

Manage an asset with strings
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An asset can be stored in a file as a string and converted back in an "asset" object

Let's convert the asset we just created into an asset string::

	from wizard.asset import main as asset_core

	asset_core.asset_to_string( my_new_asset )
	>> assets.characters.Stella.geo.main

You can also do this with the "utility" wizard module::

	from wizard.tools import utility

	utility.asset_to_string( my_new_asset )
	>> assets.characters.Stella.geo.main

How to get back an asset object from a string::

	from wizard.asset import main as asset_core

	asset_core.string_to_asset( "assets.characters.Stella.geo.main" )
	>> <wizard.asset.main.asset object at x0009098>

Use an asset object to launch a software
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Setup your softwares
====================

First you will need to setup your cg softwares, in order to do that, you cant print the list of softwares stored in wizard::

	from wizard.vars import defaults

	for software in default._softwares_list_:
		print( software )

	>>Maya
	>>Mayapy
	>>Maya + Yeti
	>>Photoshop
	>>Krita
	>>Zbrush
	>>Blender
	>>3ds Max
	>>Marvelous Designer
	>>Substance Painter
	>>Mari
	>>Guerilla Render
	>>Houdini
	>>Nuke
	>>Rumba
	>>Resolve
	>>Reaper
	>>Explorer

Let's setup "Maya"::

	from wizard.prefs.software import software
	from wizard.vars import defaults

	software_executable = "C:\Program Files\Autodesk\Maya2019\bin\maya.exe"
	software( defaults._maya_ ).init_settings( software_path = software_executable )
	>>INFO : Prefs saved for Maya

Now we can check the "Maya" setup using the same module::

	from wizard.prefs.software import software
	from wizard.vars import defaults

	software( defaults._maya_ ).get_path()
	>> C:\Program Files\Autodesk\Maya2019\bin\maya.exe

Access a launchable asset
=========================

To launch an asset, the asset will need to have an existing category, an existing name, an existing stage and an existing variant

Else it will return a fail.

It will also return a fail if the software you are asking isn't setted in your project

Let's build an asset object to launch it::

	from wizard.asset.main import asset
	from wizard.vars import defaults


	my_asset = asset( domain = defaults._assets_,
						category = defaults._characters_,
						name = "Stella",
						stage = defaults._geo_,
						variant = "main",
						software = defaults._maya_)

We also need to give the asset a work version using the "prefs" wizard module::
	
	from wizard.prefs.main import prefs

	last_version = prefs().asset( my_asset ).software.last_version
	>> 0000

If no version is existing, the prefs module return the defaults "0000" version

Now assign this version to our asset::

	my_asset.version = last_version

Launch the asset
================

Our asset is ready to be launched::

	my_asset.launch()
	>>Launching Maya...

List all the assets
^^^^^^^^^^^^^^^^^^^

You can list all the assets in the project using the wizard/project/main.py module

It will return the main project dictionnary::

  from wizard.project import main as project_prefs

  project_dic = project_prefs.read_project()
  print(project_dic)

  >>{'assets': {'characters': {'Stella': {'modeling': {'main': {'3ds Max': {}, 'Blender': {}, 'Houdini': {}, 'Marvelous Designer': {}, 'Maya': {}, 'Zbrush': {}, 'publish_id': 'NIKOLASACHSTELLAMOMAIN'}}}, 'goblin': {'design': {'main': {'Krita': {}, 'Photoshop': {}, 'publish_id': 'NIKOLASACHGOBLINDEMAIN'}}, 'modeling': {'main': {'3ds Max': {}, 'Blender': {}, 'Houdini': {}, 'Marvelous Designer': {}, 'Maya': {}, 'Zbrush': {}, 'publish_id': 'NIKOLASACHGOBLINMOMAIN'}}, 'rigging': {'main': {'3ds Max': {}, 'Blender': {}, 'Houdini': {}, 'Maya': {}, 'publish_id': 'NIKOLASACHGOBLINRIMAIN'}}}}, 'props': {}, 'set_dress': {}, 'sets': {}, 'vehicles': {}}, 'editing': {'sound_edit': {}, 'video_edit': {}}, 'library': {'autorig': {}, 'camera_rig': {}, 'cyclo': {}, 'fx_setup': {}, 'gizmo': {}, 'light_rig': {}, 'lut': {}, 'render_graph': {}, 'render_pass': {}, 'scripts': {}, 'sons': {}, 'stockshot': {}, 'video': {}}, 'sequences': {}}

You can also print the project in a more user readable way using the Yaml pip module::
  
  import yaml

  print(yaml.dump(project_dic))
  >>  assets:
      characters:
        Stella:
          modeling:
            main:
              3ds Max: {}
              Blender: {}
              Houdini: {}
              Marvelous Designer: {}
              Maya: {}
              Zbrush: {}
              publish_id: NIKOLASACHSTELLAMOMAIN
      props: {}
      set_dress: {}
      sets: {}
      vehicles: {}
    editing:
      sound_edit: {}
      video_edit: {}
    library:
      autorig: {}
      camera_rig: {}
      cyclo: {}
      fx_setup: {}
      gizmo: {}
      light_rig: {}
      lut: {}
      render_graph: {}
      render_pass: {}
      scripts: {}
      sons: {}
      stockshot: {}
      video: {}
    sequences: {}
