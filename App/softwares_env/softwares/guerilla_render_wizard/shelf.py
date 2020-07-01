from guerilla import command

from softwares.guerilla_render_wizard import plugin
from softwares.guerilla_render_wizard import reference_asset
from softwares.guerilla_render_wizard import init_scene
from softwares.guerilla_render_wizard import setup_render

from wizard.asset import main as asset_core
from wizard.vars import defaults
from wizard.tools import log
import os


logger = log.pipe_log()

class shelf():
    class Save(command):
        @staticmethod
        def action(luaObj, window, x, y, suffix):
            plugin.save()

    class import_all(command):
        @staticmethod
        def action(luaObj, window, x, y, suffix):
            reference_asset.import_all()

    class import_geo(command):
        @staticmethod
        def action(luaObj, window, x, y, suffix):
            reference_asset.import_geo()

    class import_grooming(command):
        @staticmethod
        def action(luaObj, window, x, y, suffix):
            reference_asset.import_grooming()

    class import_cyclo(command):
        @staticmethod
        def action(luaObj, window, x, y, suffix):
            reference_asset.import_cyclo()

    class import_layout(command):
        @staticmethod
        def action(luaObj, window, x, y, suffix):
            reference_asset.import_layout()

    class import_texturing(command):
        @staticmethod
        def action(luaObj, window, x, y, suffix):
            reference_asset.import_texturing()

    class import_shading(command):
        @staticmethod
        def action(luaObj, window, x, y, suffix):
            reference_asset.import_shading()

    class import_anim(command):
        @staticmethod
        def action(luaObj, window, x, y, suffix):
            reference_asset.import_anim()

    class import_camera(command):
        @staticmethod
        def action(luaObj, window, x, y, suffix):
            reference_asset.import_camera()

    class import_cfx(command):
        @staticmethod
        def action(luaObj, window, x, y, suffix):
            reference_asset.import_cfx()

    class import_render_pass(command):
        @staticmethod
        def action(luaObj, window, x, y, suffix):
            reference_asset.import_render_pass()

    class reload_all(command):
        @staticmethod
        def action(luaObj, window, x, y, suffix):
            reference_asset.reload_all()

    class reload_geo(command):
        @staticmethod
        def action(luaObj, window, x, y, suffix):
            reference_asset.import_geo(1)

    class reload_grooming(command):
        @staticmethod
        def action(luaObj, window, x, y, suffix):
            reference_asset.import_grooming(1)

    class reload_texturing(command):
        @staticmethod
        def action(luaObj, window, x, y, suffix):
            reference_asset.import_texturing(1)

    class reload_shading(command):
        @staticmethod
        def action(luaObj, window, x, y, suffix):
            reference_asset.import_shading(1)

    class reload_anim(command):
        @staticmethod
        def action(luaObj, window, x, y, suffix):
            reference_asset.import_anim(1)

    class reload_camera(command):
        @staticmethod
        def action(luaObj, window, x, y, suffix):
            reference_asset.import_camera(1)

    class reload_cfx(command):
        @staticmethod
        def action(luaObj, window, x, y, suffix):
            reference_asset.import_cfx(1)

    class reload_render_pass(command):
        @staticmethod
        def action(luaObj, window, x, y, suffix):
            reference_asset.import_render_pass(1)

    class reload_cyclo(command):
        @staticmethod
        def action(luaObj, window, x, y, suffix):
            reference_asset.import_cyclo(1)

    class reload_layout(command):
        @staticmethod
        def action(luaObj, window, x, y, suffix):
            reference_asset.import_layout(1)

    class Export(command):
        @staticmethod
        def action(luaObj, window, x, y, suffix):
            plugin.export_all()

    class Match_all(command):
        @staticmethod
        def action(luaObj, window, x, y, suffix):
            init_scene.setup_guerilla()

    class Match_project_format(command):
        @staticmethod
        def action(luaObj, window, x, y, suffix):
            init_scene.set_format()

    class Match_project_frame_rate(command):
        @staticmethod
        def action(luaObj, window, x, y, suffix):
            init_scene.set_frame_rate()

    class Match_scene_frame_range(command):
        @staticmethod
        def action(luaObj, window, x, y, suffix):
            init_scene.set_range()

    class Build_main_RenderPass(command):
        @staticmethod
        def action(luaObj, window, x, y, suffix):
            setup_render.helios_bridge()

    class Build_lighting_RenderPass(command):
        @staticmethod
        def action(luaObj, window, x, y, suffix):
            setup_render.helios_bridge().create_lighting_layer()

    class Setup_for_render_HD(command):
        @staticmethod
        def action(luaObj, window, x, y, suffix):
            setup_render.export().set_HD()

    class Setup_for_render_FML(command):
        @staticmethod
        def action(luaObj, window, x, y, suffix):
            setup_render.export().set_FML()

    class Setup_for_render_LD(command):
        @staticmethod
        def action(luaObj, window, x, y, suffix):
            setup_render.export().set_LD()

    app_path = os.environ[defaults._abs_site_path_]
    save_icon = (defaults._guerilla_save_icon_).replace('\\', '/')
    export_icon = (defaults._guerilla_export_icon_).replace('\\', '/')
    
    geo_icon = defaults._stage_icon_[defaults._geo_]
    groom_icon = defaults._stage_icon_[defaults._hair_]
    texturing_icon = defaults._stage_icon_[defaults._texturing_]
    shading_icon = defaults._stage_icon_[defaults._shading_]
    anim_icon = defaults._stage_icon_[defaults._animation_]
    camera_icon = defaults._stage_icon_[defaults._camera_]
    cfx_icon = defaults._stage_icon_[defaults._cfx_]
    render_pass_icon = defaults._stage_icon_[defaults._render_pass_]
    cyclo_icon = defaults._stage_icon_[defaults._cyclo_]
    layout_icon = defaults._stage_icon_[defaults._layout_]

    import_icon = (defaults._guerilla_import_icon_).replace('\\', '/')
    reload_icon = (defaults._guerilla_reload_icon_).replace('\\', '/')
    match_all_icon = (defaults._guerilla_match_all_icon_).replace('\\', '/')
    format_icon = (defaults._guerilla_format_icon_).replace('\\', '/')
    frame_range_icon = (defaults._guerilla_frame_range_icon_).replace('\\', '/')
    frame_rate_icon = (defaults._guerilla_frame_rate_icon_).replace('\\', '/')
    build_main_pass_icon = (defaults._guerilla_build_main_rp_).replace('\\', '/')
    build_lighting_pass_icon = (defaults._guerilla_light_layers_).replace('\\', '/')
    

    stage = (asset_core.string_to_asset(os.environ[defaults._asset_var_])).stage

    cmd = Save('Save', save_icon)
    cmd.install('Wizard')
    command.addseparator ('Wizard')
    cmd = import_all('all', import_icon)
    cmd.install('Wizard', 'Import')
    cmd = import_geo('geo', geo_icon)
    cmd.install('Wizard', 'Import')
    cmd = import_grooming('grooming', groom_icon)
    cmd.install('Wizard', 'Import')
    cmd = import_texturing('texturing', texturing_icon)
    cmd.install('Wizard', 'Import')
    cmd = import_shading('shading', shading_icon)
    cmd.install('Wizard', 'Import')
    cmd = import_anim('animation', anim_icon)
    cmd.install('Wizard', 'Import')
    cmd = import_camera('camera', camera_icon)
    cmd.install('Wizard', 'Import')
    cmd = import_cfx('cfx', cfx_icon)
    cmd.install('Wizard', 'Import')
    cmd = import_layout('layout', layout_icon)
    cmd.install('Wizard', 'Import')
    cmd = import_render_pass('render_pass', render_pass_icon)
    cmd.install('Wizard', 'Import')
    cmd = import_cyclo('cyclo', cyclo_icon)
    cmd.install('Wizard', 'Import')
    
    cmd = reload_all('all', reload_icon)
    cmd.install('Wizard', 'Refresh')
    cmd = reload_geo('geo', geo_icon)
    cmd.install('Wizard', 'Refresh')
    cmd = reload_grooming('grooming', groom_icon)
    cmd.install('Wizard', 'Refresh')
    cmd = reload_texturing('texturing', texturing_icon)
    cmd.install('Wizard', 'Refresh')
    cmd = reload_shading('shading', shading_icon)
    cmd.install('Wizard', 'Refresh')
    cmd = reload_anim('animation', anim_icon)
    cmd.install('Wizard', 'Refresh')
    cmd = reload_camera('camera', camera_icon)
    cmd.install('Wizard', 'Refresh')
    cmd = reload_cfx('cfx', cfx_icon)
    cmd.install('Wizard', 'Refresh')
    cmd = reload_layout('layout', layout_icon)
    cmd.install('Wizard', 'Refresh')
    cmd = reload_render_pass('render_pass', render_pass_icon)
    cmd.install('Wizard', 'Refresh')
    cmd = reload_cyclo('cyclo', cyclo_icon)
    cmd.install('Wizard', 'Refresh')
    
    cmd = Export('Export ({})'.format(stage), export_icon)
    cmd.install('Wizard')
    command.addseparator ('Wizard')
    cmd = Match_all('Match all', match_all_icon)
    cmd.install('Wizard')
    cmd = Match_project_format('Match project format', format_icon)
    cmd.install('Wizard')
    cmd = Match_project_frame_rate('Match project frame rate', frame_rate_icon)
    cmd.install('Wizard')
    cmd = Match_scene_frame_range('Match scene frame range', frame_range_icon)
    cmd.install('Wizard')

    command.addseparator ('Wizard')

    cmd = Build_main_RenderPass('Build main RenderPass', build_main_pass_icon)
    cmd.install('Wizard', 'Helios')
    cmd = Build_lighting_RenderPass('Build lighting RenderPass', build_lighting_pass_icon)
    cmd.install('Wizard', 'Helios')

    command.addseparator ('Wizard')

    cmd = Setup_for_render_HD('Setup for render (HD)', export_icon)
    cmd.install('Wizard', 'Render')
    cmd = Setup_for_render_FML('Setup for render (FML)', export_icon)
    cmd.install('Wizard', 'Render')
    cmd = Setup_for_render_LD('Setup for render (LD)', export_icon)
    cmd.install('Wizard', 'Render')