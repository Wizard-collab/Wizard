import hou

def get_wizard_ref_node():
    wizard_ref_node_name = "wizard_references"
    obj_node = hou.node("/obj")
    wizard_ref_node = hou.node("/obj/" + wizard_ref_node_name)
    if wizard_ref_node not in obj_node.children():
         obj_node.createNode("geo", node_name = wizard_ref_node_name)
         wizard_ref_node = hou.node("/obj/" + wizard_ref_node_name)
    return wizard_ref_node

def get_wizard_export_node():
    wizard_exports_node_name = "wizard_exports"
    obj_node = hou.node("/obj")
    wizard_exports_node = hou.node("/obj/" + wizard_exports_node_name)
    if wizard_exports_node not in obj_node.children():
         obj_node.createNode("geo", node_name = wizard_exports_node_name)
         wizard_exports_node = hou.node("/obj/" + wizard_exports_node_name)
    return wizard_exports_node

def create_node_without_duplicate(type, name, parent = None):
    if not parent:
        parent = hou.node('/obj')

    node_path = "{}/{}".format(parent.path(), name)
    node = hou.node(node_path)
    if node not in parent.children():
        node = parent.createNode(type, node_name = name)
        node = hou.node(node_path)
    return node

def node_exists(name, parent = None):
    if not parent:
        prent = hou.node('/obj')

    node_path = "{}/{}".format(parent.path(), name)
    node = hou.node(node_path)
    return node

def connect_to_input_item(node, parent, no):
    input_item_path = "{}/{}".format(parent.path(), str(no))
    input_item = hou.item(input_item_path)
    node.setInput(0, input_item)

def create_export_null_on_last_node():

    out_name = "wizard_export_OUT"

    selected = hou.selectedNodes()
    if len(selected) == 1:
        if selected[0].type().name() == 'geo':
            node = selected[0]
            last_node = None
            for child in node.children():
                if not len(child.outputConnections()):
                    last_node = hou.node(child.path())
                    break

            print(last_node.name())

            if last_node and last_node.name() != out_name:
                export_null_node = create_node_without_duplicate("null", out_name, node)
                export_null_node.setInput(0, last_node)
                return export_null_node
            elif last_node and last_node.name() == out_name:
                return last_node

            else:
                print("No output node found") 
                return None
        else:
            print('Please select a "Geometry" node')
            return None
    else:
        print('Please select one node')
        return None
