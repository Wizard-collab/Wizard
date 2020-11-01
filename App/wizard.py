import subprocess
from wizard.vars import defaults
import traceback
import os
import wizard_site
import psutil
from wizard.signal import send_signal
from socket import *

command = "python wizard_site.py"
log_file = defaults._log_file_
lock_file = defaults._lock_file_

def wizard_with_main_log():

    is_running = 0

    try:
        server = socket(AF_INET, SOCK_STREAM)
        server.connect(('localhost', 5034))
        is_running = 1
        server.close()
    except ConnectionRefusedError:
        pass

    if not is_running:
        try:
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            while True:
                output = process.stdout.readline()
                if process.poll() is not None:
                    break
                if output:
                    line = output.strip()
                    stream_output(line)
                    file_output(line)
        except:
            stream_output(str(traceback.format_exc()))
            file_output(str(traceback.format_exc()))
    else:
        message = "Wizard is already running..."
        send_signal.focus_signal()
        stream_output(message)
        file_output(message)

def stream_output(line):
    print(convert_output(line))
    
def file_output(line):
    with open(log_file, 'a+') as log:
        log.write(convert_output(line) + '\n')

def convert_output(line):
    try:
        line = line.decode('ascii')
    except:
        line = str(line)
    return line

if __name__ == '__main__':
    wizard_with_main_log()