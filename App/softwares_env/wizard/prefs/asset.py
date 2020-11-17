# coding: utf-8

# Default python modules
import os
# Wizard tools modules
from wizard.tools import utility as util
from wizard.tools import log
# Wizard variables modules
from wizard.vars import defaults
# Wizard prefs modules
from wizard.prefs.user import user
# Wizard asset modules
from wizard.asset.folder import folder

from wizard.prefs import project as project_prefs

import traceback

import shutil
# Create the main logger
logger = log.pipe_log(__name__)

user = user()


class category():
    def __init__(self, asset):
        self.database = util.database()
        self.asset = asset
        self.path = folder(self.asset).category
        self.file = os.path.join(self.path, defaults._category_prefs_)
        self.settings = self.read_settings()

    def write(self):
        if self.path:
            write_prefs(self.database, self.file, self.settings)
        else:
            logger.debug("Can't write category prefs")

    def get_creation_date(self):
        return self.settings[defaults._creation_date_key_]

    def get_creation_user(self):
        return self.settings[defaults._creation_user_key_]

    def read_settings(self):
        if self.database.isfile(2, self.file):
            settings = read_prefs(self.database, self.file)
        else:
            settings = {}
            settings[defaults._creation_date_key_] = util.get_time()
            settings[defaults._creation_user_key_] = user.get_user()
        return settings


class name():
    def __init__(self, asset, in_out=None):
        self.database = util.database()
        self.asset = asset
        self.in_out = in_out
        self.path = folder(self.asset).name
        self.file = os.path.join(self.path, defaults._name_prefs_)
        self.settings = self.read_settings()

    def write(self):
        if self.path:
            write_prefs(self.database, self.file, self.settings)
        else:
            logger.debug("Can't write name prefs")

    def get_creation_date(self):
        return self.settings[defaults._creation_date_key_]

    def get_creation_user(self):
        return self.settings[defaults._creation_user_key_]

    def get_frame_range(self):
        return self.settings[defaults._frame_range_key_]

    def set_frame_range(self, range):
        self.settings[defaults._frame_range_key_] = range
        self.write()

    def set_preroll(self, preroll):
        self.settings[defaults._preroll_key_] = preroll
        self.write()

    def get_preroll(self):
        if defaults._preroll_key_ not in self.settings.keys():
            self.set_preroll(0)
        return self.settings[defaults._preroll_key_]

    def set_postroll(self, postroll):
        self.settings[defaults._postroll_key_] = postroll
        self.write()

    def get_postroll(self):
        if defaults._postroll_key_ not in self.settings.keys():
            self.set_postroll(0)
        return self.settings[defaults._postroll_key_]

    def read_settings(self):
        if self.database.isfile(2, self.file):
            settings = read_prefs(self.database, self.file)
        else:
            if not self.in_out:
                self.in_out = [100, 196]
            settings = dict()
            settings[defaults._creation_date_key_] = util.get_time()
            settings[defaults._creation_user_key_] = user.get_user()
            settings[defaults._frame_range_key_] = self.in_out
            settings[defaults._asset_events_key_] = []
        return settings

    def add_event(self, id):
        if defaults._asset_events_key_ in self.settings.keys():
            self.settings[defaults._asset_events_key_].append(id)
        else:
            self.settings[defaults._asset_events_key_] = [id]
        self.write()

    def get_events(self):
        if defaults._asset_events_key_ in self.settings.keys():
            return self.settings[defaults._asset_events_key_]
        else:
            self.settings[defaults._asset_events_key_] = []
            self.write()
            return []


