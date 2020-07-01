# coding: utf-8

# Default python modules
import os
# Wizard modules
from wizard.vars import defaults
from wizard.tools import utility as util
from wizard.prefs import project as project_prefs
from wizard.tools import log

# Creates the main logger
logger = log.pipe_log()

class folder():

    # Init the class
    # Need an "asset" object argument
    def __init__(self, asset):
        self.asset = asset

    @property
    def domain(self):

        # Check if the requested asset variable is assigned to the "asset" object
        if self.asset.domain:

            # Build the path and return it
            path = os.path.join(
                self.asset.project,
                self.asset.domain)

            return path
        else:
            return 0

    def is_domain(self):
        return os.path.isdir(self.domain)

    @property
    def category(self):
        # Check if the requested asset variable is assigned to the "asset" object
        if self.asset.category:

            # Build the path and return it
            path = os.path.join(
                self.asset.project,
                self.asset.domain,
                self.asset.category)

            return path
        else:
            return 0

    def is_category(self):
        return os.path.isdir(self.category)

    @property
    def name(self):
        # Check if the requested asset variable is assigned to the "asset" object
        if self.asset.name:

            # Build the path and return it
            path = os.path.join(
                self.asset.project,
                self.asset.domain,
                self.asset.category,
                self.asset.name)

            return path
        else:
            return 0

    def is_name(self):

        # Check if the path exists using the folder module "name" property
        # And using the "os" pytohn module
        return os.path.isdir(self.name)

    @property
    def trash(self):

        # Get the archive ".zip" file using the project_path
        # And using the "os" python module
        # And usign the "defaults" wizard module
        # And using the "utility" wizard module to get the name of the file ( based on the "time" python module )
        trash_file = os.path.join(self.asset.project, defaults._trash_folder_, util.id_based_time()+'.zip')

        # Return the file
        return trash_file

    @property
    def stage(self):

        # Check if the requested asset variable is assigned to the "asset" object
        if self.asset.stage:

            # Build the path and return it
            path = os.path.join(
                self.asset.project,
                self.asset.domain,
                self.asset.category,
                self.asset.name,
                self.asset.stage)
            return path
        else:
            return 0

    def is_stage(self):
        return os.path.isdir(self.stage)

    @property
    def variant(self):

        # Check if the requested asset variable is assigned to the "asset" object
        if self.asset.variant:

            # Build the path and return it
            path = os.path.join(
                self.asset.project,
                self.asset.domain,
                self.asset.category,
                self.asset.name,
                self.asset.stage,
                self.asset.variant)
            return path
        else:
            return 0

    def is_variant(self):
        return os.path.isdir(self.variant)

    def export_root(self):

        # Check if a "variant" asset variable is assigned to the "asset" object and not None
        if self.asset.variant:

            # Build the path and return it
            path = os.path.join(
                self.asset.project,
                self.asset.domain,
                self.asset.category,
                self.asset.name,
                self.asset.stage,
                self.asset.variant,
                defaults._export_folder_)
            return path
        else:
            return 0

    def is_playblast(self):

        # Check if the playblast path exists using the folder "playblast" function
        # And using the "os" python module
        return os.path.isdir(self.playblast())

    def playblast(self):

        # Check if a "variant" asset variable is assigned to the "asset" object and not None
        if self.asset.variant:

            # Build the path and return it
            path = os.path.join(
                self.asset.project,
                self.asset.domain,
                self.asset.category,
                self.asset.name,
                self.asset.stage,
                self.asset.variant,
                defaults._playblast_folder_)
            return path
        else:
            return 0

    def is_export_root(self):

        # Check if the export_root path exists using the folder "export_root" function
        # And using the "os" python module
        return os.path.isdir(self.export_root())


    def export(self, version = None):

        # Check if a "variant" asset variable is assigned to the "asset" object
        # And if a "export_asset" asset variable is assigned to the "asset" object
        # And check if the "export_root" folder exists using the folder "is_export_root" function 
        if self.asset.variant and self.asset.export_asset\
            and self.is_export_root():

            # Build the path and return it
            # Uses the folder "export_root" function
            # And uses the "export_asset" asset variable
            path = os.path.join(
                self.export_root(),
                self.asset.export_asset)

            # If a version is specified
            # Build the path using the "os" python module
            if version:
                path = os.path.join(path, version)

            # Return the path as a "succeed"
            return path
        else:

            # Return the fail
            return 0

    def is_export(self, version = None):

        # Check if the requested version is existing
        # Using the "os" python module and the "export" folder function
        return os.path.isdir(self.export(version))

    @property
    def software(self):

        # Check if the requested part is assigned to the "asset" object
        if self.asset.software:

            # Build the path and return it
            path = os.path.join(
                self.asset.project,
                self.asset.domain,
                self.asset.category,
                self.asset.name,
                self.asset.stage,
                self.asset.variant,
                self.asset.software)
            return path
        else:
            return 0

    def is_software(self):

        # Check if the requested software folder is existing
        # Using the "os" python module and the "software" folder property
        return os.path.isdir(self.software)

    @property
    def file(self):

        # Build a file path+name from the "asset" object
        # without creating it, just a return
        # Get the software folder from the "asset" object
        folder = self.software

        # Get the filename template from the "asset" object
        file_name_template = self.work_name_template

        # Build the filename with the correct software extension
        file_name = '{}.{}.{}'.format(file_name_template,
                                      self.asset.version,
                                      defaults._extension_dic_[self.asset.software])

        # Join it to the folder using the "os" python module
        file = os.path.join(folder, file_name)

        # Return the file
        return file

    @property
    def export_file(self):

        # Build a file path+name from the "asset" object
        # without creating it, just a return
        # Get the filename template from the "asset" object
        file_name_template = self.export_name_template

        # Build the filename with the correct software extension
        # Get the extension dic from the "project_prefs" wizard module
        extension_dic = project_prefs.get_extension_dic()
        extension = extension_dic[self.asset.stage]

        # Build the file name
        file_name = '{}.{}'.format(file_name_template,
                                      extension)

        # Return the file name
        return file_name

    def playblast_file(self, version):

        # Build a file path+name from the "asset" object
        # without creating it, just a return
        # Get the filename template from the "asset" object
        file_name_template = self.playblast_name_template

        # Build the filename with the correct software extension
        extension_dic = project_prefs.get_extension_dic()

        # Need to create this variable in the "defaults" wizard module
        extension = 'mov'

        # Build the playblast file name
        file_name = '{}_{}.{}'.format(file_name_template, version,
                                      extension)

        # Return the playblast file name
        return file_name

    @property
    def export_proxy_file(self):

        # Build a file path+name from the "asset" object
        # without creating it, just a return
        # Get the filename template from the "asset" object
        proxy_file_name_template = self.export_proxy_name_template

        # Build the filename with the correct software extension
        # Get the extension dic from the "project_prefs" wizard module
        extension_dic = project_prefs.get_extension_dic()
        extension = extension_dic[self.asset.stage]

        # Build the proxy file name
        file_name = '{}.{}'.format(proxy_file_name_template,
                                      extension)

        # Return the file name
        return file_name

    def export_file_multiple(self, filename):

        # Build a file path+name from the "asset" object
        # without creating it, just a return
        # Get the filename template from the "asset" object
        file_name_template = '{}.{}'.format(self.export_name_template, filename)

        # Build the filename with the correct software extension
        # Get the extension dic from the "project_prefs" wizard module
        extension_dic = project_prefs.get_extension_dic()
        extension = extension_dic[self.asset.stage]

        # Build the proxy file name
        file_name = '{}.{}'.format(file_name_template,
                                      extension)

        # Return the file name
        return file_name

    @property
    def work_name_template(self):

        # Build the file name from an "asset" wizard object
        name_template = '{}_{}_{}_{}_{}'.format(defaults._work_,
                                                self.asset.category,
                                                self.asset.name,
                                                self.asset.stage,
                                                self.asset.variant)

        # Return the name template
        return name_template

    @property
    def export_name_template(self):

        # Build the file name fom an "asset" object
        name_template = '{}_{}_{}_{}_{}'.format(defaults._publish_,
                                                self.asset.category,
                                                self.asset.name,
                                                self.asset.stage,
                                                self.asset.variant)

        # Return the name template
        return name_template

    @property
    def playblast_name_template(self):

        # Build the file name fom an "asset" object
        name_template = '{}_{}_{}_{}_{}'.format(defaults._playblast_,
                                                self.asset.category,
                                                self.asset.name,
                                                self.asset.stage,
                                                self.asset.variant)

        # Return the name template
        return name_template

    @property
    def export_proxy_name_template(self):

        # Build the file name fom an "asset" object
        name_template = '{}_{}_{}_{}_{}_{}'.format(defaults._publish_,
                                                self.asset.category,
                                                self.asset.name,
                                                self.asset.stage,
                                                self.asset.variant,
                                                defaults._proxy_)

        # Return the name template
        return name_template 

    def version_from_file(self, file):

        # Return a version from a given file name or file path
        version = file.split('.')[-2]

        # Return the version
        return version
