# coding: utf8

# Import PyQt5 libraries
from PyQt5 import QtWidgets, QtCore, QtGui

# Import wizard gui libraries
from gui.project_workflow import Ui_Form
from gui import build

# Import wizard core libraries
from wizard.tools import log
from wizard.vars import defaults
from wizard.prefs.main import prefs
from wizard.prefs import project as project_prefs

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
        self.fill_ui()

    def fill_ui(self):
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
        self.ui.p_w_painter_template_label.setPixmap(
                    QtGui.QPixmap(defaults._stage_icon_[defaults._painter_template_]).scaled(ICON_SIZE, ICON_SIZE, QtCore.Qt.KeepAspectRatio,
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
