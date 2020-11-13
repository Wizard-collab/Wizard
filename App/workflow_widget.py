from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import pyqtSignal
from gui import build

from gui.workflow_widget import Ui_Form
from wizard.vars import defaults
import os
import sys

site_path = os.path.join(os.environ[defaults._wizard_site_], defaults._site_)
stats_path = os.path.join(os.environ[defaults._wizard_site_], defaults._stats_)

os.environ[defaults._site_var_] = site_path
os.environ[defaults._abs_site_path_] = os.path.abspath('')
os.environ[defaults._stats_var_] = stats_path

from wizard.tools import log
from wizard.tools import utility as utils
from wizard.prefs.main import prefs
import traceback

logger = log.pipe_log(__name__)
prefs = prefs()

class Main(QtWidgets.QWidget):

    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.custom_pub_ext_dic = prefs.custom_pub_ext_dic
        self.fill_ui()
        self.connect_functions()

    def fill_ui(self):
        stages_list = self.custom_pub_ext_dic.keys()
        sorted_stages = sorted(stages_list, key=lambda x: list(defaults._pub_ext_list_dic_.keys()).index(x))

        widget = domain_widget(defaults._assets_)
        self.ui.main_layout.addWidget(widget)

        for stage in sorted_stages:
            widget = stage_widget(stage, self.custom_pub_ext_dic[stage])
            self.ui.main_layout.addWidget(widget)
            widget.update_dic.connect(self.update_dic)
            if stage == defaults._shading_:
                widget = domain_widget(defaults._library_)
                self.ui.main_layout.addWidget(widget)
            if stage == defaults._material_:
                widget = domain_widget(defaults._sequences_)
                self.ui.main_layout.addWidget(widget)

    def update_dic(self, list):
        self.custom_pub_ext_dic[list[0]] = list[1]

    def connect_functions(self):
        self.ui.save_w_pushButton.clicked.connect(self.save)

    def save(self):
        prefs.set_custom_pub_ext_dic(self.custom_pub_ext_dic)
        logger.info("Workflow successfully saved")

class domain_widget(QtWidgets.QFrame):
    def __init__(self, domain):
        super(domain_widget, self).__init__()
        self.domain = domain
        self.init_ui()
        self.setObjectName("workflow_domain_widget")

    def init_ui(self):
        layout = QtWidgets.QHBoxLayout()
        label_icon = QtWidgets.QLabel()
        label_icon.setMaximumSize(QtCore.QSize(24, 24))
        label_icon.setMinimumSize(QtCore.QSize(24, 24))
        label_icon.setPixmap(QtGui.QPixmap(defaults._domain_icons_[self.domain]).scaled(20, 20, QtCore.Qt.KeepAspectRatio,
                                                                              QtCore.Qt.SmoothTransformation))
        domain_text = QtWidgets.QLabel(self.domain)
        layout.addWidget(label_icon)
        layout.addWidget(domain_text)
        self.setLayout(layout)

class stage_widget(QtWidgets.QFrame):

    update_dic = pyqtSignal(list)

    def __init__(self, stage, dic):
        super(stage_widget, self).__init__()
        self.stage = stage
        self.dic = dic
        self.init_ui()
        self.update_exts()
        self.connect_functions()
        self.setObjectName("workflow_stage_widget")

    def init_ui(self):
        layout = QtWidgets.QHBoxLayout()
        icon_label = QtWidgets.QLabel()
        icon_label.setMaximumSize(QtCore.QSize(16, 16))
        icon_label.setMinimumSize(QtCore.QSize(16, 16))
        icon_label.setPixmap(QtGui.QPixmap(defaults._stage_icon_[self.stage]).scaled(16, 16, QtCore.Qt.KeepAspectRatio,
                                                                              QtCore.Qt.SmoothTransformation))
        stage_label = QtWidgets.QLabel(self.stage)
        self.software_cbbox = QtWidgets.QComboBox()
        for software in defaults._pub_ext_list_dic_[self.stage].keys():
            self.software_cbbox.addItem(software)
        self.ext_cbbox = QtWidgets.QComboBox()
        layout.addWidget(icon_label)
        layout.addWidget(stage_label)
        layout.addWidget(self.software_cbbox)
        layout.addWidget(self.ext_cbbox)
        self.setLayout(layout)

    def update_exts(self):
        try:
            self.ext_cbbox.currentTextChanged.disconnect()
        except TypeError:
            pass
        software = self.get_software()
        self.ext_cbbox.clear()
        for ext in defaults._pub_ext_list_dic_[self.stage][software]:
            self.ext_cbbox.addItem(ext)
        ext = self.dic[software]
        self.ext_cbbox.setCurrentIndex(defaults._pub_ext_list_dic_[self.stage][software].index(ext))
        self.ext_cbbox.currentTextChanged.connect(self.emit_dic)

    def get_software(self):
        software = self.software_cbbox.currentText()
        return software

    def get_ext(self):
        ext = self.ext_cbbox.currentText()
        return ext

    def emit_dic(self):
        software = self.get_software()
        ext = self.get_ext()
        self.dic[software] = ext
        self.update_dic.emit([self.stage, self.dic])
        self.ext_cbbox.setStyleSheet("border:1px solid orange;")

    def connect_functions(self):
        self.software_cbbox.currentTextChanged.connect(self.update_exts)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(defaults._file_viewer_ico_))
    widget = Main()
    build.launch_normal(widget)