from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QTreeWidgetItem
from gui import tree_get

from wizard.vars import defaults


def build_tree(widget, value):
    root_parent = widget.invisibleRootItem()
    domains_list = list(value.keys())
    sorted_domains = sorted(domains_list, key=lambda x: defaults._domains_list_.index(x))
    for item in sorted_domains:
        domain = item
        domain_parent = add_item(widget, root_parent, item, editable=False)

        if domain_parent:
            categories_list = list(value[domain].keys())
            categories_list.sort()
            for item in categories_list:
                category = item
                category_parent = add_item(widget, domain_parent, item, editable=False)

                if category_parent:
                    names_list = list(value[domain][category].keys())
                    names_list.sort()
                    for item in names_list:
                        name = item
                        name_parent = add_item(widget, category_parent, item, editable=False)

                        if name_parent:
                            stages_list = list(value[domain][category][name].keys())
                            if domain == defaults._assets_:
                                sorted_stages = sorted(stages_list, key=lambda x: defaults._assets_stages_.index(x))
                            elif domain == defaults._sequences_:
                                sorted_stages = sorted(stages_list, key=lambda x: defaults._sequences_stages_.index(x))
                            else:
                                sorted_stages = stages_list
                                stages_list.sort()

                            for item in sorted_stages:
                                stage = add_item(widget, name_parent, item, editable=False, stage=1)

                            if domain == defaults._assets_:
                                for stage in defaults._assets_stages_:
                                    if stage not in value[domain][category][name].keys():
                                        create = 1
                                    else:
                                        create = 0
                                    add_item(widget=widget,
                                             parent=name_parent,
                                             name=stage,
                                             create=create,
                                             editable=False)
                            if domain == defaults._sequences_:
                                for stage in defaults._sequences_stages_:
                                    if stage not in value[domain][category][name].keys():
                                        create = 1
                                    else:
                                        create = 0
                                    add_item(widget=widget,
                                             parent=name_parent,
                                             name=stage,
                                             create=create,
                                             editable=False)
                            if domain == defaults._library_:
                                if defaults._lib_stages_dic_[category] not in value[domain][category][name].keys():
                                    create = 1
                                else:
                                    create = 0
                                add_item(widget=widget,
                                         parent=name_parent,
                                         name=defaults._lib_stages_dic_[category],
                                         create=create,
                                         editable=False)
                            if domain == defaults._editing_:
                                if defaults._editing_stages_dic_[category] not in value[domain][category][name].keys():
                                    create = 1
                                else:
                                    create = 0
                                add_item(widget=widget,
                                         parent=name_parent,
                                         name=defaults._editing_stages_dic_[category],
                                         create=create,
                                         editable=False)

                    if domain == defaults._assets_:
                        add_item(widget, category_parent, defaults._new_item_label_, create=1, editable=True)
                    if domain == defaults._sequences_:
                        add_item(widget, category_parent, defaults._new_shot_label_, create=1)
                    if domain == defaults._library_:
                        add_item(widget, category_parent, defaults._new_item_label_, create=1)
                    if domain == defaults._editing_:
                        add_item(widget, category_parent, defaults._new_item_label_, create=1)

            if domain == defaults._sequences_:
                add_item(widget, domain_parent, defaults._new_item_label_, create=1, editable=True)


def add_item(widget, parent, name, create=None, editable=False, stage=None):
    add = True

    for i in range(parent.childCount()):

        if name == parent.child(i).text(0):
            add = False
            new_item = parent.child(i)
            refresh_item(new_item, name, create)
            break

    if add:

        icon = get_icon_from_name(name)
        new_item = QTreeWidgetItem([name])

        if editable == True:

            new_item.setFlags(new_item.flags() | QtCore.Qt.ItemIsEditable)

        else:

            flags = new_item.flags()
            new_item.setFlags(new_item.flags() ^ QtCore.Qt.ItemIsEditable)

        if create:

            new_item.setText(10, defaults._add_item_)
            new_item.setForeground(0, QtGui.QBrush(QtGui.QColor(defaults._add_item_color_)))
            icon = defaults._add_icon_

        if stage:

            icon = defaults._stage_icon_[name]

        if stage and not create:

            tree_get.disable_edit(new_item)
            tree_get.remove_icon(new_item)
            tree_get.set_white(new_item)
            tree_get.reset_data_text(new_item)
            tree_get.set_icon(new_item)

        if icon:

            new_item.setIcon(0, QtGui.QIcon(icon))

        parent.addChild(new_item)

    return new_item

def refresh_item(item, name, create):
    if not create:
        tree_get.disable_edit(item)
        tree_get.remove_icon(item)
        tree_get.set_white(item)
        tree_get.reset_data_text(item)
        tree_get.set_icon(item)
        icon = get_icon_from_name(name)
        if icon:
            item.setIcon(0, QtGui.QIcon(icon))


def get_icon_from_name(name):
    icon = None
    if name == defaults._assets_:
        icon = defaults._assets_icon_
    if name == defaults._sequences_:
        icon = defaults._sequences_icon_
    if name == defaults._library_:
        icon = defaults._library_icon_
    if name == defaults._editing_:
        icon = defaults._edit_icon_
    return icon
