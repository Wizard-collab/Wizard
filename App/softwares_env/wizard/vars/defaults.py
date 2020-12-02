# coding: utf-8

# Defaults Python module
import os

_reg_key_ = "SOFTWARE\\WOW6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\Wizard"
_infos_file_lk_ = "https://storage.googleapis.com/wizard-files.com/beta/INFOS.json"
_wizard_url_ = 'https://wizard-pipeline-manager.webflow.io/'
_wizard_version_ = '0.9.8.00-b'
_doc_index_path_ = 'ressources/docs/index.html'
_license_file_ = 'ressources/LICENSE'
_contact_email_ = 'wizard-support@leobrunel.com'

import sys
def ressources_path(relative_path):
     if hasattr(sys, '_MEIPASS'):
         return os.path.join(sys._MEIPASS, relative_path)
     return os.path.join(os.path.abspath("."), relative_path)

# Promotions list
_E5_ = 'E5'
_E4_ = 'E4'
_E3_ = 'E3'
_E2_ = 'E2'
_E1_ = 'E1'
_staff_ = 'Staff'
_promotions_list_ = [_E1_, _E2_, _E3_, _E4_, _E5_, _staff_]

_email_client_id_ = "668963692252-qjequcu689vt9ovqlkhtd4oac4cgaorl.apps.googleusercontent.com"
_email_client_secret_ = "wOKkzRqR9psn43AovXEavfgR"
_email_client_token_ = "1//03gcZ2BQkh0OJCgYIARAAGAMSNwF-L9IrwFanKef1C-AhnOnRxgS6K9Z5rsVq-PpVl46kFPS_Bolf-13aga5jO6W_rw0H8w0UpHI"

_site_db_env_ = 'WIZARD_DB'
_project_db_env_ = 'PROJECT_DB'
_local_db_env_ = 'LOCAL_DB'

_wizard_site_ = 'WIZARD_SITE'

_abs_site_path_ = 'abs_site_path'

_current_assets_list_ = 'CURRENT_ASSETS_LIST'

_trash_folder_ = 'archives'

_work_count_ = 'works_count'

_copy_folder_ = 'team_files'
_copy_file_ = 'copy.ma'

_updates_folder_ = 'ressources/updates/'
_update_text_file_ = 'text.txt'
_update_state_file_ = 'state.txt'
_update_image_file_ = 'image.jpg'
_update_version_file_ = 'version.txt'
_last_updates_ = 'last_update'
_script_cache_ = 'script_cache'

_git_link_ = 'https://github.com/Wizard-collab/Wizard'

_shutter_ = 'shutter'

_rig_export_set_ = 'export_set'
_camrig_export_set_ = 'camera_export_set'
_yeti_export_set_ = 'yeti_export_set'
_scalp_export_set_ = 'scalp_export_set'

_NTSC_ = 'NTSC'
_720_ = 'HD 720'
_1080_ = 'HD 1080'
_SCOPE_ = 'SCOPE 2K'
_UHD_ = 'UHD 4K'

_formats_dic_ = dict()
_formats_dic_[_NTSC_] = [720, 480]
_formats_dic_[_720_] = [1280, 720]
_formats_dic_[_1080_] = [1920, 1080]
_formats_dic_[_SCOPE_] = [2048, 858]
_formats_dic_[_UHD_] = [3840, 2160]

_guerilla_ocio_env_ = 'OCIO'

# Domain library
_assets_ = 'assets'
_sequences_ = 'sequences'
_library_ = 'library'
_editing_ = 'editing'
_playblast_ = 'playblast'
_export_ = 'export'

_proxy_ = 'proxy'
_visible_ = 'isVisible'
_abc_workflow_ = 'abc'
_wsd_workflow_ = 'wsd'

_domains_list_ = [_assets_, _library_, _sequences_, _editing_]

_asset_id_key_ = 'publish_id'

_shared_folder_ = 'shared_files'

# Wsd library
_wsd_pos_ = 'pos'
_wsd_rot_ = 'rot'
_wsd_scale_ = 'scale'


# Asset categories library
_characters_ = 'characters'
_props_ = 'props'
_sets_ = 'sets'
_set_dress_ = 'set_dress'
_vehicles_ = 'vehicles'

# Library categories
_autorig_ = 'autorig'
_cam_rig_ = 'camera_rig'
_gizmo_ = 'gizmo'
_light_rig_ = 'light_rig'
_lut_ = 'lut'
_render_graph_ = 'render_graph'
_render_pass_ = 'render_pass'
_scripts_ = 'scripts'
_sons_ = 'sons'
_stockshot_ = 'stockshot'
_video_ = 'video'
_cyclo_ = 'cyclo'
_fx_setup_ = 'fx_setup'
_material_ = 'material'
_painter_template_ = 'painter_template'

# Editing categories
_video_edit_ = "video_edit"
_sound_edit_ = "sound_edit"
_editing_categories_list_ = [_video_edit_, _sound_edit_]
_editing_stages_dic_ = {}
_editing_stages_dic_[_video_edit_] = _video_edit_
_editing_stages_dic_[_sound_edit_] = _sound_edit_



_lib_categories_list_ = [_autorig_,
						_cam_rig_,
						_cyclo_,
						_gizmo_,
						_light_rig_,
						_lut_,
						_render_graph_,
						_render_pass_,
						_fx_setup_,
						_scripts_,
						_sons_,
						_stockshot_,
						_video_,
						_material_,
						_painter_template_]

_lib_stages_dic_ = {}
_lib_stages_dic_[_autorig_] = _autorig_
_lib_stages_dic_[_cam_rig_] = _cam_rig_
_lib_stages_dic_[_cyclo_] = _cyclo_
_lib_stages_dic_[_gizmo_] = _gizmo_
_lib_stages_dic_[_light_rig_] = _light_rig_
_lib_stages_dic_[_lut_] = _lut_
_lib_stages_dic_[_render_graph_] = _render_graph_
_lib_stages_dic_[_render_pass_] = _render_pass_
_lib_stages_dic_[_fx_setup_] = _fx_setup_
_lib_stages_dic_[_scripts_] = _scripts_
_lib_stages_dic_[_sons_] = _sons_
_lib_stages_dic_[_stockshot_] = _stockshot_
_lib_stages_dic_[_video_] = _video_
_lib_stages_dic_[_material_] = _material_
_lib_stages_dic_[_painter_template_] = _painter_template_

# Asset stages library
_design_ = 'design'
_geo_ = 'modeling'
_rig_ = 'rigging'
_texturing_ = 'texturing'
_shading_ = 'shading'
_hair_ = 'grooming'

# User scripts library
_user_script_name_ = 'name'
_user_script_image_ = 'image'
_user_script_ = 'script'
_user_scripts_ = 'scripts'
_subprocess_ = 'subprocess'

# Asset stages list
_assets_stages_ = [_design_,
					_geo_,
					_rig_,
					_hair_,
					_texturing_,
					_shading_]


# Sequence stages library
_concept_ = 'concept'
_layout_ = 'layout'
_animation_ = 'animation'
_lighting_ = 'lighting'
_cfx_ = 'cfx'
_fx_ = 'fx'
_compositing_ = 'compositing'
_camera_ = 'camera'

# Sequences stages list
_sequences_stages_ = [_concept_,
						_layout_,
						_animation_,
						_lighting_,
						_cfx_,
						_fx_,
						_compositing_,
						_camera_]

_stage_export_grp_dic_ = dict()
_stage_export_grp_dic_[_geo_] = 'geo_GRP'
_stage_export_grp_dic_[_rig_] = 'rig_GRP'
_stage_export_grp_dic_[_hair_] = 'hair_GRP'
_stage_export_grp_dic_[_cyclo_] = 'cyclo_GRP'
_stage_export_grp_dic_[_shading_] = 'shading_GRP'
_stage_export_grp_dic_[_render_pass_] = 'render_pass_GRP'
_stage_export_grp_dic_[_render_graph_] = 'render_graph_GRP'
_stage_export_grp_dic_[_light_rig_] = 'light_rig_GRP'
_stage_export_grp_dic_[_lighting_] = 'lighting_GRP'
_stage_export_grp_dic_[_autorig_] = 'autoRig_GRP'
_stage_export_grp_dic_[_cam_rig_] = 'camRig_GRP'
_stage_export_grp_dic_[_layout_] = 'layout_GRP'
_stage_export_grp_dic_[_set_dress_] = 'set_dress_GRP'

_export_manager_stage_dic_ = dict()
_export_manager_stage_dic_[_export_] = [_rig_, _hair_, _cam_rig_]
_export_manager_stage_dic_[_playblast_] = [_cam_rig_, _camera_]

# Reference keys library
_name_space_key_ = 'namespace'
_string_asset_ = 'asset'
_count_ = 'count'

# Asset state vars
_work_ = 'work'
_publish_ = 'pub'
_export_folder_ = "_EXPORT"
_playblast_folder_ = "_PLAYBLAST"

# Production states vars
_asset_state_ = 'asset_state'
_assigned_user_ = 'assigned_user'

_todo_ = 'todo'
_wip_ = 'wip'
_done_ = 'done'
_ignore_ = 'ignore'
_error_ = 'error'

# Library stages library
#_cyclo_ = 'cyclos'
#_sounds_ = 'sounds'
#_light_rigs_ = 'light_rigs'

_make_tx_ = 'ressources/plugins/maketx/maketx.exe'
_sandbox_ = '_SANDBOX'

#subprocess manager library
_percent_signal_ = 'percent:'
_subprocess_current_task_ = 'current_task:'
_subprocess_status_ = 'status:'



