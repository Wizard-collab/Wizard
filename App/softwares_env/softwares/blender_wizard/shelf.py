import bpy
import bpy.utils.previews
import os
import plugin
import reference_asset
from wizard.vars import defaults

bl_info = {
    "name": "Wizard",
    "author": "Auguste Lefort",
    "version": (1, 0),
    "blender": (2, 90, 0),
    "location": "View3D > Wizard",
    "description": "Provide Wizard's tools",
    "warning": "",
    "doc_url": "wizard-pipeline-manager.webflow.io",
    "category": "User",
}

class WizardPanel(bpy.types.Panel):
    bl_label = "Wizard"
    bl_idname = "VIEW_3D_PT_wizard_UI"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Wizard"
    bl_description = "Panel which contains all Wizard's tools."

    def draw_header(self, context):
        self.layout.label(icon_value=custom_icons["wizard_icon"].icon_id)

    def draw(self, context):
        global custom_icons
        l = self.layout
        c = l.column()
        c.label(text="Wizard Tools")
        c.operator(SaveFile.bl_idname, text="Save", icon_value=custom_icons["save_icon"].icon_id)
        c.operator(PublishFile.bl_idname, text="Publish", icon_value=custom_icons["publish_icon"].icon_id)
        c.operator(ImportAll.bl_idname, text="Import", icon_value=custom_icons["import_icon"].icon_id)
        c.operator(CreateExportGrp.bl_idname, text="Create Export grp", icon_value=custom_icons["export_grp_icon"].icon_id)


class SaveFile(bpy.types.Operator):
    bl_idname = "wizard.save_file"
    bl_label = "Save File"
    bl_description = "Save file in Wizard's hierarchy"

    def execute(self, context):
        plugin.save()
        return {'FINISHED'}

class PublishFile(bpy.types.Operator):
    bl_idname = "wm.publish_file"
    bl_label = "Publish File"
    bl_description = "Publish file in Wizard's hierarchy"

    def execute(self, context):
        plugin.export()
        return {'FINISHED'}

class ImportAll(bpy.types.Operator):
    bl_idname = "wm.import_all"
    bl_label = "Import all"
    bl_description = "Import all the references defined in Wizard."

    def execute(self, context):
        reference_asset.import_all()
        return {'FINISHED'}

class CreateExportGrp(bpy.types.Operator):
    bl_idname = "wm.create_export_grp"
    bl_label = "Create Export Grp"
    bl_description = "Create export group/collection. The content will be published."

    def execute(self, context):
        plugin.create_export_GRP()
        return {'FINISHED'}


custom_icons = None

def register():
    bpy.utils.register_class(SaveFile)
    bpy.utils.register_class(PublishFile)
    bpy.utils.register_class(ImportAll)
    bpy.utils.register_class(CreateExportGrp)
    bpy.utils.register_class(WizardPanel)
    # load custom icons
    global custom_icons
    custom_icons = bpy.utils.previews.new()
    custom_icons.load("wizard_icon", defaults._wizard_icon_, 'IMAGE')
    custom_icons.load("save_icon", defaults._maya_save_icon_, 'IMAGE')
    custom_icons.load("publish_icon", defaults._maya_export_icon_, 'IMAGE')
    custom_icons.load("import_icon", defaults._maya_import_icon_, 'IMAGE')
    custom_icons.load("export_grp_icon", defaults._maya_group_icon_, 'IMAGE')

def unregister():
    bpy.utils.unregister_class(SaveFile)
    bpy.utils.unregister_class(PublishFile)
    bpy.utils.unregister_class(ImportAll)
    bpy.utils.unregister_class(CreateExportGrp)
    bpy.utils.unregister_class(WizardPanel)
    # Unload custom icons
    global custom_icons
    bpy.utils.previews.remove(custom_icons)

if __name__ == "__main__":
    register()
