from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QFileDialog, QApplication

from gui.manual_export_dialog import Ui_Dialog
from wizard.vars import defaults
from wizard.tools import log
from wizard.tools import utility as utils
from wizard.project import wall
import shutil
from wizard.prefs import project as project_prefs
from wizard.tools.maketx import maketx
import os
import time
import ui_subprocess_manager
from gui import build

logger = log.pipe_log()


class Main(QtWidgets.QDialog):

    def __init__(self, asset):
        super(Main, self).__init__()
        # Build the ui from ui converted file
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.asset = asset
        extension_dic = project_prefs.get_extension_dic()
        self.extension = extension_dic[self.asset.stage]
        self.max_count = defaults._pub_count_dic_[self.asset.stage]
        self.ui.manual_export_listView = manual_export_listView(self.extension, self.max_count)
        self.ui.horizontalLayout_5.addWidget(self.ui.manual_export_listView)
        self.ui.manual_export_pushButton.setIcon(QtGui.QIcon(defaults._manual_publish_icon_))
        self.ui.folder_pushButton.setIcon(QtGui.QIcon(defaults._folder_icon_))
        self.ui.clear_pushButton.setIcon(QtGui.QIcon(defaults._trash_icon_))
        self.init_ui()
        self.connect_functions()

    def init_ui(self):
        self.ui.manual_export_image_label.setPixmap(
            QtGui.QPixmap(defaults._nodes_icons_dic_[self.asset.stage]).scaled(40, 40, QtCore.Qt.KeepAspectRatio,
                                                                               QtCore.Qt.SmoothTransformation))
        self.ui.manual_export_asset_name_label.setText(
            f'{self.asset.category} | {self.asset.name} | {self.asset.stage} | {self.asset.variant}')

        if self.asset.stage != defaults._texturing_:
            self.ui.texture_tex_check_frame.setVisible(0)

    def connect_functions(self):
        self.ui.clear_pushButton.clicked.connect(self.ui.manual_export_listView.remove_item)
        self.ui.manual_export_pushButton.clicked.connect(self.export)
        self.ui.folder_pushButton.clicked.connect(self.open_file)

    def open_file(self):
        options = QFileDialog.Options()
        fileList, _ = QFileDialog.getOpenFileNames(self, "QFileDialog.getOpenFileNames()", "",
                                                  "All Files (*);", options=options)
        if fileList:
            for file in fileList:
                self.ui.manual_export_listView.add_item(file)

    def export(self):
        files_list = self.ui.manual_export_listView.all_items()

        if files_list != [] and files_list and len(files_list) == 1:

            export_file = self.asset.export('{}_{}'.format(self.asset.name, self.asset.variant))
            shutil.copyfile(files_list[0], export_file)
            wall.wall().publish_event(self.asset)
            self.accept()

        elif files_list != [] and files_list and len(files_list) > 1:
            
            export_files = self.asset.export_multiple('{}_{}'.format(self.asset.name, self.asset.variant), files_list)
            exported_files_list = []
            
            for file in files_list:

                index = files_list.index(file)
                shutil.copyfile(file, export_files[index])
                exported_files_list.append(export_files[index])

            if self.asset.stage == defaults._texturing_:

                tex_creation = self.ui.create_tex_comboBox.currentText()

                if tex_creation != 'Nothing':

                    command = "from wizard.tools.maketx import maketx"
                    command += "\nmaketx({}, '{}').start()".format(exported_files_list, tex_creation)

                    temp_file = utils.temp_file_from_command(command)

                    env = os.environ.copy()

                    wizard_path = os.path.abspath('')

                    rel_site_script_path = os.path.join(defaults._softwares_scripts_path_)
                    abs_site_script_path = os.path.abspath(rel_site_script_path)

                    env[defaults._script_software_env_dic_[defaults._mayapy_]] = abs_site_script_path
                    env[defaults._script_software_env_dic_[defaults._mayapy_]] += os.pathsep + wizard_path + '\\softwares_env'

                    cwd = os.path.abspath("")

                    self.ui_subprocess_manager = ui_subprocess_manager.Main('pywizard {}'.format(temp_file), env, cwd)
                    build.launch_normal_as_child(self.ui_subprocess_manager)
                
            self.accept()

            wall.wall().publish_event(self.asset)
            


        else:
            logger.warning('No files to export...')

    def closeEvent(self, event):
        event.ignore()
        self.hide()

class manual_export_listView(QtWidgets.QListWidget):
    def __init__(self, extension, max_count):
        super(manual_export_listView, self).__init__()
        self.setAcceptDrops(True)
        self.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.extension = extension
        self.max_count = max_count

    def dragEnterEvent(self, event):
        self.setStyleSheet('border : 2px solid gray;')
        data = event.mimeData()
        urls = data.urls()
        if urls and urls[0].scheme() == 'file':
            event.acceptProposedAction()

    def dragMoveEvent(self, event):
        data = event.mimeData()
        urls = data.urls()
        if urls and urls[0].scheme() == 'file':
            event.acceptProposedAction()

    def dragLeaveEvent(self, event):
        self.setStyleSheet('border : 2px solid transparent;')

    def dropEvent(self, event):
        self.setStyleSheet('border : 2px solid transparent;')
        data = event.mimeData()
        urls = data.urls()

        for url in urls:
            if self.count() >= self.max_count:
                logger.warning('Too many files...')
            else:
                if url and url.scheme() == 'file':
                    path = str(url.path())[1:]
                    self.add_item(path)

    def add_item(self, path):
        if path.split('.')[-1] == self.extension:
            self.addItem(path)
        else:
            logger.warning(f'{path} is not a valid {self.extension} file !')

    def all_items(self):
        all_items = []
        for index in range(self.count()):
            all_items.append(self.item(index).text())
        return all_items

    def remove_item(self):
        selection = self.selectedItems()
        for item in selection:
            self.takeItem(self.row(item))

    def read_file(self, filepath):
        pass
