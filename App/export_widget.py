from PyQt5 import QtWidgets, QtCore, QtGui

import os
from gui.export_widget import Ui_Form
from gui import build
from wizard.vars import defaults
from wizard.tools import log
from wizard.prefs.main import prefs
import options_widget
import dialog_comment
from wizard.tools.tx_from_files import tx_from_files
from wizard.prefs import project as project_prefs

logger = log.pipe_log()

prefs = prefs()

class Main(QtWidgets.QWidget):

    def __init__(self, asset, sanity, count):
        super(Main, self).__init__()
        # Build the ui from ui converted file
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.sanity = sanity
        self.count = count
        self.asset = asset
        self.init_ui()
        self.connect_functions()

    def init_ui(self):
        self.ui.export_widget_folder_pushButton.setIcon(QtGui.QIcon(defaults._folder_icon_))
        self.ui.export_widget_comment_pushButton.setIcon(QtGui.QIcon(defaults._comment_icon_))
        self.ui.export_widget_tx_pushButton.setIcon(QtGui.QIcon(defaults._tx_icon_))
        icon = defaults._export_list_neutral_icon_
        export_prefs = prefs.asset(self.asset).export

        self.ui.export_widget_version_label.setText(self.asset.export_version)
        self.ui.export_widget_comment_label.setText(export_prefs.version_comment)
        self.ui.export_widget_date_label.setText(export_prefs.version_date)
        self.ui.export_widget_user_label.setText(export_prefs.version_user)
        try:
            self.ui.export_widget_software_label.setText(f'From {export_prefs.version_software}')
        except:
            pass
        if self.count:
            self.ui.list_export_widget_frame.setStyleSheet('''#list_export_widget_frame{background-color:rgba(255,255,255,5);}
                #list_export_widget_frame:hover{
                
                }''')

        if self.asset.stage != defaults._texturing_:
            self.ui.export_widget_tx_pushButton.setVisible(0)
            self.ui.tx_line.setVisible(0)

        self.update_sanity(self.sanity)

    def update_sanity(self, sanity):
        if sanity:
            list_dir = os.listdir(prefs.asset(self.asset).export.version_folder)
            if list_dir == [] or not list_dir:
                icon = defaults._missing_file_export_list_icon_
            else:
                if defaults._pub_ext_dic_[self.asset.stage][prefs.asset(self.asset).export.version_software] in list_dir[0]:
                    icon = defaults._export_list_icon_
                else:
                    icon = defaults._missing_file_export_list_icon_
        else:
            icon = defaults._export_list_neutral_icon_
        self.ui.export_widget_image_label.setPixmap(
            QtGui.QPixmap(icon).scaled(22, 22, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.RightButton:
            self.show_options_menu()

    def show_options_menu(self):
        self.options_widget = options_widget.Main()
        self.options_widget.add_item('Explorer', self.open_folder)
        build.launch_options(self.options_widget)

    def open_folder(self):
        file = prefs.asset(self.asset).export.version_folder
        os.startfile(file)

    def change_comment(self):
        self.dialog_comment = dialog_comment.Main(self.asset)
        build.launch_dialog_comment(self.dialog_comment)
        self.ui.export_widget_comment_label.setText(self.dialog_comment.comment)

    def make_tx(self):
        folder = prefs.asset(self.asset).export.version_folder
        file_names_list = os.listdir(folder)
        files_list = []

        extension = defaults._pub_ext_dic_[self.asset.stage][self.asset.software]

        for file in file_names_list:
            if file.endswith(extension):
                files_list.append(os.path.join(folder, file))
        tx_from_files(files_list)

    def connect_functions(self):
        self.ui.export_widget_folder_pushButton.clicked.connect(self.open_folder)
        self.ui.export_widget_comment_pushButton.clicked.connect(self.change_comment)
        self.ui.export_widget_tx_pushButton.clicked.connect(self.make_tx)

    def closeEvent(self, event):
        event.ignore()
        self.hide()
