# coding: utf-8

"""This section is for the creation of the project

"""
# Defaults Python modules
import os
import traceback

from wizard.prefs import project as project_prefs
from wizard.prefs.main import prefs
from wizard.project import main as project
from wizard.tools import log
# Wizard modules
from wizard.tools import utility as util
from wizard.vars import defaults

# Creates the main logger
logger = log.pipe_log(__name__)

prefs = prefs()


def create_project(
        project_name,
        path,
        frame_rate,
        format,
        password
):
    """Create a project
    """
    # Build and check the project_path
    project_path = os.path.join(path, project_name) + '/'
    # Check project existence
    projects = prefs.site.projects
    logger.info(projects)
    if not project_name or project_name == '':
        logger.warning('Please enter a project name')
    elif not path or path == '':
        logger.warning('Please enter a project path')
    elif projects and (project_name in projects):
        # Write into the log the warning
        logger.warning('Project "{}" already exists'.format(project_name))
        return 0
    #elif os.path.exists(project_path):
        #logger.warning('Folder "{}" already exists'.format(project_path))
        #return 0
    else:
        # Create the project folder
        try:
            # Add the project to the local prefs
            if os.path.isdir(path):
                if not os.path.exists(project_path):
                    os.makedirs(project_path)
            else:
                logger.error("This directory doesn't exists")
            if os.path.isdir(project_path):
                added_to_prefs = prefs.site.add_project(project_name, project_path, password)
            else:
                logger.error("This directory can't be writed")
                added_to_prefs = 0
            if added_to_prefs:
                prefs.change_project(project_name)
                # Create settings dictionnary
                settings = {}
                settings[defaults._project_name_key_] = project_name
                settings[defaults._frame_rate_key_] = frame_rate
                settings[defaults._format_key_] = format
                settings[defaults._creation_date_key_] = util.get_time()
                settings[defaults._creation_user_key_] = prefs.user
                settings[defaults._server_ip_] = None 
                # Update the current project
                # on the project_pref script
                project_prefs.get_current_project_prefs_file()
                # Write the project prefs file
                project_prefs.init_prefs(settings)
                project.create_tree_file()
                # Write into the log the info
                logger.info('Project "{}" created'.format(project_name))
                return 1
        except PermissionError:
            logger.warning("You don't have the permission to write here : {}".format(project_path))
            return 0
        except:
            logger.error(str(traceback.format_exc()))
            return 0
