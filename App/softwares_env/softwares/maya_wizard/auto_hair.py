import sys
if sys.platform == "win32":
    import ctypes
    ctypes.windll.kernel32.SetDllDirectoryA(None)

import maya.standalone
maya.standalone.initialize()
from wizard.tools import log
from wizard.asset import main as asset_core
from wizard.vars import defaults
from wizard.prefs.main import prefs
from wizard.tools import utility as utils
from wizard.project import wall
import traceback
import logging
import copy
import os
import sys
from softwares.maya_wizard.export_anim import export_anim
from softwares.maya_wizard.export_fur import export_fur
from wizard.asset.reference import references
path_to_append = os.path.abspath('softwares/')
sys.path.append(path_to_append)
from softwares.maya_wizard import reference_asset


from wizard.asset import checker

import maya.cmds as cmds
#cmds.loadPlugin( allPlugins=True )

logger = log.pipe_log()

logger.info(path_to_append)


class auto_hair():
	def __init__(self, string_asset, file, nspace_list, frange, comment = None):
		self.asset = asset_core.string_to_asset(string_asset)
		self.string_asset = string_asset
		self.file = file
		self.nspace_list = nspace_list
		self.frange = frange
		self.references_dic = prefs().asset(self.asset).software.references
		self.comment = comment

	def auto_hair(self):

		for nspace in self.nspace_list:

			self.export_anim(nspace)

			self.rig_asset = asset_core.string_to_asset(self.references_dic[nspace][defaults._asset_key_])

			if self.get_grooming_asset():

				if self.match_geos():
					if self.create_new_scene():
						if self.get_exported_asset():
							self.add_anim_reference()
							self.add_grooming_reference()
							self.build_scene()
							self.blendshape_shapes()
							self.export_hair()

							print('status:Done !')



			else:
				logger.warning("No {} publish found for this asset : {}-{}".format(defaults._hair_, self.rig_asset.category, self.rig_asset.name))

	def build_scene(self):
		os.environ[defaults._asset_var_] = utils.asset_to_string(self.cfx_asset)
		cmds.file( f=True, new=True )
		reference_asset.import_anim()
		reference_asset.import_hair()
		cmds.file( rename=self.cfx_scene )
		cmds.file( save=True, type='mayaAscii', f=True )

	def blendshape_shapes(self):
		cmds.namespace( set=self.animation_namespace )
		obj_list = cmds.namespaceInfo( listNamespace=True )
		logger.info(obj_list)

		anim_obj_list = []

		for obj in obj_list:
			logger.info(obj)
			relatives_list = cmds.listRelatives(obj, shapes = 1)
			if relatives_list and relatives_list != [] and len(relatives_list) == 1:
				if cmds.objectType(relatives_list[0]) == 'mesh':
					anim_obj_list.append(obj)

		logger.info(anim_obj_list)

		for obj in anim_obj_list:
			groom_obj = obj.replace(self.animation_namespace,
									'{}:{}'.format(self.hair_nspace, self.groom_geo_namespace))
			logger.info(obj)
			logger.info(groom_obj)
			try:
				self.blend(obj, groom_obj)
			except:
				logger.info("Can't blendshape {} and {}".format(obj, groom_obj))

		cmds.file( save=True, type='mayaAscii', f=True )

	def blend(self, base, target):
		cmds.namespace( set=':' )
		cmds.select(cl=1)
		blendShapeName = '{}_blendShape'.format(base.split(':')[-1])
		cmds.blendShape(base, target, origin='world', name=blendShapeName, tc=1 )
		cmds.setAttr(blendShapeName+'.'+(base.split(':')[-1]), 1)

	def add_anim_reference(self):
		references(self.cfx_asset).remove_all_references()
		count  = references(self.cfx_asset).add_reference(self.export_asset, 0,1)
		self.animation_namespace  = references(self.cfx_asset).get_name_space(self.export_asset, count)

	def match_geos(self):
		match = None

		rig_references = prefs().asset(self.rig_asset).variant.references
		rig_geo_asset = None
		for reference in rig_references.keys():
			asset = asset_core.string_to_asset(rig_references[reference][defaults._asset_key_])
			if asset.stage == defaults._geo_ and asset.name == self.rig_asset.name:
				rig_geo_asset = asset
				break
		groom_references = prefs().asset(self.grooming_asset).variant.references
		grooming_geo_asset = None
		for reference in groom_references.keys():
			asset = asset_core.string_to_asset(groom_references[reference][defaults._asset_key_])
			if asset.stage == defaults._geo_ and asset.name == self.grooming_asset.name:
				grooming_geo_asset = asset
				self.groom_geo_namespace = reference
				break
		if rig_geo_asset:
			if grooming_geo_asset:
				if rig_geo_asset.export_version == grooming_geo_asset.export_version:
					match = 1
				else:
					logger.warning("The geo imported in rig and the geo imported in grooming doesn't matchs")
			else:
				logger.warning("No geo imported in the grooming scene")
		else:
			logger.warning("No geo imported in the rig scene")

		return match

	def get_grooming_asset(self):
		self.grooming_asset = copy.deepcopy(self.rig_asset)
		self.grooming_asset.stage = defaults._hair_
		presence = None
		if checker.check_stage_existence(self.grooming_asset):
			self.grooming_asset.variant = self.rig_asset.variant
			if not checker.check_variant_existence(self.grooming_asset):
				self.grooming_asset.variant = prefs().asset(self.grooming_asset).stage.default_variant
			if checker.check_variant_existence(self.grooming_asset):
				self.grooming_asset.export_asset = prefs().asset(self.grooming_asset).export_root.default_export_asset
				if self.grooming_asset.export_asset:
					self.grooming_asset.export_version = prefs().asset(self.grooming_asset).export.last_version
					presence = 1
		return presence

	def add_grooming_reference(self):
		count = references(self.cfx_asset).add_reference(self.grooming_asset, 0,1)
		self.hair_nspace = references(self.cfx_asset).get_name_space(self.grooming_asset, count)

	def export_anim(self, nspace):
		export_anim(self.string_asset, self.file, [nspace], self.frange, set_done = 0).export_anim()

	def export_hair(self):
		string_asset = utils.asset_to_string(self.cfx_asset)
		export_fur(string_asset, self.cfx_scene, [self.hair_nspace], self.frange, set_done = 0).export_fur()

	def create_new_scene(self):
		asset_exists = 0
		self.cfx_asset = copy.deepcopy(self.asset)
		self.cfx_asset.stage = defaults._cfx_
		self.cfx_asset.variant = 'auto_hair'
		if not checker.check_stage_existence(self.cfx_asset):
			self.cfx_asset.variant = None
			self.cfx_asset.software = None
			self.cfx_asset.version = None
			self.cfx_asset.export_asset = None
			self.cfx_asset.export_version = None
			if self.cfx_asset.create():
				self.cfx_asset.variant = 'auto_hair'
				if not checker.check_variant_existence(self.cfx_asset):
					self.cfx_asset.software = None
					self.cfx_asset.version = None
					self.cfx_asset.export_asset = None
					self.cfx_asset.export_version = None
					if self.cfx_asset.create():
						asset_exists = 1
		else:
			asset_exists = 1
		if asset_exists:
			prefs().asset(self.cfx_asset).stage.set_default_variant('auto_hair')
			self.cfx_asset.software = prefs().asset(self.cfx_asset).variant.default_software
			self.cfx_asset.version = prefs().asset(self.cfx_asset).software.get_new_version()
			prefs().asset(self.cfx_asset).software.new_version(self.cfx_asset.version)
			self.cfx_scene = self.cfx_asset.file
		return asset_exists

	def get_exported_asset(self):
		self.export_asset = copy.deepcopy(self.asset)
		self.export_asset.export_asset = prefs().asset(self.export_asset).export_root.default_export_asset
		self.export_asset.export_version = prefs().asset(self.export_asset).export.last_version
		logger.info(prefs().asset(self.export_asset).export.full_file)
		file = prefs().asset(self.export_asset).export.full_file
		if os.path.isfile(file):
			return 1
		else:
			return 0


