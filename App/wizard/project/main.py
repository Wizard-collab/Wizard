# coding: utf-8

'''This module is used to manage the current project
It permits to write the main "asset" tree file ( located at project's root),
and get it

'''

# Defaults Python modules
import os

from wizard.prefs.main import prefs
# Wizard modules
from wizard.tools import log
from wizard.tools import utility as util
from wizard.vars import defaults
#from wizard.asset import main as asset_core

# Creates the main logger
logger = log.pipe_log(__name__)

prefs = prefs()

def read_project():
    project_tree = get_project_tree()
    project_folder = get_project_folder()
    if util.database().isfile(2, project_tree):
        project = util.database().read(2, project_tree)
        return project
    elif not util.database().isfile(2, project_tree) and \
            os.path.isdir(project_folder):
        check_tree_file()
        logger.debug('asset.wd file does not exists at {}, building it...'.format(project_folder))
        return {}


def write_project(project):
    project_tree = get_project_tree()
    util.database().write(2, project_tree, project)
    project_folder = get_project_folder()
    logger.debug('asset.wd file updated at {}'.format(project_folder))
    return project_folder


def get_project_tree():
    if get_project_folder():
        project_tree = os.path.join(get_project_folder(), defaults._tree_)
        return project_tree
    else:
        return 0


def get_project_folder():
    if prefs.project_path:
        return prefs.project_path
    else:
        return 0


def create_tree_file():
    check_tree_file()


def add_set_dress():
    project = read_project()
    if defaults._set_dress_ not in project[defaults._assets_].keys():
        project[defaults._assets_][defaults._set_dress_] = dict()
        write_project(project)

def add_fx_setup():
    project = read_project()
    if defaults._fx_setup_ not in project[defaults._library_].keys():
        project[defaults._library_][defaults._fx_setup_] = dict()
        write_project(project)

def add_material():
    project = read_project()
    if defaults._material_ not in project[defaults._library_].keys():
        project[defaults._library_][defaults._material_] = dict()

        material_pub_ext_dic = defaults._pub_ext_dic_[defaults._material_]
        texturing_designer_pub_ext_dic = defaults._pub_ext_dic_[defaults._texturing_][defaults._designer_]
        custom_publish_dic = prefs.custom_pub_ext_dic
        custom_publish_dic[defaults._material_] = material_pub_ext_dic
        custom_publish_dic[defaults._texturing_][defaults._designer_] = texturing_designer_pub_ext_dic
        prefs.set_custom_pub_ext_dic(custom_publish_dic)

        write_project(project)

def add_painter_template():
    project = read_project()
    if defaults._painter_template_ not in project[defaults._library_].keys():
        project[defaults._library_][defaults._painter_template_] = dict()

        painter_template_pub_ext_dic = defaults._pub_ext_dic_[defaults._painter_template_]
        painter_template_pub_ext = defaults._pub_ext_dic_[defaults._painter_template_][defaults._painter_]
        custom_publish_dic = prefs.custom_pub_ext_dic
        custom_publish_dic[defaults._painter_template_] = painter_template_pub_ext_dic
        custom_publish_dic[defaults._painter_template_][defaults._painter_] = painter_template_pub_ext
        prefs.set_custom_pub_ext_dic(custom_publish_dic)

        write_project(project)

def check_tree_file():
    project_tree = get_project_tree()
    if project_tree and not util.database().isfile(2, project_tree):
        # Build base assets dictionnary
        project = dict()
        project[defaults._assets_] = dict()
        project[defaults._sequences_] = dict()
        project[defaults._library_] = dict()
        project[defaults._editing_] = dict()
        project[defaults._assets_][defaults._characters_] = dict()
        project[defaults._assets_][defaults._props_] = dict()
        project[defaults._assets_][defaults._sets_] = dict()
        project[defaults._assets_][defaults._set_dress_] = dict()
        project[defaults._assets_][defaults._vehicles_] = dict()
        for lib in defaults._lib_categories_list_:
            project[defaults._library_][lib] = dict()
        for edit in defaults._editing_categories_list_:
            project[defaults._editing_][edit] = dict()
        # Write the file to the project path
        write_project(project)
        logger.debug('asset.wd file created at {}'.format(get_project_folder()))
        return project
    else:
        return 1

def get_all_assets():
    project_dic = read_project()
    assets_list = []

    for domain in project_dic.keys():
        for category in project_dic[domain].keys():
            for name in project_dic[domain][category].keys():
                for stage in project_dic[domain][category][name].keys():
                    asset = asset_core.asset(domain=domain, category=category, name=name, stage=stage)
                    assets_list.append(asset)

    return assets_list