# Icons library
_icon_path_ = ressources_path('ressources/images/')
_settings_icon_ = _icon_path_ + 'settings.png'
_pin_icon_ = _icon_path_ + 'pinned.png'
_tree_pin_ = _icon_path_ + 'tree_pin.png'
_asset_icon_ = _icon_path_ + 'asset.png'
_unpin_icon_ = _icon_path_ + 'unpinned.png'
_folder_icon_ = _icon_path_ + 'folder.png'
_tx_icon_ = _icon_path_ + 'tx_icon.png'
_asset_events_icon_ = _icon_path_ + 'asset_notif.png'
_user_events_icon_ = _icon_path_ + 'user_notif.png'
_save_icon_ = _icon_path_ + 'save.png'
_edge_image_ = _icon_path_ + 'edge.png'
_info_icon_ = _icon_path_ + 'popup_info.ico'
_warning_icon_ = _icon_path_ + 'popup_warning.ico'
_error_icon_ = _icon_path_ + 'popup_warning.ico'
_show_wizard_icon_ = _icon_path_ + 'show_wizard_arrow.png'
_hide_wizard_icon_ = _icon_path_ + 'hide_wizard_arrow.png'
_down_arrow_ = _icon_path_ + 'down_arrow.png'
_add_icon_ = _icon_path_ + 'add.png'
_user_icon_ = _icon_path_ + 'user.png'
_assets_icon_ = _icon_path_ + 'assets.png'
_sequences_icon_ = _icon_path_ + 'sequences.png'
_library_icon_ = _icon_path_ + 'library.png'
_edit_icon_ = _icon_path_ + 'edit.png'
_wizard_logo_ = _icon_path_ + 'wizard.png'
_wizard_icon_ = _icon_path_ + 'wizard_icon.png'
_file_viewer_ico_ = _icon_path_ + 'file_viewer_icon.ico'
_wizard_welcome_logo_ = _icon_path_ + 'wizard_welcome_logo.png'
_wizard_folder_ = _icon_path_ + 'wizard_images/'
_wizard_ico_ = _icon_path_ + 'wizard_icon.ico'
_server_ico_ = _icon_path_ + 'server.ico'
_server_ico_black_ = _icon_path_ + 'server_black.ico'
_trash_icon_ = _icon_path_ + 'trash.png'
_trash_large_icon_ = _icon_path_ + 'trash_large.png'
_trash_icon_hover_ = _icon_path_ + 'trash_hover.png'
_locked_icon_ = _icon_path_ + 'locked.png'
_unlocked_icon_ = _icon_path_ + 'unlocked.png'
_launch_icon_ = _icon_path_ + 'launch.png'
_launch_gif_ = _icon_path_ + 'launch.gif'
_loading_gif_ = _icon_path_ + 'loading.gif'
_server_running_gif_ = _icon_path_ + 'server_running.gif'
_email_icon_ = _icon_path_ + 'email.png'
_copy_icon_ = _icon_path_ + 'copy_icon.png'
_check_icon_ = _icon_path_ + 'checked.gif'
_no_server_icon_ = _icon_path_ + 'no_server.gif'
_new_user_chat_icon_ = _icon_path_ + 'chat_user.gif'
_message_pop_icon_ = _icon_path_ + 'message_pop.gif'
_xp_pop_icon_ = _icon_path_ + 'level_medal.png'
_creation_pop_icon_ = _icon_path_ + 'creation_pop.gif'
_publish_pop_icon_ = _icon_path_ + 'publish_pop.gif'
_playblast_pop_icon_ = _icon_path_ + 'camera_popup_icon.gif'
_ticket_pop_icon_ = _icon_path_ + 'ticket_pop.gif'
_closed_ticket_pop_icon_ = _icon_path_ + 'closed_ticket_pop.gif'
_remove_pop_icon_ = _icon_path_ + 'remove_pop.gif'
_email_flat_icon_ = _icon_path_ + 'email.png'
_clear_icon_ = _icon_path_ + 'clear.png'
_execute_icon_ = _icon_path_ + 'execute.png'
_execute_sub_icon_ = _icon_path_ + 'execute_sub.png'
_create_shelf_icon_ = _icon_path_ + 'create_shelf_icon.png'
_close_popup_icon_ = _icon_path_ + 'close_popup.png'
_avatar_images_path_ = 'Data/avatars/'
_neutral_avatar_ = _icon_path_ + 'admin.png'
_log_icon_ = _icon_path_ + 'log.png'
_focus_icon_ = _icon_path_ + 'running_focus.png'
_running_icon_ = _icon_path_ + 'running.png'
_chat_icon_ = _icon_path_ + 'chat.png'
_chat_icon_notif_ = _icon_path_ + 'chat_notif.png'
_welcome_image_ = _icon_path_ + 'welcome.png'
_server_icon_ = _icon_path_ + 'server.png'
_send_message_icon_ = _icon_path_ + 'send.png'
_join_file_icon_ = _icon_path_ + 'join_file.png'
_server_on_icon_ = _icon_path_ + 'server_on.png'
_server_off_icon_ = _icon_path_ + 'server_off.png'
_wall_icon_ = _icon_path_ + 'notif.png'
_wall_update_icon_ = _icon_path_ + 'notif_new.png'
_new_notif_ = _icon_path_ + 'new_notif.png'
_show_icon_ = _icon_path_ + 'show.png'
_hide_icon_ = _icon_path_ + 'hide.png'
_wall_event_middle_line_ = _icon_path_ + 'wall_event_middle_line.png'
_nopicture_image_ = _icon_path_ + 'nopicture.png'
_default_profile_image_ = _icon_path_ + 'admin.png'
_stats_icon_ = _icon_path_ + 'stats.png'
_day_icon_ = _icon_path_ + 'sun.png'
_night_icon_ = _icon_path_ + 'night.png'
_delete_asset_icon_ = _icon_path_ + 'remove_pop.png'
_key_icon_ = _icon_path_ + 'key.png'
_projects_icon_ = _icon_path_ + 'projects.png'
_project_folder_icon_ = _icon_path_ + 'project_folder.png'
_node_icon_ = _icon_path_ + 'node_icon.png'
_reference_list_icon_ = _icon_path_ + 'reference_list_icon.png'
_icon_mode_view_ = _icon_path_ + 'icon_mode_view.png'
_sd_icon_ = _icon_path_ + 'sd_icon.png'
_welcom_user_image_ = _icon_path_ + 'welcome_user.png'
_prod_manager_user_image_ = _icon_path_ + 'prod_manager_user_image.png'
_welcome_project_image_ = _icon_path_ + 'welcome_project.png'
_welcome_server_image_ = _icon_path_ + 'welcome_server_logo.png'
_history_icon_ = _icon_path_ + 'history_icon.png'
_playblast_icon_ = _icon_path_ + 'playblast_icon.png'
_tickets_icon_ = _icon_path_ + 'tickets_icon.png'
_show_playblast_icon_ = _icon_path_ + 'show_playblast_icon.png'
_versions_manager_icon_ = _icon_path_ + 'versions_manager_icon.png'
_export_icon_ = _icon_path_ + 'export_icon.png'
_maya_save_icon_ = _icon_path_ + 'save.png'
_maya_export_icon_ = _icon_path_ + 'maya_export.png'
_maya_import_icon_ = _icon_path_ + 'maya_import.png'
_maya_group_icon_ = _icon_path_ + 'maya_group_icon.png'
_guerilla_import_icon_ = _icon_path_ + 'guerilla_import.png'
_guerilla_reload_icon_ = _icon_path_ + 'guerilla_reload.png'
_guerilla_export_icon_ = _icon_path_ + 'guerilla_export.png'
_guerilla_save_icon_ = _icon_path_ + 'guerilla_save.png'
_guerilla_geo_icon_ = _icon_path_ + 'guerilla_geo.png'
_guerilla_groom_icon_ = _icon_path_ + 'guerilla_groom.png'
_guerilla_texturing_icon_ = _icon_path_ + 'guerilla_texturing.png'
_guerilla_shading_icon_ = _icon_path_ + 'guerilla_shading.png'
_guerilla_anim_icon_ = _icon_path_ + 'guerilla_anim.png'
_guerilla_cfx_icon_ = _icon_path_ + 'guerilla_cfx.png'
_guerilla_render_pass_icon_ = _icon_path_ + 'guerilla_render_pass.png'
_guerilla_cyclo_icon_ = _icon_path_ + 'guerilla_cyclo.png'
_guerilla_layout_icon_ = _icon_path_ + 'guerilla_layout.png'
_guerilla_match_all_icon_ = _icon_path_ + 'guerilla_match_all.png'
_guerilla_format_icon_ = _icon_path_ + 'guerilla_format.png'
_guerilla_frame_range_icon_ = _icon_path_ + 'guerilla_frame_range.png'
_guerilla_frame_rate_icon_ = _icon_path_ + 'guerilla_frame_rate.png'
_guerilla_build_main_rp_ = _icon_path_ + 'build_main_pass.png'
_guerilla_light_layers_ = _icon_path_ + 'guerilla_light_layers.png'
_dragdrop_icon_ = _icon_path_ + 'dragdrop.png'
_export_list_icon_ = _icon_path_ + 'export_list_icon.png'
_export_list_icon_gray_ = _icon_path_ + 'export_list_icon_gray.png'
_export_list_neutral_icon_ = _icon_path_ + 'export_list_neutral_icon.png'
_missing_file_export_list_icon_ = _icon_path_ + 'missing_file_export_list.png'
_kill_process_icon_ = _icon_path_ + 'kill_process.png'
_comment_icon_ = _icon_path_ + 'comment.png'
_manual_publish_icon_ = _icon_path_ + 'manual_publish.png'
_debug_icon_ = _icon_path_ + 'debug_icon.png'
_batch_publish_icon_ = _icon_path_ + 'batch_publish.png'
_extension_icon_ = _icon_path_ + 'extension_icon.png'
_open_ticket_icon_ = _icon_path_ + 'open_ticket.png'
_ticket_icon_ = _icon_path_ + 'ticket_icon.png'
_gray_ticket_icon_ = _icon_path_ + 'gray_ticket_icon.png'
_red_ticket_icon_ = _icon_path_ + 'red_ticket_icon.png'
_my_tickets_icon_ = _icon_path_ + 'my_tickets_icon.png'
_add_empty_file_icon_ = _icon_path_ + 'add_empty_file_icon.png'
_batch_playblast_icon_ = _icon_path_ + 'batch_playblast.png'
_setup_icon_ = _icon_path_ + 'setup.png'
_chat_file_icon_ = _icon_path_ + 'chat_file_icon.png'
_wizard_load_image_ = _icon_path_ + 'wizard_load_image.png'
_refresh_icon_ = _icon_path_ + "refresh.png"
_site_icon_ = _icon_path_ + "site.png"
_python_blue_icon_ = _icon_path_ + "python_blue.png"
_sandbox_icon_ = _icon_path_ + "sandbox.png"
_missing_pb_image_ = _icon_path_ + "missing_pb_image.png"

