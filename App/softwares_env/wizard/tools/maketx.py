from wizard.vars import defaults
import subprocess
import os
import traceback
import logging
import sys

import time

class maketx():

    def __init__(self, files_list, extension):
        self.files_list = files_list
        self.extension = extension

    def start(self):
        
        maketx_path = os.path.abspath(defaults._make_tx_)
        print(maketx_path)
        
        print(defaults._subprocess_current_task_+"Converting .exr maps in {}".format(self.extension))
        print(defaults._subprocess_status_+"Starting...")
        percent_step = 100.0/len(self.files_list)
        percent = 0.0
        print(defaults._percent_signal_+str(percent))
        sys.stdout.flush()
        tex_files_list = []
        for file in self.files_list:
            if os.path.isfile(file):
                print(defaults._subprocess_status_+"Working...")
                maketx_path = os.path.abspath(defaults._make_tx_)
                print(maketx_path)
                file_ext = os.path.splitext(file)[-1]
                file = file.replace('\\', '/')
                tex_file = file.replace(file_ext, '.tx')
                tex_files_list.append(tex_file)
                command = '{} "{}" -o "{}"'.format(maketx_path, file, tex_file)
                print("Executing maketx.exe for {}".format(file))
                percent+=percent_step
                process = subprocess.Popen(command)
                process.poll()
                sys.stdout.flush()
                time.sleep(1)
                print(defaults._percent_signal_+str(percent))
                sys.stdout.flush()
            else:
                print("{} doesn't exists !".format(file))

        if self.extension == '.tex':
            for file in tex_files_list:
                dest_file = file.replace('.tx', '.tex')
                while not os.path.isfile(dest_file):
                    if os.path.isfile(file):
                        print("Converting {} 'tx' file to 'tex' file...".format(file))
                        try:
                            os.rename(file, dest_file)
                            time.sleep(0.1)
                            sys.stdout.flush()
                        except PermissionError:
                            print("Can't rename {} to .tex, file isn't accessible.".format(file))
                    else:
                        print('File not found : {}'.format(file))
                    time.sleep(0.5)

        print(defaults._subprocess_status_+"Done !")