class stage():
    def __init__(self, asset):
        self.database = util.database()
        self.asset = asset
        self.path = folder(self.asset).stage
        self.file = os.path.join(self.path, defaults._stage_prefs_)
        self.settings = self.read_settings()

    def write(self):
        if self.path:
            write_prefs(self.database, self.file, self.settings)
        else:
            logger.debug("Can't write stage prefs")

    def get_creation_date(self):
        return self.settings[defaults._creation_date_key_]

    def get_creation_user(self):
        return self.settings[defaults._creation_user_key_]

    def get_softwares_list(self):
        return self.settings[defaults._softwares_list_key_]

    def get_variants_list(self):
        if self.settings[defaults._variants_list_key_] and \
                self.settings[defaults._variants_list_key_] != [None] and \
                self.settings[defaults._variants_list_key_] != []:
            return self.settings[defaults._variants_list_key_]
        else:
            return None

    def add_variant(self):
        if self.asset.variant not in self.settings[defaults._variants_list_key_]:
            self.settings[defaults._variants_list_key_].append(self.asset.variant)
            self.write()

    def set_default_variant(self, variant):
        self.settings[defaults._default_variant_key_] = variant
        self.write()

    def get_default_variant(self):
        return self.settings[defaults._default_variant_key_]

    def read_settings(self):
        if self.database.isfile(2, self.file):
            settings = read_prefs(self.database, self.file)
        else:
            settings = dict()
            settings[defaults._creation_date_key_] = util.get_time()
            settings[defaults._creation_user_key_] = user.get_user()
            settings[defaults._softwares_list_key_] = get_softwares_from_stage(self.asset.stage)
            settings[defaults._variants_list_key_] = []
            settings[defaults._default_variant_key_] = 'main'
        return settings


class variant():
    def __init__(self, asset):
        self.database = util.database()
        self.asset = asset
        self.path = folder(self.asset).variant
        self.file = os.path.join(self.path, defaults._variant_prefs_)
        self.settings = self.read_settings()

    def write(self):
        if self.path:
            write_prefs(self.database, self.file, self.settings)
        else:
            logger.debug("Can't write variant prefs")

    def set_state(self, state):
        self.settings[defaults._asset_state_] = state
        self.write()

    def get_state(self):
        if defaults._asset_state_ not in self.settings.keys():
            self.set_state(defaults._todo_)
        return self.settings[defaults._asset_state_]

    def get_creation_date(self):
        return self.settings[defaults._creation_date_key_]

    def get_creation_user(self):
        return self.settings[defaults._creation_user_key_]

    def get_default_software(self):
        return self.settings[defaults._default_software_key_]

    def get_publish_file(self):
        ext = (project_prefs.get_custom_pub_ext_dic())[self.asset.stage][self.asset.software]
        file = '{}/{}_{}_{}_{}.{}'.format(self.path, self.asset.stage, self.asset.category, self.asset.name,
                                          self.asset.variant, ext)
        return file

    def set_default_software(self, software):
        self.settings[defaults._default_software_key_] = software
        self.write()

    def read_settings(self):
        if self.database.isfile(2, self.file):
            settings = read_prefs(self.database, self.file)
        else:
            settings = dict()
            settings[defaults._creation_date_key_] = util.get_time()
            settings[defaults._creation_user_key_] = user.get_user()
            settings[defaults._default_software_key_] = get_softwares_from_stage(self.asset.stage)[0]
            
            settings[defaults._asset_state_] = defaults._todo_
        return settings

    def get_assets_list(self):
        references_list = self.get_references()
        asset_list = []
        for namespace in list(references_list.keys()):
            asset = asset_core.string_to_asset(references_list[namespace][defaults._asset_key_])
            folder = prefs().asset(asset).export.version_folder
            file = prefs().asset(asset).export.file
            full_path = os.path.join(folder, file)
            asset_list.append([asset, namespace, full_path])
        return asset_list


class export_root():
    def __init__(self, asset):
        self.database = util.database()
        self.asset = asset
        self.path = folder(self.asset).export_root()
        self.file = os.path.join(self.path, defaults._export_root_prefs_)
        self.read_settings()

    def write(self):
        if folder(self.asset).is_export_root():
            write_prefs(self.database, self.file, self.settings)
        else:
            logger.debug("Can't write export_root prefs")

    def get_creation_date(self):
        return self.settings[defaults._creation_date_key_]

    def get_creation_user(self):
        return self.settings[defaults._creation_user_key_]

    def read_settings(self):
        if self.database.isfile(2, self.file):
            self.settings = read_prefs(self.database, self.file)
        else:
            self.settings = {}
            self.settings[defaults._creation_date_key_] = util.get_time()
            self.settings[defaults._creation_user_key_] = user.get_user()
            self.settings[defaults._export_assets_list_key_] = {}
            self.settings[defaults._default_export_asset_key_] = None

    def add_export_asset(self, export_asset_namespace):
        export_asset_dic = {}
        export_asset_dic[defaults._export_asset_key_] = export_asset_namespace
        self.settings[defaults._export_assets_list_key_][export_asset_namespace] = export_asset_dic
        self.write()

    def set_default_export_asset(self, export_asset):
        self.settings[defaults._default_export_asset_key_] = export_asset
        self.write()

    def get_default_export_asset(self):
        return self.settings[defaults._default_export_asset_key_]

    def get_export_assets_dic(self):
        export_assets_dic = self.settings[defaults._export_assets_list_key_]
        return export_assets_dic

    def get_exported_assets_list(self):
        export_assets_dic = self.get_export_assets_dic()
        return list(export_assets_dic.keys())

