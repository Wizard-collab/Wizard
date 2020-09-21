# coding: utf-8

# Default python modules
import os
import shutil
import traceback
# Wizard modules
from wizard.asset import builder as build
from wizard.asset.folder import folder
from wizard.tools import log
from wizard.vars import defaults
from wizard.software.main import launch
from wizard.prefs.main import prefs
from wizard.prefs.stats import stats
# Creates the main logger
logger = log.pipe_log(__name__)

prefs = prefs()

class asset():
    '''
	This class is the main "asset" object, used everywhere in wizard.
	An "asset" object contain :
		- <domain> ( ex : 'sequences' )
		- <category> ( ex : 'characters' )
		- <name> ( ex : 'John' )
		- <stage> ( ex : 'animation' )
		- <variant> ( ex : 'main' )
		- <software> ( ex : 'Substance Painter' )
		- <version> ( ex : '0024' )
        - <export_asset> ( ex : 'John_rig_0002')
        - <export_version> ( ex : '0007')

	'''

    def __init__(self,
                 domain=None,
                 category=None,
                 name=None,
                 stage=None,
                 variant=None,
                 software=None,
                 version=None,
                 export_asset = None,
                 export_version = None
                 ):

        # Define the class variables
        # Uses the wizard "prefs" module to get the project path
        self.project = prefs.project_path
        self.domain = domain
        self.category = category
        self.name = name
        self.stage = stage
        self.variant = variant
        self.software = software
        self.version = version
        self.export_asset = export_asset
        self.export_version = export_version

        self.asset_prefs = prefs.asset(self)


    @property
    def versions(self):

        # Get the versions list of the asset using the "prefs" wizard module
        return self.asset_prefs.software.versions

    @property
    def export_versions(self):

        # Get the export versions list of the asset using the "prefs" wizard module
        return self.asset_prefs.export.versions

    @property
    def variants(self):

        # Get the variants list of the asset using the "prefs" wizard module
        return self.asset_prefs.stage.variants

    @property
    def date(self):

        # Get the work version date of the asset using the "prefs" wizard module
        return self.asset_prefs.software.version_date

    @property
    def user(self):

        # Get the work version user of the asset using the "prefs" wizard module
        return self.asset_prefs.software.version_user

    @property
    def comment(self):

        # Get the work version comment of the asset using the "prefs" wizard module
        return self.asset_prefs.software.version_comment

    @property
    def softwares(self):

        # Get the softwares list of the asset using the "prefs" wizard module
        return self.asset_prefs.stage.softwares

    @property
    def icon(self):

        # Get the software icon of the asset using the "prefs" wizard module
        return self.asset_prefs.software.icon

    @property
    def file(self):

        # Get the asset file using the "folder" wizard module
        return folder(self).file

    @property
    def folder(self):

        # Return the asset folder
        # in function of which variables are declared in the asset
        if self.stage:
            return folder(self).software
        elif self.name:
            return folder(self).name
        elif self.category:
            return folder(self).category
        else:
            return folder(self).domain

    @property
    def image(self):

        # Get the asset screenshot with the "prefs" wizard module
        return self.asset_prefs.software.image

    @property
    def export_image(self):

        # Get the asset export screenshot with the "prefs" wizard module
        return self.asset_prefs.export.image

    def set_export_version(self, version = None):

        # Assign an export version to the asset
        # Depending on hte version given in argument

        # Check if an "export_asset" variable is assigned to the asset
        if self.export_asset:
            if version :
                self.export_version = version  
            else:

                # If no version is given, assign the last to the asset
                # Using the "prefs" wizard module
                self.export_version = self.asset_prefs.export.last_version
        else:

            # If no "export_asset" variable is assigned to the asset
            # Set the "export_version" to None
            self.export_version = None


    def create(self, in_out=None):
        # Call the "stats" wizard object
        # To interact with it
        stats_prefs = stats()

        # Check if a category was given to the "asset" class
        # Check if a name was given to the "asset" class
        # Check if a stage was given to the "asset" class
        # Check if a variant was given to the "asset" class
            # Then create the asked parts, if parts are none, 
            # the parent part is created, recursively
        if self.category != None and\
                self.name == None and\
                self.stage == None and\
                self.variant == None:

            # Create and check the return in the same line
            if build.create_category(self):

                # Add "xp" to the user using the "stats" wizard module
                stats_prefs.add_xp(20)

                # Return the succeed of the "build" wizard function
                return 1
            else:
                return 0
        elif self.name != None and\
                self.stage == None and\
                self.variant == None:

            # Create and check the return in the same line
            if build.create_name(self, in_out):

                # Add "xp" to the user using the "stats" wizard module
                stats_prefs.add_xp(20)

                # Return the succeed of the "build" wizard function
                return 1
            else:
                return 0
        elif self.stage != None and\
                self.variant == None:

            # Create and check the return in the same line
            if build.create_stage(self):

                # Assign the default variant (main) to the asset
                self.variant = defaults._main_variant_

                # Create the variant and check the return in the same line
                if build.create_variant(self):

                    # Add "xp" to the user using the "stats" wizard module
                    stats_prefs.add_xp(20)

                    # Return the succeed of the "build" wizard function
                    return 1
                else:
                    return 0
            else:
                return 0
        elif self.variant != None:

            # Create and check the return in the same line
            if build.create_variant(self):

                # Add "xp" to the user using the "stats" wizard module
                stats_prefs.add_xp(20)

                # Return the succeed of the "build" wizard function
                return 1
            else:
                return 0
        else:
            return 0

    def export(self, export_asset_namespace, need_proxy = 0):

        # This function create the folders and writes the needed preferences
        # to the necessary .wd files
        # This function need thoses arguments :
            #-export_asset_namespace ( the namespace of the imported asset )
            #-need_proxy ( Does the asset need a proxy version - only used in set_dress and layouts )

        # Set the namespace from the imported asset as "export_asset" variable
        # This will influence the export folders
        self.export_asset = export_asset_namespace

        # Add the export asset to export_root '.wd' file if doesn't exists
        # Using the "prefs" wizard module
        self.asset_prefs.export_root.add_export_asset(self.export_asset)

        # Set the export_asset as default - Influence the nexts imports of this exported asset
        self.asset_prefs.export_root.set_default_export_asset(self.export_asset)

        # Create the new folders using the "wizard.asset.build" module
        build.create_export(self)

        # Get a new version with the "prefs" wizard module
        version = self.asset_prefs.export.get_new_version()

        # Create the version folder using the "wizard.asset.build" module
        path = build.create_export(self, version)

        # Get the export_file using the "folder" wizard module
        file = folder(self).export_file

        if need_proxy:

            # If a proxy is needed, get the proxy file using the "wizard.asset.folder" module
            proxy_file = folder(self).export_proxy_file

            # Build and return the full proxy file path/name using the "os" python module
            return [os.path.join(path, file), os.path.join(path, proxy_file)]

        else:

            # If no proxy needed, return only the main export file
            # Using the "os" pytohn module
            return os.path.join(path, file)

    def playblast(self):

        # This function create the defaults playblast folder in the asset variant folder
        # and return the playblast file

        # Get a new playblast version using the "prefs" wizard module
        version = self.asset_prefs.playblast.get_new_version()

        # Add the new version to the "playblast.wd" file
        self.asset_prefs.playblast.new_version(version)

        # Build and get the playblast folder using the "wizard.asset.build" wizard module
        path = build.create_playblast(self)

        # Get the playblast file using the "wizard.asset.folder" wizard module
        file = folder(self).playblast_file(version)

        # Build and return the full file usign the "os" python module
        return os.path.join(path, file)

    def export_multiple(self, export_asset_namespace, files_list):

        # This function create an export folder and return
        # an export file names list to export multiples files
        # It return a list and files and you need to copy your originals files
        # to the new names given

        # Set the namespace from the imported asset as "export_asset" variable
        # This will influence the export folders
        self.export_asset = export_asset_namespace

        # Add the export asset to export_root '.wd' file if doesn't exists
        # Using the "prefs" wizard module
        self.asset_prefs.export_root.add_export_asset(self.export_asset)

        # Set the export_asset as default - Influence the nexts imports of this exported asset
        self.asset_prefs.export_root.set_default_export_asset(self.export_asset)

        # Create the new folders using the "wizard.asset.build" module
        build.create_export(self)

        # Get a new version with the "prefs" wizard module
        version = self.asset_prefs.export.get_new_version()

        # Create the version folder using the "wizard.asset.build" module
        path = build.create_export(self, version)

        # Init the file names list
        export_files_names = []

        # Loop into the given files list in arguments
        for file in files_list:

            # Get the file name with the "os" python module
            file_name = os.path.splitext(os.path.basename(file))[0]

            # Get the file name using the "wizard.asset.folder" wizard module
            file = folder(self).export_file_multiple(file_name)

            # Append the full file name to the files names list
            # Using the "os" pytohn module to build the full file
            export_files_names.append(os.path.join(path, file))

        # Return the files names list
        return export_files_names

    def launch(self, main_window = None, sct= None):

        # Check if a category is assigned
        # Check if a name is assigned
        # Check if a stage is assigned
        # Check if a variant is assigned
        # Check if a software is assigned
        if self.category and \
                self.name and \
                self.stage and \
                self.variant and \
                self.software:

            # Get the work file using the "getter" module
            self.work = folder(self).file

            # Check if the file exists, if not, copy it from
            # the install dir
            # "null" is the equivalent in the "yaml" module to the python "None" variable
            if defaults._init_file__dic_[self.software] != 'null':

                # Check if the file to launch exists using the "os" pytohn module
                if not os.path.isfile(self.work):

                    # If the file doesn't exists, copy it from the wizard install
                    # Getting the path using the "_init_file_dic_" dictionnary
                    # from the "defaults" wizard module
                    shutil.copyfile(defaults._init_file__dic_[self.software],
                                    self.work)

                # As long as "Substance painter" is not scriptable
                # Wizard get the referenced file here to launch the software
                # directly with the referenced asset ( only one and only "geo" )
                if self.software == defaults._painter_:

                    # Get the referenced asset using the "wizard.asset.main.asset.get_reference" wizard function
                    reference = self.get_reference()
                
                else:

                    # If software isn't substance painter, assign reference to "None"
                    reference = None

                # Create the launch object using the "wizard.software.main.launch" function
                # Give it the following arguments :
                    #-asset
                    #-the main ui object
                    #-the reference
                self.instance = launch(self, main_window, reference, sct)

                # Open the software using the "launch.open" function
                # Return the launched object
                return self.instance.open()

            else:

                # If no software is assigned to the asset, try to open the folder
                # Using the "os" python module
                try:
                    os.startfile(self.folder)
                except:

                    # If an exception is raised, log it to the user
                    logger.critical(str(traceback.format_exc()))
        else:
            return 0

    def get_reference(self):

        # Get the reference dictionnary using the "prefs" wizard module
        references_dic = self.asset_prefs.variant.references

        if references_dic != {}:
            # If the reference dictionnary isn't empty
            # Get all the referenced assets by looping in the references dictionnary
            for reference in references_dic:

                # Get the "asset" (writed as string) stored in the dicionnary
                # Convert it to an "asset" wizard object using the "wizard.asset.main"
                # string_to_asset function
                reference_asset = string_to_asset(references_dic[reference][defaults._asset_key_])

                # Get the version folder of the export_asset
                # Using the "prefs" wizard module
                folder = prefs.asset(reference_asset).export.version_folder

                # Get the file using the "prefs" wizard module
                file = prefs.asset(reference_asset).export.file

                # Build the full file path using the "os" python module
                full_file = os.path.join(folder, file)

            # Return the full file
            return full_file

        else:

            # If the references dictionnary is empty, return "None"
            return None

    def remove(self):

        # Check if the current user is as "adminstrator"
        # Using the "prefs" wizard module
        if prefs.admin:

            # Check if a category was given to the "asset" class
            # Check if a name was given to the "asset" class
            # Check if a stage was given to the "asset" class
            # Check if a variant was given to the "asset" class
                # Then create the asked parts, if parts are none, 
                # the parent part is created, recursively

            # If only a "category" variable is given to the asset, delete it
            if self.category != None and\
                    self.name == None and\
                    self.stage == None and\
                    self.variant == None:

                # Create and check the return in the same line
                if self.category != defaults._characters_ and\
                    self.category != defaults._props_ and\
                    self.category != defaults._sets_ and\
                    self.category != defaults._vehicles_:

                    # Remove the asset using the "build" wizard.asset module
                    # And return the success or the fail
                    if build.remove_category(self):
                        return 1
                    else:
                        return 0
                else:
                    return 0

            # If a "name" variable exists in the "asset", delete it
            elif self.name != None and\
                    self.stage == None and\
                    self.variant == None:

                # Delete and check the return in the same line
                # Using the "build" wizard.asset module
                if build.remove_name(self):
                    return 1
                else:
                    return 0
        else:

            # If the user isn't as administrator, log it
            logger.warning("You don't have the right to do that...")

