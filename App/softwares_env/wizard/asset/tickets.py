from wizard.prefs.main import prefs
from wizard.vars import defaults
from wizard.tools import log
from wizard.tools import utility as utils
from wizard.project.wall import wall
import traceback
from wizard.asset import main as asset_core
import os

logger = log.pipe_log(__name__)

prefs = prefs()

class tickets():
    def __init__(self):
        self.tickets_file = self.get_ticket_file()
        self.open()

    def get_ticket_file(self):

        ticket_path = prefs.project_path
        tickets_file = os.path.join(ticket_path, defaults._tickets_)

        return tickets_file

    def create_tickets_file(self):

        self.settings = dict()
        self.settings[defaults._assets_tickets_] = dict()
        self.settings[defaults._user_tickets_] = dict()
        self.settings[defaults._adress_tickets_] = dict()
        self.settings[defaults._all_tickets_] = dict()

        self.write()

    def create_ticket(self, asset, message, adress):
        string_asset = utils.variant_asset_to_string(asset)
        user = prefs.user
        date = utils.get_gmtime()
        ticket_dic = dict()
        ticket_dic[defaults._creation_user_key_] = user
        ticket_dic[defaults._creation_date_key_] = date
        ticket_dic[defaults._asset_key_] = string_asset
        ticket_dic[defaults._message_key_] = message
        ticket_dic[defaults._ticket_state_] = defaults._ticket_open_
        ticket_dic[defaults._ticket_adress_] = adress
        ticket_dic[defaults._close_date_] = None
        ticket_dic[defaults._ticket_comment_] = None
        ticket_dic[defaults._ticket_close_user_] = None
        key = utils.id_based_time()

        self.settings[defaults._all_tickets_][key] = ticket_dic

        if string_asset not in self.settings[defaults._assets_tickets_].keys():
            self.settings[defaults._assets_tickets_][string_asset] = []
        self.settings[defaults._assets_tickets_][string_asset].append(key)

        if user not in self.settings[defaults._user_tickets_].keys():
            self.settings[defaults._user_tickets_][user] = []
        self.settings[defaults._user_tickets_][user].append(key)

        if adress not in self.settings[defaults._adress_tickets_].keys():
            self.settings[defaults._adress_tickets_][adress] = []
        self.settings[defaults._adress_tickets_][adress].append(key)
        self.write()
        wall().ticket_event(asset, adress)

    def get_asset_tickets_ids(self, asset):
        string_asset = utils.variant_asset_to_string(asset)
        if string_asset in self.settings[defaults._assets_tickets_].keys():
            tickets_keys = self.settings[defaults._assets_tickets_][string_asset]
        else:
            tickets_keys = []
        return tickets_keys

    def get_user_tickets_ids(self):
        user = prefs.user
        if user in self.settings[defaults._adress_tickets_].keys():
            tickets_keys = self.settings[defaults._adress_tickets_][user]
        else:
            tickets_keys = []
        return tickets_keys

    def delete_ticket(self, key):
        if key in self.settings[defaults._all_tickets_].keys():
            del self.settings[defaults._all_tickets_][key]
        for asset in list(self.settings[defaults._assets_tickets_].keys()):
            if key in self.settings[defaults._assets_tickets_][asset]:
                self.settings[defaults._assets_tickets_][asset].remove(key)
        for adress in list(self.settings[defaults._adress_tickets_].keys()):
            if key in self.settings[defaults._adress_tickets_][adress]:
                self.settings[defaults._adress_tickets_][adress].remove(key)
        for user in list(self.settings[defaults._user_tickets_].keys()):
            if key in self.settings[defaults._user_tickets_][user]:
                self.settings[defaults._user_tickets_][user].remove(key)
        self.write()
        logger.info('Ticket deleted')

    def close_ticket(self, key, comment = 'Problem solved'):
        date = utils.get_gmtime()
        self.settings[defaults._all_tickets_][key][defaults._ticket_state_] = defaults._ticket_close_
        self.settings[defaults._all_tickets_][key][defaults._close_date_] = date
        self.settings[defaults._all_tickets_][key][defaults._ticket_comment_] = comment
        self.settings[defaults._all_tickets_][key][defaults._ticket_close_user_] = prefs.user
        self.write()
        asset = asset_core.string_to_asset(self.settings[defaults._all_tickets_][key][defaults._asset_key_])
        creator = self.settings[defaults._all_tickets_][key][defaults._creation_user_key_]
        wall().close_ticket_event(asset, creator)
        logger.info('Ticket closed')

    def open_ticket(self, key):
        self.settings[defaults._all_tickets_][key][defaults._ticket_state_] = defaults._ticket_open_
        self.settings[defaults._all_tickets_][key][defaults._close_date_] = None
        self.settings[defaults._all_tickets_][key][defaults._ticket_close_user_] = None
        self.write()
        asset = asset_core.string_to_asset(self.settings[defaults._all_tickets_][key][defaults._asset_key_])
        creator = self.settings[defaults._all_tickets_][key][defaults._creation_user_key_]
        wall().ticket_event(asset, creator)
        logger.info('Ticket openned')

    def get_ticket_user(self, key):
        try:
            return self.settings[defaults._all_tickets_][key][defaults._creation_user_key_]
        except:
            logger.critical(str(traceback.format_exc()))

    def get_ticket_adress(self, key):
        try:
            return self.settings[defaults._all_tickets_][key][defaults._ticket_adress_]
        except:
            logger.critical(str(traceback.format_exc()))

    def get_ticket_comment(self, key):
        try:
            return self.settings[defaults._all_tickets_][key][defaults._ticket_comment_]
        except:
            logger.critical(str(traceback.format_exc()))

    def get_ticket_date(self, key):
        try:
            return self.settings[defaults._all_tickets_][key][defaults._creation_date_key_]
        except:
            logger.critical(str(traceback.format_exc()))

    def get_ticket_state(self, key):
        try:
            return self.settings[defaults._all_tickets_][key][defaults._ticket_state_]
        except:
            logger.critical(str(traceback.format_exc()))

    def get_ticket_message(self, key):
        try:
            return self.settings[defaults._all_tickets_][key][defaults._message_key_]
        except:
            logger.critical(str(traceback.format_exc()))

    def get_ticket_close_date(self, key):
        try:
            return self.settings[defaults._all_tickets_][key][defaults._close_date_]
        except:
            logger.critical(str(traceback.format_exc()))

    def get_ticket_close_user(self, key):
        try:
            return self.settings[defaults._all_tickets_][key][defaults._ticket_close_user_]
        except:
            logger.critical(str(traceback.format_exc()))

    def write(self):
        try:
            utils.database().write(0, self.tickets_file, self.settings)
        except:
            logger.critical(str(traceback.format_exc()))

    def open(self):
        try:
            if not os.path.isfile(self.tickets_file):
                self.create_tickets_file()
            else:
                self.settings = utils.database().read(0, self.tickets_file)
        except:
            logger.critical(str(traceback.format_exc()))