class playblast():
    def __init__(self, asset, version = None):
        self.database = util.database()
        self.asset = asset
        self.path = folder(self.asset).playblast()
        self.file = os.path.join(self.path, defaults._playblast_prefs_)
        self.read_settings()

        self.version = self.get_version()

    def write(self):
        if folder(self.asset).is_playblast():
            write_prefs(self.database, self.file, self.settings)
        else:
            logger.debug("Can't write software prefs")

    def get_creation_date(self):
        return self.settings[defaults._creation_date_key_]

    def get_creation_user(self):
        return self.settings[defaults._creation_user_key_]

    def get_versions_list(self):
        version_list = list(self.settings[defaults._versions_list_key_].keys())
        version_list.sort()
        return version_list

    def get_version(self):
        versions_list = self.get_versions_list()
        if versions_list:
            version = versions_list[-1]
        else:
            version = 0
        return version

    def get_file(self, version):
        return folder(self.asset).playblast_file(version)

    def get_version_image(self, version):
        folder_obj = folder(self.asset)
        path = os.path.join(folder_obj.playblast(), folder_obj.playblast_image(version))
        return path

    def get_folder(self):
        return folder(self.asset).playblast()

    def get_new_version(self):
        last_version = self.get_last_version()
        new_version = str(int(last_version) + 1).zfill(4)
        return new_version

    def get_last_version(self):
        versions_list = self.get_versions_list()
        if versions_list:
            version = versions_list[-1]
            return version
        else:
            return 0

    def read_settings(self):
        if self.database.isfile(2, self.file):
            self.settings = read_prefs(self.database, self.file)
        else:
            self.settings = {}
            self.settings[defaults._creation_date_key_] = util.get_time()
            self.settings[defaults._creation_user_key_] = user.get_user()
            self.settings[defaults._versions_list_key_] = {}

    def new_version(self, version=None, comment='Too bad, there is no comment...'):
        if not version:
            new_version = self.get_version()
        elif not version.isdigit():
            pass
        else:
            new_version = version
        if version not in self.settings[defaults._versions_list_key_]:
            new_version_settings = dict()
            new_version_settings[defaults._creation_date_key_] = util.get_time()
            new_version_settings[defaults._creation_user_key_] = user.get_user()
            new_version_settings[defaults._comment_key_] = comment
            self.settings[defaults._versions_list_key_][new_version] = new_version_settings
            self.write()
            return new_version

    def get_version_user(self, version):
        return self.settings[defaults._versions_list_key_] \
            [version] \
            [defaults._creation_user_key_]

    def get_version_date(self, version):
        return self.settings[defaults._versions_list_key_] \
            [version] \
            [defaults._creation_date_key_]

    def get_version_comment(self, version):
        return self.settings[defaults._versions_list_key_] \
            [version] \
            [defaults._comment_key_]

    def set_version_comment(self, comment, version):
        self.settings[defaults._versions_list_key_] \
            [version] \
            [defaults._comment_key_] = comment
        self.write()


