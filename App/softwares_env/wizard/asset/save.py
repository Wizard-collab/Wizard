from wizard.asset.folder import folder
from wizard.prefs.stats import stats
from wizard.prefs.main import prefs
from wizard.tools import log
from wizard.vars import defaults
from wizard.tools import screen_tools
from wizard.signal import send_signal
from PyQt5.QtCore import QThread, pyqtSignal
from wizard.asset import main as asset_core

import time
import traceback
import os

logger = log.pipe_log(__name__)

prefs = prefs()


class save_thread(QThread):
    def __init__(self):
        super(save_thread, self).__init__()
        self.save_dic = dict()
        self.running=1

    def run(self):
        while self.running:
            if self.save_dic != dict():
                self.save(self.save_dic)
                self.save_dic = dict()
            time.sleep(0.05)

    def do_save(self, signal_dic):
        self.save_dic = signal_dic

    def save(self, signal_dic):
        file = signal_dic[defaults._signal_file_key_]
        asset = asset_core.string_to_asset(signal_dic[defaults._signal_asset_key_])
        filename = os.path.basename(file)
        filename = filename.split('.')[0]
        if filename == folder(asset).work_name_template:
            version = folder(asset).version_from_file(file)
            if version.isdigit():
                asset.version = prefs.asset(asset).software.new_version(version=version)
                time.sleep(1)
                try:
                    im_file = prefs.asset(asset).software.image
                    screen_tools.screen_shot_current_screen(im_file)
                except:
                    logger.critical(str(traceback.format_exc()))

                # Try refreshing the ui
                try:
                    send_signal.refresh_signal()
                    logger.info('{} saved ({})'.format(file, asset.software))
                    send_signal.save_signal()
                    stats().add_xp(2)
                    stats().add_version(asset)
                except:
                    pass

    def stop(self):
        self.running = False
