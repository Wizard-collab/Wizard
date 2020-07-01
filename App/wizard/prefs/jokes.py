# coding: utf-8

'''
This module is used to manage the site preferences of the studio/school

-init_site_prefs
	init the site_prefs if don't exist

-create_user(<user_name>, <password>)
	add a user to all the users of the site

-get_users_list()
	return all the users of the site in a user list

-password_check(<user_name>, <password>)
	check if the given <password> match 
	the user password in the site for this <user>

'''
# Defaults Python modules
import os
from statistics import mean

from wizard.email import main as email
from wizard.prefs.main import prefs
# Wizard tools modules
from wizard.tools import log
from wizard.tools import utility as util
# Wizard variables modules
from wizard.vars import defaults

# Create the main logger
logger = log.pipe_log(__name__)
# Write the pref_path in console (debug level)

prefs = prefs()

class jokes:

    def __init__(self):
        self.database = util.database()
        self.jokes_file = os.path.join(os.environ[defaults._wizard_site_], defaults._jokes_)
        self.read()

    def add_joke(self, joke):
        time_id = util.id_based_time()
        joke_dic = dict()
        joke_dic[defaults._creation_date_key_] = time_id
        joke_dic[defaults._joke_data_] = joke
        joke_dic[defaults._creation_user_key_] = prefs.user
        joke_dic[defaults._note_key_] = 0
        joke_dic[defaults._notes_list_key_] = []
        joke_dic[defaults._users_jury_list_key_] = []
        self.settings[time_id] = joke_dic
        self.write()
        email.send_joke(prefs.user, joke)
        logger.info('Joke successfully added !')
        return time_id

    def get_jokes_list(self):
        jokes_list = list(self.settings.keys())
        jokes_list.sort()
        if jokes_list != []:
            return jokes_list
        else:
            return None

    def get_joke_data(self, id):
        return self.settings[id][defaults._joke_data_]

    def get_joke_note(self, id):
        return self.settings[id][defaults._note_key_]

    def get_joke_user(self, id):
        return self.settings[id][defaults._creation_user_key_]

    def delete_joke(self, id):
        if id in self.get_jokes_list():
            del self.settings[id]
            self.write()
            return 1
        else:
            return 0

    def add_note(self, id, note):
        user = prefs.user
        if user in self.settings[id][defaults._users_jury_list_key_]:
            logger.warning('You already voted for this joke...')
        elif user == self.settings[id][defaults._creation_user_key_]:
            logger.warning("You can't vote for your own joke...")
        else:
            self.settings[id][defaults._notes_list_key_].append(note)
            self.settings[id][defaults._users_jury_list_key_].append(user)
            self.refresh_note(id)

    def refresh_note(self, id):
        notes_list = self.settings[id][defaults._notes_list_key_]
        note = mean(notes_list)
        self.settings[id][defaults._note_key_] = note
        self.write()

    def write(self):
        self.database.write(0, self.jokes_file, self.settings)

    def read(self):
        if self.is_file():
            self.settings = self.database.read(0, self.jokes_file)
        else:
            self.settings = dict()
            self.write()
            logger.debug("Jokes file doesn't exist : {}".format(os.path.abspath(self.jokes_file)))
            return None

    def is_file(self):
        return self.database.isfile(0, self.jokes_file)
