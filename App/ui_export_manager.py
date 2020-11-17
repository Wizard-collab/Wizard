# coding: utf8

# Import python base libraries
import subprocess
import traceback
import os
import sys
import copy

# Import PyQt5 libraries
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication

# Import wizard gui libraries
from gui.export_manager import Ui_Form
from gui import build

# Import wizard core libraries
from wizard.prefs.main import prefs
from wizard.vars import defaults
from wizard.tools import log
from wizard.tools import utility as utils
from wizard.asset import main as asset_core
from wizard.prefs import software as software_prefs
from wizard.software import main as software
from wizard.asset.reference import references
from wizard.asset import checker

# Import wizard widgets
import dialog_report
import ui_subprocess_manager

# Initializing the logger and the prefs module
logger = log.pipe_log(__name__)
prefs = prefs()

class Main(QtWidgets.QWidget):

    def __init__(self, asset, action = defaults._export_):
        super(Main, self).__init__()
        # Build the ui from ui converted file
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.asset = asset
        self.action = action
        self.is_cam = 0
        self.init_ui()
        self.connect_functions()

    def init_ui(self):

        if self.action == defaults._export_:
            self.ui.playblast_options_frame.setVisible(0)
        elif self.action == defaults._playblast_:
            self.ui.export_options_frame.setVisible(0)

        self.stage = self.asset.stage
        if self.stage == defaults._cfx_:
            self.ui.export_options_frame.setVisible(0)

        self.ui.export_ma_stage_lineEdit.setText(self.stage)

        self.frange = prefs.asset(self.asset).name.range
        self.preroll = prefs.asset(self.asset).name.preroll
        self.postroll = prefs.asset(self.asset).name.postroll
        self.ui.export_ma_in_frange_lineEdit.setText(str(self.frange[0]))
        self.ui.export_ma_out_frange_lineEdit.setText(str(self.frange[1]))
        self.ui.export_m_preroll_lineEdit.setText(str(self.preroll))
        self.ui.export_m_postroll_lineEdit.setText(str(self.postroll))
        self.change_range()

        self.ui.export_ma_sequence_lineEdit.setText('{} - {} - {}'.format(self.asset.category,
                                                                            self.asset.name,
                                                                            self.asset.variant))

        self.references = prefs.asset(self.asset).software.references

        for ref_asset in self.references:

            asset = asset_core.string_to_asset(self.references[ref_asset][defaults._asset_key_])

            if asset.stage in defaults._export_manager_stage_dic_[self.action]:

                item = QtWidgets.QListWidgetItem()
                item.setText(ref_asset)
                try:
                    item.setIcon(QtGui.QIcon(defaults._stage_icon_[asset.stage]))
                except:
                    pass

                self.ui.export_ma_assets_listWidget.addItem(item)
                item.setSelected(True)

            if (asset.stage == defaults._camera_) and (asset.category == self.asset.category) and (asset.name == self.asset.name):
                self.is_cam = 1

        if (self.asset.domain == defaults._sequences_) and (self.action == defaults._playblast_) and not self.is_cam:
            cam_asset = copy.deepcopy(self.asset)
            cam_asset.stage = defaults._camera_

            if checker.check_stage_existence(cam_asset):

                for variant in prefs.asset(cam_asset).stage.variants:
                    cam_asset.variant = variant
                    cam_asset.export_asset = prefs.asset(cam_asset).export_root.default_export_asset
                    if cam_asset.export_asset:
                        cam_asset.export_version = prefs.asset(cam_asset).export.last_version
                        cam_asset.software =  prefs.asset(cam_asset).export.version_software
                        if cam_asset.export_version and cam_asset.software:
                            
                            self.add_sequence_camera(cam_asset)

                        

        self.ui.export_ma_export_pushButton.setText(self.action)

        if self.action == defaults._export_:
            self.ui.export_ma_export_pushButton.clicked.connect(self.export)
        elif self.action == defaults._playblast_:
            self.ui.export_ma_export_pushButton.clicked.connect(self.playblast)

    def add_sequence_camera(self, cam_asset):
            asset_references = references(self.asset)
            count  = asset_references.add_reference(cam_asset, 0,1)
            cam_asset_namespace  = asset_references.get_name_space(cam_asset, count)
            item = QtWidgets.QListWidgetItem()
            item.setText(cam_asset_namespace)
            try:
                item.setIcon(QtGui.QIcon(defaults._stage_icon_[cam_asset.stage]))
            except:
                pass

            self.ui.export_ma_assets_listWidget.addItem(item)
            item.setSelected(True)

    def connect_functions(self):
        self.ui.export_ma_in_frange_lineEdit.textChanged.connect(self.change_range)
        self.ui.export_ma_out_frange_lineEdit.textChanged.connect(self.change_range)
        self.ui.preroll_postroll_checkBox.stateChanged.connect(self.change_range)

    def change_range(self):

        apply_pre_post_roll = self.ui.preroll_postroll_checkBox.isChecked()

        in_frame = self.ui.export_ma_in_frange_lineEdit.text()
        try:
            in_frame = int(in_frame)
            if in_frame != self.frange[0]:
                self.ui.export_ma_in_frange_lineEdit.setStyleSheet('#export_ma_in_frange_lineEdit{border:1px solid Orange}')
            else:
                self.ui.export_ma_in_frange_lineEdit.setStyleSheet('#export_ma_in_frange_lineEdit{border:1px solid Green}')
        except:
            logger.critical(str(traceback.format_exc()))
            logger.warning('Please only enter an int')
            self.ui.export_ma_in_frange_lineEdit.setStyleSheet('#export_ma_in_frange_lineEdit{border:1px solid Red}')

        out_frame = self.ui.export_ma_out_frange_lineEdit.text()
        try:
            out_frame = int(out_frame)
            if out_frame != self.frange[1]:
                self.ui.export_ma_out_frange_lineEdit.setStyleSheet('#export_ma_out_frange_lineEdit{border:1px solid Orange}')
            else:
                self.ui.export_ma_out_frange_lineEdit.setStyleSheet('#export_ma_out_frange_lineEdit{border:1px solid Green}')
        except:
            logger.critical(str(traceback.format_exc()))
            logger.warning('Please only enter an int')
            self.ui.export_ma_out_frange_lineEdit.setStyleSheet('#export_ma_out_frange_lineEdit{border:1px solid Red}')

        try:
            if apply_pre_post_roll:
                self.out_range = [int(in_frame)-int(self.preroll), int(self.postroll)+int(out_frame)] 
                self.is_preroll = 1
            else:
                self.out_range = [int(in_frame), int(out_frame)]
                self.is_preroll = 0
        except:
            self.out_range = None

    def export(self):
        items_list = self.ui.export_ma_assets_listWidget.selectedItems()
        if self.out_range:

            nspace_list = []
            cam_nspace_list = []
            for item in items_list:

                asset_item = asset_core.string_to_asset(self.references[item.text()][defaults._asset_key_])
                if asset_item.stage == defaults._cam_rig_:
                    cam_nspace_list.append(item.text())
                else:
                    nspace_list.append(item.text())

            self.asset.version = prefs.asset(self.asset).software.last_version
            auto_hair = self.ui.export_auto_hair_checkBox.isChecked()
            refresh_assets = self.ui.export_m_refresh_assets_checkBox.isChecked()

            command = ''

            if nspace_list != []:

                if cam_nspace_list != []:
                    set_done = 0
                else:
                    set_done = 1

                if self.asset.stage == defaults._animation_ and auto_hair:
                    command = 'from softwares.maya_wizard.auto_hair import auto_hair\n'
                    command += 'auto_hair("{}", "{}", {}, frange = {}, set_done = {}, refresh_assets = {}).auto_hair()'.format(utils.asset_to_string(self.asset),
                                                                                            self.asset.file.replace('\\', '/'),
                                                                                            nspace_list,
                                                                                            self.out_range,
                                                                                            set_done,
                                                                                            refresh_assets)

                elif self.asset.stage == defaults._animation_ and not auto_hair:
                    command += 'from softwares.maya_wizard.export_anim import export_anim\n'
                    command += 'export_anim("{}", "{}", {}, frange = {}, set_done = {}, refresh_assets = {}).export_anim()'.format(utils.asset_to_string(self.asset),
                                                                                            self.asset.file.replace('\\', '/'),
                                                                                            nspace_list,
                                                                                            self.out_range,
                                                                                            set_done,
                                                                                            refresh_assets)

                elif self.asset.stage == defaults._cfx_:
                    command = 'from softwares.maya_wizard.export_fur import export_fur\n'
                    command += 'export_fur("{}", "{}", {}, {}, refresh_assets = {}).export_fur()'.format(utils.asset_to_string(self.asset),
                                                                                        self.asset.file.replace('\\', '/'),
                                                                                        nspace_list,
                                                                                        self.out_range,
                                                                                        refresh_assets)

            else:
                if cam_nspace_list == []:
                    logger.warning("Please select at least an asset")
                else:
                    pass

            if cam_nspace_list != []:

                if self.asset.software == defaults._maya_:
                    command += '\nfrom softwares.maya_wizard.export_anim import export_anim\n'
                    command += 'export_anim("{}", "{}", {}, frange = {}, refresh_assets = {}).export_cam()'.format(utils.asset_to_string(self.asset),
                                                                                            self.asset.file.replace('\\', '/'),
                                                                                            cam_nspace_list,
                                                                                            self.out_range,
                                                                                            refresh_assets)


            if command != '':

                file = utils.temp_file_from_command(command)
                mayapy = prefs.software(defaults._mayapy_).path
                env = software.get_env(defaults._mayapy_, 0)
                env[defaults._asset_var_] = utils.asset_to_string(self.asset)

                self.ui_subprocess_manager = ui_subprocess_manager.Main([mayapy, "-u", file], env)
                build.launch_normal_as_child(self.ui_subprocess_manager, minimized = 1)

                self.hide()

            else:
                logger.warning('Nothing to export !')

        else:
            logger.warning("Please enter a valid frame range")

    def playblast(self):
        if self.out_range:
            if self.asset.software == defaults._maya_ or self.asset.software == defaults._maya_yeti_ or self.asset.software == defaults._houdini_:

                show_ornaments = self.ui.playblast_ornaments_checkBox.isChecked()
                show_playblast = self.ui.playblast_show_checkBox.isChecked()
                items_list = self.ui.export_ma_assets_listWidget.selectedItems()
                refresh_assets = self.ui.export_m_refresh_assets_checkBox.isChecked()

                nspace_list = []
                for item in items_list:
                    nspace_list.append(item.text())
                if nspace_list != [] and len(nspace_list) == 1:

                    env_path = os.path.abspath('softwares_env').replace('\\', '/')

                    command = 'import sys\nsys.path.append("{}")\n'.format(env_path)
                    command += 'from wizard.tools.playblast import playblast\n'
                    command += 'playblast("{}", {}, {}, is_preroll={}).playblast("{}", {}, {})'.format(utils.asset_to_string(self.asset),
                                                                                        self.out_range,
                                                                                        refresh_assets,
                                                                                        self.is_preroll,
                                                                                        nspace_list[-1],
                                                                                        show_ornaments,
                                                                                        show_playblast)

                    file = utils.temp_file_from_command(command)
                    
                    python_system = 'pywizard'
                    if sys.argv[0].endswith('.py'):
                        python_system = 'python'

                    env = os.environ.copy()
                    env[defaults._asset_var_] = utils.asset_to_string(self.asset)


                    self.ui_subprocess_manager = ui_subprocess_manager.Main("{} {}".format(python_system, file), env)
                    build.launch_normal_as_child(self.ui_subprocess_manager, minimized = 1)

                    self.hide()

                else:
                    logger.warning("Please select one camera")      
        else:
            logger.warning("Please enter a valid frame range")
