import sys
import os

# pip modules
import watchdog
#import mss
import pyautogui
import pyperclip

import yaml

import fix_qt
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import pyqtSignal

import wizard.vars.defaults as defaults

# building local environment
site_path = os.path.join(os.environ[defaults._wizard_site_], defaults._site_)
stats_path = os.path.join(os.environ[defaults._wizard_site_], defaults._stats_)

os.environ[defaults._site_var_] = site_path
os.environ[defaults._abs_site_path_] = os.path.abspath('')
os.environ[defaults._stats_var_] = stats_path

# wizard modules
from wizard.asset import main
from wizard.asset import builder
from wizard.asset import checker
from wizard.asset import folder
from wizard.asset import reference

from wizard.chat import client
from wizard.chat import send
from wizard.chat import shared_files

from wizard.email import main
from wizard.email import verification

from wizard.nodes import core
from wizard.nodes import main

from wizard.prefs import asset
from wizard.prefs import jokes
from wizard.prefs import main
from wizard.prefs import production
from wizard.prefs import project
from wizard.prefs import site
from wizard.prefs import software
from wizard.prefs import stats
from wizard.prefs import stats_maker
from wizard.prefs import user
from wizard.prefs import user_events

from wizard.project import chat_archives
from wizard.project import create
from wizard.project import main
from wizard.project import wall

from wizard.site import main

from wizard.software import main

from wizard.tools import build_g_conf
from wizard.tools import convert_playblast
from wizard.tools import create_video
from wizard.tools import log
from wizard.tools import maketx
from wizard.tools import password
from wizard.tools import playblast
from wizard.tools import utility

from wizard.prefs import user_scripts

user_scripts.user_scripts()

from wizard import api

try:
	file = sys.argv[1]
	exec(open(file).read())
except IndexError:
	import code
	console = code.InteractiveConsole()
	console.interact(banner=None, exitmsg=None)