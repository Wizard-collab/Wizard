# coding: utf-8

# Default python modules
import os
# Wizard modules
from wizard.project import main as project

def check_category_existence(asset):

    # First read the main project dictionnary
    project_dic = project.read_project()

    # Check the presence in the project dictionnary
    if asset.category in project_dic \
            [asset.domain]:

        # Return the presence
        return 1
    else:
        return 0


def check_name_existence(asset):

    # First read the main project dictionnary
    project_dic = project.read_project()

    # Check the presence in the project dictionnary
    if asset.name in project_dic \
            [asset.domain] \
            [asset.category]:

        # Return the presence
        return 1
    else:
        return 0


def check_stage_existence(asset):

    # First read the main project dictionnary
    project_dic = project.read_project()

    # Check the presence in the project dictionnary
    if asset.stage in project_dic \
            [asset.domain] \
            [asset.category] \
            [asset.name]:

        # Return the presence
        return 1
    else:
        return 0


def check_variant_existence(asset):

    # First read the main project dictionnary
    project_dic = project.read_project()

    # Check the presence in the project dictionnary
    if asset.variant in project_dic \
            [asset.domain] \
            [asset.category] \
            [asset.name] \
            [asset.stage]:

        # Return the presence
        return 1
    else:
        return 0


def check_software_existence(asset):

    # First read the main project dictionnary
    project_dic = project.read_project()

    # Return the requested part existence
    if asset.software in project_dic \
            [asset.domain] \
            [asset.category] \
            [asset.name] \
            [asset.stage] \
            [asset.variant]:

        # Return the presence
        return 1
    else:
        return 0
