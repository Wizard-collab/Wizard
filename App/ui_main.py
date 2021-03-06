# coding: utf8

# Importing python base libraries
import os
import traceback
import time
import inspect
import random
import copy
import webbrowser
import sys
from PIL import Image
import pyperclip


# Importing PyQt5 libraries
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import pyqtSignal

# Importing wizard gui libraries
import gui.tree_get as tree_get
import gui.fill_tree as fill
import gui.log_to_gui as log_to_gui
from gui.tree_get import tree
from gui import build
from gui import stats_to_gui
from gui.main import Ui_Wizard

# Importing wizard core libraries
from wizard.asset import main as asset_core
from wizard.asset import save as asset_save
from wizard.vars import defaults
from wizard.project import main as project
from wizard.prefs.main import prefs
import wizard.prefs.project as project_prefs
from wizard.tools import log
from wizard.tools import utility as utils
from wizard.email import main as send_email
from wizard.chat import client
from wizard.signal.signal_server import signal_server
from wizard.prefs.user_scripts import user_scripts
from wizard.user_scripts import user_scripts_library
from wizard.screen_record.screen_record import screen_record
from wizard import api
from wizard.tools.batch_asset_creation import batch_asset_creation
#from wizard.shortcuts.shortcuts_listener import shortcuts_listener

# Importing wizard widgets
import dialog_new_variant
import dialog_softwares_prefs
import ui_image_viewer
import dialog_new_project
import dialog_projects
import dialog_new_user
import dialog_users
import dialog_contact
import log_widget
import popup
import preferences_ui
import wall_widget
import ui_wizard_desktop
import node_editor_widget
import tree_widget
import options_widget
import file_viewer
import ui_subprocess_manager
import user_widget
import jokes_widget
import dialog_delete_asset
import exports_widget
import versions_manager_widget
import reference_list_widget
import running_widget
import dialog_confirm_email
import dialog_shot_creation
import dialog_modify_range
import dialog_asset_creation
import dialog_quit_popup
import ui_welcome
import ui_workflow
import ui_export_manager
import playblasts_widget
import ui_updates
import dialog_merge_projects
import dialog_new_version
import ui_error_handler
import user_scripts_widget
import tickets_widget
import task_progress_info_widget
import ui_about
import ui_project_workflow
import ui_project_preferences
import ui_renamer
import recording_ui
#import chat_house

# Initializing the logger and the prefs module
logger = log.pipe_log()
prefs = prefs()

