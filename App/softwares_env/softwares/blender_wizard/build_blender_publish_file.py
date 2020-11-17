import bpy
import reference_asset
import tools

sys.path.append(str(os.path.dirname(os.path.abspath(__file__))))

def build_blender_publish_file():
    '''Builds Blender publish file.'''
    # delete all scene content
    for c in bpy.context.scene.collection.children:
        scene.collection.children.unlink(c)
    bpy.data.orphans_purge() # delete all unused data-blocks

    # import Maya .abc
    root = reference_asset.import_alembic()

    # convert Maya groups to Blender's collections
    replace_maya_grp_by_collection(root)

    # save file and exit
    bpy.ops.wm.save_mainfile(filepath='', exit=True)



build_blender_publish_file()
