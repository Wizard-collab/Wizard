^^^^^^^^^^
Python SDK
^^^^^^^^^^

wizard.api.preferences
======================

- get_site_path()
    - This function takes no arguments
    - Return the current site path ( `string` )

- get_current_user()
    - This function takes no arguments
    - Return the current user ( `string` )

- get_all_user()
    - This function takes no arguments
    - Return all the site users ( `list` )

- get_user_email( user = None )
    - If a user ( `string` ) is given, return the user email ( `string` )
    - Else, return the current user email ( `string` )

- get_user_admin( user = None )
    - If a user ( `string` ) is given, return the user admin state ( `boolean` )
    - Else, return the current user admin state ( `boolean` )

- get_user_full_name( user = None )
    - If a user ( `string` ) is given, return the user full name ( `string` )
    - Else, return the current user full name ( `string` )

- get_current_project()
    - This function takes no arguments
    - Return the current project name ( `string` )

- get_all_projects()
    - This function takes no arguments
    - Return all the projects names ( `list` )

- get_project_path( project_name = None )
    - If a project name ( `string` ) is given, return the project path ( `string` )
    - Else, return the current project path ( `string` )

- get_project_format()
    - This function takes no arguments
    - Return the current project pixel format as [width, height] ( [`int`, `int`])

- get_project_frame_rate()
    - This function takes no arguments
    - Return the current project frame rate ( `int` )

- set_user( user_name, password )
    - This function needs a user ( `string` ) and a password ( `string` )
    - Return nothing

wizard.api.assets
=================

- create_character( name )
    - `Create a character`
    - args:
        - name ( `string` )

- create_prop( name )
    - `Create a prop`
    - args:
        - name ( `string` )

- create_set( name )
    - `Create a set`
    - args:
        - name ( `string` )

- create_set_dress( name )
    - `Create a set dress`
    - args:
        - name ( `string` )

- create_vehicle( name )
    - `Create a vehicle`
    - args:
        - name ( `string` )

- create_auto_rig( name )
    - `Create an auto rig`
    - args:
        - name ( `string` )

- create_camera_rig( name )
    - `Create a camera rig`
    - args:
        - name ( `string` )

- create_gizmo( name )
    - `Create a gizmo`
    - args:
        - name ( `string` )

- create_light_rig( name )
    - `Create a light rig`
    - args:
        - name ( `string` )

- create_lut( name )
    - `Create a lut`
    - args:
        - name ( `string` )

- create_render_graph( name )
    - `Create a render graph`
    - args:
        - name ( `string` )

- create_render_pass( name )
    - `Create a render pass`
    - args:
        - name ( `string` )

- create_script( name )
    - `Create a script`
    - args:
        - name ( `string` )

- create_sound( name )
    - `Create a sound`
    - args:
        - name ( `string` )

- create_stockshot( name )
    - `Create a stockshot`
    - args:
        - name ( `string` )

- create_video( name )
    - `Create a video`
    - args:
        - name ( `string` )

- create_cyclo( name )
    - `Create a cyclo`
    - args:
        - name ( `string` )

- create_fx_setup( name )
    - `Create a fx setup`
    - args:
        - name ( `string` )

- create_variant( asset, variant )
    - `Create an asset variant`
    - args:
        - asset ( `wizard.asset.main.asset` )
        - variant ( `string` )

- create_sequence( sequence )
    - `Create a sequence`
    - args:
        - sequence ( `string` )

- create_shot( sequence, shot )
    - `Create a shot for a given sequence`
    - args:
        - sequence ( `string` )
        - shot ( `string` )

- create_animation_stage( sequence, shot )
    - `Create an animation stage for a given sequence and shot`
    - args:
        - sequence ( `string` )
        - shot ( `string` )

- create_lighting_stage( sequence, shot )
    - `Create a lighting stage for a given sequence and shot`
    - args:
        - sequence ( `string` )
        - shot ( `string` )

- create_fx_stage( sequence, shot )
    - `Create a fx stage for a given sequence and shot`
    - args:
        - sequence ( `string` )
        - shot ( `string` )

- create_camera_stage( sequence, shot )
    - `Create a camera stage for a given sequence and shot`
    - args:
        - sequence ( `string` )
        - shot ( `string` )

- create_concept_stage( sequence, shot )
    - `Create a concept stage for a given sequence and shot`
    - args:
        - sequence ( `string` )
        - shot ( `string` )

- create_layout_stage( sequence, shot )
    - `Create a layout stage for a given sequence and shot`
    - args:
        - sequence ( `string` )
        - shot ( `string` )

- create_compositing_stage( sequence, shot )
    - `Create a compositing stage for a given sequence and shot`
    - args:
        - sequence ( `string` )
        - shot ( `string` )

- create_cfx_stage( sequence, shot )
    - `Create a cfx stage for a given sequence and shot`
    - args:
        - sequence ( `string` )
        - shot ( `string` )

- asset_to_string( asset )
    - `Return the asset path`
    - args:
        - asset ( `wizard.asset.main.asset` )

- string_to_asset( string_asset ):
    - `Convert the asset path to an asset object`
    - args:
        - string_asset ( `string` )