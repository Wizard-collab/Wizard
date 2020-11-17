import bpy

def list_collections(root):
    ''' Recursive function to go down a hierarachy of collections from the 'root' node. '''
    yield root
    for child in root.children:
        yield from list_collections(child)


def list_objects(root):
    ''' Recursive function to go down a hierarachy of objects from the 'root' node. '''
    yield root
    for child in root.children:
        yield from list_objects(child)


def error_popup(self, context):
    '''Builds popup window. Displays the text of the global error_message var.'''
    global error_message
    self.layout.label(text=error_message)


def raise_error(message):
    '''Takes message and call a popup window with it.'''
    global error_message
    error_message = message
    bpy.context.window_manager.popup_menu(error_popup, title="Wizard Error", icon='ERROR')


def add_namespace(root, namespace, version='0000'):
    '''
    Add prefix to all objects under the 'root' node.
    -> returns new root node
    '''
    for c in list_objects(root):
        c.name = f'{namespace}_{c.name}'
        c['namespace'] = namespace
        c['current_version'] = version

    return root


def replace_maya_grp_by_collection(root):
    '''
    Detect all Maya groups base on pattern ('EMPTY' type node with '_grp' extension),
    stores datas and rebuilds hierarchy with Blender's node type Collection.
    Inverse of replace_blender_collection_by_maya_grp().
    -> returns new root node
    '''
    all_objects = list(bpy.context.scene.objects)
    maya_grp = []
    maya_objects = []
    blender_grp = []

    for c in list_objects(root):
        parent = None
        for parent_object in bpy.data.objects:
            if c in list(parent_object.children):
                parent = parent_object
        object_data = {'name': c.name, 'parent': parent}
        if c.type == 'MESH':
            maya_objects.append(object_data)
        else:
            maya_grp.append(object_data)

    # set active object as Master scene collection to not have to unparent each grp
    scene_collection = bpy.context.view_layer.layer_collection
    bpy.context.view_layer.active_layer_collection = scene_collection
    # create all new groups
    for object in maya_grp:
        # create collection
        collection = bpy.data.collections.new(object['name'])
        bpy.context.scene.collection.children.link(collection)
        blender_grp.append(collection)

    # parent all collections under its parent
    for collection in blender_grp:
        for object in maya_grp:
            if collection.name == object['name']:
                if root.name == object['name']:
                    continue
                # exit if no parent
                if object['parent'] is None:
                    continue
                # reparent
                parent = object['parent'].name
                bpy.data.collections[parent].children.link(collection)
                bpy.context.scene.collection.children.unlink(collection)

    # reorder object in hierarchy
    for object in maya_objects:
        parent_coll = bpy.data.collections[object['parent'].name]
        obj = bpy.data.objects[object['name']]
        current_parent = object['parent']
        obj.parent = None
        parent_coll.objects.link(obj)
        bpy.context.scene.collection.objects.unlink(obj)

    stage_GRP = root.name
    # delete Maya grp (empties)
    for object in maya_grp:
        delete_object(bpy.data.objects[object['name']])
    delete_object(root)

    return bpy.data.collections[stage_GRP]


def replace_blender_collection_by_maya_grp(root):
    '''
    Detect all Blender collections, stores datas and rebuilds
    hierarchy with Maya node group (empties with '_grp' extension).
    Inverse of replace_maya_grp_by_collection().
    -> returns new root node
    '''
    maya_grp = []
    blender_grp = []

    for c in list_collections(root):
        parent = None
        for parent_collection in bpy.data.collections:
            if c in list(parent_collection.children):
                parent = parent_collection
        collection_data = {'name': c.name, 'parent': parent}
        blender_grp.append(collection_data)

    # set active object as Master scene collection to not have to unparent each grp
    scene_collection = bpy.context.view_layer.layer_collection
    bpy.context.view_layer.active_layer_collection = scene_collection
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
                if root.name == collection['name']:
                    continue
                # exit if no parent
                if collection['parent'] is None:
                    continue
                # reparent
                parent = collection['parent'].name
                group.parent = bpy.data.objects[parent]

    # reorder object in hierarchy
    for collection in blender_grp:
        for children in bpy.data.collections[collection['name']].objects:
            # check if object is stage_GRP
            if bpy.data.objects[collection['name']] == root.name:
                continue
            coll = bpy.data.collections[collection['name']].name
            bpy.data.collections[collection['name']].objects.unlink(children)
            bpy.context.scene.collection.objects.link(children)
            children.parent = bpy.data.objects[collection['name']]

    stage_GRP = root.name
    # delete Maya grp (empties)
    for collection in blender_grp:
        delete_collection(bpy.data.collections[collection['name']])
    delete_collection(root)

    return bpy.data.objects[stage_GRP]


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
