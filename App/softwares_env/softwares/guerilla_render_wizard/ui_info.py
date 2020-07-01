import os, sys
from guerilla import Document
from PySide import QtGui

class info_ui(QtGui.QWidget):
    def __init__(self, text):
        super(info_ui, self).__init__()
        self.setWindowTitle('Warning')

        # 2 push buttons...
        self.closeButton = QtGui.QPushButton('Close')
        self.label = QtGui.QLabel(text)

        # ...in a vertical layout
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(self.closeButton)

        # set our vertical layout
        self.setLayout(vbox)

        # connect signals
        self.closeButton.clicked.connect(self.close)

app = QtGui.QApplication.instance()
if app is None:
    app = QtGui.QApplication(sys.argv)
text='mdr'
window = info_ui(text)
window.show()