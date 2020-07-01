from PyQt5 import QtWidgets, QtCore, QtGui

from gui.imported_asset_manager_dialog import Ui_Dialog
from wizard.prefs.main import prefs
from wizard.asset.folder import folder
from wizard.vars import defaults
from wizard.tools import log
from wizard.tools import utility as utils
import os
from wizard.asset.reference import references

logger = log.pipe_log()

prefs = prefs()

class Main(QtWidgets.QDialog):

    def __init__(self, asset, count, proxy, visible):
        super(Main, self).__init__()
        # Build the ui from ui converted file
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.asset = asset
        self.count = count
        self.proxy = proxy
        self.visible = visible
        self.init_wsd()
        self.setup_infos()
        self.refresh_versions(1)
        self.connect_functions()

        self.shadow = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(8)
        self.shadow.setColor(QtGui.QColor(0, 0, 0, 180))
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.setGraphicsEffect(self.shadow)

    def init_wsd(self):

        self.ui.wsd_proxy_pushButton.clicked.connect(lambda:self.ui.wsd_asset_pushButton.setEnabled(1))
        self.ui.wsd_proxy_pushButton.clicked.connect(lambda:self.ui.wsd_asset_pushButton.setChecked(0))
        self.ui.wsd_proxy_pushButton.clicked.connect(lambda:self.ui.wsd_proxy_pushButton.setChecked(1))

        self.ui.wsd_asset_pushButton.clicked.connect(lambda:self.ui.wsd_proxy_pushButton.setEnabled(1))
        self.ui.wsd_asset_pushButton.clicked.connect(lambda:self.ui.wsd_proxy_pushButton.setChecked(0))
        self.ui.wsd_asset_pushButton.clicked.connect(lambda:self.ui.wsd_asset_pushButton.setChecked(1))

        self.ui.wsd_visible_pushButton.clicked.connect(lambda:self.ui.wsd_hidden_pushButton.setEnabled(1))
        self.ui.wsd_visible_pushButton.clicked.connect(lambda:self.ui.wsd_hidden_pushButton.setChecked(0))
        self.ui.wsd_visible_pushButton.clicked.connect(lambda:self.ui.wsd_visible_pushButton.setChecked(1))
        
        self.ui.wsd_hidden_pushButton.clicked.connect(lambda:self.ui.wsd_visible_pushButton.setEnabled(1))
        self.ui.wsd_hidden_pushButton.clicked.connect(lambda:self.ui.wsd_visible_pushButton.setChecked(0))
        self.ui.wsd_hidden_pushButton.clicked.connect(lambda:self.ui.wsd_hidden_pushButton.setChecked(1))

        self.ui.wsd_proxy_pushButton.clicked.connect(self.change_proxy_state)
        self.ui.wsd_asset_pushButton.clicked.connect(self.change_proxy_state)
        self.ui.wsd_visible_pushButton.clicked.connect(self.change_visibility_state)
        self.ui.wsd_hidden_pushButton.clicked.connect(self.change_visibility_state)

        
    def refresh_wsd(self):

        if self.asset.category != defaults._sets_ or not prefs.asset(self.asset).export.is_proxy:
            self.ui.wsd_proxy_pushButton.setEnabled(0)
            self.ui.wsd_asset_pushButton.setEnabled(0)
            self.ui.wsd_proxy_file_lineEdit.setText('NO PROXY FOUND')
            st = '#wsd_proxy_file_lineEdit{color:rgb(240,120,120);}\n'
            st+= '#wsd_proxy_size_lineEdit{color:rgb(240,120,120);}'
            self.ui.wsd_proxy_file_lineEdit.setStyleSheet(st)
            self.ui.wsd_proxy_size_lineEdit.setStyleSheet(st)
            self.ui.wsd_proxy_size_lineEdit.setText('No file')
            self.proxy = 0

        else:
            self.ui.wsd_proxy_pushButton.setEnabled(1)
            self.ui.wsd_asset_pushButton.setEnabled(1)
            self.ui.wsd_proxy_file_lineEdit.setText(prefs.asset(self.asset).export.full_proxy)
            self.ui.wsd_proxy_file_lineEdit.setStyleSheet('#wsd_proxy_file_lineEdit{color:white);}')
            self.ui.wsd_proxy_size_lineEdit.setStyleSheet('#wsd_proxy_size_lineEdit{color:white);}')
            proxy_size = utils.convert_size(os.path.getsize(prefs.asset(self.asset).export.full_proxy))
            self.ui.wsd_proxy_size_lineEdit.setText(proxy_size)
        
        proxy_file = prefs.asset(self.asset).export.full_proxy
        file = prefs.asset(self.asset).export.full_file

        if os.path.isfile(file):
            file_size = utils.convert_size(os.path.getsize(prefs.asset(self.asset).export.full_file))
            self.ui.wsd_file_size_lineEdit.setText(file_size)

        self.ui.wsd_proxy_pushButton.setChecked(self.proxy)
        self.ui.wsd_asset_pushButton.setChecked(1-self.proxy)

        self.ui.wsd_visible_pushButton.setChecked(self.visible)
        self.ui.wsd_hidden_pushButton.setChecked(1-self.visible)

    def change_proxy_state(self, state):
        self.proxy = self.ui.wsd_proxy_pushButton.isChecked()

    def change_visibility_state(self, state):
        self.visible = self.ui.wsd_visible_pushButton.isChecked()

    def move_ui(self):
        win_size = (self.frameSize().width(), self.frameSize().height())
        posx = QtGui.QCursor.pos().x() - 10
        posy = int(QtGui.QCursor.pos().y()) - win_size[1] + 10
        self.move(posx, posy)

    def setup_infos(self):
        if self.asset:
            icon = defaults._nodes_icons_dic_[self.asset.stage]
        else:
            icon = defaults._missing_node_icon_
        self.ui.image_label.setPixmap(
            QtGui.QPixmap(icon).scaled(40, 40, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
        self.refresh_variants()

    def variant_changed(self):
        self.asset.variant = self.ui.variant_comboBox.currentText()
        logger.info(self.ui.variant_comboBox.currentText())
        self.refresh_exported_asset()

    def export_asset_changed(self):
        self.asset.export_asset = self.ui.exported_asset_comboBox.currentText()
        prefs.asset(self.asset).export_root.set_default_export_asset(self.ui.exported_asset_comboBox.currentText())
        self.refresh_versions(0)

    def refresh_working_scene(self):
        working_scene_text = "{}-{}-{}-{}-{}".format(self.asset.domain, \
                                                     self.asset.category, \
                                                     self.asset.name, \
                                                     self.asset.stage, \
                                                     self.asset.variant)
        self.ui.working_scene_label.setText(working_scene_text)

    def refresh_variants(self):
        variants = prefs.asset(self.asset).stage.variants
        for variant in variants:
            self.ui.variant_comboBox.addItem(variant)
        index = variants.index(self.asset.variant)
        self.ui.variant_comboBox.setCurrentIndex(index)
        self.variant_changed()

    def refresh_exported_asset(self):
        self.ui.exported_asset_comboBox.clear()
        exported_assets_list = prefs.asset(self.asset).export_root.exported_assets_list
        if self.asset.export_asset not in exported_assets_list:
            self.asset.export_asset = prefs.asset(self.asset).export_root.default_export_asset
        for exported_asset in exported_assets_list:
            self.ui.exported_asset_comboBox.addItem(exported_asset)
        index = exported_assets_list.index(self.asset.export_asset)
        self.ui.exported_asset_comboBox.setCurrentIndex(index)
        self.export_asset_changed()

    def refresh_versions(self, init=1):
        self.ui.exported_version_comboBox.clear()
        self.versions = prefs.asset(self.asset).export.versions
        for version in self.versions:
            self.ui.exported_version_comboBox.addItem(version)
        if init:
            index = self.versions.index(self.asset.export_version)
            self.ui.exported_version_comboBox.setCurrentIndex(index)
            self.version_changed()

    def refresh_update(self):
        if self.asset.export_version != self.versions[-1]:
            self.ui.exported_version_comboBox.setStyleSheet(
                "#exported_version_comboBox{border:1px solid rgb(255,153,51)}")
        else:
            self.ui.exported_version_comboBox.setStyleSheet(
                "#exported_version_comboBox{border:1px solid rgb(153,255,102)}")

    def set_last_version(self):
        index = self.versions.index(self.versions[-1])
        self.ui.exported_version_comboBox.setCurrentIndex(index)
        self.version_changed()

    def version_changed(self):
        self.asset.export_version = self.ui.exported_version_comboBox.currentText()
        self.refresh_working_scene()
        self.refresh_file()
        self.refresh_namespace()
        self.refresh_infos()
        self.refresh_update()
        self.refresh_wsd()

    def refresh_file(self):
        file = folder(self.asset).export_file
        self.ui.file_label.setText(file)

    def refresh_namespace(self):
        name_space = references(self.asset).get_name_space(self.asset, self.count)
        self.ui.namespace_label.setText(name_space)

    def refresh_infos(self):

        self.asset.export_asset =  prefs.asset(self.asset).export_root.default_export_asset
        if not self.asset.export_asset or self.asset.export_asset == '':
            export_assets_list = prefs.asset(self.asset).export_root.exported_assets_list
            if export_assets_list != []:
                for export_asset in export_assets_list:
                    self.asset.export_asset = export_asset
                    prefs.asset(self.asset).export_root.set_default_export_asset(export_asset)
                    break
        if not self.asset.export_version:
            self.asset.set_export_version()

        logger.info(self.asset.variant)
        logger.info(self.asset.export_asset)
        logger.info(self.asset.export_version)
        user = prefs.asset(self.asset).export.version_user
        date = prefs.asset(self.asset).export.version_date
        comment = prefs.asset(self.asset).export.version_comment
        self.ui.user_name_label.setText(user)
        self.ui.date_label.setText(date)
        self.ui.comment_label.setText(comment)

    def connect_functions(self):
        self.ui.exported_version_comboBox.currentIndexChanged.connect(self.version_changed)
        self.ui.variant_comboBox.currentIndexChanged.connect(self.variant_changed)
        self.ui.exported_asset_comboBox.currentIndexChanged.connect(self.export_asset_changed)
        self.ui.exported_asset_comboBox.currentIndexChanged.connect(self.set_last_version)
        self.ui.imported_asset_update_pushButton.clicked.connect(self.accept)
