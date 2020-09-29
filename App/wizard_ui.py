"""
Created on 2019

This module is the main module for the wizard ui
It uses the wizard pipeline API and wrap it to the ui

It contains the class:
    - Main_application

@author : Leo BRUNEL

"""

# coding: utf-8

# python modules
import sys
import os
import fix_qt

# external modules
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer

# wizard modules
import wizard.vars.defaults as defaults
from wizard.tools import utility as utils

# building local environment
main_site_path = utils.database().read(0, os.path.join(defaults._user_path_, 'site.wd'))
site_path = os.path.join(main_site_path, defaults._site_)
stats_path = os.path.join(main_site_path, defaults._stats_)

os.environ[defaults._wizard_site_] = main_site_path
os.environ[defaults._site_var_] = site_path
os.environ[defaults._abs_site_path_] = os.path.abspath('')
os.environ[defaults._stats_var_] = stats_path
os.environ[defaults._project_db_env_] = ''
os.environ[defaults._current_assets_list_] = ''


# wizard modules
from wizard.prefs import project as project_prefs
import gui.build as build
from wizard.tools import log
from wizard.prefs.main import prefs
import ui_main
import ui_load
import ui_welcome
import ui_wizard_desktop
import time
import sys

#from wizard.prefs import version
import dialog_new_version

# connect to the main logger
logger = log.pipe_log(__name__)


class Main_application():
    '''
	The application is created here.
	All the processes will depends of this function.
	'''

    def __init__(self):

        # Create the pyqt5 application
        self.app = QtWidgets.QApplication(sys.argv)
        

        # Add the default wizard icon
        self.app.setWindowIcon(QtGui.QIcon(defaults._wizard_ico_))

        # Call the introduction widget
        # This widget is used to help the users in the using of Wizard
        self.ui_welcome = ui_welcome.Main()

        

        # Define the "run" variable
        # it will permit to block the process in a case of exception
        run = 1

        # Check if we need this widget before launching wizard main ui
        # Needed if no user is logged
        # no project is logged 
        # or no server is launched
        if self.ui_welcome.need:

            # Check if the widget call was successful
            if not build.launch_dialog_as_child_frameless_trans(self.ui_welcome):

                # If not stop the process
                run = 0
        
        # If the variable "run" is not 0 or None, continue the process
        if run:

            run= 0

            '''
            try:
                new_version = version.check_version().check_version()
            except:
            '''
            new_version = None
                
            if new_version and prefs().show_new_version:
                self.dialog_new_version = dialog_new_version.Main(new_version)
                if build.launch_dialog_as_child(self.dialog_new_version):
                    pass
                else:
                    run = 1
            else:
                run = 1

            if run :
                # Call the loading ui
                self.ui_load = ui_load.Main()

                # Launch the loading ui with the module "gui.build"
                build.launch_normal_as_child_frameless_no_transparent(self.ui_load)

                # When the ui is showed, start the wizard introduction gif
                #self.ui_load.start_gif()

                # Wait for the wizard introduction gif to end
                #while not self.ui_load.go :

                    # Refresh the ui while the wizard gif is running
                QApplication.processEvents()

                self.prefs = prefs()

                # Fake some loadings
                # Need to remove that
                self.ui_load.ui.loading_user_label.setText('User : {}'.format(self.prefs.user))
                self.ui_load.ui.loading_project_label.setText('Project : {}'.format(self.prefs.project_name))
                self.update_loading_infos('Reading project...', 65)

                # Call the main ui but don't launch it - This function is the longest to run
                self.ui_main = ui_main.Main()

                self.update_loading_infos('Launching main ui...', 85)
                self.update_loading_infos('Launching main ui...', 90)
                self.update_loading_infos('Launching main ui...', 100)

                # Close the loading ui
                self.ui_load.close()

                # Call the desktop shutter and give it the main ui object
                shutter = prefs.shutter
                if shutter:
                    self.wizard_desktop = ui_wizard_desktop.wizard_desktop(self.ui_main)

                # Show the main ui with the "build" module (from wizard)
                build.launch_stray_as_child(self.ui_main, self.app, title=f'Wizard - Project : {self.prefs.project_name}')

                # Refresh the main ui
                self.ui_main.asset_item_changed()

                # Show the wizard desktop tray icon with the "build" module ( from wizard )
                if shutter:
                    build.launch_wizard_desktop(self.wizard_desktop)


    def update_loading_infos(self, text, percent):
        '''
		This function update the loading ui
		'''

        # Refresh the application
        QApplication.processEvents()

        # Change the text in the loading ui
        self.ui_load.ui.loading_label.setText(text)

        # Change the percent in the loading ui
        self.ui_load.ui.loading_progressBar.setValue(percent)

        # Refresh the application
        QApplication.processEvents()

if __name__ == '__main__':
    main_app = Main_application()
