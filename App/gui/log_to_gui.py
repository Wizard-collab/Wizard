import logging

from PyQt5.QtCore import pyqtSignal, QObject


class log_viewer(logging.Handler):
    def __init__(self, ui):
        super().__init__()
        self.ui = ui
        self.widget = self.ui.log_lineEdit
        self.frame = self.ui.log_frame
        self.setFormatter(logging.Formatter("%(asctime)s [%(name)-23.23s] [%(levelname)s] %(message)s"))

    def emit(self, record):
        record = self.format(record)
        if 'ERROR' in record:
            text_color = "color: rgb(26, 26, 32);"
            background_color = "background-color: #de7777;"
        elif 'WARN' in record:
            text_color = "color: rgb(26, 26, 32);"
            background_color = "background-color: #deb177;"
            color = 'rgb(210,210,120)'
        else:
            text_color = "color: White;"
            background_color = "background-color: rgb(36, 36, 42);"
        try:
            self.widget.setStyleSheet(text_color)
            self.frame.setStyleSheet(background_color)
            self.widget.setText(record)
        except:
            pass

class log_widget_viewer(QObject, logging.Handler):
    new_record = pyqtSignal(object)

    def __init__(self, parent):
        super().__init__(parent)
        super(logging.Handler).__init__()
        formatter = Formatter("%(asctime)s [%(name)-23.23s] [%(levelname)s] %(message)s")
        self.setFormatter(formatter)

    def emit(self, record):
        msg = self.format(record)
        if 'WARNING' in msg:
            text = '<span style="color:#f7b100;">' + msg
        elif 'ERROR' in msg:
            text = '<span style="color:#d65050;">' + msg
        elif 'CRITICAL' in msg:
            text = '<span style="color:#d65050;">' + msg
        else:
            text = msg
        self.new_record.emit(text)


class main_ui_log_viewer(QObject, logging.Handler):
    new_record = pyqtSignal(object)

    def __init__(self, parent):
        super().__init__(parent)
        super(logging.Handler).__init__()
        formatter = Formatter("%(asctime)s [%(name)-23.23s] [%(levelname)s] %(message)s")
        self.setFormatter(formatter)

    def emit(self, record):
        msg = self.format(record)
        self.new_record.emit(msg)  # <---- emit signal here


class Formatter(logging.Formatter):
    def formatException(self, ei):
        result = super(Formatter, self).formatException(ei)
        return result

    def format(self, record):
        s = super(Formatter, self).format(record)
        if record.exc_text:
            s = s.replace('\n', '')
        return s