_menu_icon_path_ = _icon_path_ + 'menu/'

_menu_git_icon_ = _menu_icon_path_ + 'git.png'
_menu_new_icon_ = _menu_icon_path_ + 'plus.png'
_menu_projects_icon_ = _menu_icon_path_ + 'book.png'
_menu_settings_icon_ = _menu_icon_path_ + 'gear.png'
_menu_user_icon_ = _menu_icon_path_ + 'user.png'
_menu_password_icon_ = _menu_icon_path_ + 'key.png'
_menu_api_icon_ = _menu_icon_path_ + 'api.png'
_menu_contact_icon_ = _menu_icon_path_ + 'mail.png'

# Domain icons
_domain_icons_ = dict()
_domain_icons_[_assets_] = _assets_icon_
_domain_icons_[_library_] = _library_icon_
_domain_icons_[_editing_] = _edit_icon_
_domain_icons_[_sequences_] = _sequences_icon_

#Sounds library
_sound_path_ = 'ressources/sounds/'
_tick_sound_ = _sound_path_ + 'tick.wav'
_bubble_sound_ = _sound_path_ + 'bubble.mp3'
_woo_sound_ = _sound_path_ + 'woo.mp3'

_tick_key_ = 'Tick'
_bubble_key_ = 'Bubble'
_woo_key_ = 'Woo'

_pop_sounds_dic_ = dict()
_pop_sounds_dic_[_tick_key_] = _tick_sound_
_pop_sounds_dic_[_bubble_key_] = _bubble_sound_
_pop_sounds_dic_[_woo_key_] = _woo_sound_


# Stage icons library ( dictionnary )
_design_icon_ = 'design.png'
_geo_icon_ = 'modeling.png'
_rig_icon_ = 'rigging.png'
_texturing_icon_ = 'texturing.png'
_shading_icon_ = 'shading.png'
_hair_icon_ = 'grooming.png'
_concept_icon_ = 'concept.png'
_layout_icon_ = 'layout.png'
_animation_icon_ = 'animation.png'
_lighting_icon_ = 'lighting.png'
_fx_icon_ = 'fx.png'
_compositing_icon_ = 'compositing.png'
_camera_icon_ = 'camera.png'
_cfx_icon_ = 'cfx.png'
_autorig_icon_ = 'autorig.png'
_cam_rig_icon_ = 'cam_rig.png'
_cyclo_icon_ = 'cyclo.png'
_gizmo_icon_ = 'gizmo.png'
_light_rig_icon_ = 'light_rig.png'
_lut_icon_ = 'lut.png'
_render_graph_icon_ = 'render_graph.png'
_render_pass_icon_ = 'render_pass.png'
_fx_setup_icon_ = 'fx_setup.png'
_scripts_icon_ = 'scripts.png'
_sons_icon_ = 'sons.png'
_stockshot_icon_ = 'stockshot.png'
_video_icon_ = 'video.png'
_video_edit_icon_ = 'video_edit.png'
_sound_edit_icon_ = 'sound_edit.png'
_material_icon_ = 'material.png'
_painter_template_icon_ = 'painter_template.png'

_design_icon_large_ = _icon_path_ + 'design_large.png'
_geo_icon_large_ = _icon_path_ + 'modeling_large.png'
_rig_icon_large_ = _icon_path_ + 'rigging_large.png'
_texturing_icon_large_ = _icon_path_ + 'texturing_large.png'
_shading_icon_large_ = _icon_path_ + 'shading_large.png'
_hair_icon_large_ = _icon_path_ + 'grooming_large.png'
_concept_icon_large_ = _icon_path_ + 'concept_large.png'
_layout_icon_large_ = _icon_path_ + 'layout_large.png'
_animation_icon_large_ = _icon_path_ + 'animation_large.png'
_lighting_icon_large_ = _icon_path_ + 'lighting_large.png'
_fx_icon_large_ = _icon_path_ + 'fx_large.png'
_compositing_icon_large_ = _icon_path_ + 'compositing_large.png'
_cfx_icon_large_ = _icon_path_ + 'cfx_large.png'
_autorig_icon_large_ = _icon_path_ + 'autorig_large.png'
_cam_rig_icon_large_ = _icon_path_ + 'cam_rig_large.png'
_cyclo_icon_large_ = _icon_path_ + 'cyclo_large.png'
_gizmo_icon_large_ = _icon_path_ + 'gizmo_large.png'
_light_rig_icon_large_ = _icon_path_ + 'light_rig_large.png'
_lut_icon_large_ = _icon_path_ + 'lut_large.png'
_render_graph_icon_large_ = _icon_path_ + 'render_graph_large.png'
_render_pass_icon_large_ = _icon_path_ + 'render_pass_large.png'
_fx_setup_icon_large_ = _icon_path_ + 'fx_setup_large.png'
_scripts_icon_large_ = _icon_path_ + 'scripts_large.png'
_sons_icon_large_ = _icon_path_ + 'sons_large.png'
_stockshot_icon_large_ = _icon_path_ + 'stockshot_large.png'
_video_icon_large_ = _icon_path_ + 'video_large.png'
_video_edit_icon_large_ = _icon_path_ + 'video_edit_large.png'
_sound_edit_icon_large_ = _icon_path_ + 'sound_edit_large.png'
_material_icon_large_ = _icon_path_ + 'video_edit_large.png'
_painter_template_icon_large_ = _icon_path_ + 'painter_template_large.png'


_stage_icon_={}
_stage_icon_[_design_] = _icon_path_ + _design_icon_
_stage_icon_[_geo_] = _icon_path_ + _geo_icon_
_stage_icon_[_rig_] = _icon_path_ + _rig_icon_
_stage_icon_[_texturing_] = _icon_path_ + _texturing_icon_
_stage_icon_[_shading_] = _icon_path_ + _shading_icon_
_stage_icon_[_hair_] = _icon_path_ + _hair_icon_
_stage_icon_[_concept_] = _icon_path_ + _concept_icon_
_stage_icon_[_layout_] = _icon_path_ + _layout_icon_
_stage_icon_[_animation_] = _icon_path_ + _animation_icon_
_stage_icon_[_lighting_] = _icon_path_ + _lighting_icon_
_stage_icon_[_cfx_] = _icon_path_ + _cfx_icon_
_stage_icon_[_fx_] = _icon_path_ + _fx_icon_
_stage_icon_[_compositing_] = _icon_path_ + _compositing_icon_
_stage_icon_[_camera_] = _icon_path_ + _camera_icon_
_stage_icon_[_autorig_]= _icon_path_ + _autorig_icon_
_stage_icon_[_cam_rig_] = _icon_path_ + _cam_rig_icon_
_stage_icon_[_cyclo_] = _icon_path_ + _cyclo_icon_
_stage_icon_[_gizmo_] = _icon_path_ + _gizmo_icon_
_stage_icon_[_light_rig_] = _icon_path_ + _light_rig_icon_
_stage_icon_[_lut_] = _icon_path_ + _lut_icon_
_stage_icon_[_render_graph_] = _icon_path_ + _render_graph_icon_
_stage_icon_[_render_pass_] = _icon_path_ + _render_pass_icon_
_stage_icon_[_fx_setup_] = _icon_path_ + _fx_setup_icon_
_stage_icon_[_scripts_] = _icon_path_ + _scripts_icon_
_stage_icon_[_sons_] = _icon_path_ + _sons_icon_
_stage_icon_[_stockshot_] = _icon_path_ + _stockshot_icon_
_stage_icon_[_video_] = _icon_path_ + _video_icon_
_stage_icon_[_video_edit_] = _icon_path_ + _video_edit_icon_
_stage_icon_[_sound_edit_] = _icon_path_ + _sound_edit_icon_
_stage_icon_[_material_] = _icon_path_ + _material_icon_
_stage_icon_[_painter_template_] = _icon_path_ + _painter_template_icon_



