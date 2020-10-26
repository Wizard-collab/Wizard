# coding: utf8

# Import PyQt5 libraries
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication

# Import wizard core libraries
from wizard.tools import log
from wizard.vars import defaults
from wizard.prefs import asset as asset_prefs
from wizard.asset.main import asset as asset_core
from wizard.asset import checker
from wizard.tools import utility as utils
from wizard.prefs.main import prefs

# Import wizard gui libraries
from gui import build
from gui import tree_get

# Import wizard widgets
import options_widget

# Import python base libraries
import pickle
import copy

# Init the main logger and prefs module
logger = log.pipe_log(__name__)
prefs = prefs()

class treeWidget(QtWidgets.QTreeWidget):

    def __init__(self, parent=None):
        super().__init__(parent.ui.centralwidget)
        self.parent = parent
        self.setupUI()

    def setupUI(self):
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(320, 0))
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.setDragEnabled(True)
        self.setDragDropMode(QtWidgets.QAbstractItemView.DragOnly)
        self.setIndentation(30)
        self.setAnimated(True)
        self.setHeaderHidden(True)
        self.setExpandsOnDoubleClick(True)
        self.setObjectName("treeWidget")
        self.header().setVisible(False)
        self.header().setSortIndicatorShown(True)
        self.parent.ui.treeWidget_layout.addWidget(self)

    def startDrag(self, event):
        if not self.parent.pin:
            logger.warning("Please 'pin' an asset before importing something...")
        elif not self.parent.selected_asset.stage:
            logger.warning("Must import a stage...")

        else:
            assets_list = []
            asset = copy.deepcopy(self.parent.selected_asset)
            default_variant = prefs.asset(asset).stage.default_variant
            variants_list = prefs.asset(asset).stage.variants
            variants_list.remove(default_variant)
            asset.variant = default_variant
            exported_assets_list = prefs.asset(asset).export_root.exported_assets_list
            if exported_assets_list != []:
                for exported_asset in exported_assets_list:
                    asset.export_asset = exported_asset
                    asset.export_version = prefs.asset(asset).export.last_version
                    asset.software =  prefs.asset(asset).export.version_software
                    if asset.export_version:
                        string_asset = utils.asset_to_string(asset)
                        assets_list.append(string_asset)
            if assets_list == []:
                for variant in variants_list:
                    asset.variant = variant
                    exported_assets_list = prefs.asset(asset).export_root.exported_assets_list
                    if exported_assets_list != []:
                        for exported_asset in exported_assets_list:
                            asset.export_asset = exported_asset
                            asset.export_version = prefs.asset(asset).export.last_version
                            asset.software =  prefs.asset(asset).export.version_software
                            if asset.export_version:
                                string_asset = utils.asset_to_string(asset)
                                assets_list.append(string_asset)
                        break
            if assets_list != []:
                mimeData = QtCore.QMimeData()
                mimeData.setText((pickle.dumps(assets_list, 0)).decode())
                drag = QtGui.QDrag(self)
                drag.setMimeData(mimeData)
                icon = defaults._nodes_icons_dic_[self.parent.selected_asset.stage]
                pixmap = QtGui.QPixmap(icon).scaled(38, 38, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
                drag.setPixmap(pixmap)
                drag.setHotSpot(QtCore.QPoint(pixmap.width() / 2, pixmap.height()))
                drag.setPixmap(pixmap)
                result = drag.exec_(QtCore.Qt.MoveAction)
            else:
                logger.warning("No publish found...")

    def refresh_all(self):
        QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        root = self.invisibleRootItem()
        child_count = root.childCount()
        for i in range(child_count):
            domain = root.child(i)
            domain_string = domain.text(0)
            for i in range(domain.childCount()):
                category = domain.child(i)
                category_string = category.text(0)
                for i in range(category.childCount()):
                    name = category.child(i)
                    name_string = name.text(0)
                    for i in range(name.childCount()):
                        stage = name.child(i)
                        stage_string = stage.text(0)
                        asset = asset_core(domain_string, category_string, name_string, stage_string)
                        if checker.check_stage_existence(asset):
                            tree_get.disable_edit(stage)
                            tree_get.remove_icon(stage)
                            tree_get.set_white(stage)
                            tree_get.reset_data_text(stage)
                            tree_get.set_icon(stage)
        QApplication.restoreOverrideCursor()

    def refresh_asset(self, asset):
        item = tree_get.item_from_asset(self, asset)

        if item:
            tree_get.disable_edit(item)
            tree_get.remove_icon(item)
            tree_get.set_white(item)
            tree_get.reset_data_text(item)
            tree_get.set_icon(item)

    def show_options_menu(self):
        self.options_widget = options_widget.Main()
        self.options_widget.add_item('Launch', self.parent.open)
        self.options_widget.add_item('Folder', self.parent.open_folder)
        self.options_widget.add_item('Add to user shelf', self.parent.add_asset_to_shelf)
        self.options_widget.add_item('Archive', self.parent.remove_asset)
        if (self.parent.selected_asset.stage == None and self.parent.selected_asset.name != None and self.parent.selected_asset.domain == defaults._sequences_):
            self.options_widget.add_item('Change range', self.parent.modify_frame_range)
        if (self.parent.selected_asset.name == self.parent.asset.name) and (
                self.parent.selected_asset.stage == self.parent.asset.stage) and self.parent.pin:
            label = 'Unpin'
        elif (self.parent.selected_asset.name == self.parent.asset.name) and (
                self.parent.selected_asset.stage == self.parent.asset.stage) and not self.parent.pin:
            label = 'Pin'
        else:
            label = None
        if label:
            self.options_widget.add_item(label, self.parent.toggle_pin)
        build.launch_options(self.options_widget)

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        event.accept()
        if event.button() == QtCore.Qt.RightButton:
            self.show_options_menu()
