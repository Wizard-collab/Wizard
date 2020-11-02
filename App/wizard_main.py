import subprocess
from wizard.vars import defaults
import traceback
import os
import wizard_site
import psutil
from wizard.signal import send_signal
from socket import *
import sys

command = "wizard_site"
    
if sys.argv[0].endswith('.py'):
    command = "python wizard_site.py"

log_file = defaults._log_file_

class wizard():

    def __init__(self):
        is_running = 0

        try:
            server = socket(AF_INET, SOCK_STREAM)
            server.connect(('localhost', 5034))
            is_running = 1
            server.close()
        except ConnectionRefusedError:
            pass
        except:
            self.stream_output(str(traceback.format_exc()))
            self.file_output(str(traceback.format_exc()))

        if not is_running:
            try:
                env = os.environ.copy()
                process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, env=env, cwd=os.path.abspath(''))
                while True:
                    output = process.stdout.readline()
                    if process.poll() is not None:
                        break
                    if output:
                        line = output.strip()
                        self.stream_output(line)
                        self.file_output(line)
            except:
                self.stream_output(str(traceback.format_exc()))
                self.file_output(str(traceback.format_exc()))
        else:
            message = "Wizard is already running..."
            send_signal.focus_signal()
            self.stream_output(message)
            self.file_output(message)

    def stream_output(self, line):
        log = self.convert_output(line)
        print(log)
        if log and log != '':
            send_signal.log_line(log)
        
    def file_output(self, line):
        with open(log_file, 'a+') as log:
            log.write(self.convert_output(line) + '\n')

    def convert_output(self, line):
        try:
            line = line.decode('ascii')
        except:
            line = str(line)
        return line

wizard()