# Publish files count
_pub_count_dic_ = {}
_pub_count_dic_[_design_] = 1
_pub_count_dic_[_geo_] = 1
_pub_count_dic_[_rig_] = 1
_pub_count_dic_[_texturing_] = 10000
_pub_count_dic_[_shading_] = 1
_pub_count_dic_[_hair_] = 1
_pub_count_dic_[_concept_] = 1
_pub_count_dic_[_layout_] = 1
_pub_count_dic_[_animation_] = 1
_pub_count_dic_[_lighting_] = 1000000
_pub_count_dic_[_cfx_] = 1
_pub_count_dic_[_fx_] = 1
_pub_count_dic_[_fx_setup_] = 1
_pub_count_dic_[_compositing_] = 1000000

# Softs library
_maya_ = 'Maya'
_mayapy_ = 'Mayapy'
_maya_yeti_ = 'Maya + Yeti'
_photoshop_ = 'Photoshop'
_krita_ = 'Krita'
_zbrush_ = 'Zbrush'
_blender_ = 'Blender'
_3dsmax_ = '3ds Max'
_marvelous_ = 'Marvelous Designer'
_painter_ = 'Substance Painter'
_designer_ = 'Substance Designer'
_mari_ = 'Mari'
_guerilla_ = 'Guerilla Render'
_houdini_ = 'Houdini'
_hython_ = 'Hython'
_nuke_ = 'Nuke'
_rumba_ = 'Rumba'
_resolve_ = 'Resolve'
_reaper_ = 'Reaper'
_folder_ = 'Explorer'
_softwares_list_ = [_maya_,
					_maya_yeti_,
					_mayapy_,
					_photoshop_,
					_krita_,
					_zbrush_,
					_blender_,
					_3dsmax_,
					_marvelous_,
					_painter_,
					_designer_,
					_mari_,
					_guerilla_,
					_houdini_,
					_hython_,
					_nuke_,
					_rumba_,
					_resolve_,
					_reaper_,
					_folder_]

_publish_softwares_list_ = [_maya_, _blender_, _maya_yeti_, _guerilla_, _nuke_]

# Publish extension dictionary
_pub_ext_dic_ = {}
_pub_ext_dic_[_design_] = {}
_pub_ext_dic_[_design_][_photoshop_] = 'png'
_pub_ext_dic_[_geo_] = {}
_pub_ext_dic_[_geo_][_maya_] = 'abc'
_pub_ext_dic_[_geo_][_blender_] = 'abc'
_pub_ext_dic_[_rig_] = {}
_pub_ext_dic_[_rig_][_maya_] = 'ma'
_pub_ext_dic_[_rig_][_blender_] = 'blend'
_pub_ext_dic_[_autorig_] = {}
_pub_ext_dic_[_autorig_][_maya_] = 'ma'
_pub_ext_dic_[_cam_rig_] = {}
_pub_ext_dic_[_cam_rig_][_maya_] = 'ma'
_pub_ext_dic_[_texturing_] = {}
_pub_ext_dic_[_texturing_][_painter_] = 'exr'
_pub_ext_dic_[_texturing_][_designer_] = 'sbsar'
_pub_ext_dic_[_shading_] = {}
_pub_ext_dic_[_shading_][_guerilla_] = 'gnode'
_pub_ext_dic_[_shading_][_maya_] = 'ma'
_pub_ext_dic_[_render_pass_] = {}
_pub_ext_dic_[_render_pass_][_guerilla_] = 'gnode'
_pub_ext_dic_[_render_graph_] = {}
_pub_ext_dic_[_render_graph_][_guerilla_] = 'gnode'
_pub_ext_dic_[_light_rig_] = {}
_pub_ext_dic_[_light_rig_][_maya_] = 'ma'
_pub_ext_dic_[_light_rig_][_guerilla_] = 'gnode'
_pub_ext_dic_[_hair_] = {}
_pub_ext_dic_[_hair_][_maya_] = 'ma'
_pub_ext_dic_[_hair_][_maya_yeti_] = 'ma'
_pub_ext_dic_[_concept_] = {}
_pub_ext_dic_[_concept_][_photoshop_] = 'png'
_pub_ext_dic_[_layout_] = {}
_pub_ext_dic_[_layout_][_maya_] = 'abc'
_pub_ext_dic_[_animation_] = {}
_pub_ext_dic_[_animation_][_maya_] = 'abc'
_pub_ext_dic_[_lighting_] = {}
_pub_ext_dic_[_lighting_][_maya_] = 'exr'
_pub_ext_dic_[_lighting_][_guerilla_] = 'exr'
_pub_ext_dic_[_cfx_] = {}
_pub_ext_dic_[_cfx_][_maya_] = 'fur'
_pub_ext_dic_[_cfx_][_maya_yeti_] = 'fur'
_pub_ext_dic_[_fx_] = {}
_pub_ext_dic_[_fx_][_maya_] = 'abc'
_pub_ext_dic_[_fx_][_houdini_] = 'hipnc'
_pub_ext_dic_[_fx_setup_] = {}
_pub_ext_dic_[_fx_setup_][_houdini_] = 'hipnc'
_pub_ext_dic_[_compositing_] = {}
_pub_ext_dic_[_compositing_][_nuke_] = 'exr'
_pub_ext_dic_[_camera_] = {}
_pub_ext_dic_[_camera_][_maya_] = 'abc'
_pub_ext_dic_[_cyclo_] = {}
_pub_ext_dic_[_cyclo_][_maya_] = 'abc'
_pub_ext_dic_[_cyclo_][_guerilla_] = 'gproject'
_pub_ext_dic_[_material_] = {}
_pub_ext_dic_[_material_][_designer_] = 'sbsar'
_pub_ext_dic_[_material_][_photoshop_] = 'png'
_pub_ext_dic_[_painter_template_] = {}
_pub_ext_dic_[_painter_template_][_painter_] = 'spt'
	
_extension_key_ = 'extension'

# Publish extensions lists dictionary
_pub_ext_list_dic_ = {}
_pub_ext_list_dic_[_design_] = {}
_pub_ext_list_dic_[_design_][_photoshop_] = ['png']
_pub_ext_list_dic_[_geo_] = {}
_pub_ext_list_dic_[_geo_][_maya_] = ['abc', 'ma']
_pub_ext_list_dic_[_geo_][_blender_] = ['abc', 'blend']
_pub_ext_list_dic_[_rig_] = {}
_pub_ext_list_dic_[_rig_][_maya_] = ['ma']
_pub_ext_list_dic_[_rig_][_blender_] = ['blend']
_pub_ext_list_dic_[_hair_] = {}
_pub_ext_list_dic_[_hair_][_maya_] = ['ma']
_pub_ext_list_dic_[_hair_][_maya_yeti_] = ['ma']
_pub_ext_list_dic_[_texturing_] = {}
_pub_ext_list_dic_[_texturing_][_painter_] = ['exr', 'png', 'tiff']
_pub_ext_list_dic_[_texturing_][_designer_] = ['sbsar']
_pub_ext_list_dic_[_shading_] = {}
_pub_ext_list_dic_[_shading_][_guerilla_] = ['gnode']
_pub_ext_list_dic_[_shading_][_maya_] = ['ma']

_pub_ext_list_dic_[_autorig_] = {}
_pub_ext_list_dic_[_autorig_][_maya_] = ['ma']
_pub_ext_list_dic_[_cam_rig_] = {}
_pub_ext_list_dic_[_cam_rig_][_maya_] = ['ma']
_pub_ext_list_dic_[_render_pass_] = {}
_pub_ext_list_dic_[_render_pass_][_guerilla_] = ['gnode']
_pub_ext_list_dic_[_render_graph_] = {}
_pub_ext_list_dic_[_render_graph_][_guerilla_] = ['gnode']
_pub_ext_list_dic_[_light_rig_] = {}
_pub_ext_list_dic_[_light_rig_][_maya_] = ['ma']
_pub_ext_list_dic_[_light_rig_][_guerilla_] = ['gnode']
_pub_ext_list_dic_[_fx_setup_] = {}
_pub_ext_list_dic_[_fx_setup_][_houdini_] = ['hipnc', 'vdb', 'abc']
_pub_ext_list_dic_[_cyclo_] = {}
_pub_ext_list_dic_[_cyclo_][_maya_] = ['abc', 'ma']
_pub_ext_list_dic_[_cyclo_][_guerilla_] = ['gproject']
_pub_ext_list_dic_[_material_] = {}
_pub_ext_list_dic_[_material_][_designer_] = ['sbsar', 'png', 'exr', 'tiff']
_pub_ext_list_dic_[_material_][_photoshop_] = ['png']
_pub_ext_list_dic_[_painter_template_] = {}
_pub_ext_list_dic_[_painter_template_][_painter_] = ['spt']

_pub_ext_list_dic_[_concept_] = {}
_pub_ext_list_dic_[_concept_][_photoshop_] = ['png']
_pub_ext_list_dic_[_layout_] = {}
_pub_ext_list_dic_[_layout_][_maya_] = ['abc', 'ma']
_pub_ext_list_dic_[_animation_] = {}
_pub_ext_list_dic_[_animation_][_maya_] = ['abc', 'ma']
_pub_ext_list_dic_[_lighting_] = {}
_pub_ext_list_dic_[_lighting_][_maya_] = ['exr']
_pub_ext_list_dic_[_lighting_][_guerilla_] = ['exr']
_pub_ext_list_dic_[_cfx_] = {}
_pub_ext_list_dic_[_cfx_][_maya_] = ['fur', 'abc']
_pub_ext_list_dic_[_cfx_][_maya_yeti_] = ['fur', 'abc']
_pub_ext_list_dic_[_fx_] = {}
_pub_ext_list_dic_[_fx_][_maya_] = ['abc', 'ma']
_pub_ext_list_dic_[_fx_][_houdini_] = ['hipnc', 'vdb', 'abc']
_pub_ext_list_dic_[_compositing_] = {}
_pub_ext_list_dic_[_compositing_][_nuke_] = ['exr']
_pub_ext_list_dic_[_camera_] = {}
_pub_ext_list_dic_[_camera_][_maya_] = ['abc', 'ma']



