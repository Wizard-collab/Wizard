

# coding: utf-8

# Basic python modules
import os
import shutil

# Wizard modules
from wizard.tools import log
from wizard.tools import utility as util
from wizard.project import main as project
from wizard.prefs.main import prefs
from wizard.asset import checker
from wizard.asset.folder import folder
from wizard.vars import defaults
from wizard.project.wall import wall
from wizard.nodes import core as nodes

# Creating the main logger
logger = log.pipe_log(__name__)

prefs = prefs()

def create_category(asset):

    # Creates a new category with an "asset" object in arg
    # First read the project dictionnary
    project_dic = project.read_project()

    # Check if category doesn't exists
    # Using the wizard "checker" module
    if not checker.check_category_existence(asset):

        # Add the category to the project dictionnary
        project_dic \
            [asset.domain] \
            [asset.category] = {}

        # Write the project dictionnary to the tree.wd
        project.write_project(project_dic)

        # Build the folders
        create_folders(asset)

        # Init the asset category prefs
        prefs.asset(asset).category.write()

        # Log the success to user
        logger.debug('Sequence {} added to asset.wd'.format(asset.category))
        logger.info('{} created'.format(asset.category))

        # Emit the event with the "wall" module ( from wizard )
        wall().create_event(asset)

        # Return the success
        return 1
    else:

        # Return the fail and log it to the user
        logger.warning('{} already exists'.format(asset.category))
        return 0

def remove_category(asset):

    # Creates a new category with an "asset" object in arg
    # First read the project dictionnary
    project_dic = project.read_project()

    # Check if category doesn't exists
    if checker.check_category_existence(asset):

        # Add the category to the project dictionnary
        del project_dic \
            [asset.domain] \
            [asset.category]

        # write the project file
        project.write_project(project_dic)

        # Return the success
        return 1
    else:

        # Return the fail
        return 0


def create_name(asset, in_out=None):

    # Creates a new name with an "asset" object in arg
    # First read the project dictionnary
    project_dic = project.read_project()
    
    # Check special characters
    if not util.check_illegal(asset.name):

        # Return the fail and log the problem to the user
        logger.warning('{} contains illegal characters'.format(asset.name))
        return 0

    else:

        # Check if category exists
        # Check if name doesn't exists
        if checker.check_category_existence(asset):
            if not checker.check_name_existence(asset):

                # Add the name to the project dictionnary
                project_dic \
                    [asset.domain] \
                    [asset.category] \
                    [asset.name] = {}

                # Write the project dictionnary to the tree.wd
                project.write_project(project_dic)

                # Build the folders
                create_folders(asset)

                # Init the asset name prefs
                prefs.asset(asset).name.write(in_out)

                # Log the success to user
                logger.debug('Asset {} added to asset.wd'.format(asset.name))
                logger.info('{} created'.format(asset.name))


                # Create the wall event
                wall().create_event(asset)

                # Return the success
                return 1
            else:

                # Return the fail and log it to the user
                logger.warning('{} already exists'.format(asset.name))
                return 0
        else:
            logger.warning("{} doesn't exists".format(asset.category))
            return 0

def remove_name(asset):

    # Creates a new name with an "asset" object in arg
    # First read the project dictionnary
    project_dic = project.read_project()

    # Check if category exists
    # Check if name doesn't exists
    if checker.check_category_existence(asset) and \
            checker.check_name_existence(asset):

        # Add the name to the project dictionnary
        del project_dic \
            [asset.domain] \
            [asset.category] \
            [asset.name]

        # Write the project dictionnary to the tree.wd
        # Only if the folder suppression succeed
        if delete_folder(asset):
            project.write_project(project_dic)

            # Create the "wall" event using the wizard "wall" module
            wall().remove_event(asset)

            # Return the success to the user
            return 1

        else:

            # Return the fail
            return 0
    else:

        # Return the fail and log it to the user
        logger.warning('{} already exists'.format(asset.name))
        return 0


