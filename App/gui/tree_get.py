from PyQt5 import QtCore, QtGui

from wizard.vars import defaults


class tree():

    def __init__(self, item):

        parent = item.parent()
        item_name = item.text(0)
        agrandpa_name = None
        grandpa_name = None
        parent_name = None
        has_grandpa = 0
        has_agrandpa = 0

        if parent:
            parent_name = parent.text(0)
            grandpa = parent.parent()
            has_grandpa = 0
            if grandpa:
                grandpa_name = grandpa.text(0)
                agrandpa = grandpa.parent()
                has_grandpa = 1
                has_agrandpa = 0
                if agrandpa:
                    agrandpa_name = agrandpa.text(0)
                    has_agrandpa = 1

        if has_agrandpa:
            self.domain = agrandpa_name
            self.category = grandpa_name
            self.name = parent_name
            self.stage = item_name
        elif not has_agrandpa and has_grandpa:
            self.domain = grandpa_name
            self.category = parent_name
            self.name = item_name
            self.stage = None
        else:
            self.domain = parent_name
            self.category = item_name
            self.name = None
            self.stage = None

    def get_domain(self):
        return self.domain

    def get_category(self):
        return self.category

    def get_name(self):
        return self.name

    def get_stage(self):
        return self.stage


def remove_item(item):
    parent = item.parent()
    parent.removeChild(item)


def disable_edit(item):
    flags = item.flags()
    item.setFlags(item.flags() ^ QtCore.Qt.ItemIsEditable)


def remove_icon(item):
    item.setIcon(0, QtGui.QIcon(''))


def set_white(item):
    item.setForeground(0, QtGui.QBrush(QtGui.QColor(defaults._white_color_hexa_)))


def check_add_item(item):
    if item.text(10) == defaults._add_item_:
        return 1
    else:
        return 0


def set_icon(item):
    name = item.text(0)
    if name in defaults._assets_stages_ or \
            name in defaults._sequences_stages_ or \
            name in defaults._lib_stages_dic_ or \
            name in defaults._editing_categories_list_:
        item.setIcon(0, QtGui.QIcon(defaults._stage_icon_[name]))
    else:
        pass


def reset_data_text(item):
    item.setText(10, defaults._asset_item_)


def search(treeWidget, name):
    found_category = None
    root = treeWidget.invisibleRootItem()
    for domain in range(root.childCount()):
        domain = root.child(domain)
        if domain.text(0) == defaults._assets_:
            domain.setExpanded(1)
            for category in range(domain.childCount()):
                category = domain.child(category)
                for item in range(category.childCount()):
                    item = category.child(item)
                    category.setExpanded(0)
                    item.setExpanded(0)
                    if name.upper() in item.text(0).upper():
                        found_category = category
                        found_item = item
    if found_category:
        found_category.setExpanded(1)
        found_item.setExpanded(1)
        treeWidget.clearSelection()
        found_item.setSelected(1)


def select_asset(treeWidget, asset):
    root = treeWidget.invisibleRootItem()
    for domain in range(root.childCount()):
        domain = root.child(domain)
        if domain.text(0) == asset.domain:
            domain.setExpanded(1)
            break
    for category in range(domain.childCount()):
        category = domain.child(category)
        if category.text(0) == asset.category:
            category.setExpanded(1)
            break
    for name in range(category.childCount()):
        name = category.child(name)
        name.setExpanded(0)
        if name.text(0) == asset.name:
            name.setExpanded(1)
            break
    for stage in range(name.childCount()):
        stage = name.child(stage)
        if stage.text(0) == asset.stage:
            treeWidget.selectionModel().clearSelection()
            stage.setSelected(1)
            treeWidget.setCurrentIndex(treeWidget.selectedIndexes()[0])
            break

def item_from_asset(treeWidget, asset):
    root = treeWidget.invisibleRootItem()

    stage_item = None
    name_item = None

    for domain in range(root.childCount()):
        domain = root.child(domain)
        if domain.text(0) == asset.domain:
            #domain.setExpanded(1)
            break
    for category in range(domain.childCount()):
        category = domain.child(category)
        if category.text(0) == asset.category:
            #category.setExpanded(1)
            break
    for name in range(category.childCount()):
        name = category.child(name)
        #name.setExpanded(0)
        if name.text(0) == asset.name:
            #name.setExpanded(1)
            name_item = name
            break
    for stage in range(name.childCount()):
        stage = name.child(stage)
        if stage.text(0) == asset.stage:
            stage_item = stage
            #treeWidget.selectionModel().clearSelection()
            #stage.setSelected(1)
            #treeWidget.setCurrentIndex(treeWidget.selectedIndexes()[0])
            break

    if stage_item:
        return stage_item
    else:
        if name_item:
            return name_item
        else:
            return None