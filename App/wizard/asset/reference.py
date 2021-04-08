# coding: utf-8

# Wizard modules
from wizard.asset import main as asset_core
from wizard.asset.folder import folder
from wizard.prefs.main import prefs
from wizard.tools import log
from wizard.vars import defaults

# Creates the main logger
logger = log.pipe_log(__name__)

prefs = prefs()

class references():

    # This module is used to store and get references from an asset object
    # Theses references as stored in a dic, writed in a ".prefs" file

    def __init__(self, asset):

        # This class need an "asset" wizard object
        self.asset = asset
        self.asset_prefs = prefs.asset(self.asset)
        
        # The class is initiated getting all the references 
        self.get_references()

    def get_references(self):

        # Init a references list
        self.references_list = []

        # Init an "assets" list
        self.assets_list = []

        # Get the references dictionnary using the "prefs" wizard module
        self.references_dic = self.asset_prefs.software.references

        # Loop in the keys of the dictionnary to list the references
        # The keys are the imported assets namepsaces
        for reference in list(self.references_dic.keys()):

            # Append the namespace to the references_list
            self.references_list.append(reference)

            # Get the asset from the namespace key
            # The asset is stored as a string and converted into an asset
            # Using the "wizard.asset.main" string_to_asset function
            # The key to access the string_asset is stored in the "defaults" wizard module
            string_asset = self.references_dic[reference][defaults._string_asset_]
            asset = asset_core.string_to_asset(string_asset)

            # The key to access the count is stored in the "defaults" wizard module
            # The count is used to differenciate the sames imported assets
            # Example :
                #-Characters_John_rigging_main_0001
                #-Characters_John_rigging_main_0002
                #-Characters_John_rigging_main_0003
                #-Characters_Albert_rigging_main_0001
            count = self.references_dic[reference][defaults._count_]

            # Check if the stored reference in the references dictionnary has a proxy and need to be visible 
            # The keys to access thoses variables are stored in the "defaults" wizard module 
            if (defaults._proxy_ and defaults._visible_) in self.references_dic[reference].keys():
                proxy = self.references_dic[reference][defaults._proxy_]
                visible = self.references_dic[reference][defaults._visible_]
            else:

                # If thoses keys are not stored in the dictionnary, set proxy to 0 and visible to 1
                proxy = 0

                # If the asset category is sets and the exported asset contain a proxy file
                # Set the proxy by defaults to 1
                if asset.category == defaults._sets_ and prefs.asset(asset).export.is_proxy:
                    proxy = 1
                visible = 1

                # If the keys are not in the references dictionnary, add them
                # by defaults
                self.add_proxy_and_visible_keys(reference, proxy, visible)

            # Add a list in the assets_list
            # This list contains all the keys from the reference dictionnary
                #-asset
                #-count
                #-proxy
                #-pvisible
            if folder(asset).export():
                self.assets_list.append([asset, count, proxy, visible])

    def add_proxy_and_visible_keys(self, reference, proxy, visible):

        # Add the proxy and visible keys to the dictionnary
        self.references_dic[reference][defaults._proxy_] = proxy
        self.references_dic[reference][defaults._visible_] = visible

        # Write the dictionnary ".prefs" file
        # Using the "prefs" wizard module
        self.asset_prefs.software.set_references(self.references_dic)

    @property
    def references(self):

        # Return the assets_list builded with the "get_references" function
        return self.assets_list

    def add_reference(self, asset, proxy, visible):

        # Convert the asset object to an asset string using the "wizard.asset.main" module
        string_asset = asset_core.asset_to_string(asset)

        # Set the count to 1 by defaults
        count = 1

        # Iterate the references list to check if this namespace already exists
        # Uses the function "get_namespace" to build the name space of the asset
        while self.get_name_space(asset, count) in self.references_list:

            # Convert the count int to a string with 4 characters
            # Example :
                # 1 > 0001
                # 24 > 0024
            # Uses the "zfill" string function 
            count = str(int(count) + 1).zfill(4)

        # Build the name space using the "get_name_space" function
        name_space = self.get_name_space(asset, count)

        # Set the reference and return the count using the "set_reference" function
        return self.set_reference(string_asset, count, name_space, proxy, visible)

    def set_reference(self, string_asset, count, name_space, proxy, visible):

        # Create an empty dictionnary and assign the reference keys
        # All the keys are stored in teh "defaults" wizard module
        reference_dic = {}
        reference_dic[defaults._string_asset_] = string_asset
        reference_dic[defaults._count_] = count
        reference_dic[defaults._proxy_] = proxy
        reference_dic[defaults._visible_] = visible

        # Add this dictionnary to the main references dictionnary
        # The key is the name space
        self.references_dic[name_space] = reference_dic

        # Write the main dictionnary to the ".prefs" file using the "prefs" wizard module
        self.asset_prefs.software.set_references(self.references_dic)

        # Return the namespace count
        return count

    def replace_reference(self, asset, count, old_namespace = None, proxy = 0, visible = 1):

        # This function access the main references dictionnary and override the imported asset
        # Using the namespace key

        # Build the name space using the "get_name_space" function
        count = 1

        # Iterate the references list to check if this namespace already exists
        # Uses the function "get_namespace" to build the name space of the asset
        while self.get_name_space(asset, count) in self.references_list:

            # Convert the count int to a string with 4 characters
            # Example :
                # 1 > 0001
                # 24 > 0024
            # Uses the "zfill" string function 
            count = str(int(count) + 1).zfill(4)

        name_space = self.get_name_space(asset, count)

        # Convert the asset to a string using the "wizard.asset.main" module
        string_asset = asset_core.asset_to_string(asset)

        # Create an empty dictionnary to override the old one
        # Assign the differents variables to the namespace dictionnary
        # All the keys are stored in the "defaults" wizard module
        reference_dic = {}
        reference_dic[defaults._string_asset_] = string_asset
        reference_dic[defaults._count_] = count
        reference_dic[defaults._proxy_] = proxy
        reference_dic[defaults._visible_] = visible

        # If an old_namespace is given, delete it and
        # assign the new namespace dictionnary to the main references dictionnary
        if old_namespace:
            del self.references_dic[old_namespace]

        # Assign the new namespace dictionnary to the main references dictionnary
        # The key is the new asset namespace
        self.references_dic[name_space] = reference_dic

        # Write the main references dictionnary to the ".prefs" file
        # Using the "prefs" wizard module
        self.asset_prefs.software.set_references(self.references_dic)

        # Return the namespace count
        return count


    def remove_reference(self, asset, count):

        # Build the imported asset namespace using the "get_name_space" function
        name_space = self.get_name_space(asset, count)

        # Check if the namespace is in the main references dictionnary
        # If yes, delete it
        if name_space in list(self.references_dic.keys()):
            del self.references_dic[name_space]

            # Write the main references dictionnary to the ".prefs" file
            # Using the "prefs" wizard module
            self.asset_prefs.software.set_references(self.references_dic)

    def remove_all_references(self):

        # Iterate the main references dictionnary to delete all the namespace keys
        for name_space in self.references_dic.keys():
            del self.references_dic[name_space]

        # Write the main references dictionnary to the ".prefs" file
        # Using the "prefs" wizard module
        self.asset_prefs.software.set_references(self.references_dic)

    def get_name_space(self, asset, count):

        # Build the namespace string using the asset object and the count
        name_space = "{}_{}_{}_{}_{}_{}".format(asset.domain,
                                                asset.category,
                                                asset.name,
                                                asset.stage,
                                                asset.variant,
                                                str(count).zfill(4))

        # Return the name space
        return name_space

def get_name_space(asset, count):

        # Build the namespace string using the asset object and the count
        name_space = "{}_{}_{}_{}_{}_{}".format(asset.domain,
                                                asset.category,
                                                asset.name,
                                                asset.stage,
                                                asset.variant,
                                                str(count).zfill(4))
        
        # Return the name space
        return name_space
