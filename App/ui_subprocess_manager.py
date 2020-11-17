# coding: utf8

# Import PyQt6 libraries
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QFileDialog

# Import wizard gui libraries
from gui.subprocess_manager import Ui_Form
from gui import build

# Import wizard core libraries
from wizard.vars import defaults
from wizard.tools import log
from wizard.tools import utility as utils
from wizard.signal import send_signal

# Import python base libraries ( or installed with pip )
import traceback
import dialog_report
import subprocess
import sys
import os
import pyperclip
import contextlib
import time

# Init main logger
logger = log.pipe_log(__name__)


class Main(QtWidgets.QWidget):

    def __init__(self, command = None, env=None, cwd = 'softwares_env'):
        super(Main, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.command = command
        self.env = env
        self.cwd = cwd
        self.log_file = os.path.join(defaults._log_path_, f'subprocess_log_{utils.id_based_time()}.log')
        if command:
            self.ui.subprocess_command_textEdit.setText(str(self.command))
        else:
            self.ui.subprocess_command_textEdit.setText('')
        self.ui.subprocess_execute_pushButton.clicked.connect(self.execute)
        self.ui.subprocess_execute_pushButton.setIcon(QtGui.QIcon(defaults._running_icon_))
        self.ui.report_logs_pushButton.clicked.connect(self.launch_report_dialog)
        self.ui.report_logs_pushButton.setIcon(QtGui.QIcon(defaults._email_icon_))
        self.ui.copy_logs_pushButton.clicked.connect(self.copy_logs)
        self.ui.copy_logs_pushButton.setIcon(QtGui.QIcon(defaults._copy_icon_))
        self.ui.save_logs_pushButton.clicked.connect(self.save_logs)
        self.ui.save_logs_pushButton.setIcon(QtGui.QIcon(defaults._save_icon_))
        self.ui.subprocess_ma_stop_pushButton.setIcon(QtGui.QIcon(defaults._kill_process_icon_))
        self.sub_thread = None
        if self.command:
            self.run_subprocess()

    def copy_logs(self):
        pyperclip.copy(self.get_logs())

    def save_logs(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getSaveFileName(self, 'Save Logs', 'my_log.log', "Log Files (*.log)", options=options)
        if filename:
            with open(filename, 'w') as f:
                f.write(self.get_logs())

    def closeEvent(self, event):
        event.ignore()
        if self.sub_thread:
            self.sub_thread.kill_process(0)
        self.hide()

    def run_subprocess(self):
        self.sub_thread = run_subprocess(self.command, self, self.env, self.cwd)
        self.sub_thread.start()
        self.sub_thread.time_signal.connect(self.update_clock)
        self.sub_thread.out_signal.connect(self.append_out)
        self.sub_thread.err_signal.connect(self.append_err)
        self.sub_thread.err_signal.connect(self.write_logs_to_file)
        self.sub_thread.out_signal.connect(self.write_logs_to_file)
        self.sub_thread.task_signal.connect(self.update_task_name)
        self.sub_thread.status_signal.connect(self.ui.subprocess_status_lineEdit.setText)
        self.sub_thread.status_signal.connect(self.update_loading)
        self.sub_thread.percent_signal.connect(self.update_progress_bar)

    def append_out(self, log):
        log = convert_string(log)
        self.ui.process_stdout_textEdit.append(log)

    def append_err(self, log):
        log = convert_string(log)
        self.ui.process_stderr_textEdit.append(log)

    def update_clock(self, int_time):
        text_time = time.strftime("%H:%M:%S", time.gmtime(int_time))
        self.ui.subprocess_time_lineEdit.setText(text_time)

    def update_task_name(self, name):
        self.ui.subprocess_current_task_lineEdit.setText(name)
        send_signal.task_name_signal(name)

    def update_loading(self, status):
        if status == 'Done !':
            send_signal.task_signal(100)
            send_signal.task_name_signal('Done !')
            self.ui.subprocess_percent_progressBar.setStyleSheet('#subprocess_percent_progressBar::chunk{background-color:#B7E266;}')
            self.stop_loading_gif()
            if self.windowState() == QtCore.Qt.WindowMinimized:
                self.close()
        if status == 'Starting...':
            send_signal.task_signal(0)
            self.ui.subprocess_percent_progressBar.setStyleSheet('#subprocess_percent_progressBar::chunk{background-color:#FF9966;}')
            self.start_loading_gif()
        if status == 'Stopped':
            self.ui.subprocess_percent_progressBar.setStyleSheet('#subprocess_percent_progressBar::chunk{background-color:#db5c5c;}')
            self.ui.subprocess_percent_progressBar.setValue(100)
            self.stopped_process_icon()
            send_signal.task_name_signal('Process manually stopped')


    def start_loading_gif(self):
        try:
            self.loading_gif = QtGui.QMovie(defaults._loading_gif_)
            self.ui.subprocess_manager_loading_label.setMovie(self.loading_gif)
            self.loading_gif.setScaledSize(QtCore.QSize(20, 20))
            self.loading_gif.setSpeed(200)
            self.loading_gif.start()
        except:
            logger.critical(str(traceback.format_exc()))

    def stop_loading_gif(self):
        self.ui.subprocess_manager_loading_label.setPixmap(QtGui.QPixmap(defaults._export_list_icon_).scaled(20, 20, QtCore.Qt.KeepAspectRatio,
                                                                              QtCore.Qt.SmoothTransformation))

    def stopped_process_icon(self):
        self.ui.subprocess_manager_loading_label.setPixmap(QtGui.QPixmap(defaults._missing_file_export_list_icon_).scaled(20, 20, QtCore.Qt.KeepAspectRatio,
                                                                              QtCore.Qt.SmoothTransformation))

    def launch_report_dialog(self):
        try:
            self.dialog_report = dialog_report.Main(self.get_logs())
            build.launch_dialog_as_child(self.dialog_report)
        except:
            logger.error(str(traceback.format_exc()))

    def update_progress_bar(self, percent):
        self.ui.subprocess_percent_progressBar.setValue(percent)
        send_signal.task_signal(percent)

    def get_logs(self):
        stdout = self.ui.process_stdout_textEdit.toPlainText()
        stderr = self.ui.process_stderr_textEdit.toPlainText()
        logs = 'Subprocess manager LOGS\n\n\nSTDOUT :\n\n'
        logs+= stdout
        logs+= '\n\nSTDERR :\n\n'
        logs+= stderr
        return logs

    def write_logs_to_file(self, log):
        with open(self.log_file, 'a+') as f:
            f.write(log +'\n')

    def execute(self):
        self.command = self.ui.subprocess_command_textEdit.toPlainText()
        if self.command and self.command != '':
            self.run_subprocess()

class run_subprocess(QThread):

    out_signal = pyqtSignal(str)
    err_signal = pyqtSignal(str)
    task_signal = pyqtSignal(str)
    status_signal = pyqtSignal(str)
    percent_signal = pyqtSignal(float)
    time_signal = pyqtSignal(int)

    def __init__(self, command, parent, env, cwd):
        super(run_subprocess, self).__init__()
        self.command = command
        self.parent = parent
        self.env = env
        self.stop = None
        self.cwd = cwd

    def run(self):
        self.process = subprocess.Popen(self.command, shell=True,stdout = subprocess.PIPE, stderr = subprocess.PIPE, env = self.env, cwd=self.cwd)
        self.parent.ui.subprocess_ma_stop_pushButton.clicked.connect(self.kill_process)
        self.errThread = errThread(self.process, self)
        self.errThread.start()
        self.timerThread = timerThread()
        self.timerThread.start()
        self.timerThread.time_signal.connect(self.time_signal.emit)
        self.errThread.err_signal.connect(self.err_signal.emit)
        self.errThread.task_signal.connect(self.task_signal.emit)
        self.errThread.status_signal.connect(self.status_signal.emit)
        self.errThread.percent_signal.connect(self.percent_signal.emit)
        self.outThread = outThread(self.process, self)
        self.outThread.start()
        self.outThread.out_signal.connect(self.out_signal.emit)
        self.outThread.task_signal.connect(self.task_signal.emit)
        self.outThread.status_signal.connect(self.status_signal.emit)
        self.outThread.percent_signal.connect(self.percent_signal.emit)
        while not (self.process.poll() == 0 or self.stop):
            QApplication.processEvents()
        self.outThread.quit()
        self.errThread.quit()

    def kill_process(self, manual = 1):
        try:
            if manual:
                self.out_signal.emit("Process manualy stopped")
                self.status_signal.emit("Stopped")
            subprocess.Popen("TASKKILL /F /PID {pid} /T".format(pid=self.process.pid))
            self.timerThread.running = 0  
            self.stop = 1     
            self.errThread.quit()     
            self.outThread.quit()     
            self.timerThread.quit()     
        except:
            self.out_signal.emit(str(traceback.format_exc()))

class errThread(QThread):

    err_signal = pyqtSignal(str)
    percent_signal = pyqtSignal(float)
    task_signal = pyqtSignal(str)
    status_signal = pyqtSignal(str)

    def __init__(self, process, run_process):
        super(errThread, self).__init__()
        self.process = process
        self.run_process = run_process

    def run(self):
        while not self.run_process.stop:
            QApplication.processEvents()
            error = self.process.stderr.readline()
            if error:
                try:
                    err = error.strip().decode('utf-8')
                except:
                    err = "{}".format(str(error.strip())) 
                #err = convert_string(err)
                if self.check_string(err):
                    self.err_signal.emit(err)

    def check_string(self, string):
        if defaults._percent_signal_ in string:
            try:
                percent = float(string.split(defaults._percent_signal_)[-1])
                self.percent_signal.emit(percent)
                return 0
            except:
                return 1
        elif defaults._subprocess_current_task_ in string:
            self.task_signal.emit(string.split(defaults._subprocess_current_task_)[-1])
            return 0
        elif defaults._subprocess_status_ in string:
            self.status_signal.emit(string.split(defaults._subprocess_status_)[-1])
            return 0
        else:
            return 1

class outThread(QThread):

    out_signal = pyqtSignal(str)
    percent_signal = pyqtSignal(float)
    task_signal = pyqtSignal(str)
    status_signal = pyqtSignal(str)

    def __init__(self, process, run_process):
        super(outThread, self).__init__()
        self.process = process
        self.run_process = run_process

    def run(self):

        while not self.run_process.stop:
            QApplication.processEvents()
            output = self.process.stdout.readline()
            if self.process.poll() is not None:
                break
                self.out_signal.emit('status:finished')
            if output:
                try:
                    out = output.strip().decode('utf-8')
                except:
                    out = "{}".format(str(output.strip())) 
                self.check_string(out)
                self.out_signal.emit(out)

    def check_string(self, string):
        if defaults._percent_signal_ in string:
            try:
                percent = float(string.split(defaults._percent_signal_)[-1])
                self.percent_signal.emit(percent)
                return 0
            except:
                return 1
        elif defaults._subprocess_current_task_ in string:
            self.task_signal.emit(string.split(defaults._subprocess_current_task_)[-1])
            return 0
        elif defaults._subprocess_status_ in string:
            self.status_signal.emit(string.split(defaults._subprocess_status_)[-1])
            return 0
        else:
            return 1

class timerThread(QThread):

    time_signal = pyqtSignal(int)
    running = 1

    def __init__(self):
        super(timerThread, self).__init__()

    def run(self):

        time_count = 0

        while self.running:
            time.sleep(1)
            self.time_signal.emit(time_count)
            time_count += 1

def convert_string(string):
        if 'WARN' in string:
            text = '<span style="color:#f7b100;">' + string
        elif 'ERRO' in string:
            text = '<span style="color:#d65050;">' + string
        elif 'CRIT' in string:
            text = '<span style="color:#d65050;">' + string
        else:
            text = '<span style="color:#ffffff;">' + string
        return text

def convert_env(env):
    if env:
        env = env.splitlines()
        return env
    else:
        return None

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(defaults._wizard_ico_))
    subprocess_manager = Main
    build.launch_normal(subprocess_manager)