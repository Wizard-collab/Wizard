from PyQt5 import QtWidgets, QtGui
from gui.modify_range_dialog import Ui_Dialog
from wizard.tools import log

logger = log.pipe_log(__name__)


class Main(QtWidgets.QDialog):

    def __init__(self, range):
        super(Main, self).__init__()
        # Build the ui from ui converted file
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.shadow = QtWidgets.QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(8)
        self.shadow.setColor(QtGui.QColor(0, 0, 0, 180))
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.setGraphicsEffect(self.shadow)

        self.inFrame = range[0]
        self.outFrame = range[1]

        self.ui.shot_inFrame_spinBox.setValue(self.inFrame)
        self.ui.shot_outFrame_spinBox.setValue(self.outFrame)

        self.ui.shot_crea_create_pushButton.clicked.connect(self.modify_range)

    def move_ui(self):
        win_size = (self.frameSize().width(), self.frameSize().height())
        posx = QtGui.QCursor.pos().x()
        posy = int(QtGui.QCursor.pos().y()) - win_size[1] + 10
        self.move(posx, posy)

    def modify_range(self):
        self.inFrame = self.ui.shot_inFrame_spinBox.value()
        self.outFrame = self.ui.shot_outFrame_spinBox.value()
        self.accept()

    def closeEvent(self, event):
        event.ignore()
        self.hide()