class export():
    def __init__(self, asset):
        self.database = util.database()
        self.asset = asset
        self.path = folder(self.asset).export()
        self.file = os.path.join(self.path, defaults._export_prefs_)
        self.read_settings()
        self.get_version()
        self.version_path = folder(self.asset).export(self.asset.export_version)

    def write(self):
        if folder(self.asset).is_export():
            write_prefs(self.database, self.file, self.settings)
        else:
            logger.debug("Can't write software prefs")

    def get_creation_date(self):
        return self.settings[defaults._creation_date_key_]

    def get_creation_user(self):
        return self.settings[defaults._creation_user_key_]

    def get_versions_list(self):
        version_list = list(self.settings[defaults._versions_list_key_].keys())
        version_list.sort()
        return version_list

    def get_version(self):
        if not self.asset.export_version:
            versions_list = self.get_versions_list()
            if versions_list:
                version = versions_list[-1]
            else:
                version = None
            self.asset.export_version = version

    def get_file(self):
        return folder(self.asset).export_file

    def get_proxy_file(self):
        return folder(self.asset).export_proxy_file

    def get_new_version(self):
        last_version = self.get_last_version()
        new_version = str(int(last_version) + 1).zfill(4)
        return new_version

    def get_last_version(self):
        versions_list = self.get_versions_list()
        if versions_list:
            version = versions_list[-1]
            return version
        else:
            return 0

    def read_settings(self):
        if self.database.isfile(2, self.file):
            self.settings = read_prefs(self.database, self.file)
        else:
            self.settings = {}
            self.settings[defaults._creation_date_key_] = util.get_time()
            self.settings[defaults._creation_user_key_] = user.get_user()
            self.settings[defaults._versions_list_key_] = {}
            self.settings[defaults._publish_] = 0

    def new_version(self, version=None, comment='Too bad, there is no comment...'):
        if not version:
            new_version = self.get_version()
        elif not version.isdigit():
            pass
        else:
            new_version = version
        if version not in self.settings[defaults._versions_list_key_]:
            new_version_settings = dict()
            new_version_settings[defaults._creation_date_key_] = util.get_time()
            new_version_settings[defaults._creation_user_key_] = user.get_user()
            new_version_settings[defaults._comment_key_] = comment
            new_version_settings[defaults._software_key_] = self.asset.software
            self.settings[defaults._versions_list_key_][new_version] = new_version_settings
            self.write()
            return new_version

    def get_image(self):
        image_name = 'capture.{}.png'.format(self.asset.export_version)
        image_path = os.path.join(folder(self.asset).export, image_name)
        return image_path

    def get_version_user(self):
        return self.settings[defaults._versions_list_key_] \
            [self.asset.export_version] \
            [defaults._creation_user_key_]

    def get_version_date(self):
        return self.settings[defaults._versions_list_key_] \
            [self.asset.export_version] \
            [defaults._creation_date_key_]

    def get_version_comment(self):
        return self.settings[defaults._versions_list_key_] \
            [self.asset.export_version] \
            [defaults._comment_key_]

    def set_version_comment(self, comment):
        self.settings[defaults._versions_list_key_] \
            [self.asset.export_version] \
            [defaults._comment_key_] = comment
        self.write()

    def set_version_software(self):
        self.settings[defaults._versions_list_key_] \
            [self.asset.export_version] \
            [defaults._software_key_] = self.asset.software
        self.write()

    def set_from_asset(self, asset):
        self.settings[defaults._versions_list_key_] \
            [self.asset.export_version] \
            [defaults._from_asset_key_] = util.version_asset_to_string(asset)
        self.write()

    def get_version_software(self):
        return self.settings[defaults._versions_list_key_] \
            [self.asset.export_version] \
            [defaults._software_key_]

    def get_from_asset(self):
        if defaults._from_asset_key_ in self.settings[defaults._versions_list_key_][self.asset.export_version].keys():
            return self.settings[defaults._versions_list_key_] \
                [self.asset.export_version] \
                [defaults._from_asset_key_]
        else:
            return None

    def is_published(self):
        return self.settings[defaults._publish_]

    def set_publish(self, state=1):
        self.settings[defaults._publish_] = state
        self.write()


