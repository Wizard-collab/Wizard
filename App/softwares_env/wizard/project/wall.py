# coding: utf-8

'''
This module is used to manage the local preferences of the user
It permits to set and get the user name and the current project

'''
# Defaults Python modules
import os
import sys

from wizard.chat import send
# Wizard prefs modules
from wizard.prefs.main import prefs
# Wizard tools modules
from wizard.tools import log
from wizard.tools import utility as util
# Wizard variables modules
from wizard.vars import defaults

# Create the main logger
logger = log.pipe_log(__name__)

# Write the user prefs file to the log
logger.debug(os.path.abspath(defaults._user_))

prefs = prefs()


class wall:

    def __init__(self):

        if prefs.project_path:
            self.wall = os.path.join(prefs.project_path, defaults._wall_)
            if not self.is_wall():
                # Create settings dictionnary
                settings = dict()
                # Write the .manager file as YAML with setting dict
                logger.info('{} file created'.format(defaults._wall_))
                self.write_wall_file(settings, new=1)

        else:
            self.wall = None

    def get_all_keys(self):
        if self.is_wall():
            settings = self.open_wall_file()
            keys_list = sorted(list(settings.keys()))
            if keys_list and type(keys_list) == list:
                return keys_list
            else:
                return list()

    def event(self, message, id, key, asset=None):
        settings = self.open_wall_file()
        user = prefs.user
        date = util.get_gmtime()
        message = message
        settings[key] = dict()
        settings[key][defaults._creation_user_key_] = user
        settings[key][defaults._creation_date_key_] = date
        settings[key][defaults._message_key_] = message
        settings[key][defaults._wall_id_key_] = id
        settings[key][defaults._wall_time_id_key_] = key
        if asset:
            asset = util.asset_to_string(asset)
        settings[key][defaults._asset_key_] = asset
        if id != defaults._wall_xp_event_:
            self.write_wall_file(settings)
        message = util.encode_message(settings[key])
        send.send_message(message)

    def create_event(self, asset):
        if asset.category and not asset.name:
            message = 'created  {} - {}'.format(asset.domain, asset.category)
        elif asset.name and not asset.stage:
            message = 'created  {} - {} - {}'.format(asset.domain, asset.category, asset.name)
        elif asset.stage:
            message = 'created  {} - {} - {} - {} - {}'.format(asset.domain, asset.category, asset.name, asset.stage,
                                                               asset.variant)
        id = defaults._wall_creation_event_
        key = util.id_based_time()
        if asset.name:
            prefs.asset(asset).add_event(key)
        prefs.add_event(key)
        self.event(message, id, key, asset)

    def remove_event(self, asset):
        if asset.category and not asset.name:
            message = 'removed  {} - {}'.format(asset.domain, asset.category)
        elif asset.name and not asset.stage:
            message = 'removed  {} - {} - {}'.format(asset.domain, asset.category, asset.name)
        elif asset.stage:
            message = 'removed  {} - {} - {} - {} - {}'.format(asset.domain, asset.category, asset.name, asset.stage,
                                                               asset.variant)
        id = defaults._wall_remove_event_
        key = util.id_based_time()
        if asset.name:
            prefs.asset(asset).add_event(key)
        prefs.add_event(key)
        self.event(message, id, key, asset)

    def publish_event(self, asset):
        if asset.stage:
            message = 'published  {} - {} - {} - {} - {} | version : {}'.format(asset.domain, asset.category,
                                                                                asset.name, asset.stage, asset.variant,
                                                                                asset.export_version)
        id = defaults._wall_publish_event_
        key = util.id_based_time()
        if asset.name:
            prefs.asset(asset).add_event(key)
        prefs.add_event(key)
        self.event(message, id, key, asset)

    def playblast_event(self, asset):
        if asset.stage:
            message = 'playblasted  {} - {} - {} - {} - {}'.format(asset.domain, asset.category,
                                                                                asset.name, asset.stage, asset.variant)
        id = defaults._wall_playblast_event_
        key = util.id_based_time()
        if asset.name:
            prefs.asset(asset).add_event(key)
        prefs.add_event(key)
        self.event(message, id, key, asset)

    def ticket_event(self, asset, adress):
        if asset.stage:
            message = 'adressed a ticket to {} about  {} - {} - {} - {} - {}'.format(adress, asset.domain, asset.category,
                                                                                asset.name, asset.stage, asset.variant)
        id = defaults._wall_ticket_event_
        key = util.id_based_time()
        if asset.name:
            prefs.asset(asset).add_event(key)
        prefs.add_event(key)
        self.event(message, id, key, asset)

    def close_ticket_event(self, asset, creator):
        if asset.stage:
            message = 'closed a ticket from {} about  {} - {} - {} - {} - {}'.format(creator, asset.domain, asset.category,
                                                                                asset.name, asset.stage, asset.variant)
        id = defaults._wall_close_ticket_event_
        key = util.id_based_time()
        if asset.name:
            prefs.asset(asset).add_event(key)
        prefs.add_event(key)
        self.event(message, id, key, asset)

    def xp_event(self, level):
        message = 'has reached level {} !'.format(str(level))
        id = defaults._wall_xp_event_
        key = util.id_based_time()
        prefs.add_event(key)
        self.event(message, id, key)

    def open_wall_file(self):
        try:
            if self.is_wall():
                settings = util.database().read(2, self.wall)
                return settings
            else:
                logger.warning("Wall file doesn't exist...")

        except:
            logger.error(sys.exc_info()[1])

    def write_wall_file(self, settings, new=0):
        try:
            util.database().write(2, self.wall, settings)
            if not new:
                logger.debug('{} file updated'.format(defaults._wall_))
        except:
            logger.error(sys.exc_info()[1])

    def is_wall(self):
        if self.wall:
            return util.database().isfile(2, self.wall)
        else:
            return None

    def get_user(self, event=None):
        if not event or (type(event) != dict):
            settings = self.open_wall_file()
            events_list = sorted(list(settings.keys()))
            if len(events_list) >= 1:
                key = events_list[-1]
                user = settings[key][defaults._creation_user_key_]
            else:
                user = None
        else:
            user = event[defaults._creation_user_key_]
        return user

    def get_asset(self, event=None):
        if not event or (type(event) != dict):
            settings = self.open_wall_file()
            events_list = sorted(list(settings.keys()))
            if len(events_list) >= 1:
                key = events_list[-1]
                if defaults._asset_key_ in settings[key].keys():
                    asset = settings[key][defaults._asset_key_]
                else:
                    asset = None
            else:
                user = None
        else:
            if defaults._asset_key_ in event.keys():
                asset = event[defaults._asset_key_]
            else:
                asset = None
        return asset

    def get_date(self, event=None):
        if not event or (type(event) != dict):
            settings = self.open_wall_file()
            events_list = sorted(list(settings.keys()))
            if len(events_list) >= 1:
                key = events_list[-1]
                date = settings[key][defaults._creation_date_key_]
            else:
                date = None
        else:
            date = event[defaults._creation_date_key_]
        return date

    def get_id(self, event=None):
        if not event or (type(event) != dict):
            settings = self.open_wall_file()
            events_list = sorted(list(settings.keys()))
            if len(events_list) >= 1:
                key = events_list[-1]
                id = settings[key][defaults._wall_id_key_]
            else:
                id = None
        else:
            id = event[defaults._wall_id_key_]
        return id

    def get_time_id(self, event=None):
        if not event or (type(event) != dict):
            settings = self.open_wall_file()
            events_list = sorted(list(settings.keys()))
            if len(events_list) >= 1:
                key = events_list[-1]
                id = settings[key][defaults._wall_time_id_key_]
            else:
                id = None
        else:
            id = event[defaults._wall_time_id_key_]
        return id

    def get_message(self, event=None):
        if not event or (type(event) != dict):
            settings = self.open_wall_file()
            events_list = sorted(list(settings.keys()))
            if len(events_list) >= 1:
                key = events_list[-1]
                message = settings[key][defaults._message_key_]
            else:
                message = None
        else:
            message = event[defaults._message_key_]
        return message