def create_stage(asset):

    # Creates a new stage with an "asset" object in arg
    # First read the project dictionnary
    project_dic = project.read_project()

    # Check if category and name exists
    # Check if stage doesn't exists
    if checker.check_category_existence(asset):
        if checker.check_name_existence(asset):
            if not checker.check_stage_existence(asset):

                # Add the stage to the project dictionnary
                project_dic[asset.domain] \
                    [asset.category] \
                    [asset.name] \
                    [asset.stage] = {}

                # Write the project dictionnary to the tree.wd
                project.write_project(project_dic)

                # Build the folders
                create_folders(asset)

                # Init the asset stage prefs
                prefs.asset(asset).stage.write()


                # Return and log the success to user
                logger.debug('Stage {} added to asset.wd'.format(asset.stage))
                return 1
            else:

                # Return and log the fail to the user
                logger.warning('{} - {} already exists'.format(asset.name, asset.stage))
                return 0
        else:
            logger.warning("{} doesn't exists".format(asset.name))
            return 0
    else:
        logger.warning("{} doesn't exists".format(asset.category))
        return 0

def remove_stage(asset):

    # Creates a new stage with an "asset" object in arg
    # First read the project dictionnary
    project_dic = project.read_project()

    # Check if category and name exists
    # Check if stage doesn't exists
    if checker.check_category_existence(asset) and \
            checker.check_name_existence(asset) and \
            checker.check_stage_existence(asset):

        # Remove the stage from the project dictionnary
        del project_dic[asset.domain] \
            [asset.category] \
            [asset.name] \
            [asset.stage]

        # Write the project dictionnary to the tree.wd
        project.write_project(project_dic)

        # Return the success
        return 1
    else:

        # Return the fail and log it to the user
        logger.warning('{} - {} already exists'.format(asset.name, asset.stage))
        return 0


def create_variant(asset):

    # Creates a new variant with an "asset" object in arg
    # First read the project dictionnary
    project_dic = project.read_project()

    # Check if category, name, stage exists
    # Check if variant doesn't exists
    if checker.check_category_existence(asset):
        if checker.check_name_existence(asset):
            if checker.check_stage_existence(asset):
                if not checker.check_variant_existence(asset):

                    # Add the variant to the project dictionnary
                    project_dic[asset.domain] \
                        [asset.category] \
                        [asset.name] \
                        [asset.stage] \
                        [asset.variant] = {}

                    # Add an ID for the variant
                    id = nodes.asset_to_id(asset)
                    project_dic[asset.domain] \
                        [asset.category] \
                        [asset.name] \
                        [asset.stage] \
                        [asset.variant] \
                        [defaults._asset_id_key_] = id

                    # Write the project dictionnary to the tree.wd
                    project.write_project(project_dic)

                    # Build the folders
                    create_folders(asset)

                    # Init the asset variant prefs
                    prefs.asset(asset).variant.write()

                    # Add the variant to the stage prefs
                    prefs.asset(asset).stage.add_variant()

                    # Create the softwares prefs and folders, childs of variant
                    create_softwares(asset)
                    create_export_root(asset)
                    create_playblast(asset)

                    # Log the success to user
                    logger.info('{} - {} - {} created'.format(asset.name,
                                                              asset.stage,
                                                              asset.variant))

                    # Create the wall event with the "wall" wizard module
                    wall().create_event(asset)

                    # Return the success
                    return 1
                else:

                    # Return the fail and log it to the user
                    logger.warning('{} - {} - {} already exists'.format(asset.name,
                                                                        asset.stage,
                                                                        asset.variant))
                    return 0
            else:
                logger.warning("{} doesn't exists".format(asset.stage))
                return 0
        else:
            logger.warning("{} doesn't exists".format(asset.name))
            return 0
    else:
        logger.warning("{} doesn't exists".format(asset.category))
        return 0


def create_softwares(asset):

    # Creates a new software with an "asset" object in arg
    # First read the project dictionnary
    project_dic = project.read_project()

    # Check if category, name, stage and variant exists
    if checker.check_category_existence(asset) and \
            checker.check_name_existence(asset) and \
            checker.check_stage_existence(asset) and \
            checker.check_variant_existence(asset):

        # Loop, add every softwares of the concerned stage
        for software in prefs.asset(asset).stage.softwares:

            # Assign the software from the loop to the "asset" object
            asset.software = software

            # Check if this software doesn't already exists
            if not checker.check_software_existence(asset):

                # Add the software to the project dictionnary
                project_dic[asset.domain] \
                    [asset.category] \
                    [asset.name] \
                    [asset.stage] \
                    [asset.variant] \
                    [asset.software] = {}

                # Write the project dictionnary to the tree.wd
                project.write_project(project_dic)

                # Build the folders
                create_software_folder(asset)

                # Init the asset software prefs
                prefs.asset(asset).software.write()

                # Log the success to user
                logger.debug('Software {} added to asset.wd'.format(software))

