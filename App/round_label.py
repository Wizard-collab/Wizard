from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPainter, QPainterPath
from PyQt5.QtWidgets import QLabel


class Label(QLabel):
    def __init__(self, antialiasing=True):
        super(Label, self).__init__(*args, **kwargs)
        self.Antialiasing = antialiasing
        self.setMaximumSize(50, 50)
        self.setMinimumSize(50, 50)
        self.radius = 25

        self.target = QPixmap(self.size())
        self.target.fill(Qt.transparent)

        p = QPixmap(self.image).scaled(
            50, 50, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)

        painter = QPainter(self.target)
        if self.Antialiasing:
            painter.setRenderHint(QPainter.Antialiasing, True)
            painter.setRenderHint(QPainter.HighQualityAntialiasing, True)
            painter.setRenderHint(QPainter.SmoothPixmapTransform, True)

        path = QPainterPath()
        path.addRoundedRect(
            0, 0, self.width(), self.height(), self.radius, self.radius)

        painter.setClipPath(path)
        painter.drawPixmap(0, 0, p)
        self.setPixmap(self.target)
