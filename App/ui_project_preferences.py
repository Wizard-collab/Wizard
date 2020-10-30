# coding: utf8

# Import PyQt5 libraries
from PyQt5 import QtWidgets, QtCore, QtGui

# Import wizard gui libraries
from gui.project_preferences import Ui_Form
from gui import build

# Import wizard core libraries
from wizard.tools import log
from wizard.vars import defaults
from wizard.prefs.main import prefs
from wizard.prefs import project as project_prefs
from wizard.prefs import software as software_prefs
from wizard.vars import softwares

# Import wizard widgets
import project_widget

# Import python base libraries
import sys

# Init main logger
logger = log.pipe_log(__name__)

ICON_SIZE = 18

class Main(QtWidgets.QWidget):

    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.fill_project_settings()
        self.ui.save_prefs_pushButton.clicked.connect(self.save_prefs)
        self.init_listWidget()
        self.update_softwares()
        self.refresh_ui()
        self.connect_functions()
        self.fill_workflow_ui()

    def init_listWidget(self):
        self.ui.preferences_ui_listWidget.FocusPolicy = QtCore.Qt.NoFocus
        self.ui.preferences_ui_listWidget.setCurrentRow(0)
        self.ui.preferences_ui_listWidget.currentRowChanged.connect(self.ui.stackedWidget.setCurrentIndex)

    def fill_project_settings(self):
        self.custom_ext_dic = project_prefs.get_custom_pub_ext_dic()
        format = project_prefs.get_format()
        format_width = format[0]
        format_height = format[1]
        fur_ext = self.custom_ext_dic[defaults._cfx_][defaults._maya_]
        self.ui.f_width_lineEdit.setText(str(format_width))
        self.ui.f_height_lineEdit.setText(str(format_height))
        if fur_ext == 'fur':
            index = 0
        else:
            index = 1
        self.ui.cfx_ext_comboBox.setCurrentIndex(index)
        f_rate = project_prefs.get_frame_rate()
        self.ui.frame_rate_spinBox.setValue(f_rate)

    def save_prefs(self):
        format_width = self.ui.f_width_lineEdit.text()
        format_height = self.ui.f_height_lineEdit.text()
        format = [format_width, format_height]
        fur_ext = (self.ui.cfx_ext_comboBox.currentText()).replace('.', '')
        self.custom_ext_dic[defaults._cfx_][defaults._maya_] = fur_ext
        self.custom_ext_dic[defaults._cfx_][defaults._maya_yeti_] = fur_ext
        frame_rate = self.ui.frame_rate_spinBox.value()
        project_prefs.set_frame_rate(frame_rate)
        project_prefs.set_format(format)
        project_prefs.set_custom_pub_ext_dic(self.custom_ext_dic)
        logger.info("Preferences saved !")
        self.hide()

    def refresh_ui(self):
        self.update_launch_button()
        software = self.ui.setup_softwares_comboBox.currentText()
        executable = software_prefs.software(software).get_path()
        command = softwares._cmd_dic_[software]
        env = software_prefs.software(software).get_env()
        env_paths = software_prefs.software(software).get_env_paths()
        if executable:
            self.ui.executable_lineEdit.setText(executable)
        else:
            self.ui.executable_lineEdit.clear()

        self.ui.command_lineEdit.setText(command)

        if env:
            self.ui.additionnal_textEdit.setText(env)
        else:
            self.ui.additionnal_textEdit.clear()
        if env_paths:
            self.ui.env_textEdit.setText(env_paths)
        else:
            self.ui.env_textEdit.clear()

    def update_softwares(self):
        for software in defaults._softwares_list_:
            self.ui.setup_softwares_comboBox.addItem(software)

    def update_launch_button(self):
        current_software = self.ui.setup_softwares_comboBox.currentText()
        if current_software:
            icon = defaults._soft_icons_dic_[current_software]
            self.ui.save_setup_pushButton.setIcon(QtGui.QIcon(icon))
            self.ui.save_setup_pushButton.setIconSize(QtCore.QSize(28, 28))

    def update_prefs(self):
        executable = self.ui.executable_lineEdit.text()
        scripts_path = self.ui.additionnal_textEdit.toPlainText()
        env_paths = self.ui.env_textEdit.toPlainText()
        software = self.ui.setup_softwares_comboBox.currentText()
        if executable.endswith('"'):
            executable = executable[:-1]
        if executable.startswith('"'):
            executable = executable[1:]
        software_prefs.software(software).init_settings(executable, env_paths, scripts_path)

    def connect_functions(self):
        self.ui.setup_softwares_comboBox.currentIndexChanged.connect(self.refresh_ui)
        self.ui.save_setup_pushButton.clicked.connect(self.update_prefs)

    def fill_workflow_ui(self):
        self.ui.p_w_modeling_label.setPixmap(
                    QtGui.QPixmap(defaults._stage_icon_[defaults._geo_]).scaled(ICON_SIZE, ICON_SIZE, QtCore.Qt.KeepAspectRatio,
                                                                              QtCore.Qt.SmoothTransformation))
        self.ui.p_w_rigging_label.setPixmap(
                    QtGui.QPixmap(defaults._stage_icon_[defaults._rig_]).scaled(ICON_SIZE, ICON_SIZE, QtCore.Qt.KeepAspectRatio,
                                                                              QtCore.Qt.SmoothTransformation))
        self.ui.p_w_grooming_label.setPixmap(
                    QtGui.QPixmap(defaults._stage_icon_[defaults._hair_]).scaled(ICON_SIZE, ICON_SIZE, QtCore.Qt.KeepAspectRatio,
                                                                              QtCore.Qt.SmoothTransformation))
        self.ui.p_w_texturing_label.setPixmap(
                    QtGui.QPixmap(defaults._stage_icon_[defaults._texturing_]).scaled(ICON_SIZE, ICON_SIZE, QtCore.Qt.KeepAspectRatio,
                                                                              QtCore.Qt.SmoothTransformation))
        self.ui.p_w_shading_label.setPixmap(
                    QtGui.QPixmap(defaults._stage_icon_[defaults._shading_]).scaled(ICON_SIZE, ICON_SIZE, QtCore.Qt.KeepAspectRatio,
                                                                              QtCore.Qt.SmoothTransformation))
        self.ui.p_w_autorig_label.setPixmap(
                    QtGui.QPixmap(defaults._stage_icon_[defaults._autorig_]).scaled(ICON_SIZE, ICON_SIZE, QtCore.Qt.KeepAspectRatio,
                                                                              QtCore.Qt.SmoothTransformation))
        self.ui.p_w_camera_rig_label.setPixmap(
                    QtGui.QPixmap(defaults._stage_icon_[defaults._cam_rig_]).scaled(ICON_SIZE, ICON_SIZE, QtCore.Qt.KeepAspectRatio,
                                                                              QtCore.Qt.SmoothTransformation))
        self.ui.p_w_cyclo_label.setPixmap(
                    QtGui.QPixmap(defaults._stage_icon_[defaults._cyclo_]).scaled(ICON_SIZE, ICON_SIZE, QtCore.Qt.KeepAspectRatio,
                                                                              QtCore.Qt.SmoothTransformation))
        self.ui.p_w_fx_setup_label.setPixmap(
                    QtGui.QPixmap(defaults._stage_icon_[defaults._fx_setup_]).scaled(ICON_SIZE, ICON_SIZE, QtCore.Qt.KeepAspectRatio,
                                                                              QtCore.Qt.SmoothTransformation))
        self.ui.p_w_gizmo_label.setPixmap(
                    QtGui.QPixmap(defaults._stage_icon_[defaults._gizmo_]).scaled(ICON_SIZE, ICON_SIZE, QtCore.Qt.KeepAspectRatio,
                                                                              QtCore.Qt.SmoothTransformation))
        self.ui.p_w_light_rig_label.setPixmap(
                    QtGui.QPixmap(defaults._stage_icon_[defaults._light_rig_]).scaled(ICON_SIZE, ICON_SIZE, QtCore.Qt.KeepAspectRatio,
                                                                              QtCore.Qt.SmoothTransformation))
        self.ui.p_w_lut_label.setPixmap(
                    QtGui.QPixmap(defaults._stage_icon_[defaults._lut_]).scaled(ICON_SIZE, ICON_SIZE, QtCore.Qt.KeepAspectRatio,
                                                                              QtCore.Qt.SmoothTransformation))
        self.ui.p_w_material_label.setPixmap(
                    QtGui.QPixmap(defaults._stage_icon_[defaults._material_]).scaled(ICON_SIZE, ICON_SIZE, QtCore.Qt.KeepAspectRatio,
                                                                              QtCore.Qt.SmoothTransformation))
        self.ui.p_w_render_graph_label.setPixmap(
                    QtGui.QPixmap(defaults._stage_icon_[defaults._render_graph_]).scaled(ICON_SIZE, ICON_SIZE, QtCore.Qt.KeepAspectRatio,
                                                                              QtCore.Qt.SmoothTransformation))
        self.ui.p_w_render_pass_label.setPixmap(
                    QtGui.QPixmap(defaults._stage_icon_[defaults._render_pass_]).scaled(ICON_SIZE, ICON_SIZE, QtCore.Qt.KeepAspectRatio,
                                                                              QtCore.Qt.SmoothTransformation))
        self.ui.p_w_scripts_label.setPixmap(
                    QtGui.QPixmap(defaults._stage_icon_[defaults._scripts_]).scaled(ICON_SIZE, ICON_SIZE, QtCore.Qt.KeepAspectRatio,
                                                                              QtCore.Qt.SmoothTransformation))
        self.ui.p_w_sounds_label.setPixmap(
                    QtGui.QPixmap(defaults._stage_icon_[defaults._sons_]).scaled(ICON_SIZE, ICON_SIZE, QtCore.Qt.KeepAspectRatio,
                                                                              QtCore.Qt.SmoothTransformation))
        self.ui.p_w_stockshots_label.setPixmap(
                    QtGui.QPixmap(defaults._stage_icon_[defaults._stockshot_]).scaled(ICON_SIZE, ICON_SIZE, QtCore.Qt.KeepAspectRatio,
                                                                              QtCore.Qt.SmoothTransformation))
        self.ui.p_w_video_label.setPixmap(
                    QtGui.QPixmap(defaults._stage_icon_[defaults._video_]).scaled(ICON_SIZE, ICON_SIZE, QtCore.Qt.KeepAspectRatio,
                                                                              QtCore.Qt.SmoothTransformation))
        self.ui.p_w_concept_label.setPixmap(
                    QtGui.QPixmap(defaults._stage_icon_[defaults._concept_]).scaled(ICON_SIZE, ICON_SIZE, QtCore.Qt.KeepAspectRatio,
                                                                              QtCore.Qt.SmoothTransformation))
        self.ui.p_w_layout_label.setPixmap(
                    QtGui.QPixmap(defaults._stage_icon_[defaults._layout_]).scaled(ICON_SIZE, ICON_SIZE, QtCore.Qt.KeepAspectRatio,
                                                                              QtCore.Qt.SmoothTransformation))
        self.ui.p_w_animation_label.setPixmap(
                    QtGui.QPixmap(defaults._stage_icon_[defaults._animation_]).scaled(ICON_SIZE, ICON_SIZE, QtCore.Qt.KeepAspectRatio,
                                                                              QtCore.Qt.SmoothTransformation))
        self.ui.p_w_lighting_label.setPixmap(
                    QtGui.QPixmap(defaults._stage_icon_[defaults._lighting_]).scaled(ICON_SIZE, ICON_SIZE, QtCore.Qt.KeepAspectRatio,
                                                                              QtCore.Qt.SmoothTransformation))
        self.ui.p_w_cfx_label.setPixmap(
                    QtGui.QPixmap(defaults._stage_icon_[defaults._cfx_]).scaled(ICON_SIZE, ICON_SIZE, QtCore.Qt.KeepAspectRatio,
                                                                              QtCore.Qt.SmoothTransformation))
        self.ui.p_w_fx_label.setPixmap(
                    QtGui.QPixmap(defaults._stage_icon_[defaults._fx_]).scaled(ICON_SIZE, ICON_SIZE, QtCore.Qt.KeepAspectRatio,
                                                                              QtCore.Qt.SmoothTransformation))
        self.ui.p_w_compositing_label.setPixmap(
                    QtGui.QPixmap(defaults._stage_icon_[defaults._compositing_]).scaled(ICON_SIZE, ICON_SIZE, QtCore.Qt.KeepAspectRatio,
                                                                              QtCore.Qt.SmoothTransformation))
        self.ui.p_w_camera_label.setPixmap(
                    QtGui.QPixmap(defaults._stage_icon_[defaults._camera_]).scaled(ICON_SIZE, ICON_SIZE, QtCore.Qt.KeepAspectRatio,
                                                                              QtCore.Qt.SmoothTransformation))
