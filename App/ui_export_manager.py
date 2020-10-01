# coding: utf8

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication

from gui.export_manager import Ui_Form
from gui import build
from wizard.prefs.main import prefs
from wizard.vars import defaults
from wizard.tools import log
from wizard.tools import utility as utils
from wizard.asset import main as asset_core
import traceback
import dialog_report
import subprocess
import sys
import os
import ui_subprocess_manager
from wizard.prefs import software as software_prefs
from wizard.software import main as software

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
        self.ui.export_ma_in_frange_lineEdit.setText(str(self.frange[0]))
        self.ui.export_ma_out_frange_lineEdit.setText(str(self.frange[1]))
        self.change_range()

        self.ui.export_ma_sequence_lineEdit.setText('{} - {} - {}'.format(self.asset.category, self.asset.name, self.asset.variant))

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

        self.ui.export_ma_export_pushButton.setText(self.action)

        if self.action == defaults._export_:
            self.ui.export_ma_export_pushButton.clicked.connect(self.export)
        elif self.action == defaults._playblast_:
            self.ui.export_ma_export_pushButton.clicked.connect(self.playblast)

    def connect_functions(self):
        self.ui.export_ma_in_frange_lineEdit.textChanged.connect(self.change_range)
        self.ui.export_ma_out_frange_lineEdit.textChanged.connect(self.change_range)

    def change_range(self):
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
            self.out_range = [int(in_frame), int(out_frame)]
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

            command = ''

            if nspace_list != []:

                if cam_nspace_list != []:
                    set_done = 0
                else:
                    set_done = 1

                if self.asset.stage == defaults._animation_ and auto_hair:
                    command = 'from softwares.maya_wizard.auto_hair import auto_hair\n'
                    command += 'auto_hair("{}", "{}", {}, frange = {}).auto_hair()'.format(utils.asset_to_string(self.asset),
                                                                                            self.asset.file.replace('\\', '/'),
                                                                                            nspace_list,
                                                                                            self.out_range)

                elif self.asset.stage == defaults._animation_ and not auto_hair:
                    command += 'from softwares.maya_wizard.export_anim import export_anim\n'
                    command += 'export_anim("{}", "{}", {}, frange = {}, set_done = {}).export_anim()'.format(utils.asset_to_string(self.asset),
                                                                                            self.asset.file.replace('\\', '/'),
                                                                                            nspace_list,
                                                                                            self.out_range,
                                                                                            set_done)
                elif self.asset.stage == defaults._cfx_:
                    command = 'from softwares.maya_wizard.export_fur import export_fur\n'
                    command += 'export_fur("{}", "{}", {}, {}).export_fur()'.format(utils.asset_to_string(self.asset),
                                                                                        self.asset.file.replace('\\', '/'),
                                                                                        nspace_list,
                                                                                        self.out_range)
            else:
                if cam_nspace_list == []:
                    logger.warning("Please select at least an asset")
                else:
                    pass

            if cam_nspace_list != []:

                if self.asset.software == defaults._maya_:
                    command += '\nfrom softwares.maya_wizard.export_anim import export_anim\n'
                    command += 'export_anim("{}", "{}", {}, frange = {}).export_cam()'.format(utils.asset_to_string(self.asset),
                                                                                            self.asset.file.replace('\\', '/'),
                                                                                            cam_nspace_list,
                                                                                            self.out_range)

            if command != '':

                file = utils.temp_file_from_command(command)
                mayapy = prefs.software(defaults._mayapy_).path
                env = software.get_env(defaults._mayapy_, 0)

                self.ui_subprocess_manager = ui_subprocess_manager.Main([mayapy, "-u", file], env)
                build.launch_normal_as_child(self.ui_subprocess_manager, minimized = 1)

                self.hide()

            else:
                logger.warning('Nothing to export !')

        else:
            logger.warning("Please enter a valid frame range")

    def playblast(self):
        if self.out_range:
            if self.asset.software == defaults._maya_ or self.asset.software == defaults._maya_yeti_:

                show_ornaments = self.ui.playblast_ornaments_checkBox.isChecked()
                show_playblast = self.ui.playblast_show_checkBox.isChecked()
                items_list = self.ui.export_ma_assets_listWidget.selectedItems()

                nspace_list = []
                for item in items_list:
                    nspace_list.append(item.text())
                if nspace_list != [] and len(nspace_list) == 1:

                    env_path = os.path.abspath('softwares_env').replace('\\', '/')

                    command = 'import sys\nsys.path.append("{}")\n'.format(env_path)
                    command += 'from wizard.tools.playblast import playblast\n'
                    command += 'playblast("{}", {}).playblast("{}", {}, {})'.format(utils.asset_to_string(self.asset),
                                                                                        self.out_range, nspace_list[-1],
                                                                                        show_ornaments, show_playblast)

                    file = utils.temp_file_from_command(command)
                    
                    python_system = 'pywizard'
                    if sys.argv[0].endswith('.py'):
                        python_system = 'python'

                    self.ui_subprocess_manager = ui_subprocess_manager.Main("{} {}".format(python_system, file))
                    build.launch_normal_as_child(self.ui_subprocess_manager, minimized = 1)

                    self.hide()

                else:
                    logger.warning("Please select one camera")      
        else:
            logger.warning("Please enter a valid frame range")
