from PyQt5 import QtWidgets, QtGui, QtCore
from wizard.tools import log

logger = log.pipe_log()

class screen_record_ui(QtWidgets.QWidget):
    def __init__(self):
        super(screen_record_ui, self).__init__()
        test_shortcut = QtWidgets.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_F3), self)
        test_shortcut.setContext(QtCore.Qt.ApplicationShortcut)
        test_shortcut.activated.connect(self.test)

    def test(self):
        logger.warning('test')