class Main(QtWidgets.QMainWindow): # The main wizard class

    # Signal emitted when the is moved
    move_signal = pyqtSignal(str)

    def __init__(self):
        try:
            super(Main, self).__init__()

            # Init ui
            self.stylesheet = build.load_stylesheet()
            self.ui = Ui_Wizard()
            self.ui.setupUi(self)
            self.displace_animation = QtCore.QPropertyAnimation(self, b"pos", self)
            self.displace_animation.finished.connect(self.hide)
            #self.resize_window()

            # Init widgets
            self.wizard_version_update()
            self.init_log_widget()
            self.init_log_ui()
            self.init_log_button()
            self.init_locked_assets_button()
            self.init_wall_button()
            self.init_running_button()
            self.init_settings_button()
            self.init_server_button()
            self.init_main_tab()
            self.init_user_widget()
            self.init_jokes_widget()
            self.init_tree_widget()
            self.init_wizard_desktop()
            self.init_pin_button()
            self.init_folder_button()
            self.init_node_editor_widget()
            self.init_reference_list_widget()
            self.init_exports_widget()
            self.init_playblasts_widget()
            self.init_tickets_widget()
            self.init_versions_manager_widget()
            self.init_image()
            self.init_wall_widget()
            self.init_main_refresh_button()
            self.init_user_scripts_widget()
            self.init_sandbox_button()
            self.init_screen_record()
            #self.init_shorcuts()

            # Init vars
            self.prefs = prefs
            self.selected_asset = None
            self.asset = None
            self.old_exports_tab_asset = None
            self.old_graph_tab_asset = None
            self.old_history_tab_asset = None
            self.pin = False
            self.pinned_asset = None

            # Refresh ui and start threads
            self.update_tree(1)
            self.update_infos()
            self.start_stats()
            self.asset_item_changed()
            self.show_updates()
            self.add_user_to_project()
            self.show_task_info_widget()
            self.go_to_tab()
            self.connect_functions()
            self.start_save_thread()
            self.init_local_server()
            self.first_tab_refresh()
            #self.init_chat_house()
            prefs.set_custom_pub_ext_dic()

        except:
            logger.critical(str(traceback.format_exc()))

    def init_chat_house(self):
        self.chat_house = chat_house.Main()

    def show_task_info_widget(self):
        try:
            self.task_progress_info_widget = task_progress_info_widget.Main()
            self.ui.task_info_widget_layout.addWidget(self.task_progress_info_widget)
        except:
            logger.critical(str(traceback.format_exc()))

    def start_save_thread(self):
        self.save_thread = asset_save.save_thread()
        self.save_thread.start()

    def init_local_server(self):
        try:
            self.signal_server = signal_server()
            self.signal_server.refresh_signal.connect(self.refresh_main_ui)
            self.signal_server.refresh_launcher_signal.connect(self.version_changed)
            self.signal_server.log_signal.connect(self.log_widget.ui.log_textEdit.append)
            self.signal_server.focus_signal.connect(self.focus_wizard)
            self.signal_server.save_signal.connect(lambda:popup.popup().save_pop())
            self.signal_server.save_request_signal.connect(self.save_thread.do_save)
            self.signal_server.task_signal.connect(self.task_progress_info_widget.set_progress)
            self.signal_server.task_name_signal.connect(logger.info)
            self.signal_server.start()
        except:
            logger.critical(str(traceback.format_exc()))

    def refresh_main_ui(self):
        try:
            self.update_tree(0)
            self.asset_item_changed()
            self.user_widget.refresh_widget()
            self.user_scripts_widget.refresh_scripts()
            #self.refresh_server(0)
        except:
            logger.critical(str(traceback.format_exc()))

    def init_shorcuts(self):
        self.shortcuts_listener = shortcuts_listener()
        self.shortcuts_listener.start()
        self.shortcuts_listener.screen_record_signal.connect(self.toggle_screen_record)

    def init_screen_record(self):
        self.ui.record_pushButton.setIcon(QtGui.QIcon(defaults._start_record_icon_))
        self.screen_record = screen_record()
        self.ui.record_pushButton.clicked.connect(self.toggle_screen_record)
        self.recording_ui = recording_ui.recording_ui()

    def toggle_screen_record(self):
        if self.screen_record.running:
            logger.info("Record stopped")
            self.screen_record.stop()
            self.ui.record_pushButton.setIcon(QtGui.QIcon(defaults._start_record_icon_))
            self.recording_ui.hide()
        else:
            logger.info("Starting record")
            self.screen_record.start()
            self.ui.record_pushButton.setIcon(QtGui.QIcon(defaults._stop_record_icon_))
            build.launch_normal_as_child_frameless_ontop(self.recording_ui)

    def add_user_to_project(self):
        try:
            project_prefs.add_user(prefs.user)
        except:
            logger.critical(str(traceback.format_exc()))

    def init_main_refresh_button(self):
        try:
            self.ui.refresh_pushButton.setIcon(QtGui.QIcon(defaults._refresh_icon_))
            self.ui.refresh_pushButton.clicked.connect(lambda:self.update_tree(0))
        except:
            logger.critical(str(traceback.format_exc()))

    def init_sandbox_button(self):
        try:
            self.ui.sandbox_pushButton.setIcon(QtGui.QIcon(defaults._sandbox_icon_))
        except:
            logger.critical(str(traceback.format_exc()))

    def show_updates(self, force = None):
        try:
            last_update = prefs.last_update

            version = defaults._wizard_version_

            if prefs.show_updates or last_update != version or force:
                prefs.set_last_update(version)
                prefs.set_show_updates(1)
                self.ui_updates = ui_updates.Main()
                build.launch_normal_as_child_ontop(self.ui_updates)
        except:
            logger.critical(str(traceback.format_exc()))

    def wizard_version_update(self):
        try:
            project.add_material()
            project.add_painter_template()
        except:
            logger.critical(str(traceback.format_exc()))

    def init_main_tab(self):
        try:
            self.ui.main_tabWidget.setTabIcon(0, QtGui.QIcon(defaults._node_icon_))  # <---
            self.ui.main_tabWidget.setTabIcon(1, QtGui.QIcon(defaults._reference_list_icon_))  # <---
            self.ui.main_tabWidget.setTabIcon(2, QtGui.QIcon(defaults._export_icon_))  # <---
            self.ui.main_tabWidget.setTabIcon(3, QtGui.QIcon(defaults._versions_manager_icon_))  # <---
            self.ui.main_tabWidget.setTabIcon(4, QtGui.QIcon(defaults._playblast_icon_))  # <---
            self.ui.main_tabWidget.setTabIcon(5, QtGui.QIcon(defaults._tickets_icon_))  # <---
            self.ui.main_tabWidget.setIconSize(QtCore.QSize(18, 18))
        except:
            logger.critical(str(traceback.format_exc()))

    def init_user_widget(self):
        try:
            self.user_widget = user_widget.Main()
            self.ui.user_widget_layout.insertWidget(0, self.user_widget)
        except:
            logger.critical(str(traceback.format_exc()))

    def init_user_scripts_widget(self):
        try:
            self.user_scripts_widget = user_scripts_widget.Main()
            self.ui.user_scripts_layout.addWidget(self.user_scripts_widget)
        except:
            logger.critical(str(traceback.format_exc()))

    def init_jokes_widget(self):
        try:
            self.jokes_widget = jokes_widget.Main()
            self.ui.jokes_widget_layout.insertWidget(0, self.jokes_widget)
            self.jokes_thread = jokes_widget.jokes_thread(self.jokes_widget)
            self.jokes_thread.start()
        except:
            logger.critical(str(traceback.format_exc()))

    def init_tree_widget(self):
        try:
            self.ui.treeWidget = tree_widget.treeWidget(self)
        except:
            logger.critical(str(traceback.format_exc()))

    def init_folder_button(self):
        try:
            self.ui.open_folder_pushButton.setIcon(QtGui.QIcon(defaults._folder_icon_))
            self.ui.open_folder_pushButton.setIconSize(QtCore.QSize(18, 18))
        except:
            logger.critical(str(traceback.format_exc()))

    def resize_window(self):
        try:
            self.resize(self.minimumSizeHint())
        except:
            logger.critical(str(traceback.format_exc()))

    def init_wizard_desktop(self):
        try:

            shutter = prefs.shutter

            if shutter:
                self.wizard_desktop = ui_wizard_desktop.wizard_desktop(self)
                build.launch_wizard_desktop(self.wizard_desktop)

        except:
            logger.critical(str(traceback.format_exc()))

    def init_log_button(self):
        try:
            self.ui.log_pushButton.setIcon(QtGui.QIcon(defaults._log_icon_))
            self.ui.log_pushButton.setIconSize(QtCore.QSize(20, 20))
        except:
            logger.critical(str(traceback.format_exc()))

    def init_locked_assets_button(self):
        try:
            self.ui.locked_assets_pushButton.setIcon(QtGui.QIcon(defaults._unlocked_icon_))
            self.ui.locked_assets_pushButton.setIconSize(QtCore.QSize(20, 20))
        except:
            logger.critical(str(traceback.format_exc()))

    def init_running_button(self):
        try:
            self.ui.running_pushButton.setIcon(QtGui.QIcon(defaults._running_icon_))
            self.ui.running_pushButton.setIconSize(QtCore.QSize(20, 20))
        except:
            logger.critical(str(traceback.format_exc()))

    def init_chat_button(self):
        try:
            self.ui.chat_pushButton.setIcon(QtGui.QIcon(defaults._chat_icon_))
            self.ui.chat_pushButton.setIconSize(QtCore.QSize(20, 20))
        except:
            logger.critical(str(traceback.format_exc()))

    def init_settings_button(self):
        try:
            self.ui.settings_pushButton.setIcon(QtGui.QIcon(defaults._settings_icon_))
            self.ui.settings_pushButton.setIconSize(QtCore.QSize(18, 18))
        except:
            logger.critical(str(traceback.format_exc()))

    def set_chat_new_notif_icon(self):
        try:
            self.ui.chat_pushButton.setIcon(QtGui.QIcon(defaults._chat_icon_notif_))
        except:
            logger.critical(str(traceback.format_exc()))

    def init_server_button(self):
        try:
            self.ui.server_pushButton.setIconSize(QtCore.QSize(20, 20))
            self.refresh_conn(client.test_conn_once())
        except:
            logger.critical(str(traceback.format_exc()))

    def restart_wall(self):
        try:
            self.wall_widget.start_wall()
        except:
            logger.critical(str(traceback.format_exc()))

    def refresh_server(self, do_log=1):
        try:
            if client.test_conn_once():
                self.refresh_conn(1, do_log)
                self.restart_wall()
            else:
                self.refresh_conn(0, do_log)
        except:
            logger.critical(str(traceback.format_exc()))

    def refresh_conn(self, is_conn, do_log=1):
        try:
            if is_conn:
                icon = defaults._server_on_icon_
                if do_log:
                    logger.info('Wizard is connected to the server !')
                self.ui.server_pushButton.setIcon(QtGui.QIcon(icon))
            else:
                icon = defaults._server_off_icon_
                logger.warning('Connection with server lost. Please run a server and restart Wizard.')
                self.ui.server_pushButton.setIcon(QtGui.QIcon(icon))
        except:
            logger.critical(str(traceback.format_exc()))
            return 0

    def init_wall_button(self):
        try:
            self.ui.wall_pushButton.setIcon(QtGui.QIcon(defaults._wall_icon_))
            self.ui.wall_pushButton.setIconSize(QtCore.QSize(20, 20))
        except:
            logger.critical(str(traceback.format_exc()))

    def new_notif(self):
        try:
            self.ui.wall_pushButton.setIcon(QtGui.QIcon(defaults._wall_update_icon_))
        except:
            logger.critical(str(traceback.format_exc()))

    def no_new_notif(self):
        try:
            self.ui.wall_pushButton.setIcon(QtGui.QIcon(defaults._wall_icon_))
        except:
            logger.critical(str(traceback.format_exc()))

    def init_pin_button(self):
        try:
            self.ui.pin_pushButton.setIcon(QtGui.QIcon(defaults._unpin_icon_))
            self.ui.pin_pushButton.setIconSize(QtCore.QSize(28, 28))
        except:
            logger.critical(str(traceback.format_exc()))

    def init_log_widget(self):
        try:
            self.log_widget = log_widget.Main()
        except:
            logger.critical(str(traceback.format_exc()))

    def init_node_editor_widget(self):
        try:
            self.node_editor_widget = node_editor_widget.Main(self)
            self.ui.node_editor_layout.addWidget(self.node_editor_widget)
        except:
            logger.critical(str(traceback.format_exc()))

    def init_reference_list_widget(self):
        try:
            self.reference_list_widget = reference_list_widget.Main(self)
            self.ui.reference_list_tab_layout.addWidget(self.reference_list_widget)
        except:
            logger.critical(str(traceback.format_exc()))

    def init_exports_widget(self):
        try:
            self.exports_widget = exports_widget.Main()
            self.ui.exports_layout.addWidget(self.exports_widget)
        except:
            logger.critical(str(traceback.format_exc()))

    def init_playblasts_widget(self):
        try:
            self.playblasts_widget = playblasts_widget.Main()
            self.ui.playblasts_layout.addWidget(self.playblasts_widget)
        except:
            logger.critical(str(traceback.format_exc()))

    def init_tickets_widget(self):
        try:
            self.tickets_widget = tickets_widget.Main()
            self.ui.tickets_layout.addWidget(self.tickets_widget)
        except:
            logger.critical(str(traceback.format_exc()))

    def init_versions_manager_widget(self):
        try:
            self.versions_manager_widget = versions_manager_widget.Main()
            self.versions_manager_widget.open_signal.connect(self.open_str)
            self.versions_manager_widget.refresh_signal.connect(self.asset_item_changed)
            self.ui.versions_manager_layout.addWidget(self.versions_manager_widget)
        except:
            logger.critical(str(traceback.format_exc()))

    def init_wall_widget(self):
        try:
            self.wall_widget = wall_widget.Main(self)
            self.wall_widget.refresh_signal.connect(lambda:self.update_tree(0))
            self.wall_widget.refresh_signal.connect(self.asset_item_changed)
            self.ui.wall_layout.insertWidget(0, self.wall_widget)
            self.wall_widget.hide()
        except:
            logger.critical(str(traceback.format_exc()))

    def open_asset_wall(self):
        try:
            self.asset_wall_widget = wall_widget.Main(self, self.asset)
            build.launch_normal_as_child(self.asset_wall_widget)
        except:
            logger.critical(str(traceback.format_exc()))

    def start_stats(self):
        try:
            self.statThread = stats_to_gui.statThread(self)
            self.statThread.start()
            self.statThread.ram_signal.connect(self.update_ram_stats)
            self.statThread.cpu_signal.connect(self.update_cpu_stats)
        except:
            logger.critical(str(traceback.format_exc()))

    def stop_threads(self):
        try:
            self.statThread.stop()
            self.signal_server.stop()
            self.jokes_thread.quit()
            self.wall_widget.quit_wall()
        except:
            logger.critical(str(traceback.format_exc()))

    def update_ram_stats(self, percent):
        try:
            self.ui.ram_progressBar.setValue(percent)
            self.ui.ram_progressBar.setFormat('%.02f%%' % (percent))
        except:
            logger.critical(str(traceback.format_exc()))

    def update_cpu_stats(self, percent):
        try:
            self.ui.cpu_progressBar.setValue(percent)
            self.ui.cpu_progressBar.setFormat('%.02f%%' % (percent))
        except:
            logger.critical(str(traceback.format_exc()))

    def update_tree(self, init = None):
        try:
            project_tree = project.read_project()
            if project_tree:
                fill.build_tree(self.ui.treeWidget, project_tree)
                string_asset = self.prefs.context
                if string_asset:
                    asset = asset_core.string_to_asset(string_asset)
                    if asset.domain and asset.category and asset.name and init:
                        self.asset = asset
                        if self.asset.stage:
                            tree_get.select_asset(self.ui.treeWidget, self.asset)
                    else:
                        self.asset = asset_core.asset()
                else:
                    self.asset = asset_core.asset()
        except:
            logger.critical(str(traceback.format_exc()))

    def focus_asset(self, string_asset):
        try:
            asset = asset_core.string_to_asset(string_asset)
            self.asset = asset
            self.selected_asset = asset
            tree_get.select_asset(self.ui.treeWidget, self.asset)
            self.asset_item_changed()
        except:
            logger.critical(str(traceback.format_exc()))

    def update_variants(self):
        try:
            self.connect_variants(0)
            self.ui.variants_comboBox.clear()
            if self.asset.stage:
                variants = self.asset.variants
                main_variant = self.asset_prefs.stage.default_variant
                if self.asset.variants:
                    self.ui.variants_comboBox.addItems(variants)
                    index = variants.index(main_variant)
                    self.ui.variants_comboBox.setCurrentIndex(index)
                    self.asset.variant = main_variant
                    self.variant_changed()
                    self.connect_variants()
                    if self.asset.variant:
                        self.ui.main_frame.setEnabled(1)
                else:
                    self.connect_variants()
                    self.empty_manager()
            else:
                self.connect_variants()
                self.empty_manager() 
        except:
            self.connect_variants()
            logger.critical(str(traceback.format_exc()))

    def connect_variants(self, do = 1):
        if do:
            self.ui.variants_comboBox.currentIndexChanged.connect(self.variant_changed)
        else:
            try:
                self.ui.variants_comboBox.currentIndexChanged.disconnect()
            except TypeError:
                pass

    def empty_manager(self):
        try:
            self.ui.main_frame.setEnabled(0)
            self.ui.software_comboBox.clear()
            self.ui.versions_comboBox.clear()
            self.update_creation_date()
            self.update_creation_user()
            self.ui.asset_comment_textEdit.clear()
            #self.update_tabs()
        except:
            logger.critical(str(traceback.format_exc()))

    def variant_changed(self):
        try:

            variant = self.ui.variants_comboBox.currentText()
            if variant and variant != '':
                self.asset_prefs.stage.set_default_variant(variant)
                self.asset.variant = variant
                self.update_softwares()

        except:
            logger.critical(str(traceback.format_exc()))

    def update_tabs(self):
        try:
            if self.node_editor_widget.isVisible():
                self.node_editor_widget.refresh_scene(self.asset)
            if self.reference_list_widget.isVisible():
                self.reference_list_widget.refresh_scene(self.asset)
            if self.exports_widget.isVisible():
                self.exports_widget.refresh_all(self.asset)
            if self.playblasts_widget.isVisible():
                self.playblasts_widget.refresh_all(self.asset)
            if self.versions_manager_widget.isVisible():
                self.versions_manager_widget.refresh_all(self.asset)
            if self.tickets_widget.isVisible():
                self.tickets_widget.refresh_all(self.asset)
        except:
            logger.critical(str(traceback.format_exc()))

    def first_tab_refresh(self):
        self.node_editor_widget.refresh_scene(self.asset)
        self.reference_list_widget.refresh_scene(self.asset)
        self.exports_widget.refresh_all(self.asset)
        self.playblasts_widget.refresh_all(self.asset)
        self.versions_manager_widget.refresh_all(self.asset)
        self.tickets_widget.refresh_all(self.asset)

    def go_to_tab(self, tab = None):
        try:
            if not tab:
                tab = self.prefs.tab_context
            self.ui.main_tabWidget.setCurrentIndex(tab)
        except:
            logger.critical(str(traceback.format_exc()))

    def main_tab_changed(self, index):
        try:
            if index == 0:
                self.node_editor_widget.refresh_scene(self.asset)
            if index == 1:
                self.reference_list_widget.refresh_scene(self.asset)
            elif index == 2:
                self.exports_widget.refresh_all(self.asset)
            elif index == 3:
                self.versions_manager_widget.refresh_all(self.asset)
            elif index == 4:
                self.playblasts_widget.refresh_all(self.asset)
            elif index == 5:
                self.tickets_widget.refresh_all(self.asset)
            self.prefs.set_tab_context(index)
        except:
            logger.critical(str(traceback.format_exc()))

    def update_softwares(self):
        try:
            self.connect_softwares(0)
            self.ui.software_comboBox.clear()
            if self.asset.stage and self.asset.variant:
                softwares = self.asset.softwares
                default_software = self.asset_prefs.variant.default_software
                if softwares:
                    self.ui.software_comboBox.addItems(softwares)
                    index = softwares.index(default_software)
                    self.ui.software_comboBox.setCurrentIndex(index)
                    self.asset.software = default_software
                    self.software_changed()
                self.connect_softwares()
            else:
                self.connect_softwares()
                self.update_versions()
        except:
            self.connect_softwares()
            logger.critical(str(traceback.format_exc()))

    def connect_softwares(self, do = 1):
        try:
            if do:
                self.ui.software_comboBox.currentIndexChanged.connect(self.software_changed)
            else:
                try:
                    self.ui.software_comboBox.currentIndexChanged.disconnect()
                except TypeError:
                    pass
        except:
            logger.critical(str(traceback.format_exc()))

    def software_changed(self):
        try:
            software = self.ui.software_comboBox.currentText()
            if software:
                self.asset.software = software
                self.asset_prefs.variant.set_default_software(software)
                self.update_versions()
                self.update_launch_button()
                self.update_tabs()
        except:
            logger.critical(str(traceback.format_exc()))

    def update_versions(self):
        try:
            self.connect_versions(0)
            self.ui.versions_comboBox.clear()
            if self.asset.stage and self.asset.variant:
                versions = prefs.asset(self.asset).software.versions#[-10:]
                if versions:
                    self.ui.versions_comboBox.addItems(versions)
                    index = list(versions).index(list(versions)[-1])
                    self.ui.versions_comboBox.setCurrentIndex(index)
                self.version_changed()
                self.connect_versions()
            else:
                self.connect_versions()
                self.update_creation_date()
                self.update_creation_user()
                self.update_comment()
                self.update_image()
        except:
            self.connect_versions()
            logger.critical(str(traceback.format_exc()))

    def connect_versions(self, do = 1):
        try:
            if do:
                self.ui.versions_comboBox.currentIndexChanged.connect(self.version_changed)
            else:
                try:
                    self.ui.versions_comboBox.currentIndexChanged.disconnect()
                except TypeError:
                    pass
        except:
            logger.critical(str(traceback.format_exc()))

    def version_changed(self):
        try:
            version = self.ui.versions_comboBox.currentText()
            self.asset.version = version
            self.update_creation_date()
            self.update_creation_user()
            self.update_comment()
            self.update_image()
            self.update_lock()
            self.ui.current_asset_label.setText(utils.version_asset_to_string(self.asset))
            api.scene.set_current_asset(self.asset)
        except:
            logger.critical(str(traceback.format_exc()))

    def update_creation_date(self):
        try:
            self.ui.asset_date_label.clear()
            if self.asset.variant:
                date = self.asset.date
                self.ui.asset_date_label.setText(date)
            else:
                self.ui.asset_date_label.setText('Date')
        except:
            logger.critical(str(traceback.format_exc()))

    def update_creation_user(self):
        try:
            self.ui.asset_user_label.clear()
            if self.asset.variant:
                user = self.asset.user
                self.ui.asset_user_label.setText(user)
            else:
                self.ui.asset_user_label.setText('User')
        except:
            logger.critical(str(traceback.format_exc()))

    def update_comment(self):
        try:
            self.ui.asset_comment_textEdit.clear()
            if self.asset.stage and self.asset.variant:
                comment = self.asset.comment
                self.ui.asset_comment_textEdit.setText(comment)
        except:
            logger.critical(str(traceback.format_exc()))

    def comment(self):
        try:
            comment = self.ui.asset_comment_textEdit.toPlainText()
            self.asset_prefs.software.set_version_comment(comment)
            logger.info(f'Comment posted, "{comment}"')
        except:
            logger.critical(str(traceback.format_exc()))

    def update_infos(self):
        try:
            user_name = self.prefs.user
            project_name = self.prefs.project_name
            project_path = self.prefs.project_path
            if project_name:
                self.ui.project_name_label.setText(project_name)
                self.ui.project_path_label.setText(project_path)
            else:
                self.ui.project_name_label.setText(defaults._missing_project_)
                self.ui.project_path_label.setText(defaults._missing_project_)
        except:
            logger.critical(str(traceback.format_exc()))

    def init_image(self):
        try:
            self.ui.image_button.setIconSize(QtCore.QSize(363, 228))
        except:
            logger.critical(str(traceback.format_exc()))

    def update_image(self):
        try:
            if self.asset.stage and self.asset.variant:
                image = self.asset.image
                if not os.path.isfile(image):
                    image = defaults._nopicture_image_
                self.ui.image_button.setIcon(QtGui.QIcon(image))
            else:
                image = defaults._nopicture_image_
                self.ui.image_button.setIcon(QtGui.QIcon(image))
            self.resize_image_button(image)
        except:
            logger.critical(str(traceback.format_exc()))

    def resize_image_button(self, image):
        try:
            im = Image.open(image)
            width, height = im.size
            ratio = width/height
            button_height = 363/ratio
            self.ui.image_button.setFixedSize(QtCore.QSize(363, button_height))
        except:
            logger.critical(str(traceback.format_exc()))

    def open_image(self):
        try:
            image = self.asset.image
            self.ui_image_viewer = ui_image_viewer.Main(image)
            build.launch_normal_as_child_frameless(self.ui_image_viewer)
        except:
            logger.critical(str(traceback.format_exc()))

    def update_lock(self):
        try:
            if self.asset.stage and self.asset.variant:
                lock = self.asset_prefs.software.get_lock
                if lock:
                    image = defaults._locked_icon_
                    text = f'Locked ({lock})'
                    if lock != self.prefs.user:
                        self.ui.lock_pushButton.setEnabled(False)
                        self.ui.launch_pushButton.setText(f'Locked by {lock}')
                        self.ui.lock_pushButton.setStyleSheet("#lock_pushButton{background-color: #eb5250;}")
                        self.update_launch_button()
                    else:
                        self.ui.lock_pushButton.setEnabled(True)
                        self.ui.lock_pushButton.setStyleSheet("")
                        self.update_launch_button()
                    self.ui.lock_pushButton.setIcon(QtGui.QIcon(image))
                else:
                    self.reset_lock_button()
            else:
                self.reset_lock_button()
            self.ui.lock_pushButton.setIconSize(QtCore.QSize(32, 32))
        except:
            logger.critical(str(traceback.format_exc()))

    def reset_lock_button(self):
        try:
            image = defaults._unlocked_icon_
            text = 'Lock'
            self.ui.lock_pushButton.setEnabled(True)
            self.ui.launch_pushButton.setEnabled(True)
            self.ui.launch_pushButton_Frame.setEnabled(True)
            self.update_launch_button()
            self.ui.lock_pushButton.setStyleSheet("")
            self.ui.lock_pushButton.setIcon(QtGui.QIcon(image))
        except:
            logger.critical(str(traceback.format_exc()))

    def lock(self):
        try:
            if self.asset.stage:
                lock = self.asset_prefs.software.get_lock
                if lock and self.prefs.user == lock:
                    self.asset_prefs.software.unlock()
                    prefs.remove_lock(utils.short_asset_to_string(self.asset))
                elif lock:
                    logger.warning(f"Asset locked by {lock}, can't unlock")
                else:
                    self.asset_prefs.software.lock()
                    prefs.add_lock(utils.short_asset_to_string(self.asset))
                self.update_lock()
        except:
            logger.critical(str(traceback.format_exc()))

    def create(self, item, in_out=None):
        try:
            self.refresh_asset(item)
            '''
            created = self.selected_asset.create(in_out)
            QApplication.restoreOverrideCursor()
            if not created:
                tree_get.remove_item(item)
            '''
            file = batch_asset_creation(self.selected_asset, in_out)
            env = os.environ.copy()
            python_system = 'pywizard'
            if sys.argv[0].endswith('.py'):
                python_system = 'python'
            self.ui_subprocess_manager = ui_subprocess_manager.Main(f"{python_system} {file}", env, cwd=os.path.abspath(''))
            build.launch_normal_as_child(self.ui_subprocess_manager, minimized = 1)

        except:
            logger.critical(str(traceback.format_exc()))

    def remove_asset(self, item):
        try:
            self.refresh_asset(item)
            self.dialog_delete_asset = dialog_delete_asset.Main()
            if build.launch_dialog_as_child(self.dialog_delete_asset):
                removed = self.selected_asset.remove()
                if removed:
                    tree_get.remove_item(self.ui.treeWidget.currentItem())
                    logger.info('Asset removed from project !')
                self.update_tree()
                self.asset_item_changed()
        except:
            logger.critical(str(traceback.format_exc()))

    def double_click_item(self, item):
        try:
            self.refresh_asset(item)
            if tree_get.check_add_item(item) and \
                    item.text(0) != defaults._new_item_label_ and \
                    item.text(0) != defaults._new_shot_label_:
                self.create(item)
            elif tree_get.check_add_item(item) and \
                    item.text(0) != defaults._new_item_label_ and \
                    item.text(0) == defaults._new_shot_label_:
                self.dialog_shot_creation = dialog_shot_creation.Main()
                if build.launch_running_dialog(self.dialog_shot_creation):
                    name = self.dialog_shot_creation.shot_name
                    inFrame = self.dialog_shot_creation.inFrame
                    outFrame = self.dialog_shot_creation.outFrame
                    item.setText(0, name)
                    self.create(item, [inFrame, outFrame])
            elif item.text(0) == defaults._new_item_label_:
                self.dialog_asset_creation = dialog_asset_creation.Main()
                if build.launch_running_dialog(self.dialog_asset_creation):
                    name = self.dialog_asset_creation.asset_name
                    item.setText(0, name)
                    self.create(item)
            else:
                self.open(item)
        except:
            logger.critical(str(traceback.format_exc()))

    def modify_frame_range(self):
        try:
            frange = self.selected_asset_prefs.name.range
            preroll = self.selected_asset_prefs.name.preroll
            postroll = self.selected_asset_prefs.name.postroll
            self.dialog_modify_range = dialog_modify_range.Main(frange, preroll, postroll)
            if build.launch_running_dialog(self.dialog_modify_range):
                inFrame = self.dialog_modify_range.inFrame
                outFrame = self.dialog_modify_range.outFrame
                preroll = self.dialog_modify_range.preroll
                postroll = self.dialog_modify_range.postroll
                self.selected_asset_prefs.name.set_range([inFrame, outFrame])
                self.selected_asset_prefs.name.set_preroll(preroll)
                self.selected_asset_prefs.name.set_postroll(postroll)
        except:
            logger.critical(str(traceback.format_exc()))


    def asset_item_changed(self):
        try:
            item = self.ui.treeWidget.currentItem()
            self.refresh_asset(item)
            self.update_current_asset()
            self.update_variants()
        except:
            logger.critical(str(traceback.format_exc()))

    def init_launch_button(self):
        try:
            software = self.asset.software
            lock = self.prefs.asset(self.asset).software.get_lock
            if software:
                if lock != self.prefs.user and lock != '0' and lock != 0:
                    text = f'Locked by {lock}'
                else:
                    text = software
                self.ui.launch_pushButton.setText(text)
                self.ui.launch_image_label.setPixmap(
                    QtGui.QPixmap(defaults._soft_icons_dic_[software]).scaled(40, 40, QtCore.Qt.KeepAspectRatio,
                                                                              QtCore.Qt.SmoothTransformation))
            else:
                self.ui.launch_pushButton.setText('')
                self.ui.launch_image_label.setPixmap(QtGui.QPixmap(defaults._asset_icon_).scaled(40, 40, QtCore.Qt.KeepAspectRatio,
                                                                                  QtCore.Qt.SmoothTransformation))
        except:
            logger.critical(str(traceback.format_exc()))

    def update_launch_button(self):
        try:
            if self.asset.stage and self.asset.variant:
                software = self.asset.software
                lock = self.asset_prefs.software.get_lock
                if software:
                    if lock != self.prefs.user and lock != '0' and lock != 0:
                        text = f'Locked by {lock}'
                    else:
                        text = software
                    self.ui.launch_pushButton.setText(text)
                    self.ui.launch_image_label.setPixmap(
                        QtGui.QPixmap(defaults._soft_icons_dic_[software]).scaled(40, 40, QtCore.Qt.KeepAspectRatio,
                                                                                  QtCore.Qt.SmoothTransformation))
                else:
                    self.ui.launch_pushButton.setText('Launch')
                    self.ui.launch_image_label.setPixmap(QtGui.QPixmap(defaults._asset_icon_).scaled(40, 40, QtCore.Qt.KeepAspectRatio,
                                                                                  QtCore.Qt.SmoothTransformation))
                string_asset = utils.short_asset_to_string(self.asset)
                if string_asset in os.environ[defaults._current_assets_list_].split(':'):
                    self.start_launch_gif()
                else:
                    self.stop_launch_gif()
            else:
                self.ui.launch_pushButton.setText('Launch')
                self.ui.launch_image_label.setPixmap(QtGui.QPixmap(defaults._asset_icon_).scaled(40, 40, QtCore.Qt.KeepAspectRatio,
                                                                                  QtCore.Qt.SmoothTransformation))
        except:
            logger.critical(str(traceback.format_exc()))

    def refresh_asset(self, item):
        try:
            if item:
                current_tree = tree(item)
                self.selected_asset = asset_core.asset(
                    domain=current_tree.get_domain(),
                    category=current_tree.get_category(),
                    name=current_tree.get_name(),
                    stage=current_tree.get_stage())

                self.selected_asset_prefs = prefs.asset(self.selected_asset)
        except:
            logger.critical(str(traceback.format_exc()))

    def update_current_asset(self):
        try:
            if not self.pin:
                if self.selected_asset:
                    self.asset = copy.deepcopy(self.selected_asset)
                    self.asset_prefs = prefs.asset(self.asset)
                    
            else:
                self.asset = copy.deepcopy(self.pinned_asset)
        except:
            logger.critical(str(traceback.format_exc()))

    def open(self, item):
        try:
            launching_asset = copy.deepcopy(self.asset)
            if launching_asset.launch():
                if not self.asset_prefs.software.get_lock:
                    self.lock()
                    self.update_lock()
                software = self.asset.software
                self.version_changed()
        except:
            logger.critical(str(traceback.format_exc()))

    def open_str(self, string_asset):
        try:
            old_asset = self.asset
            self.asset = asset_core.string_to_asset(string_asset)
            if self.asset.launch():
                if not self.asset_prefs.software.get_lock:
                    self.lock()
                    self.update_lock()
                self.version_changed()
            self.asset = old_asset
        except:
            logger.critical(str(traceback.format_exc()))

    def add_asset_to_shelf(self):
        try:
            icon = defaults._stage_icon_[self.asset.stage]
            name = f"import {self.asset.category}-{self.asset.name}-{self.asset.stage}-{self.asset.variant}"
            string_asset = utils.asset_to_string(self.asset)
            script = user_scripts_library.import_asset_script.replace('ASSET_STRING', string_asset)
            user_scripts().create_user_script(name, icon, script, 0)
            self.user_scripts_widget.refresh_scripts()
        except:
            logger.critical(str(traceback.format_exc()))

    def copy_asset_path(self):
        string_asset = utils.asset_to_string(self.asset)
        pyperclip.copy(string_asset)

    def start_launch_gif(self):
        try:
            self.launch_gif = QtGui.QMovie(defaults._launch_gif_)
            self.ui.launch_image_label.setMovie(self.launch_gif)
            self.launch_gif.setScaledSize(QtCore.QSize(58, 58))
            self.launch_gif.setSpeed(200)
            self.launch_gif.start()
        except:
            logger.critical(str(traceback.format_exc()))

    def stop_launch_gif(self):
        try:
            self.init_launch_button()
        except:
            logger.critical(str(traceback.format_exc()))

    def search(self):
        try:
            name = self.ui.search_lineEdit.text()
            if name != '' and len(name) > 1:
                tree_get.search(self.ui.treeWidget, name)
        except:
            logger.critical(str(traceback.format_exc()))

    def init_log_ui(self):
        try:
            self.main_handler = log_to_gui.main_ui_log_viewer(self)
            logger.main_logger.addHandler(self.main_handler)
            self.main_handler.new_record.connect(self.update_log_lineEdit)
        except:
            logger.critical(str(traceback.format_exc()))

    def update_log_lineEdit(self, record):
        try:
            if 'ERROR' in record or 'CRITI' in record:
                text_color = "color: rgb(26, 26, 32);"
                background_color = "background-color: #de7777;"
            elif 'WARN' in record:
                text_color = "color: rgb(26, 26, 32);"
                background_color = "background-color: #deb177;"
                color = 'rgb(210,210,120)'
            else:
                stylesheet = build.load_stylesheet()
                text_color = stylesheet
                background_color = stylesheet

            if 'CRITI' in record:
                self.ui_error_handler = ui_error_handler.Main(record)
                if prefs.show_error_handler:
                    build.launch_normal_as_child(self.ui_error_handler)
                else:
                    self.ui_error_handler.submit_error()
            self.ui.log_lineEdit.setStyleSheet(text_color)
            self.ui.log_frame.setStyleSheet(background_color)
            self.ui.log_lineEdit.setText(record)
        except:
            logger.critical(str(traceback.format_exc()))

    def open_log_widget(self):
        try:
            build.launch_normal_as_child(self.log_widget)
        except:
            logger.critical(str(traceback.format_exc()))

    def open_wall_widget(self):
        try:
            visible = self.wall_widget.isVisible()
            self.wall_widget.setVisible(1 - int(visible))
            if not visible:
                self.no_new_notif()
            if visible and self.wall_widget.new_notif_widget:
                self.wall_widget.new_notif_widget.setParent(None)
                self.wall_widget.new_notif_widget = None
                self.wall_widget.new_widgets = []
                self.wall_widget.refresh_wall()
        except:
            logger.critical(str(traceback.format_exc()))

    def launch_software_prefs_ui(self):
        try:
            self.ui_soft_prefs = dialog_softwares_prefs.Main()
            build.launch_dialog_as_child(self.ui_soft_prefs)
        except:
            logger.critical(str(traceback.format_exc()))

    def add_variant(self):
        try:
            self.dialog_new_variant = dialog_new_variant.Main()
            if build.launch_dialog_as_child(self.dialog_new_variant):
                variant = self.dialog_new_variant.variant_name
                self.asset.variant = variant
                if self.asset.create():
                    self.asset_prefs.stage.set_default_variant(variant)
                    self.update_variants()
        except:
            logger.critical(str(traceback.format_exc()))

    def new_project(self):
        try:
            self.dialog_new_project = dialog_new_project.Main()
            if build.launch_dialog_as_child(self.dialog_new_project):
                QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
                time.sleep(0.5)
                restart_ui(self)
        except:
            logger.critical(str(traceback.format_exc()))

    def open_project(self):
        try:
            self.dialog_projects = dialog_projects.Main()
            if build.launch_dialog_as_child(self.dialog_projects):
                QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
                time.sleep(0.5)
                restart_ui(self)
        except:
            logger.critical(str(traceback.format_exc()))

    def merge_project(self):
        try:
            self.dialog_merge_projects = dialog_merge_projects.Main()
            build.launch_dialog_as_child(self.dialog_merge_projects)
        except:
            logger.critical(str(traceback.format_exc()))

    def change_user(self, force=None):
        try:
            self.dialog_users = dialog_users.Main(force)
            if build.launch_dialog_as_child(self.dialog_users):
                project_prefs.add_user(prefs.user)
                restart_ui(self)
        except:
            logger.critical(str(traceback.format_exc()))

    def new_user(self):
        try:
            self.dialog_new_user = dialog_new_user.Main()
            if build.launch_dialog_as_child(self.dialog_new_user):
                self.update_infos()
                self.update_lock()
        except:
            logger.critical(str(traceback.format_exc()))

    def contact(self):
        try:
            self.dialog_contact = dialog_contact.Main()
            build.launch_dialog_as_child(self.dialog_contact)
        except:
            logger.critical(str(traceback.format_exc()))

    def show_popup(self):
        try:
            popup.popup().creation_pop()
        except:
            logger.critical(str(traceback.format_exc()))

    def launch_preferences_ui(self):
        try:
            self.preferences_ui = preferences_ui.Main(self)
            build.launch_normal_as_child(self.preferences_ui)
        except:
            logger.critical(str(traceback.format_exc()))

    def toggle_pin(self):
        try:
            if self.pin:
                self.ui.pin_pushButton.setIcon(QtGui.QIcon(defaults._unpin_icon_))
                self.ui.pin_pushButton.setStyleSheet('')
                #self.ui.main_frame.setStyleSheet('')
                self.ui.current_asset_label.setStyleSheet('')
                self.pin = False
                self.refresh_pinned_item(pin=0)
                self.pinned_item = None
                self.pinned_asset = None
                tree_get.select_asset(self.ui.treeWidget, self.asset)
                self.asset_item_changed()
            else:
                if self.asset.variant:
                    self.ui.pin_pushButton.setIcon(QtGui.QIcon(defaults._pin_icon_))
                    self.ui.pin_pushButton.setStyleSheet('background-color:#7785de')
                    #self.ui.main_frame.setStyleSheet('#main_frame{border: 1px solid #7785de}')
                    self.ui.current_asset_label.setStyleSheet('background-color:#454c7b')
                    self.pin = True
                    self.pinned_item = self.ui.treeWidget.selectedItems()[0]
                    self.refresh_pinned_item(pin=1)
                    self.pinned_asset = self.asset
                else:
                    logger.info("No asset to pin")
        except:
            logger.critical(str(traceback.format_exc()))

    def refresh_pinned_item(self, pin):
        try:
            if pin:
                self.pinned_item.setIcon(0,QtGui.QIcon(defaults._tree_pin_))
            else:
                name = tree(self.pinned_item).get_stage()
                self.pinned_item.setIcon(0,QtGui.QIcon(defaults._stage_icon_[name]))
        except:
            logger.critical(str(traceback.format_exc()))

    def open_folder(self):
        try:
            os.startfile(self.asset.folder)
        except:
            logger.critical(str(traceback.format_exc()))

    def open_sandbox(self):
        try:
            if not os.path.isdir(self.asset.sandbox):
                os.makedirs(self.asset.sandbox)
            os.startfile(self.asset.sandbox)
        except:
            logger.critical(str(traceback.format_exc()))

    def steal_asset(self):
        try:
            locker_user = self.asset_prefs.software.get_lock
            temp_pass = str(random.randint(1000000, 10000000))
            email = prefs.get_email_from_user(locker_user)
            send_email.request_unlock(locker_user, prefs.user, email, temp_pass, self.asset)
            self.dialog_confirm_email = dialog_confirm_email.Main(self, temp_pass)
            if build.launch_dialog_as_child(self.dialog_confirm_email):
                self.steal_asset_raw()
        except:
            logger.critical(str(traceback.format_exc()))

    def steal_asset_raw(self):
        locker_user = self.asset_prefs.software.get_lock
        self.asset_prefs.software.unlock()
        prefs.remove_lock_from_user(utils.asset_to_string(self.asset), locker_user)
        self.update_lock()
        logger.info("Asset unlocked !")

    def launch_options_widget(self):
        try:
            self.options_widget = options_widget.Main(self)
            lock = self.asset_prefs.software.get_lock
            if lock and lock != prefs.user:
                if prefs.admin:
                    self.options_widget.add_item('Force unlock', self.steal_asset_raw)
                else:
                    self.options_widget.add_item('Request email unlock', self.steal_asset)
            self.options_widget.add_item('Show file', self.open_folder)
            build.launch_options(self.options_widget)
        except:
            logger.critical(str(traceback.format_exc()))

    def closeEvent(self, event):
        try:
            if self.asset:
                self.prefs.set_context(self.asset)
            runs = len(os.environ[defaults._current_assets_list_].split(':')) - 1
            locks = len(prefs.locks)
            if runs or locks:
                self.dialog_quit_popup = dialog_quit_popup.Main(runs, locks)
                if build.launch_dialog_as_child(self.dialog_quit_popup):
                    self.stop_threads()
                    print(defaults._wizard_correctly_stopped_)
                    sys.stdout.flush()
                    QApplication.quit()
                else:
                    event.ignore()
            else:
                self.stop_threads()
                print(defaults._wizard_correctly_stopped_)
                sys.stdout.flush()
                QApplication.quit()
        except:
            logger.critical(str(traceback.format_exc()))
            QApplication.quit()

    def mousePressEvent(self, event):
        try:
            self.ui.log_frame.setStyleSheet(self.stylesheet)
            self.ui.log_lineEdit.setStyleSheet(self.stylesheet)
            event.accept()
        except:
            logger.critical(str(traceback.format_exc()))

    def show_file_viewer(self):
        try:
            self.file_viewer = file_viewer.Main(0)
            build.launch_normal_as_child(self.file_viewer)
        except:
            logger.critical(str(traceback.format_exc()))

    def show_ui_renamer(self):
        try:
            self.ui_renamer = ui_renamer.Main()
            build.launch_normal_as_child(self.ui_renamer)
        except:
            logger.critical(str(traceback.format_exc()))

    def show_workflow(self):
        try:
            self.ui_project_preferences = ui_project_preferences.Main()
            build.launch_normal_as_child(self.ui_project_preferences)
        except:
            logger.critical(str(traceback.format_exc()))

    def show_running_widget(self):
        try:
            self.running_widget = running_widget.Main()
            build.launch_running(self.running_widget)
            self.running_widget.focus.connect(self.focus_asset)
            self.running_widget.refresh_lock.connect(self.update_lock)
        except:
            logger.critical(str(traceback.format_exc()))

    def show_locked_widget(self):
        try:
            self.running_widget = running_widget.Main(1)
            build.launch_running(self.running_widget)
            self.running_widget.focus.connect(self.focus_asset)
            self.running_widget.refresh_lock.connect(self.update_lock)
        except:
            logger.critical(str(traceback.format_exc()))

    def leave_user(self):
        try:
            prefs.leave_user()
            self.change_user(force=1)
        except:
            logger.critical(str(traceback.format_exc()))

    def show_about(self):
        try:
            self.ui_about = ui_about.Main()
            build.launch_normal_as_child(self.ui_about)
        except:
            logger.critical(str(traceback.format_exc()))

    def show_project_workflow(self):
        try:
            self.ui_project_workflow = ui_project_workflow.Main()
            build.launch_normal_as_child(self.ui_project_workflow)
        except:
            logger.critical(str(traceback.format_exc()))

    def show_process_manager(self):
        try:
            self.ui_subprocess_manager = ui_subprocess_manager.Main()
            build.launch_normal_as_child(self.ui_subprocess_manager)
        except:
            logger.critical(str(traceback.format_exc()))

    def show_version_manager(self):
        try:
            new_version = None
            if new_version:
                self.dialog_new_version = dialog_new_version.Main(new_version)
                if build.launch_dialog_as_child(self.dialog_new_version):
                    self.close()
            else:
                logger.info("Wizard is up to date !")
        except:
            logger.critical(str(traceback.format_exc()))

    def launch_docs(self):
        try:
            url = defaults._wizard_doc_url_
            webbrowser.open(url, new=0, autoraise=True)
        except:
            logger.critical(str(traceback.format_exc()))

    def show_git(self):
        try:
            url = defaults._git_link_
            webbrowser.open(url, new=0, autoraise=True)
        except:
            logger.critical(str(traceback.format_exc()))

    def show_pywizard(self):
        try:
            os.startfile("pywizard.exe")
        except:
            logger.critical(str(traceback.format_exc()))

    def show_chat_house(self):
        try:
            logger.info('Not available, in development...')
            #build.launch_normal_as_child(self.chat_house)
        except:
            logger.critical(str(traceback.format_exc()))

    def create_crash(self):
        a=0/0

    def connect_functions(self):
        try:
            software_settings_shortcut = QtWidgets.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_F2), self)
            software_settings_shortcut.activated.connect(self.launch_software_prefs_ui)
            logShortcut = QtWidgets.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_F1), self)
            logShortcut.activated.connect(self.open_log_widget)

            self.ui.treeWidget.itemDoubleClicked.connect(self.double_click_item)
            self.ui.treeWidget.itemSelectionChanged.connect(self.asset_item_changed)
            self.ui.search_lineEdit.textChanged.connect(self.search)
            self.ui.variants_comboBox.currentIndexChanged.connect(self.variant_changed)
            self.ui.software_comboBox.currentIndexChanged.connect(self.software_changed)
            self.ui.versions_comboBox.currentIndexChanged.connect(self.version_changed)
            self.ui.log_pushButton.clicked.connect(self.open_log_widget)
            self.ui.wall_pushButton.clicked.connect(self.open_wall_widget)
            self.ui.running_pushButton.clicked.connect(self.show_running_widget)
            self.ui.settings_pushButton.clicked.connect(self.launch_preferences_ui)
            self.ui.locked_assets_pushButton.clicked.connect(self.show_locked_widget)
            self.ui.add_variant_pushButton.clicked.connect(self.add_variant)
            self.ui.launch_pushButton.clicked.connect(self.open)
            self.ui.image_button.clicked.connect(self.open_image)
            self.ui.lock_pushButton.clicked.connect(self.lock)
            self.ui.comment_pushButton.clicked.connect(self.comment)
            self.ui.pin_pushButton.clicked.connect(self.toggle_pin)
            self.ui.open_folder_pushButton.clicked.connect(self.open_folder)
            self.ui.sandbox_pushButton.clicked.connect(self.open_sandbox)
            self.ui.launch_pushButton.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
            self.ui.launch_pushButton.customContextMenuRequested.connect(self.launch_options_widget)
            self.ui.main_tabWidget.currentChanged.connect(self.main_tab_changed)
            self.ui.server_pushButton.clicked.connect(self.refresh_server)
            self.ui.actionGitHub.triggered.connect(self.show_git)
            self.ui.actionWizard_API.triggered.connect(self.launch_docs)
            self.ui.actionLast_updates.triggered.connect(lambda:self.show_updates(force=1))
            self.ui.actionPreferences_2.triggered.connect(self.launch_preferences_ui)
            self.ui.actionNew.triggered.connect(self.new_project)
            self.ui.actionOpen.triggered.connect(self.open_project)
            self.ui.actionMerge.triggered.connect(self.merge_project)
            self.ui.actionNew_2.triggered.connect(self.new_user)
            self.ui.actionChange.triggered.connect(self.change_user)
            self.ui.actionContact.triggered.connect(self.contact)
            self.ui.actionQuit.triggered.connect(self.close)
            self.ui.actionSettings.triggered.connect(self.show_workflow)
            self.ui.actionUnlog.triggered.connect(self.leave_user)
            self.ui.actionFile_viewer.triggered.connect(self.show_file_viewer)
            self.ui.actionAbout.triggered.connect(self.show_about)
            self.ui.actionProcess_manager.triggered.connect(self.show_process_manager)
            self.ui.actionLast_version.triggered.connect(self.show_version_manager)
            self.ui.actionPyWizard.triggered.connect(self.show_pywizard)
            self.ui.actionRenamer.triggered.connect(self.show_ui_renamer)
            self.ui.actionChat.triggered.connect(self.show_chat_house)
            self.ui.actionCreate_crash.triggered.connect(self.create_crash)
            

        except:
            logger.critical(str(traceback.format_exc()))

    def focus_wizard(self):
        shutter = self.prefs.shutter
        if shutter:
            if not self.isVisible():
                self.show_animation()
        else:
            if self.windowState() != QtCore.Qt.WindowMaximized:
                self.showMaximized()
            else:
                self.showMaximized()
        self.raise_()
        self.activateWindow()
        self.show()

    def show_animation(self):
        try:
            QtWidgets.QMainWindow.show(self)
            win_size = (self.frameSize().width(), self.frameSize().height())
            init_y = -win_size[1]
            end_y = 0
            self.displace_animation.setDuration(200)
            self.displace_animation.setStartValue(QtCore.QPointF(self.x_pos, init_y))
            self.displace_animation.setEndValue(QtCore.QPointF(self.x_pos, end_y))
            self.displace_animation.start()
        except:
            logger.critical(str(traceback.format_exc()))

    def hide_animation(self):
        try:
            win_size = (self.frameSize().width(), self.frameSize().height())
            init_y = -win_size[1]
            end_y = 0
            self.displace_animation.setDuration(200)
            self.displace_animation.setStartValue(QtCore.QPointF(self.x_pos, end_y))
            self.displace_animation.setEndValue(QtCore.QPointF(self.x_pos, init_y))
            self.displace_animation.start()
        except:
            logger.critical(str(traceback.format_exc()))

    def hide(self):
        try:
            if self.pos().y() < -5:
                QtWidgets.QMainWindow.hide(self)
        except:
            logger.critical(str(traceback.format_exc()))

    def move_window(self, toggle_tab_ui=0):
        try:
            screen_index = self.prefs.screen
            monitor = QtWidgets.QDesktopWidget().screenGeometry(screen_index)
            screen_geometry = QtWidgets.QDesktopWidget().availableGeometry(screen_index)
            win_size = (self.frameSize().width(), self.frameSize().height())
            self.x_pos = monitor.left() + ((screen_geometry.width()) - win_size[0]) / 2
            y = monitor.top() - win_size[1]
            if toggle_tab_ui:
                y = 0
            self.move(self.x_pos, y)
            self.move_signal.emit('')
        except:
            logger.critical(str(traceback.format_exc()))

def restart_ui(self):
    try:
        self.stop_threads()
        self.close()
        self.prefs.set_context(None)
        if not os.path.isfile('wizard.exe'):
            os.startfile('wizard_site.bat')
        else:
            os.startfile('wizard.exe')        
    except:
        logger.critical(str(traceback.format_exc()))
