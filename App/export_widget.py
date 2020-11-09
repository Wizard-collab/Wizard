from PyQt5 import QtWidgets, QtCore, QtGui

import os
#from gui.export_widget import Ui_Form
from editable_list_widget import list_widget
from gui import build
from wizard.vars import defaults
from wizard.tools import log
from wizard.prefs.main import prefs
import options_widget
import dialog_comment
from wizard.tools.tx_from_files import tx_from_files
from wizard.prefs import project as project_prefs

logger = log.pipe_log(__name__)

prefs = prefs()

class Main(list_widget):

    def __init__(self, asset, sanity, count):
        super(Main, self).__init__()
        self.sanity = sanity
        self.count = count
        self.asset = asset
        self.init_ui()
        self.connect_functions()

    def init_ui(self):

        self.export_widget_folder_pushButton = self.add_button(defaults._folder_icon_)
        self.export_widget_comment_pushButton = self.add_button(defaults._comment_icon_)
        self.export_widget_tx_pushButton = self.add_button(defaults._tx_icon_)
        icon = defaults._export_list_neutral_icon_
        export_prefs = prefs.asset(self.asset).export
        self.export_widget_version_label = self.add_label(self.asset.export_version, "export_widget_version_label", 40)
        self.export_widget_user_label = self.add_label(export_prefs.version_user, "export_widget_user_label", 120)
        self.export_widget_date_label = self.add_label(export_prefs.version_date, "export_widget_date_label", 180)
        self.export_widget_comment_label = self.add_label(export_prefs.version_comment, "export_widget_comment_label", 230, QtCore.Qt.AlignLeft)
        try:
            self.ui.export_widget_software_label.setText(f'From {export_prefs.version_software}')
        except:
            pass
        if self.asset.stage != defaults._texturing_:
            self.export_widget_tx_pushButton.setVisible(0)
        self.update_sanity(self.sanity)

    def update_sanity(self, sanity):
        if sanity:
            list_dir = os.listdir(prefs.asset(self.asset).export.version_folder)
            if list_dir == [] or not list_dir:
                icon = defaults._missing_file_export_list_icon_
            else:
                if (project_prefs.get_custom_pub_ext_dic())[self.asset.stage][prefs.asset(self.asset).export.version_software] in list_dir[0]:
                    icon = defaults._export_list_icon_
                else:
                    icon = defaults._missing_file_export_list_icon_
        else:
            icon = defaults._export_list_neutral_icon_
        self.set_icon(icon)

    def open_folder(self):
        file = prefs.asset(self.asset).export.version_folder
        os.startfile(file)

    def change_comment(self):
        self.dialog_comment = dialog_comment.Main(self.asset)
        if build.launch_dialog_comment(self.dialog_comment):
            self.export_widget_comment_label.setText(self.dialog_comment.comment)

    def make_tx(self):
        folder = prefs.asset(self.asset).export.version_folder
        file_names_list = os.listdir(folder)
        files_list = []
        extension = (project_prefs.get_custom_pub_ext_dic())[self.asset.stage][self.asset.software]
        for file in file_names_list:
            if file.endswith(extension):
                files_list.append(os.path.join(folder, file))
        tx_from_files(files_list)

    def connect_functions(self):
        self.export_widget_folder_pushButton.clicked.connect(self.open_folder)
        self.export_widget_comment_pushButton.clicked.connect(self.change_comment)
        self.export_widget_tx_pushButton.clicked.connect(self.make_tx)

    def closeEvent(self, event):
        event.ignore()
        self.hide()
