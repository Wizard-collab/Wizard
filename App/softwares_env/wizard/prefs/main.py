from wizard.prefs import asset as asset_prefs
from wizard.prefs import project as project_prefs
from wizard.prefs.user import user
from wizard.prefs.site import site
from wizard.prefs import software as software_prefs
from wizard.prefs.user_events import user_events
from wizard.tools import log
from wizard.vars import defaults
import os

user_prefs = user()
site_prefs = site()

logger = log.pipe_log(__name__)

class prefs:
    def __init__(self):
        self.site = self.site()

    @property
    def user(self):
        return user_prefs.get_user()

    def set_user(self, user_name):
        user_prefs.set_user(user_name)

    @property
    def chat_seen(self):
        return user_prefs.get_seen_dict()

    def set_seen(self, room, message_key):
        user_prefs.add_seen(room, message_key)

    @property
    def server_ip(self):
        return user_prefs.get_server_ip()

    def set_server_ip(self, ip):
        user_prefs.set_server_ip(ip)

    @property
    def events(self):
        return user_events(self.project_path, self.user).get_events()

    def add_event(self, id):
        user_events(self.project_path, self.user).add_event(id)

    @property
    def locks(self):
        return user_events(self.project_path, self.user).get_locks()

    def add_lock(self, string_asset):
        user_events(self.project_path, self.user).add_lock(string_asset)

    def remove_lock(self, string_asset):
        user_events(self.project_path, self.user).remove_lock(string_asset)

    def remove_lock_from_user(self, string_asset, user):
        user_events(self.project_path, user).remove_lock(string_asset)

    @property
    def screen(self):
        return user_prefs.get_screen()

    @property
    def local_project_path(self):
        return user_prefs.get_local_project_path()

    def copy_file(self):
        path = os.path.join(self.project_path, defaults._copy_folder_)
        if not os.path.isdir(path):
            os.makedirs(path)
        full_file = os.path.join(path, defaults._copy_file_)
        return full_file

    def set_screen(self, index):
        user_prefs.set_screen(index)

    @property
    def promotion(self):
        return site_prefs.get_user_promotion(self.user)

    def change_user(self, user_name, password):
        # Check the password concordance
        if site_prefs.password_check(user_name, password):
            user_prefs.set_user(user_name)
            return 1
        else:
            return 0

    def set_local_project_path(self, local_project_path):
        user_prefs.set_local_project_path(local_project_path)

    def leave_user(self):
        user_prefs.set_user(None)

    @property
    def context(self):
        return user_prefs.get_context()

    def set_context(self, asset):
        return user_prefs.set_context(asset)

    @property
    def tab_context(self):
        return user_prefs.get_tab_context()

    def set_tab_context(self, tab):
        return user_prefs.set_tab_context(tab)
    

    @property
    def quit_on_close(self):
        return user_prefs.get_quit_on_close()

    def change_project(self, project_name):
        return user_prefs.change_project(project_name)

    @property
    def project_path(self):
        project_name = user_prefs.get_current_project_name()
        if project_name:
            path = site_prefs.get_project_path_from_name(project_name)
            return path
        else:
            return 0

    def get_path_from_project(self, project_name):
        return site_prefs.get_project_path_from_name(project_name)

    @property
    def user_image(self):
        return user_prefs.get_image()

    @property
    def project_name(self):
        return user_prefs.get_current_project_name()

    @property
    def shutter(self):
        return user_prefs.get_shutter()

    @property
    def path(self):
        return user_prefs.get_prefs_path()

    @property
    def user_email(self):
        return site_prefs.get_email_from_user(self.user)

    @property
    def user_full_name(self):
        return site_prefs.get_user_full_name(self.user)
        
    def get_email_from_user(self, user):
        return site_prefs.get_email_from_user(user)

    def get_full_name_from_user(self, user):
        return site_prefs.get_user_full_name(user)

    @property
    def admin(self):
        return site_prefs.get_user_admin(self.user)

    def admin_from_user(self, user):
        return site_prefs.get_user_admin(user)

    @property
    def frame_rate(self):
        return project_prefs.get_frame_rate()

    @property
    def custom_pub_ext_dic(self):
        return project_prefs.get_custom_pub_ext_dic()

    def set_custom_pub_ext_dic(self, pub_ext_dic = defaults._pub_ext_dic_):
        project_prefs.set_custom_pub_ext_dic(pub_ext_dic)

    @property
    def format(self):
        return project_prefs.get_format()

    @property
    def color_managment(self):
        return project_prefs.get_color_managment()

    @property
    def project_users(self):
        return project_prefs.get_users()

    @property
    def show_updates(self):
        return user_prefs.get_show_updates()

    @property
    def show_new_version(self):
        return user_prefs.get_show_new_version()

    @property
    def show_error_handler(self):
        return user_prefs.get_show_error_handler()

    @property
    def last_update(self):
        return user_prefs.get_last_update()

    @property
    def script_cache(self):
        return user_prefs.get_script_cache()

    def set_script_cache(self, script):
        return user_prefs.set_script_cache(script)

    def set_show_updates(self, show_updates):
        user_prefs.set_show_updates(show_updates)

    def set_show_new_version(self, show_new_version):
        user_prefs.set_show_new_version(show_new_version)

    def set_show_error_handler(self, show_error_handler):
        user_prefs.set_show_error_handler(show_error_handler)

    def set_last_update(self, last_update):
        user_prefs.set_last_update(last_update)

    def set_shutter(self, shutter):
        user_prefs.set_shutter(shutter)
    
    class site:
        def __init__(self):
            pass

        @property
        def users(self):
            return site_prefs.get_users_list()

        @property
        def projects(self):
            return site_prefs.get_projects_list()        

        def add_project(self, project_name, project_path, password):
            return site_prefs.add_project(project_name, project_path, password)

    class software:
        def __init__(self, software):
            self.software = software

        @property
        def path(self):
            return software_prefs.software(self.software).get_path()

        @property
        def env(self):
            return software_prefs.software(self.software).get_env()

        @property
        def settings_path(self):
            return software_prefs.software(self.software).get_settings_path()

    class asset:
        def __init__(self, asset):
            self.asset = asset
            self.category = self.category(asset)
            self.name = self.name(asset)
            self.stage = self.stage(asset)
            self.variant = self.variant(asset)
            self.software = self.software(asset)
            self.export_root = self.export_root(asset)
            self.export = self.export(asset)
            self.playblast = self.playblast(asset)

        def add_event(self, id):
            asset_prefs.name(self.asset).add_event(id)

        @property
        def events(self):
            return asset_prefs.name(self.asset).get_events()

        @property
        def folder(self):
            if self.asset.category and \
                    not self.asset.name:
                folder = asset_prefs.category(self.asset).path
            elif self.asset.name and \
                    not self.asset.stage:
                folder = asset_prefs.name(self.asset).path
            else:
                folder = asset_prefs.variant(self.asset).path
            return folder

        class category:
            def __init__(self, asset):
                self.asset = asset

            @property
            def user(self):
                return asset_prefs.category(self.asset).get_creation_user()

            @property
            def date(self):
                return asset_prefs.category(self.asset).get_creation_date()

            def write(self):
                return asset_prefs.category(self.asset).write()

        class name:
            def __init__(self, asset):
                self.asset = asset

            @property
            def user(self):
                return asset_prefs.name(self.asset).get_creation_user()

            @property
            def date(self):
                return asset_prefs.name(self.asset).get_creation_date()

            @property
            def range(self):
                return asset_prefs.name(self.asset).get_frame_range()

            @property
            def preroll(self):
                return asset_prefs.name(self.asset).get_preroll()
            
            @property
            def postroll(self):
                return asset_prefs.name(self.asset).get_postroll()

            def set_preroll(self, preroll):
                return asset_prefs.name(self.asset).set_preroll(preroll)

            def set_postroll(self, postroll):
                return asset_prefs.name(self.asset).set_postroll(postroll)

            def set_range(self, range):
                return asset_prefs.name(self.asset).set_frame_range(range)

            def write(self, in_out=None):
                return asset_prefs.name(self.asset, in_out).write()

        class stage:
            def __init__(self, asset):
                self.asset = asset

            @property
            def user(self):
                return asset_prefs.stage(self.asset).get_creation_user()

            @property
            def date(self):
                return asset_prefs.stage(self.asset).get_creation_date()

            @property
            def softwares(self):
                return asset_prefs.stage(self.asset).get_softwares_list()

            @property
            def variants(self):
                return asset_prefs.stage(self.asset).get_variants_list()

            @property
            def default_variant(self):
                return asset_prefs.stage(self.asset).get_default_variant()

            def set_default_variant(self, variant):
                return asset_prefs.stage(self.asset).set_default_variant(variant)

            def write(self):
                return asset_prefs.stage(self.asset).write()

            def add_variant(self):
                return asset_prefs.stage(self.asset).add_variant()

        class variant:
            def __init__(self, asset):
                self.asset = asset

            @property
            def user(self):
                return asset_prefs.variant(self.asset).get_creation_user()

            @property
            def folder(self):
                return asset_prefs.variant(self.asset).path

            @property
            def date(self):
                return asset_prefs.variant(self.asset).get_creation_date()

            @property
            def default_software(self):
                return asset_prefs.variant(self.asset).get_default_software()

            @property
            def state(self):
                return asset_prefs.variant(self.asset).get_state()
            
            def set_state(self, state):
                return asset_prefs.variant(self.asset).set_state(state)

            def set_default_software(self, software):
                return asset_prefs.variant(self.asset).set_default_software(software)

            def write(self):
                return asset_prefs.variant(self.asset).write()

        class software:
            def __init__(self, asset):
                self.asset = asset

            @property
            def user(self):
                return asset_prefs.software(self.asset).get_creation_user()

            @property
            def extension(self):
                return asset_prefs.software(self.asset).get_extension()

            @property
            def date(self):
                return asset_prefs.software(self.asset).get_creation_date()

            @property
            def versions(self):
                return asset_prefs.software(self.asset).get_versions_list()

            @property
            def version(self):
                return asset_prefs.software(self.asset).get_version()

            @property
            def last_version(self):
                return asset_prefs.software(self.asset).get_last_version()

            @property
            def icon(self):
                return asset_prefs.software(self.asset).get_icon()

            @property
            def image(self):
                return asset_prefs.software(self.asset).get_image()

            @property
            def version_user(self):
                return asset_prefs.software(self.asset).get_version_user()

            @property
            def version_date(self):
                return asset_prefs.software(self.asset).get_version_date()            

            @property
            def version_comment(self):
                return asset_prefs.software(self.asset).get_version_comment()

            def set_version_comment(self, comment):
                return asset_prefs.software(self.asset).set_version_comment(comment)

            @property
            def running(self):
                return asset_prefs.software(self.asset).get_running()

            def set_running(self, running):
                return asset_prefs.software(self.asset).set_running(running)

            @property
            def get_lock(self):
                return asset_prefs.software(self.asset).get_lock()

            def lock(self):
                asset_prefs.software(self.asset).lock()

            def unlock(self):
                asset_prefs.software(self.asset).unlock()

            def write(self):
                return asset_prefs.software(self.asset).write()

            def new_version(self, version):
                return asset_prefs.software(self.asset).new_version(version=version)

            def get_new_version(self):
                return asset_prefs.software(self.asset).get_new_version()

            def set_asset_extension(self, extension):
                return asset_prefs.software(self.asset).set_asset_extension(extension)

            def remove_version(self, version):
                return asset_prefs.software(self.asset).remove_version(version=version)

            def merge_version(self, file):
                return asset_prefs.software(self.asset).merge_version(file)

            @property
            def references(self):
                return asset_prefs.software(self.asset).get_references()

            def set_references(self, dic):
                return asset_prefs.software(self.asset).set_references(dic)

        class export_root:
            def __init__(self, asset):
                self.asset = asset

            def add_export_asset(self, export_asset):
                asset_prefs.export_root(self.asset).add_export_asset(export_asset)
                self.set_default_export_asset(export_asset)

            def set_default_export_asset(self, export_asset):
                asset_prefs.export_root(self.asset).set_default_export_asset(export_asset)

            @property
            def default_export_asset(self):
                return asset_prefs.export_root(self.asset).get_default_export_asset()

            @property
            def exported_assets_list(self):
                return asset_prefs.export_root(self.asset).get_exported_assets_list()

            @property
            def folder(self):
                return asset_prefs.export_root(self.asset).path

            def write(self):
                return asset_prefs.export_root(self.asset).write()

        class export:
            def __init__(self, asset):
                self.asset = asset

            @property
            def user(self):
                return asset_prefs.export(self.asset).get_creation_user()

            @property
            def date(self):
                return asset_prefs.export(self.asset).get_creation_date()

            @property
            def versions(self):
                return asset_prefs.export(self.asset).get_versions_list()

            @property
            def version(self):
                return asset_prefs.export(self.asset).get_version()

            @property
            def last_version(self):
                return asset_prefs.export(self.asset).get_last_version()

            @property
            def image(self):
                return asset_prefs.export(self.asset).get_image()

            @property
            def version_user(self):
                return asset_prefs.export(self.asset).get_version_user()

            @property
            def version_date(self):
                return asset_prefs.export(self.asset).get_version_date()

            @property
            def version_comment(self):
                return asset_prefs.export(self.asset).get_version_comment()

            @property
            def version_software(self):
                return asset_prefs.export(self.asset).get_version_software()  

            @property
            def from_asset(self):
                return asset_prefs.export(self.asset).get_from_asset() 
            

            def set_version_comment(self, comment):
                return asset_prefs.export(self.asset).set_version_comment(comment)

            def set_version_software(self):
                return asset_prefs.export(self.asset).set_version_software()

            def set_from_asset(self, asset):
                return asset_prefs.export(self.asset).set_from_asset(asset)

            def write(self):
                return asset_prefs.export(self.asset).write()

            def new_version(self, version):
                return asset_prefs.export(self.asset).new_version(version=version)

            def get_new_version(self):
                return asset_prefs.export(self.asset).get_new_version()

            @property
            def file(self):
                return asset_prefs.export(self.asset).get_file()

            @property
            def proxy(self):
                return asset_prefs.export(self.asset).get_proxy_file()

            @property
            def is_proxy(self):
                return os.path.isfile(self.full_proxy)

            @property
            def folder(self):
                return asset_prefs.export(self.asset).path

            @property
            def full_file(self):
                full_file = os.path.join(self.version_folder, self.file)
                return full_file

            @property
            def full_proxy(self):
                full_file = os.path.join(self.version_folder, self.proxy)
                return full_file

            @property
            def version_folder(self):
                return asset_prefs.export(self.asset).version_path

        class playblast:
            def __init__(self, asset):
                self.asset = asset

            @property
            def user(self):
                return asset_prefs.playblast(self.asset).get_creation_user()

            @property
            def date(self):
                return asset_prefs.playblast(self.asset).get_creation_date()

            @property
            def versions(self):
                return asset_prefs.playblast(self.asset).get_versions_list()

            @property
            def version(self):
                return asset_prefs.playblast(self.asset).get_version()

            @property
            def last_version(self):
                return asset_prefs.playblast(self.asset).get_last_version()

            @property
            def image(self):
                return asset_prefs.playblast(self.asset).get_image()

            def version_user(self, version):
                return asset_prefs.playblast(self.asset).get_version_user(version)

            def version_date(self, version):
                return asset_prefs.playblast(self.asset).get_version_date(version)

            def version_comment(self, version):
                return asset_prefs.playblast(self.asset).get_version_comment(version)

            def version_image(self, version):
                return asset_prefs.playblast(self.asset).get_version_image(version)

            def set_version_comment(self, comment, version):
                return asset_prefs.playblast(self.asset).set_version_comment(comment, version)

            def write(self):
                return asset_prefs.playblast(self.asset).write()

            def new_version(self, version):
                return asset_prefs.playblast(self.asset).new_version(version=version)

            def get_new_version(self):
                return asset_prefs.playblast(self.asset).get_new_version()

            def file(self, version):
                return asset_prefs.playblast(self.asset).get_file(version)

            @property
            def proxy(self):
                return asset_prefs.playblast(self.asset).get_proxy_file()

            @property
            def folder(self):
                return asset_prefs.playblast(self.asset).path

            def full_file(self, version):
                full_file = os.path.join(self.folder, self.file(version))
                return full_file

            @property
            def folder(self):
                return asset_prefs.playblast(self.asset).get_folder()
