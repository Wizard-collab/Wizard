from PyQt5 import QtWidgets, QtGui

from gui.options_widget import Ui_Form
from wizard.tools import log

logger = log.pipe_log(__name__)


class Main(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(Main, self).__init__()
        # Build the ui from ui converted file
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.shadow = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(8)
        self.shadow.setColor(QtGui.QColor(0, 0, 0, 180))
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.setGraphicsEffect(self.shadow)

        self.items = []

    def leaveEvent(self, event):
        self.close()

    def move_ui(self):
        win_size = (self.frameSize().width(), self.frameSize().height())
        posx = QtGui.QCursor.pos().x() - 10
        posy = int(QtGui.QCursor.pos().y()) - win_size[1] + 10
        self.move(posx, posy)

    def add_item(self, name, function):
        pushButton = QtWidgets.QPushButton(self.ui.options_frame)
        pushButton.setObjectName('options_pushButton')
        pushButton.setText(name)
        self.ui.buttons_layout.addWidget(pushButton)
        self.items.append(pushButton)
        pushButton.clicked.connect(self.close)
        pushButton.clicked.connect(function)
