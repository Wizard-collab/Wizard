from wizard.project.wall import wall
from wizard.tools import log
from wizard.vars import defaults
from wizard.asset import main as asset_core
from wizard.prefs.main import prefs
from wizard.project import main as project
from wizard.asset import checker as check
from wizard.prefs.stats import stats

logger = log.pipe_log()

def show_stats():
	all_events = wall().get_all_keys()
	events_dic = wall().open_wall_file()

	stages_list = list()

	for event in all_events:
		if events_dic[event][defaults._creation_user_key_] == prefs().user and events_dic[event][defaults._wall_id_key_] == defaults._wall_publish_event_:
			asset_string = events_dic[event][defaults._asset_key_]
			asset = asset_core.string_to_asset(asset_string)
			if asset.stage and asset.stage!='None':
				stages_list.append(asset.stage)

	all_versions = get_all_versions() + len(stages_list)
	versions_dic = stats().get_versions()

	design_occu = stages_list.count(defaults._design_)
	design_percent = ((design_occu+versions_dic[defaults._design_])/all_versions)*100
	geo_occu = stages_list.count(defaults._geo_)
	geo_percent = ((geo_occu+versions_dic[defaults._geo_])/all_versions)*100
	rig_occu = stages_list.count(defaults._rig_)
	rig_percent = ((rig_occu+versions_dic[defaults._rig_])/all_versions)*100
	hair_occu = stages_list.count(defaults._hair_)
	hair_percent = ((hair_occu+versions_dic[defaults._hair_])/all_versions)*100
	texturing_occu = stages_list.count(defaults._texturing_)
	texturing_percent = ((texturing_occu+versions_dic[defaults._texturing_])/all_versions)*100
	shading_occu = stages_list.count(defaults._shading_)
	shading_percent = ((shading_occu+versions_dic[defaults._shading_])/all_versions)*100

	return [design_percent, geo_percent, rig_percent, hair_percent, texturing_percent, shading_percent]

def get_save_stats():
	versions_dic = stats().get_versions()
	design_saves = versions_dic[defaults._design_]
	geo_saves = versions_dic[defaults._geo_]
	rig_saves = versions_dic[defaults._rig_]
	texturing_saves = versions_dic[defaults._texturing_]
	hair_saves = versions_dic[defaults._hair_]
	shading_saves = versions_dic[defaults._shading_]
	return [design_saves, geo_saves, rig_saves, texturing_saves, hair_saves, shading_saves]

def get_publish_stats():
	all_events = wall().get_all_keys()
	events_dic = wall().open_wall_file()

	stages_list = list()

	for event in all_events:
		if events_dic[event][defaults._creation_user_key_] == prefs().user and events_dic[event][defaults._wall_id_key_] == defaults._wall_publish_event_:
			asset_string = events_dic[event][defaults._asset_key_]
			asset = asset_core.string_to_asset(asset_string)
			if asset.stage and asset.stage!='None':
				stages_list.append(asset.stage)

	design_pubs = stages_list.count(defaults._design_)
	geo_pubs = stages_list.count(defaults._geo_)
	rig_pubs = stages_list.count(defaults._rig_)
	texturing_pubs = stages_list.count(defaults._texturing_)
	hair_pubs = stages_list.count(defaults._hair_)
	shading_pubs = stages_list.count(defaults._shading_)
	return [design_pubs, geo_pubs, rig_pubs, texturing_pubs, hair_pubs, shading_pubs]

def show_work_stats():
	all_versions = get_all_versions()
	versions_dic = stats().get_versions()

	design_percent = (versions_dic[defaults._design_]/all_versions)*100
	geo_percent = (versions_dic[defaults._geo_]/all_versions)*100
	rig_percent = (versions_dic[defaults._rig_]/all_versions)*100
	hair_percent = (versions_dic[defaults._hair_]/all_versions)*100
	texturing_percent = (versions_dic[defaults._texturing_]/all_versions)*100
	shading_percent = (versions_dic[defaults._shading_]/all_versions)*100

	return [design_percent, geo_percent, rig_percent, hair_percent, texturing_percent, shading_percent]

def get_all_versions():
	versions_dic = stats().get_versions()
	all_versions = 0
	for stage in versions_dic.keys():
		all_versions += versions_dic[stage]
	return all_versions

def rebuild_work_stats():
	project_dic = project.read_project()
	asset_version_list = []
	stats().reset_versions_count()

	for domain in project_dic.keys():
		for category in project_dic[domain].keys():
			for name in project_dic[domain][category].keys():
				for stage in project_dic[domain][category][name].keys():
					asset = asset_core.asset(domain=domain, category=category, name=name, stage=stage)
					for variant in prefs().asset(asset).stage.variants:
						if variant and variant != 'None':
							asset.variant = variant
							for software in prefs().asset(asset).stage.softwares:
								asset.software = software
								version_list = prefs().asset(asset).software.versions
								for version in version_list:
									if version != '0000':
										asset.version = version
										if prefs().asset(asset).software.version_user == prefs().user:
											asset_version_list.append(asset)
											stats().add_version(asset)