def create_export_root(asset):

    # First read the project dictionnary
    project_dic = project.read_project()

    # Check if category, name, stage and variant exists
    if checker.check_category_existence(asset) and \
            checker.check_name_existence(asset) and \
            checker.check_stage_existence(asset) and \
            checker.check_variant_existence(asset):

        # Create the folder tree and return the path
        path = create_export_root_folder(asset)

        # Create the prefs file with the wizard "prefs" module
        prefs.asset(asset).export_root.write()

        # Log the success to user
        # And return the path
        logger.info('Export root folder created')
        return path

def create_export(asset, version = None):

    # First read the project dictionnary
    project_dic = project.read_project()

    # Check if category, name, stage and variant exists
    if checker.check_category_existence(asset) and \
            checker.check_name_existence(asset) and \
            checker.check_stage_existence(asset) and \
            checker.check_variant_existence(asset):

        # Create the folder tree and get the path
        path = create_export_folder(asset, version)

        # Init the asset software prefs
        # Use the wizard "prefs" module
        if version:
            asset.export_version = version
        prefs.asset(asset).export.write()

        # If a version was specified, add it to the prefs file
        if version:
            prefs.asset(asset).export.new_version(version)

        # Log the success to user
        # And return the folder path
        logger.info('Export folder created')
        return path

def create_playblast(asset):

    # First read the project dictionnary
    project_dic = project.read_project()

    # Check if category, name, stage and variant exists
    if checker.check_category_existence(asset) and \
            checker.check_name_existence(asset) and \
            checker.check_stage_existence(asset) and \
            checker.check_variant_existence(asset):

        # Get the playblast folder path
        path = folder(asset).playblast()

        # Create the folder tree if it doesn't exists
        if not os.path.isdir(path):
            os.makedirs(path)

            # Log it to the user
            logger.info('Playblast folder created')

        # Init the asset software prefs using the wizard "prefs" module
        prefs.asset(asset).playblast.write()

        # Return the path
        return path

def create_folders(asset):

    # Create the folders from the "asset" object
    # For each part of the asset, check if the part is 
    # assigned and create the concerned folders
    if asset.domain and\
            not folder(asset).is_domain():
        os.mkdir(folder(asset).domain)
    if asset.category and\
            not folder(asset).is_category():
        os.mkdir(folder(asset).category)
    if asset.name and\
            not folder(asset).is_name():
        os.mkdir(folder(asset).name)
    if asset.stage and\
            not folder(asset).is_stage():
        os.mkdir(folder(asset).stage)
    if asset.variant and\
            not folder(asset).is_variant():
        os.mkdir(folder(asset).variant)

def delete_folder(asset):

    # Check if the folder exists
    if asset.name and folder(asset).is_name():

        # Get the source folder ( from the pipe tree )
        # Use the "folder" wizard module
        source = folder(asset).name

        # Get the destination archive folder using the "prefs" wizard module
        destination = folder(asset).trash

        # Check if the default archives folder exists
        # Using the project variable ( from the asset object )
        # And the "defaults" wizard module
        if not os.path.isdir(os.path.join(asset.project, defaults._trash_folder_)):

            # Create the archive folder
            os.mkdir(os.path.join(asset.project, defaults._trash_folder_))

        # Create the .zip archive file ( name with the python "time" module)
        # And using the "utility" wizard module
        util.zip_folder(destination, source)

        # Remove the the source tree ( from the pipeline folder's tree)
        shutil.rmtree(source)

        # Return the success
        return 1

    else:

        # Return the fail
        return 0

def create_software_folder(asset):

    # Check if the asset object as a software assigned
    # And check if the concerned folder doesn't exists
    if asset.software and\
            not folder(asset).is_software():

        # Create the folder using the "os" python module
        # And using the "folder" wizard module
        os.mkdir(folder(asset).software)

def create_export_root_folder(asset):

    # Check if the asset object as a variant assigned
    # And check if the concerned folder doesn't exists
    if asset.variant:
        path = folder(asset).export_root()

        # Create the folder using the "os" python module
        os.mkdir(path)

        # Return the path
        return path

def create_export_folder(asset, version = None):

    # Check if the asset object as a variant assigned
    # Check if the asset object as an expoet_asset assigned
    # And check if the concerned folder doesn't exists
    # Usign the "folder" wizard module
    if asset.variant and asset.export_asset and\
            not folder(asset).is_export(version):

        # Get the path using the "folder" wizard module
        path = folder(asset).export(version)

        # Create the folder tree using the "os" pytohn module
        os.mkdir(path)

        # Return the path
        return path
        