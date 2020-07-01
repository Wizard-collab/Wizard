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
import traceback
import time

# Create the main logger
logger = log.pipe_log(__name__)

prefs = prefs()

class archives:

    def __init__(self):

        if prefs.project_path:
            self.chat = os.path.join(prefs.project_path, defaults._chat_)
            if not self.is_archives():
                # Create settings dictionnary
                self.history = dict()
                # Write the .manager file as YAML with setting dict
                logger.info('{} file created'.format(defaults._chat_))
                self.write_chat_file(new=1)
            else:
                self.read_chat_file()
        else:
            self.chat = None

        self.dump_count = 0
        self.dump_breakpoint = 3


    def is_archives(self):
        if self.chat:
            return util.database().isfile(2, self.chat)
        else:
            return None

    def write_chat_file(self, new=0):
        try:
            util.database().write(2, self.chat, self.history)
            self.dump_count = 0
            if not new:
                logger.debug('{} file updated'.format(defaults._chat_))
        except:
            logger.error(sys.exc_info()[1])

    def read_chat_file(self):
        try:
            if self.is_archives():
                self.history = util.database().read(2, self.chat)
            else:
                logger.warning("Chat file doesn't exist...")

        except:
            logger.error(sys.exc_info()[1])

    def add_message(self, message_dic):
        key = util.id_based_time()
        try:
            self.history[key] = message_dic
            self.dump_count +=1
            if self.dump_count >= self.dump_breakpoint:
                self.write_chat_file()
        except:
            logger.critical(str(traceback.format_exc()))
            