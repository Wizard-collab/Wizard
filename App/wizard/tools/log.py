# coding: utf-8
# Defaults Python modules
import logging
import logging.handlers
import sys
import os
# Wizard variables modules
from wizard.vars import defaults

'''This moddule concern the main logger
used in all the scripts. 
It build a basic python logger and windows popups 
using win10toast module

'''


def create_logger(name=None, server=None):
    if name:
        logger = logging.getLogger(name)
    else:
        logger = logging.getLogger()
    if server:
        file = defaults._server_logging_
    else:
        file = defaults._logging_
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(name)-23.23s] [%(levelname)-5.5s] %(message)s",
        handlers=[
            logging.handlers.WatchedFileHandler(file),
            logging.StreamHandler(sys.stdout)
        ])
    handler_stderr = logging.StreamHandler(sys.stderr)
    handler_stderr.setLevel(logging.ERROR)
    logger.addHandler(handler_stderr)
    return (logger)


class pipe_log():
    def __init__(self, name=None):
        if not os.path.isdir(defaults._log_path_):
            os.makedirs(defaults._log_path_)
        if name:
            self.main_logger = create_logger(name)
        else:
            self.main_logger = create_logger()

    def info(self, message):
        self.main_logger.info(message)

    def warning(self, message):
        self.main_logger.warning(message)

    def error(self, message):
        self.main_logger.error(message)

    def debug(self, message):
        self.main_logger.debug(message)

    def critical(self, message):
        self.main_logger.critical(message)


class server_log():
    def __init__(self, name=None):
        if not os.path.isdir(defaults._log_path_):
            os.makedirs(defaults._log_path_)
        if name:
            self.main_logger = create_logger(name, server=1)
        else:
            self.main_logger = create_logger(server=1)

    def info(self, message):
        self.main_logger.info(message)

    def warning(self, message):
        self.main_logger.warning(message)

    def error(self, message):
        self.main_logger.error(message)

    def debug(self, message):
        self.main_logger.debug(message)

    def critical(self, message):
        self.main_logger.critical(message)
