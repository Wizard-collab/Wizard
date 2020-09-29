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


def create_logger(name=None):
    
    if sys.argv[-1] == 'DEBUG':
        logging_level = logging.DEBUG
    else:
        logging_level = logging.INFO

    file = defaults._logging_

    file_handler = logging.handlers.WatchedFileHandler(file)
    file_handler.setLevel(logging.DEBUG)
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setLevel(logging.INFO)
    handler_stderr = logging.StreamHandler(sys.stderr)
    handler_stderr.setLevel(logging.ERROR)

    logging.basicConfig(level=logging_level,
        format="%(asctime)s [%(name)-23.23s] [%(levelname)-5.5s] %(message)s")
    
    if name:
        logger = logging.getLogger(name)
    else:
        logger = logging.getLogger()

    logger.addHandler(handler_stderr)
    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)

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
