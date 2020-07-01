from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication
from wizard.tools import log
import copy
import pickle
from wizard.vars import defaults
from wizard.prefs import asset as asset_prefs
from wizard.asset.main import asset as asset_core
from wizard.asset import checker
from gui import tree_get

from wizard.prefs.main import prefs
import options_widget
from gui import build

logger = log.pipe_log()

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
        #elif self.parent.asset.stage == self.parent.selected_asset.stage and \
        #self.parent.asset.name == self.parent.selected_asset.name:
        #logger.warning("Can't import the asset itself...")
        else:
            asset = copy.deepcopy(self.parent.selected_asset)
            for variant in prefs.asset(asset).stage.variants:
                asset.variant = variant
                asset.software = asset_prefs.variant(asset).get_default_software()
                asset.export_asset = prefs.asset(asset).export_root.default_export_asset
                if asset.export_asset:
                    encode_asset = pickle.dumps(asset, 0).decode('utf-8')

                    mimeData = QtCore.QMimeData()
                    mimeData.setText(encode_asset)
                    drag = QtGui.QDrag(self)
                    drag.setMimeData(mimeData)
                    # Si l'on veut une icône ...
                    icon = defaults._nodes_icons_dic_[self.parent.selected_asset.stage]
                    pixmap = QtGui.QPixmap(icon).scaled(38, 38, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
                    drag.setPixmap(pixmap)
                    drag.setHotSpot(QtCore.QPoint(pixmap.width() / 2, pixmap.height()))
                    drag.setPixmap(pixmap)
                    result = drag.exec_(QtCore.Qt.MoveAction)
                    break
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
        if self.parent.selected_asset.stage == None:
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
