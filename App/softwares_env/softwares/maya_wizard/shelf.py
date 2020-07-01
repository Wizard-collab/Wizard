import maya.cmds as cmds
from wizard.vars import defaults
from wizard.prefs import project as project_prefs


class shelf:

    def __init__(self, name="new_shelve", iconPath=""):
        self.name = name

        self.iconPath = iconPath
        self.labelBackground = (0, 0, 0, 0)
        self.labelColour = (.9, .9, .9)

        self._cleanOldShelf()
        cmds.setParent(self.name)
        self.build()

    def _cleanOldShelf(self):
        if cmds.shelfLayout(self.name, ex=1):
            if cmds.shelfLayout(self.name, q=1, ca=1):
                for each in cmds.shelfLayout(self.name, q=1, ca=1):
                    cmds.deleteUI(each)
        else:
            cmds.shelfLayout(self.name, p="ShelfLayout")

    def addButon(self, label, icon="commandButton.png", command='', doubleCommand='', docTag=None, add_doctag=None):
        cmds.setParent(self.name)
        if icon:
            icon = self.iconPath + icon
            if add_doctag: 
                cmds.shelfButton(width=37, height=37, image=icon, l=label, command=command, dcc=doubleCommand,
                                 imageOverlayLabel=docTag)
            else:
                cmds.shelfButton(width=37, height=37, image=icon, l=label, command=command, dcc=doubleCommand)#,
                #                 imageOverlayLabel=docTag)

    def addMenuItem(self, parent, label, command='', icon=""):
        if icon:
            icon = self.iconPath + icon
        return cmds.menuItem(p=parent, l=label, c=command, i="")

    def addSubMenu(self, parent, label, icon=None):
        if icon:
            icon = self.iconPath + icon
        return cmds.menuItem(p=parent, l=label, i=icon, subMenu=1)


    def build(self):

        save = 'from maya_wizard import plugin\n'
        save += 'reload(plugin)\n'
        save += 'plugin.save()'

        export = 'from maya_wizard import plugin\n'
        export += 'reload(plugin)\n'
        export += 'plugin.export()'

        reload_references = 'from maya_wizard import reference_asset\n'
        reload_references += 'reload(reference_asset)\n'
        reload_references += 'reference_asset.refresh_all()'

        import_geo = 'from maya_wizard import reference_asset\n'
        import_geo += 'reload(reference_asset)\n'
        import_geo += 'reference_asset.import_geo()'

        import_rig = 'from maya_wizard import reference_asset\n'
        import_rig += 'reload(reference_asset)\n'
        import_rig += 'reference_asset.import_rig()'

        import_camRig = 'from maya_wizard import reference_asset\n'
        import_camRig += 'reload(reference_asset)\n'
        import_camRig += 'reference_asset.import_camRig()'

        import_autoRig = 'from maya_wizard import reference_asset\n'
        import_autoRig += 'reload(reference_asset)\n'
        import_autoRig += 'reference_asset.import_autoRig()'

        import_hair = 'from maya_wizard import reference_asset\n'
        import_hair += 'reload(reference_asset)\n'
        import_hair += 'reference_asset.import_hair()'

        import_layout = 'from maya_wizard import reference_asset\n'
        import_layout += 'reload(reference_asset)\n'
        import_layout += 'reference_asset.import_layout()'

        import_anim = 'from maya_wizard import reference_asset\n'
        import_anim += 'reload(reference_asset)\n'
        import_anim += 'reference_asset.import_anim()'

        import_camera = 'from maya_wizard import reference_asset\n'
        import_camera += 'reload(reference_asset)\n'
        import_camera += 'reference_asset.import_camera()'

        import_textures = 'from maya_wizard import reference_asset\n'
        import_textures += 'reload(reference_asset)\n'
        import_textures += 'reference_asset.import_textures()'

        switch_proxy = 'from maya_wizard import reference_asset\n'
        switch_proxy += 'reload(reference_asset)\n'
        switch_proxy += 'reference_asset.switch_proxy()'

        switch_asset = 'from maya_wizard import reference_asset\n'
        switch_asset += 'reload(reference_asset)\n'
        switch_asset += 'reference_asset.switch_proxy(0)'

        duplicate_asset = 'from maya_wizard import reference_asset\n'
        duplicate_asset += 'reload(reference_asset)\n'
        duplicate_asset += 'reference_asset.duplicate_reference()'

        delete_asset = 'from maya_wizard import reference_asset\n'
        delete_asset += 'reload(reference_asset)\n'
        delete_asset += 'reference_asset.delete_asset()'

        hide_asset = 'from maya_wizard import reference_asset\n'
        hide_asset += 'reload(reference_asset)\n'
        hide_asset += 'reference_asset.hide_ref()'

        unhide_asset = 'from maya_wizard import reference_asset\n'
        unhide_asset += 'reload(reference_asset)\n'
        unhide_asset += 'reference_asset.unhide_reference()'

        create_rig_set = 'from maya_wizard import reference_asset\n'
        create_rig_set += 'reload(reference_asset)\n'
        create_rig_set += 'reference_asset.create_set(1, 0, 0)'

        create_yeti_set = 'from maya_wizard import reference_asset\n'
        create_yeti_set += 'reload(reference_asset)\n'
        create_yeti_set += 'reference_asset.create_set(0, 1, 0)'

        create_scalp_set = 'from maya_wizard import reference_asset\n'
        create_scalp_set += 'reload(reference_asset)\n'
        create_scalp_set += 'reference_asset.create_set(0, 0, 1)'

        f_range = 'from maya_wizard import scene_setup\n'
        f_range += 'reload(scene_setup)\n'
        f_range += 'scene_setup.set_f_range()'

        set_format = 'from maya_wizard import scene_setup\n'
        set_format += 'reload(scene_setup)\n'
        set_format += 'scene_setup.setFormatToMaya()'

        clean_obj = 'from maya_wizard import tools\n'
        clean_obj += 'reload(tools)\n'
        clean_obj += 'tools.clean()'

        tag = 'from maya_wizard import gtags\n'
        tag += 'reload(gtags)'

        self.addButon(label="Save", icon='maya_save.png', command=save, docTag='Save')
        self.addButon(label="Export", icon='maya_export.png', command=export, docTag='export')
        self.addButon(label="Update references", icon='maya_reload_icon.png', command=reload_references,
                      docTag='update')
        self.addButon(label="Import geo", icon='maya_import_geo.png', command=import_geo, docTag='geo')
        self.addButon(label="Import rig", icon='maya_import_rig.png', command=import_rig, docTag='rig')
        self.addButon(label="Import hair", icon='maya_import_hair.png', command=import_hair, docTag='hair')
        self.addButon(label="Import textures", icon='maya_import_textures.png', command=import_textures, docTag='textures')
        self.addButon(label="Import autoRig", icon='maya_import_autoRig.png', command=import_autoRig, docTag='autoRig')
        self.addButon(label="Import camRig", icon='maya_import_camRig.png', command=import_camRig, docTag='camRig')
        self.addButon(label="Import camera", icon='maya_import_camera.png', command=import_camera, docTag='camera')
        self.addButon(label="Import anim", icon='maya_import_anim.png', command=import_anim, docTag='anim')
        self.addButon(label="Import layout", icon='maya_import_layout.png', command=import_layout, docTag='layout')
        self.addButon(label="GTags", icon='maya_guerilla.png', command=tag, docTag='Tags')
        self.addButon(label="Create rig set", icon='maya_sel_set.png', command=create_rig_set, docTag='Rig', add_doctag=1)
        self.addButon(label="Create yeti set", icon='maya_sel_set.png', command=create_yeti_set, docTag='Yeti', add_doctag=1)
        self.addButon(label="Create scalp set", icon='maya_sel_set.png', command=create_scalp_set, docTag='Scalp', add_doctag=1)
        self.addButon(label="Match frame range", icon='maya_frame_range.png', command=f_range, docTag='Range')
        self.addButon(label="Match project format", icon='maya_format.png', command=set_format, docTag='Format')
        self.addButon(label="Clean selection", icon='maya_clean.png', command=clean_obj, docTag='Clean')
        if project_prefs.get_setdress_workflow() == defaults._wsd_workflow_:
            self.addButon(label="Switch proxy", icon='maya_switch_proxy.png', command=switch_proxy, docTag='Proxy')
            self.addButon(label="Switch asset", icon='maya_switch_asset.png', command=switch_asset, docTag='Asset')
            self.addButon(label="Duplicate asset", icon='maya_duplicate_asset.png', command=duplicate_asset, docTag='Duplicate')
            self.addButon(label="Delete asset", icon='maya_delete_asset.png', command=delete_asset, docTag='Delete')
            self.addButon(label="Hide asset", icon='maya_hide_asset.png', command=hide_asset, docTag='Hide')
            self.addButon(label="Unhide asset", icon='maya_unhide_asset.png', command=unhide_asset, docTag='Unhide')
        '''
		self.addButon("popup")
		p = cmds.popupMenu(b=1)
		self.addMenuItem(p, "popupMenuItem1")
		self.addMenuItem(p, "popupMenuItem2")
		sub = self.addSubMenu(p, "subMenuLevel1")
		self.addMenuItem(sub, "subMenuLevel1Item1")
		sub2 = self.addSubMenu(sub, "subMenuLevel2")
		self.addMenuItem(sub2, "subMenuLevel2Item1")
		self.addMenuItem(sub2, "subMenuLevel2Item2")
		self.addMenuItem(sub, "subMenuLevel1Item2")
		self.addMenuItem(p, "popupMenuItem3")
		self.addButon("button3")
		'''
