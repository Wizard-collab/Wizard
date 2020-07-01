import pymel.core as pm
from wizard.asset import main as asset_core
import os
from wizard.vars import defaults


def tagGuerillaAuto(*arg):
    selectionGuerilla_List = pm.ls(sl=1)
    asset = asset_core.string_to_asset(os.environ[defaults._asset_var_])

    if selectionGuerilla_List:
        for mesh in selectionGuerilla_List:
            if pm.attributeQuery('GuerillaTags', node=mesh, exists=1) == 0:
                pm.addAttr(mesh, ln="GuerillaTags", dt="string")

            currentAttr = mesh.name() + '.GuerillaTags'
            currentTag = pm.getAttr(currentAttr)

            tags_list = []
            if currentTag:
                tags_list = currentTag.split(',')

            if mesh.name() not in tags_list:
                tags_list.append(mesh.name())
            if asset.category not in tags_list:
                tags_list.append(asset.category)
            if asset.name not in tags_list:
                tags_list.append(asset.name)
            if asset.variant not in tags_list:
                tags_list.append(asset.variant)
            name_variant = '{}_{}'.format(asset.name, asset.variant)
            if name_variant not in tags_list:
                tags_list.append(name_variant)

            attrs = (',').join(tags_list)

            pm.setAttr(mesh + '.GuerillaTags', attrs, type="string")

    else:
        pm.warning('Your selection is empty')