_custom_ext_dic_key_ = "custom_ext_dic"

# Publish extension dictionary

_project_extension_dic_key_ = 'extensions_dic'

_workflow_ext_dic_custom_ = dict()

_workflow_ext_dic_custom_[_rig_] = dict()
_workflow_ext_dic_custom_[_rig_][_maya_] = 'ma'
_workflow_ext_dic_custom_[_rig_][_blender_] = 'blend'
_workflow_ext_dic_custom_[_rig_][_houdini_] = 'hipnc'
_workflow_ext_dic_custom_[_rig_][_3dsmax_] = 'max'

_workflow_ext_dic_custom_[_hair_] = dict()
_workflow_ext_dic_custom_[_hair_][_maya_yeti_] = 'ma'
_workflow_ext_dic_custom_[_hair_][_maya_] = 'ma'
_workflow_ext_dic_custom_[_hair_][_blender_] = 'blend'
_workflow_ext_dic_custom_[_hair_][_houdini_] = 'hipnc'
_workflow_ext_dic_custom_[_hair_][_3dsmax_] = 'max'

_workflow_ext_dic_custom_[_shading_] = dict()
_workflow_ext_dic_custom_[_shading_][_guerilla_] = 'gnode'
_workflow_ext_dic_custom_[_shading_][_maya_] = 'ma'
_workflow_ext_dic_custom_[_shading_][_blender_] = 'blend'
_workflow_ext_dic_custom_[_shading_][_houdini_] = 'hipnc'
_workflow_ext_dic_custom_[_shading_][_3dsmax_] = 'max'

_workflow_ext_dic_ = dict()
_workflow_ext_dic_[_design_] = 'png'
_workflow_ext_dic_[_geo_] = 'abc'

_workflow_ext_dic_[_autorig_] = 'ma'
_workflow_ext_dic_[_cam_rig_] = 'ma'
_workflow_ext_dic_[_texturing_] = 'exr'

_workflow_ext_dic_[_render_pass_] = 'gnode'
_workflow_ext_dic_[_render_graph_] = 'gnode'
_workflow_ext_dic_[_light_rig_] = 'gnode'
_workflow_ext_dic_[_concept_] = 'png'
_workflow_ext_dic_[_layout_] = 'abc'
_workflow_ext_dic_[_animation_] = 'abc'
_workflow_ext_dic_[_lighting_] = 'exr'
_workflow_ext_dic_[_cfx_] = 'fur'
_workflow_ext_dic_[_fx_] = 'abc'
_workflow_ext_dic_[_compositing_] = 'exr'
_workflow_ext_dic_[_cyclo_] = 'gproject'

_textures_ext_list_ = ['exr', 'png', 'tiff']


# Softs icons library
_photoshop_icon_ = _icon_path_ + 'photoshop.png'
_krita_icon_ = _icon_path_ + 'krita.png'
_maya_icon_ = _icon_path_ + 'maya.png'
_maya_py_icon_ = _icon_path_ + 'maya.png'
_maya_yeti_icon_ = _icon_path_ + 'maya_yeti.png'
_painter_icon_ = _icon_path_ + 'painter.png'
_blender_icon_ = _icon_path_ + 'blender.png'
_3dsmax_icon_ = _icon_path_ + '3dsmax.png'
_designer_icon_ = _icon_path_ + 'designer.png'
_zbrush_icon_ = _icon_path_ + 'zbrush.png'
_mari_icon_ = _icon_path_ + 'mari.png'
_marvelous_icon_ = _icon_path_ + 'marvelous.png'
_guerilla_icon_ = _icon_path_ + 'guerilla.png'
_houdini_icon_ = _icon_path_ + 'houdini.png'
_nuke_icon_ = _icon_path_ + 'nuke.png'
_rumba_icon_ = _icon_path_ + 'rumba.png'
_resolve_icon_ = _icon_path_ + 'resolve.png'
_reaper_icon_ = _icon_path_ + 'reaper.png'
_folder_icon_ = _icon_path_ + 'folder.png'

# Soft icons dic
_soft_icons_dic_ = {}
_soft_icons_dic_[_maya_]=_maya_icon_
_soft_icons_dic_[_mayapy_]=_maya_icon_
_soft_icons_dic_[_maya_yeti_]=_maya_yeti_icon_
_soft_icons_dic_[_photoshop_]=_photoshop_icon_
_soft_icons_dic_[_krita_]=_krita_icon_
_soft_icons_dic_[_painter_]=_painter_icon_
_soft_icons_dic_[_blender_]=_blender_icon_
_soft_icons_dic_[_3dsmax_]=_3dsmax_icon_
_soft_icons_dic_[_designer_]=_designer_icon_
_soft_icons_dic_[_zbrush_]=_zbrush_icon_
_soft_icons_dic_[_marvelous_]=_marvelous_icon_
_soft_icons_dic_[_guerilla_]=_guerilla_icon_
_soft_icons_dic_[_houdini_]=_houdini_icon_
_soft_icons_dic_[_hython_]=_houdini_icon_
_soft_icons_dic_[_mari_]=_mari_icon_
_soft_icons_dic_[_nuke_]=_nuke_icon_
_soft_icons_dic_[_rumba_]=_rumba_icon_
_soft_icons_dic_[_resolve_]=_resolve_icon_
_soft_icons_dic_[_reaper_]=_reaper_icon_
_soft_icons_dic_[_folder_]=_folder_icon_

_maya_icon_path_ = 'XBMLANGPATH'
_maya_scripts_path_ = 'MAYA_SCRIPT_PATH'
_mel_startup_ = 'maya_wizard/startup.mel'

_guerilla_conf_file_ = 'guerilla.conf'
_guerilla_custom_python_ = 'GUERILLA_PYTHON_LIBRARY'
_guerilla_node_type_ = 'SceneGraphNode'

_blender_startup_ = 'blender_wizard/startup.py'
_houdini_startup_ = 'houdini_wizard/startup.py'

_script_software_env_dic_=dict()
_script_software_env_dic_[_maya_]='PYTHONPATH'
_script_software_env_dic_[_mayapy_]='PYTHONPATH'
_script_software_env_dic_[_maya_yeti_]='PYTHONPATH'
_script_software_env_dic_[_photoshop_]='PYTHONPATH'
_script_software_env_dic_[_krita_]='PYTHONPATH'
_script_software_env_dic_[_nuke_]='NUKE_PATH'
_script_software_env_dic_[_houdini_]='PYTHONPATH'
_script_software_env_dic_[_hython_]='PYTHONPATH'
_script_software_env_dic_[_zbrush_]='PYTHONPATH'
_script_software_env_dic_[_guerilla_]='GUERILLA_CONF'
_script_software_env_dic_[_painter_]='SUBSTANCE_PAINTER_PLUGINS_PATH'
_script_software_env_dic_[_designer_]='SBS_DESIGNER_PYTHON_PATH'
_script_software_env_dic_[_blender_]='PYTHONPATH'
_script_software_env_dic_[_3dsmax_]='PYTHONPATH'
_script_software_env_dic_[_resolve_]='PYTHONPATH'
_script_software_env_dic_[_reaper_]='PYTHONPATH'
_script_software_env_dic_[_folder_]='null'

# Extensions dictionary
_extension_dic_ = {}
_extension_dic_[_maya_]='ma'
_extension_dic_[_mayapy_]='ma'
_extension_dic_[_maya_yeti_]='ma'
_extension_dic_[_photoshop_]='psd'
_extension_dic_[_krita_]='kra'
_extension_dic_[_painter_]='spp'
_extension_dic_[_designer_]='sbs'
_extension_dic_[_zbrush_]='zpr'
_extension_dic_[_marvelous_]='hw'
_extension_dic_[_guerilla_]='gproject'
_extension_dic_[_houdini_]='hipnc'
_extension_dic_[_hython_]='hipnc'
_extension_dic_[_mari_]='Mari'
_extension_dic_[_nuke_]='nk'
_extension_dic_[_blender_]='blend'
_extension_dic_[_3dsmax_]='max'
_extension_dic_[_resolve_]='drp'
_extension_dic_[_reaper_]='rpp'
_extension_dic_[_folder_]='null'

