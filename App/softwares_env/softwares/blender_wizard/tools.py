import bpy

def replace_maya_grp_by_collection(root):
    '''
    Detect all Maya groups base on pattern ('EMPTY' type node with '_grp' extension),
    stores datas and rebuilds hierarchy with Blender's node type Collection.
    Inverse of replace_blender_collection_by_maya_grp().
    -> returns new root node
    '''
    all_objects = list(bpy.context.scene.objects)
    maya_grp = []
    blender_grp = []
    for object in all_objects:
        if object.name.endswith('_grp') or object.name.endswith('_GRP') and object.type == 'EMPTY':
            object_data = {'name': object.name, 'parent': object.parent}
            maya_grp.append(object_data)

    # create all new collections
    for group in maya_grp:
        new_coll = bpy.data.collections.new(group['name'])
        bpy.context.scene.collection.children.link(new_coll)
        blender_grp.append(new_coll)

    # parent all collections under its parent
    for collection in blender_grp:
        for group in maya_grp:
            if collection.name == group['name']:
                if group['parent'] is None:
                    continue
                parent = group['parent'].name
                bpy.data.collections[parent].children.link(collection)
                bpy.context.scene.collection.children.unlink(collection)

    # reorder object in hierarchy
    for object in maya_grp:
        for children in bpy.data.objects[object['name']].children:
            if children.name.endswith('_grp') or children.name.endswith('_GRP') or children.name.endswith('Shape') or children.type == 'EMPTY':
                continue
            children.parent = None
            parent = children.parent
            old_coll = children.users_collection
            bpy.data.collections[object['name']].objects.link(children)
            for coll in old_coll:
                coll.objects.unlink(children)

    # delete Maya grp (empties)
    for grp in maya_grp:
        delete_object(bpy.data.objects[grp['name']])
    delete_object(root)

    return bpy.data.collections['geo_GRP']


def replace_blender_collection_by_maya_grp(root):
    '''
    Detect all Blender collections, stores datas and rebuilds
    hierarchy with Maya node group (empties with '_grp' extension).
    Inverse of replace_maya_grp_by_collection().
    -> returns new root node
    '''
    maya_grp = []
    blender_grp = []
    for collection in bpy.data.collections:
        parent = None
        for parent_collection in bpy.data.collections:
            if collection in list(parent_collection.children):
                parent = parent_collection
        collection_data = {'name': collection.name, 'parent': parent}
        blender_grp.append(collection_data)

    # create all new groups
    for collection in blender_grp:
        bpy.ops.object.empty_add(type='PLAIN_AXES', align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
        obj = bpy.context.active_object
        obj.name = collection['name']
        maya_grp.append(obj)

    # parent all groups under its parent
    for group in maya_grp:
        for collection in blender_grp:
            if group.name == collection['name']:
                if collection['parent'] is None:
                    continue
                parent = collection['parent'].name
                group.parent = bpy.data.objects[parent]

    # reorder object in hierarchy
    for collection in blender_grp:
        for children in bpy.data.collections[collection['name']].objects:
            coll = bpy.data.collections[collection['name']].name
            bpy.data.collections[collection['name']].objects.unlink(children)
            bpy.context.scene.collection.objects.link(children)
            children.parent = bpy.data.objects[collection['name']]

    # delete Maya grp (empties)
    for collection in blender_grp:
        delete_collection(bpy.data.collections[collection['name']])
    delete_collection(root)

    return bpy.data.objects['geo_GRP']


def delete_object(object):
    try:
        bpy.data.objects.remove(object, do_unlink=True)
    except:
        pass


def delete_collection(collection):
    try:
        bpy.data.collections.remove(collection, do_unlink=True)
    except:
        pass