class software():
    def __init__(self, asset):
        self.database = util.database()
        self.asset = asset
        self.path = folder(self.asset).software
        self.file = os.path.join(self.path, defaults._software_prefs_)
        self.read_settings()
        self.get_version()

    def write(self):
        if self.asset.software:
            write_prefs(self.database, self.file, self.settings)
        else:
            logger.debug("Can't write software prefs")

    def get_creation_date(self):
        return self.settings[defaults._creation_date_key_]

    def get_creation_user(self):
        return self.settings[defaults._creation_user_key_]

    def get_versions_list(self):
        versions_list = list(self.settings[defaults._versions_list_key_].keys())
        versions_list.sort()
        return versions_list

    def get_version(self):
        if not self.asset.version:
            versions_list = self.get_versions_list()
            if versions_list:
                version = versions_list[-1]
            else:
                version = None
            self.asset.version = version

    def get_new_version(self):
        last_version = self.get_last_version()
        new_version = str(int(last_version) + 1).zfill(4)
        return new_version

    def get_last_version(self):
        versions_list = self.get_versions_list()
        if versions_list:
            version = versions_list[-1]
            return version
        else:
            return None

    def get_icon(self):
        icon = ''
        if self.asset.software:
            icon = defaults._soft_icons_dic_[self.asset.software]
        return icon

    def read_settings(self):
        if self.database.isfile(2, self.file):
            self.settings = read_prefs(self.database, self.file)
        else:
            self.settings = {}
            self.settings[defaults._creation_date_key_] = util.get_time()
            self.settings[defaults._creation_user_key_] = user.get_user()
            self.settings[defaults._lock_key_] = 0
            self.settings[defaults._run_key_] = 0
            self.settings[defaults._versions_list_key_] = {}
            self.settings[defaults._variant_references_list_] = {}
            self.new_version(version='0000', comment='Asset creation')

    def new_version(self, version=None, comment='Too bad, there is no comment...'):
        if not version:
            new_version = self.get_version(1)
        elif not version.isdigit():
            pass
        else:
            new_version = version
        new_version_settings = dict()
        new_version_settings[defaults._creation_date_key_] = util.get_time()
        new_version_settings[defaults._creation_user_key_] = user.get_user()
        new_version_settings[defaults._comment_key_] = comment
        self.settings[defaults._versions_list_key_][new_version] = new_version_settings
        self.write()
        return new_version

    def merge_version(self, file):
        self.asset.version = self.get_new_version()
        try:
            if not os.path.isfile(self.asset.file):
                shutil.copy(file, self.asset.file)
            self.new_version(version = self.asset.version, comment='Manually merged version')
            return 1
        except:
            logger.critical(str(traceback.format_exc()))
            return 0

    def remove_version(self, version):
        if version != '0000':
            del self.settings[defaults._versions_list_key_][version]
            self.write()
            os.rename(self.asset.file, self.asset.file + '_archived')
            logger.info("Version {} removed !".format(version))
            return 1
        else:
            logger.warning("Can't remove the default version, try to archive the asset instead !")
            return 0

    def get_image(self):
        image_name = 'capture.{}.png'.format(self.asset.version)
        image_path = os.path.join(folder(self.asset).software, image_name)
        return image_path

    def get_version_user(self):
        return self.settings[defaults._versions_list_key_] \
            [self.asset.version] \
            [defaults._creation_user_key_]

    def get_version_date(self):
        return self.settings[defaults._versions_list_key_] \
            [self.asset.version] \
            [defaults._creation_date_key_]

    def get_version_comment(self):
        return self.settings[defaults._versions_list_key_] \
            [self.asset.version] \
            [defaults._comment_key_]

    def set_version_comment(self, comment):
        self.settings[defaults._versions_list_key_] \
            [self.asset.version] \
            [defaults._comment_key_] = comment
        self.write()

    def get_lock(self):
        return self.settings[defaults._lock_key_]

    def lock(self):
        self.settings[defaults._lock_key_] = user.get_user()
        self.write()
        logger.info('Asset locked')

    def unlock(self):
        self.settings[defaults._lock_key_] = 0
        self.write()
        logger.info('Asset unlocked')

    def set_running(self, run):
        self.settings[defaults._run_key_] = run
        self.write()
        if run:
            logger.info('Software running...')
        else:
            pass

    def get_running(self):
        return self.settings[defaults._run_key_]

    def set_references(self, dic):
        self.settings[defaults._variant_references_list_] = dic
        self.write()

    def get_references(self):
        references_dic = self.settings[defaults._variant_references_list_]
        return references_dic

    def get_assets_list(self):
        references_list = self.get_references()
        asset_list = []
        for namespace in list(references_list.keys()):
            asset = asset_core.string_to_asset(references_list[namespace][defaults._asset_key_])
            folder = prefs().asset(asset).export.version_folder
            file = prefs().asset(asset).export.file
            full_path = os.path.join(folder, file)
            asset_list.append([asset, namespace, full_path])
        return asset_list


def write_prefs(database, file, settings):
    database.write(2, file, settings)
    logger.debug('{} updated'.format(file))


def read_prefs(database, file):
    settings = database.read(2, file)
    return settings


def get_softwares_from_stage(stage):
    softwares_list = defaults._stage_softs_dic_[stage]
    return softwares_list