# Init file for each software
_init_file_='ressources/init_files/init_file'
_init_file__dic_=dict()
_init_file__dic_[_maya_]='{}.{}'.format(_init_file_,_extension_dic_[_maya_])
_init_file__dic_[_mayapy_]='{}.{}'.format(_init_file_,_extension_dic_[_mayapy_])
_init_file__dic_[_maya_yeti_]='{}.{}'.format(_init_file_,_extension_dic_[_maya_yeti_])
_init_file__dic_[_photoshop_]='{}.{}'.format(_init_file_,_extension_dic_[_photoshop_])
_init_file__dic_[_krita_]='{}.{}'.format(_init_file_,_extension_dic_[_krita_])
_init_file__dic_[_painter_]='{}.{}'.format(_init_file_,_extension_dic_[_painter_])
_init_file__dic_[_blender_]='{}.{}'.format(_init_file_,_extension_dic_[_blender_])
_init_file__dic_[_3dsmax_]='{}.{}'.format(_init_file_,_extension_dic_[_3dsmax_])
_init_file__dic_[_designer_]='{}.{}'.format(_init_file_,_extension_dic_[_designer_])
_init_file__dic_[_zbrush_]='{}.{}'.format(_init_file_,_extension_dic_[_zbrush_])
_init_file__dic_[_marvelous_]='{}.{}'.format(_init_file_,_extension_dic_[_marvelous_])
_init_file__dic_[_guerilla_]='{}.{}'.format(_init_file_,_extension_dic_[_guerilla_])
_init_file__dic_[_houdini_]='{}.{}'.format(_init_file_,_extension_dic_[_houdini_])
_init_file__dic_[_hython_]='{}.{}'.format(_init_file_,_extension_dic_[_houdini_])
_init_file__dic_[_mari_]='{}.{}'.format(_init_file_,_extension_dic_[_mari_])
_init_file__dic_[_nuke_]='{}.{}'.format(_init_file_,_extension_dic_[_nuke_])
_init_file__dic_[_resolve_]='null'
_init_file__dic_[_reaper_]='{}.{}'.format(_init_file_,_extension_dic_[_reaper_])
_init_file__dic_[_folder_]='null'
# Stage softs dic
_stage_softs_dic_ = {}
_stage_softs_dic_[_design_]=[_photoshop_, _krita_]
_stage_softs_dic_[_concept_]=[_photoshop_, _krita_]
_stage_softs_dic_[_geo_]=[_maya_, _zbrush_, _marvelous_, _blender_, _houdini_, _3dsmax_]
_stage_softs_dic_[_rig_]=[_maya_, _blender_, _houdini_, _3dsmax_]
_stage_softs_dic_[_texturing_]=[_painter_, _designer_, _mari_, _blender_, _houdini_, _3dsmax_]
_stage_softs_dic_[_shading_]=[_guerilla_, _maya_, _blender_, _houdini_, _3dsmax_]
_stage_softs_dic_[_hair_]=[_maya_, _blender_, _houdini_, _3dsmax_, _maya_yeti_]
_stage_softs_dic_[_layout_]=[_maya_, _blender_, _houdini_, _3dsmax_]
_stage_softs_dic_[_animation_]=[_maya_, _rumba_, _blender_, _houdini_, _3dsmax_]
_stage_softs_dic_[_lighting_]=[_guerilla_, _maya_, _maya_yeti_, _blender_, _houdini_, _3dsmax_]
_stage_softs_dic_[_cfx_]=[_maya_, _blender_, _houdini_, _3dsmax_, _maya_yeti_]
_stage_softs_dic_[_fx_]=[_houdini_, _maya_, _blender_, _3dsmax_]
_stage_softs_dic_[_fx_setup_]=[_houdini_, _maya_, _blender_, _3dsmax_]
_stage_softs_dic_[_compositing_]=[_nuke_, _blender_]
_stage_softs_dic_[_camera_]=[_maya_, _rumba_, _blender_, _houdini_, _3dsmax_]
_stage_softs_dic_[_autorig_]=[_maya_, _blender_]
_stage_softs_dic_[_cam_rig_] =[_maya_, _blender_]
_stage_softs_dic_[_cyclo_] = [_maya_, _blender_, _guerilla_]
_stage_softs_dic_[_gizmo_] = [_nuke_]
_stage_softs_dic_[_light_rig_] = [_maya_, _blender_, _guerilla_]
_stage_softs_dic_[_lut_] = [_nuke_, _guerilla_]
_stage_softs_dic_[_render_graph_] = [_guerilla_]
_stage_softs_dic_[_render_pass_] = [_guerilla_]
_stage_softs_dic_[_scripts_] = [_folder_]
_stage_softs_dic_[_sons_] = [_folder_]
_stage_softs_dic_[_stockshot_] = [_folder_]
_stage_softs_dic_[_video_] = [_folder_]
_stage_softs_dic_[_video_edit_] = [_resolve_]
_stage_softs_dic_[_sound_edit_] = [_reaper_]
_stage_softs_dic_[_material_] = [_designer_, _photoshop_]
_stage_softs_dic_[_painter_template_] = [_painter_]


# Game icons library
_life_progress_0_ = _icon_path_ + 'life0.png'
_life_progress_1_ = _icon_path_ + 'life1.png'
_life_progress_2_ = _icon_path_ + 'life2.png'
_life_progress_3_ = _icon_path_ + 'life3.png'
_life_progress_4_ = _icon_path_ + 'life4.png'
_lvl_progress_0_ = _icon_path_ + 'lvl0.png'
_lvl_progress_1_ = _icon_path_ + 'lvl1.png'
_lvl_progress_2_ = _icon_path_ + 'lvl2.png'
_lvl_progress_3_ = _icon_path_ + 'lvl3.png'
_lvl_progress_4_ = _icon_path_ + 'lvl4.png'
_heart_icon_ = _icon_path_ + 'heart.png'
_xp_icon_ = _icon_path_ + 'xp.png'
_gold_icon_ = _icon_path_ + 'gold.png'
_lvl_icon_ = _icon_path_ + 'l.png'
_cup_icon_ = _icon_path_ + 'cup.png'
_stuff_icon_ = _icon_path_ + 'stuff.png'
_shop_icon_ = _icon_path_ + 'shop.png'
_buy_icon_ = _icon_path_ + 'buy.png'

# Jokes library
_previous_icon_ = _icon_path_ + 'previous.png'
_next_icon_ = _icon_path_ + 'next.png'
_star_empty_icon_ = _icon_path_ + 'star_empty.png'
_star_full_icon_ = _icon_path_ + 'star_full.png'
_star_hover_icon_ = _icon_path_ + 'star_hover.png'
_joke_data_ = 'joke'
_note_key_ = 'note'
_notes_list_key_ = 'note_list'
_users_jury_list_key_ = 'jury_list'
_high_quote_icon_ = _icon_path_ + 'high_quote.png'
_low_quote_icon_ = _icon_path_ + 'low_quote.png'
_police_icon_ = _icon_path_ + 'policeman.png'

_star1_ = 'star1'
_star2_ = 'star2'
_star3_ = 'star3'
_star4_ = 'star4'
_star5_ = 'star5'

_stars_states_dic_ = {}
_stars_states_dic_[0] = []
_stars_states_dic_[1] = [_star1_]
_stars_states_dic_[2] = [_star1_, _star2_]
_stars_states_dic_[3] = [_star1_, _star2_, _star3_]
_stars_states_dic_[4] = [_star1_, _star2_, _star3_, _star4_]
_stars_states_dic_[5] = [_star1_, _star2_, _star3_, _star4_, _star5_]


# Game keys library
_user_avatar_ = 'avatar'
_user_gold_ = 'gold'
_user_level_ = 'level'
_user_xp_ = 'xp'
_user_life_ = 'life'

# Tickets library
_all_tickets_ = 'all_tickets'
_user_tickets_ = 'user_tickets'
_adress_tickets_ = 'adress_tickets'
_assets_tickets_ = 'assets_tickets'
_ticket_state_ = 'state'
_ticket_open_ = 'opened'
_ticket_close_ = 'closed'
_close_date_ = 'close_date'
_ticket_adress_ = 'adress'
_ticket_comment_ = 'comment'
_ticket_close_user_ = 'close_user'

# Wall library
_message_key_ = 'message'
_file_key_ = 'file'
_wall_id_key_ = 'id'
_wall_creation_event_ = 'creation'
_wall_publish_event_ = 'publish'
_wall_xp_event_ = 'xp'
_wall_message_event_ = 'message'
_wall_remove_event_ = 'remove'
_wall_playblast_event_ = 'playblast'
_wall_ticket_event_ = 'ticket'
_wall_close_ticket_event_ = 'close_ticket'
_wall_time_key_ = 'date'
_wall_time_id_key_ = 'time_id'
_asset_key_ = 'asset'
_classic_message_ = 'classic_message_'
_file_message_ = 'file_message_'
_message_id_key_ = 'id'

# Lan keys library
_server_ip_ = 'host_ip'

_create_event_icon_ =  _icon_path_ + 'create_event.png'
_remove_event_icon_ =  _icon_path_ + 'remove_event.png'
_publish_event_icon_ =  _icon_path_ + 'publish_event.png'
_xp_event_icon_ =  _icon_path_ + 'level_medal.png'
_event_icon_dic_ = dict()
_event_icon_dic_[_wall_creation_event_] = _create_event_icon_
_event_icon_dic_[_wall_remove_event_] = _remove_event_icon_
_event_icon_dic_[_wall_publish_event_] = _publish_event_icon_
_event_icon_dic_[_wall_playblast_event_] = _publish_event_icon_
_event_icon_dic_[_wall_xp_event_] = _xp_event_icon_
_event_icon_dic_[_wall_ticket_event_] = _xp_event_icon_
_event_icon_dic_[_wall_close_ticket_event_] = _xp_event_icon_

_event_color_dic_ = dict()
_event_color_dic_[_wall_creation_event_] = '#93d1ff'
_event_color_dic_[_wall_remove_event_] = '#ff8383'
_event_color_dic_[_wall_publish_event_] = '#a4ff83'
_event_color_dic_[_wall_xp_event_] = '#faff89'
_event_color_dic_[_wall_playblast_event_] = '#f6ff67'
_event_color_dic_[_wall_ticket_event_] = '#8693FF'
_event_color_dic_[_wall_close_ticket_event_] = '#8693FF'

