import maya.cmds as cmds
import os

from wizard.vars import defaults
from wizard.asset import main as asset_core
from wizard.tools import log
from wizard.prefs.main import prefs
from wizard.vars import defaults
from wizard.wsd.main import wsd
from wizard.vars import defaults
from wizard.project import wall

logger = log.pipe_log()

def go_to_wsd():

	main_asset = asset_core.string_to_asset(os.environ[defaults._asset_var_])
	
	if main_asset.stage == defaults._geo_ and main_asset.category == defaults._set_dress_:
		grp = 'geo_GRP'
	elif main_asset.stage == defaults._layout_:
		grp = 'layout_GRP'

	namespace_list = get_namespaces_list(grp)

	export_list = build_export_list(main_asset, namespace_list)

def get_namespaces_list(grp):
	namespace_list = []

	if cmds.objExists(grp):
		childs = cmds.listRelatives(grp, allDescendents = 1)
		for child in childs:
			if cmds.referenceQuery(child, isNodeReferenced = 1):
				namespace = cmds.referenceQuery(child, namespace = 1).replace(':', '')
				if namespace not in namespace_list:
					namespace_list.append(namespace)
	return namespace_list

def build_export_list(main_asset, namespace_list):

	references_list = prefs().asset(main_asset).variant.references

	for namespace in namespace_list:
		if namespace in references_list.keys():
			
			asset = references_list[namespace][defaults._asset_key_]
			locator = namespace+'_CTRL'
			world_infos = get_world_infos(locator)

			export_dic = dict()
			export_dic[namespace] = dict()
			export_dic[namespace][defaults._asset_key_] = asset
			export_dic[namespace][defaults._wsd_pos_] = world_infos[0]
			export_dic[namespace][defaults._wsd_rot_] = world_infos[1]
			export_dic[namespace][defaults._wsd_scale_] = world_infos[2]

			logger.info(export_dic)

			file = main_asset.export('{}-{}'.format(main_asset.name, main_asset.variant))
			logger.info(file)
			wsd(file, export_dic).write_sd()
			wall.wall().publish_event(main_asset)

		else:
			logger.warning('Ignoring {}, not in references'.format(namespace))

def get_world_infos(locator):

	position = cmds.xform(locator,q=1,ws=1,rp=1)
	rotation = cmds.xform(locator, q=True, ws=True, ro=True )
	scale = cmds.xform(locator, q=True, ws=True, scalePivot=True )
	prs = [position, rotation, scale]
	return prs