def get_asset_from_file(file):

    # Normalize the asset full path to avoid "\" path separation
    # Split the asset full path using the "os" python module
    path = os.path.normpath(file)
    folders = path.split(os.sep)

    # Get the asset variables from the splitted full path
    domain = folders[2]
    category = folders[3]
    name = folders[4]
    stage = folders[5]
    variant = folders[6]
    software = folders[7]

    # Get the version from the file name
    version = file.split('.')[-2]

    # Build and return the asset object using the "wizard.asset.main.asset" wizard module
    return asset(domain, category, name, stage, variant, software, version)

def asset_to_string(asset):

    # Convert the asset object to a string separated by '.'
    string_asset = "{}".format(asset.domain)
    string_asset+= ".{}".format(asset.category)
    string_asset+= ".{}".format(asset.name)
    string_asset+= ".{}".format(asset.stage)
    string_asset+= ".{}".format(asset.variant)
    string_asset+= ".{}".format(asset.software)
    string_asset+= ".{}".format(asset.version)
    string_asset+= ".{}".format(asset.export_asset)
    string_asset+= ".{}".format(asset.export_version)

    # Return the string
    return string_asset

def string_to_asset(string):

    # Split the given string and get the asset variables
    domain = string.split('.')[0]
    category = string.split('.')[1]
    name = string.split('.')[2]
    stage = string.split('.')[3]
    variant = string.split('.')[4]
    try:
        software = string.split('.')[5]
    except IndexError:
        software = None

    # Try to get :
        #-version
        #-export_asset
        #-export_version
    try:
        version = string.split('.')[6]
        export_asset = string.split('.')[7]
        export_version = string.split('.')[8]

    # If thoses variables are not in the string,
    # Assign defaults variables
    except IndexError:
        version = '0000'
        export_asset = None
        export_version = None
    
    # Create the asset object using the "wizard.asset.main.asset" wizard module
    asset_object = asset(domain,
                  category,
                  name,
                  stage,
                  variant,
                  software,
                  version,
                  export_asset,
                  export_version)

    # Return the asset object
    return asset_object