# Prefs files
_site_ = 'Data/site.wd'
_site_path_ = 'Data/_/'
_site_db_ = 'Data/site.db'
_stats_ = 'Data/'
_jokes_ = 'Data/jokes.wd'
_site_var_ = 'SITE_FILE'
_jokes_var_ = 'JOKES_FILE'
_stats_var_ = 'STATS_FILE'
_asset_var_ = 'ASSET_VAR'
_softwares_scripts_path_ = 'softwares_env/softwares/'
_project_ = 'project.wd'
_project_db_ = 'project.db'
_tree_ = 'tree.wd'
_production_ = 'production.wd'
_user_path_ = '{}/Documents/wizard/'.format(os.getenv("USERPROFILE"))
_lock_file_ = _user_path_ + '.lock'
_user_ = _user_path_ + 'user.wd'
_user_db_ = _user_path_ + 'user.db'
_user_scripts_file_ = _user_path_ + 'scripts.yaml'
_project_script_file_ = 'scripts.yaml'
_user_custom_scripts_path_ = _user_path_ + 'scripts/'
_session_file_ = _user_custom_scripts_path_ + 'session.py'
_user_custom_icons_ = _user_path_ + 'custom_icons'
_wall_ = 'wall.log'
_tickets_ = 'tickets.wd'
_chat_ = 'chat.log'
_stylesheet_template_ = ressources_path("ressources/stylesheet/stylesheet_template.st")
_software_path_key_ = "software_path"
_software_additionnal_script_key_ = "software_additionnal_script_path"
_software_additionnal_env_key_ = "software_additionnal_env_paths"

# Scene keys library
_scene_current_asset_ = "scene_current_asset"

# Project settings keys library
_project_name_key_ = 'project_name'
_frame_rate_key_ = 'frame_rate'
_yeti_as_abc_key_ = 'yeti_as_abc'
_format_key_ = 'format'
_color_management_key_ = 'color_management'
_sampling_rate_key_ = 'sampling_rate'

# Main keys library
_creation_date_key_ = 'creation_date'
_creation_user_key_ = 'creation_user'
_creation_id_key_ = 'creation_id'
_asset_events_key_ = 'events'
_events_ = 'events'
_locks_ = 'locks'
_comment_key_ = 'comment'
_softwares_list_key_ = 'softwares_list'
_variants_list_key_ = 'variants_list'
_default_software_key_ = 'default_software'
_variant_references_list_ = 'references_list'
_default_variant_key_ = 'default_variant'
_versions_list_key_ = 'versions_list'
_versions_list_ = 'versions_list_soft'
_export_assets_list_key_ = 'export_assets_list'
_export_asset_key_ = 'export_asset'
_default_export_asset_key_ = 'default_export_asset'
_frame_range_key_ = 'frame_range'
_preroll_key_ = 'preroll'
_postroll_key_ = 'postroll'
_lock_key_ = 'lock'
_run_key_ = 'run'
_software_key_ = 'software'
_from_asset_key_ = "from_asset"

# User pref dic variables library
_user_name_key_ = 'user_name'
_asset_context_ = 'asset'
_tab_context_ = 'current_tab'
_popup_prefs_key_ = 'popup'
_user_screen_index_key_ = 'screen_index'
_user_theme_key_ = 'theme'
_user_chat_theme_key_ = 'chat_color'
_windows_quit_key_ = 'quit_on_close'
_show_updates_ = 'show_updates'
_show_new_version_ = 'show_new_version'
_show_error_handler_ = 'show_error_handler'
_local_project_path_ = 'local_project_path'
_popup_enable_key_ = 'enable'
_popup_sound_key_ = 'sound'
_popup_sound_file_key_ = 'sound_file'
_popup_duration_key_ = 'duration'
_popup_creation_key_ = 'creation'
_popup_publish_key_ = 'publish'
_popup_playblast_key_ = 'playblast'
_popup_save_key_ = 'save'
_popup_message_key_ = 'message'
_popup_position_key_ = 'position'
_user_email_key_ = 'user_email'
_promotion_key_ = 'promotion'
_current_project_key_ = 'current_project'
_project_path_key_ = 'project_path'

# Site settings library
_password_key_ = 'password'
_admin_key_ = 'administrator'
_full_name_key_ = 'full_name'
_users_list_key_ = 'users'
_projects_list_key_ = 'projects'

# Asset settings library
_category_prefs_ = 'category.wd'
_name_prefs_ = 'asset.wd'
_stage_prefs_ = 'stage.wd'
_variant_prefs_ = 'variant.wd'
_export_prefs_ = 'export.wd'
_playblast_prefs_ = 'playblast.wd'
_export_root_prefs_ = 'export_root.wd'
_software_prefs_ = 'software.wd'
_image_name_ = 'capture.png'

# Logging ile
_logging_path_ = '../Data/log_files/'
_log_path_ = _user_path_ + 'log/'
_stdout_file_ = _log_path_+'stdout.log'
_logging_ = _log_path_ + 'main.log'
_server_logging_ = _log_path_ + 'server.log'

# QTree sub data library
_add_item_ = 'add_item'
_add_shot_ = 'add_shot'
_asset_item_ = 'asset_item'
_shot_ietm_ = 'shot_item'
_new_item_label_ = 'new'
_new_shot_label_ = 'shot'

# Colors library
_white_color_hexa_ = "#FFFFFF"
_add_item_color_ = "#808080"
_main_color_ = 'rgb(255, 178, 133);'

# Display missing text
_missing_user_ = 'No user found'
_missing_project_ = 'No project found'

# Chat conform library
_message_layout_ = "message_main_layout"
_message_vertical_layout_ = "message_main_vertical_layout"
_message_info_label_left_ = "message_info_label_left"
_message_info_label_right_ = "message_info_label_right"
_message_frame_left_ = "message_frame_left"
_message_frame_right_ = "message_frame_right"
_message_label_ = "message_content"

# Password library
_alphabet_ = ['a', 'b','c','d',
'e','f','g','h','i','j',
'k','l','m','n','o','p',
'q','r','s','t','u','v',
'w','x','y','z','A','B',
'C','D','E','F','G','H',
'I','J','K','L','M','N',
'O','P','Q','R','T','U',
'V','W','X','Y','Z','1',
'2','3','4','5','6','7',
'8','9','0','']

# Data files
_data_path_ = 'Data/'
_log_citical_file_ = _data_path_ + 'log_files/critical_error.log'

_log_file_ = _log_path_ + 'main.log'
_lock_file_ = _log_path_ + '.lock'

# Asset default library
_main_variant_ = 'main'

# Stylesheet color dic

_dark_theme_key_ = 'Modern'
_white_theme_key_ = 'White'
_cream_theme_key_ = 'Cream'
_chocolate_theme_key_ = 'Chocolate'
_blue_theme_key_ = 'Blue'
_geek_theme_key_ = 'Geek'

_text_color_key_ = '_text_color_'
_bg_color_key_ = '_background_color_'
_frame_color_key_ = '_middle_level_widget_color_'
_top_color_key_ = '_top_level_widget_color_'
_low_color_key_ = '_low_level_widget_color_'
_low_2_color_key_ = '_very_lower_level_widget_color_'
_tree_h_color_key_ = '_tree_hover_item_color_'
_tree_p_color_key_ = '_tree_press_item_color_'
_widget_h_color_key_ = '_hover_widget_color_'
_widget_p_color_key_ = '_pressed_widget_color_'

#	themes dics
dark_theme_dic = dict()
dark_theme_dic[_text_color_key_] = '200,200,203'
dark_theme_dic[_bg_color_key_] = '20,20,27'
dark_theme_dic[_frame_color_key_] = '36,36,43'
dark_theme_dic[_top_color_key_] = '44,44,51'
dark_theme_dic[_low_color_key_] = '24,24,30'
dark_theme_dic[_low_2_color_key_] = '14,14,19'
dark_theme_dic[_tree_h_color_key_] = '26,26,42'
dark_theme_dic[_tree_p_color_key_] = '36,36,43'
dark_theme_dic[_widget_h_color_key_] = '50,50,57'
dark_theme_dic[_widget_p_color_key_] = '16,16,23'

geek_theme_dic = dict()
geek_theme_dic[_text_color_key_] = '20,255,20'
geek_theme_dic[_bg_color_key_] = '6,6,6'
geek_theme_dic[_frame_color_key_] = '26,26,26'
geek_theme_dic[_top_color_key_] = '46,46,46'
geek_theme_dic[_low_color_key_] = '10,10,10'
geek_theme_dic[_low_2_color_key_] = '0,0,0'
geek_theme_dic[_tree_h_color_key_] = '16,16,16'
geek_theme_dic[_tree_p_color_key_] = '26,26,26'
geek_theme_dic[_widget_h_color_key_] = '76,76,76'
geek_theme_dic[_widget_p_color_key_] = '6,6,6'

blue_theme_dic = dict()
blue_theme_dic[_text_color_key_] = '255,255,255'
blue_theme_dic[_bg_color_key_] = '35,48,66'
blue_theme_dic[_frame_color_key_] = '45,60,83'
blue_theme_dic[_top_color_key_] = '66,88,120'
blue_theme_dic[_low_color_key_] = '66,88,120'
blue_theme_dic[_low_2_color_key_] = '35,48,66'
blue_theme_dic[_tree_h_color_key_] = '86,108,140'
blue_theme_dic[_tree_p_color_key_] = '66,88,120'
blue_theme_dic[_widget_h_color_key_] = '142,199,237'
blue_theme_dic[_widget_p_color_key_] = '46,68,100'

cream_theme_dic = dict()
cream_theme_dic[_text_color_key_] = '0,0,0'
cream_theme_dic[_bg_color_key_] = '189,169,169'
cream_theme_dic[_frame_color_key_] = '209,189,189'
cream_theme_dic[_top_color_key_] = '249,229,229'
cream_theme_dic[_low_color_key_] = '249,229,229'
cream_theme_dic[_low_2_color_key_] = '239,219,219'
cream_theme_dic[_tree_h_color_key_] = '255,239,239'
cream_theme_dic[_tree_p_color_key_] = '209,189,189'
cream_theme_dic[_widget_h_color_key_] = '245,235,235'
cream_theme_dic[_widget_p_color_key_] = '159,139,139'

white_theme_dic = dict()
white_theme_dic[_text_color_key_] = '0,0,0'
white_theme_dic[_bg_color_key_] = '200,200,200'
white_theme_dic[_frame_color_key_] = '189,189,189'
white_theme_dic[_top_color_key_] = '229,229,229'
white_theme_dic[_low_color_key_] = '229,229,229'
white_theme_dic[_low_2_color_key_] = '219,219,219'
white_theme_dic[_tree_h_color_key_] = '199,199,199'
white_theme_dic[_tree_p_color_key_] = '189,189,189'
white_theme_dic[_widget_h_color_key_] = '245,245,245'
white_theme_dic[_widget_p_color_key_] = '139,139,139'

chocolate_theme_dic = dict()
chocolate_theme_dic[_text_color_key_] = '255,255,255'
chocolate_theme_dic[_bg_color_key_] = '36,26,26'
chocolate_theme_dic[_frame_color_key_] = '56,46,46'
chocolate_theme_dic[_top_color_key_] = '76,66,66'
chocolate_theme_dic[_low_color_key_] = '40,30,30'
chocolate_theme_dic[_low_2_color_key_] = '30,20,20'
chocolate_theme_dic[_tree_h_color_key_] = '46,36,36'
chocolate_theme_dic[_tree_p_color_key_] = '56,46,46'
chocolate_theme_dic[_widget_h_color_key_] = '106,96,96'
chocolate_theme_dic[_widget_p_color_key_] = '26,16,16'

_themes_dic_ = dict()
_themes_dic_[_dark_theme_key_] = dark_theme_dic
_themes_dic_[_white_theme_key_] = white_theme_dic
_themes_dic_[_cream_theme_key_] = cream_theme_dic
_themes_dic_[_chocolate_theme_key_] = chocolate_theme_dic
_themes_dic_[_blue_theme_key_] = blue_theme_dic
_themes_dic_[_geek_theme_key_] = geek_theme_dic

# Popup positions library
_bt_r_key_ = 'Bottom-Right'
_bt_l_key_ = 'Bottom-Left'
_tp_l_key_ = 'Top-Left'
_tp_r_key_ = 'Top-Right'


_purple_color_ = 'Purple'
_blue_color_ = 'Blue'

_message_color_replace_key_ = '_message_gradient_'
_message_colors_dic_ = dict()
_message_colors_dic_[_purple_color_] = 'qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(130, 109, 190, 255), stop:1 rgba(148, 51, 180, 255))'
_message_colors_dic_[_blue_color_] = 'qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(79, 190, 183, 255), stop:1 rgba(17, 158, 180, 255))'

_pop_position_dic_ = [_bt_r_key_,
						_bt_l_key_,
						_tp_l_key_,
						_tp_r_key_]

# Nodes variables

_geo_node_icon_ = _icon_path_ + 'geo_node_main.png'
_rig_node_icon_ = _icon_path_ + 'rig_node_main.png'
_hair_node_icon_ = _icon_path_ + 'fur_node_main.png'
_shading_node_icon_ = _icon_path_ + 'shading_node_main.png'
_texturing_node_icon_ = _icon_path_ + 'texturing_node_main.png'
_layout_node_icon_ = _icon_path_ + 'layout_node_main.png'
_anim_node_icon_ = _icon_path_ + 'anim_node_main.png'
_lighting_node_icon_ = _icon_path_ + 'lighting_node_main.png'
_fx_node_icon_ = _icon_path_ + 'fx_node_main.png'
_fx_setup_node_icon_ = _icon_path_ + 'fx_setup_node_main.png'
_cfx_node_icon_ = _icon_path_ + 'fur_sim_node_main.png'
_compo_node_icon_ = _icon_path_ + 'compo_node_main.png'
_camera_node_icon_ = _icon_path_ + 'camera_node_main.png'
_design_node_icon_ = _icon_path_ + 'design_node_main.png'
_concept_node_icon_ = _icon_path_ + 'concept_node_main.png'
_missing_node_icon_ = _icon_path_ + 'missing_node_main.png'
_auto_rig_node_icon_ = _icon_path_ + 'auto_rig_node_main.png'
_material_node_icon_ = _icon_path_ + 'material_node_main.png'
_painter_template_node_icon_ = _icon_path_ + 'painter_template_node_main.png'
_cam_rig_node_icon_ = _icon_path_ + 'cam_rig_node_main.png'
_cyclo_node_icon_ = _icon_path_ + 'cyclo_node_main.png'
_gizmo_node_icon_ = _icon_path_ + 'gizmo_node_main.png'
_light_rig_node_icon_ = _icon_path_ + 'light_rig_node_main.png'
_lut_node_icon_ = _icon_path_ + 'lut_node_main.png'
_render_graph_node_icon_ = _icon_path_ + 'render_graph_node_main.png'
_render_pass_node_icon_ = _icon_path_ + 'render_pass_node_main.png'
_script_node_icon_ = _icon_path_ + 'scripts_node_main.png'
_sons_node_icon_ = _icon_path_ + 'sons_node_main.png'
_stockshot_node_icon_ = _icon_path_ + 'stockshot_node_main.png'
_video_node_icon_ = _icon_path_ + 'video_node_main.png'
_video_edit_node_icon_ = _icon_path_ + 'video_edit_node_main.png'
_sound_edit_node_icon_ = _icon_path_ + 'sound_edit_node_main.png'


_nodes_icons_dic_ = {}
_nodes_icons_dic_[_geo_] = _geo_node_icon_
_nodes_icons_dic_[_rig_] = _rig_node_icon_
_nodes_icons_dic_[_hair_] = _hair_node_icon_
_nodes_icons_dic_[_shading_] = _shading_node_icon_
_nodes_icons_dic_[_texturing_] = _texturing_node_icon_
_nodes_icons_dic_[_layout_] = _layout_node_icon_
_nodes_icons_dic_[_animation_] = _anim_node_icon_
_nodes_icons_dic_[_lighting_] = _lighting_node_icon_
_nodes_icons_dic_[_fx_] = _fx_node_icon_
_nodes_icons_dic_[_fx_setup_] = _fx_setup_node_icon_
_nodes_icons_dic_[_cfx_] = _cfx_node_icon_
_nodes_icons_dic_[_compositing_] = _compo_node_icon_
_nodes_icons_dic_[_camera_] = _camera_node_icon_
_nodes_icons_dic_[_design_] = _design_node_icon_
_nodes_icons_dic_[_concept_] = _concept_node_icon_
_nodes_icons_dic_[_autorig_]=_auto_rig_node_icon_
_nodes_icons_dic_[_cam_rig_] =_cam_rig_node_icon_
_nodes_icons_dic_[_cyclo_] = _cyclo_node_icon_
_nodes_icons_dic_[_gizmo_] = _gizmo_node_icon_
_nodes_icons_dic_[_light_rig_] = _light_rig_node_icon_
_nodes_icons_dic_[_lut_] = _lut_node_icon_
_nodes_icons_dic_[_render_graph_] = _render_graph_node_icon_
_nodes_icons_dic_[_render_pass_] = _render_pass_node_icon_
_nodes_icons_dic_[_scripts_] = _script_node_icon_
_nodes_icons_dic_[_sons_] = _sons_node_icon_
_nodes_icons_dic_[_stockshot_] = _stockshot_node_icon_
_nodes_icons_dic_[_video_] = _video_node_icon_
_nodes_icons_dic_[_video_edit_] = _video_edit_node_icon_
_nodes_icons_dic_[_sound_edit_] = _sound_edit_node_icon_
_nodes_icons_dic_[_material_] = _material_node_icon_
_nodes_icons_dic_[_painter_template_] = _painter_template_node_icon_

_python_27_zip_ = 'plugins/Guerilla Render/python27.zip'
_python_27_dll_ = 'plugins/Guerilla Render/python27.dll'
_python_27_DLLs_ = 'plugins/Guerilla Render/DLLs'
_guerilla_python26_zip_ = 'python26.zip'
_guerilla_python27_zip_ = 'python27.zip'
_guerilla_python26_dll_ = 'python26.dll'
_guerilla_python27_dll_ = 'python27.dll'
_guerilla_python26_DLLs_ = 'python'

_substance_plugin_ = 'plugins/Substance Painter/wizard'
_substance_plugin_path_ = '{}/Documents//Allegorithmic/Substance Painter/plugins/wizard'.format(os.getenv("USERPROFILE"))


# Signal keys library
_signal_type_key_ = 'type'
_refresh_signal_ = 'refresh'
_refresh_launcher_signal_ = 'refresh_launcher'
_log_signal_ = 'log'
_log_line_ = 'line'
_focus_signal_ = 'focus'
_save_signal_ = 'save'
_task_value_ = 'value'
_task_signal_ = 'task_signal'
_task_name_signal_ = 'task_name_signal'
_task_name_ = 'task_name'

# Script editor library
_widget_key_ = 'widget'
_name_key_ = 'name'
_index_key_ = 'index'
