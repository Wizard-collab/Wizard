import sys

from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.Qsci import QsciScintilla
from PyQt5 import Qsci
from lexers import python_lexer
from lexers import yaml_lexer
from lexers import neutral_lexer

class SimplePythonEditor(QsciScintilla):
    ARROW_MARKER_NUM = 8

    def __init__(self, parent=None, python = 1, yaml = 0):
        super(SimplePythonEditor, self).__init__(parent)

        self.font = QtGui.QFont()
        self.font.setFamily('Consolas')
        self.font.setFixedPitch(True)
        self.font.setPointSize(9)

        self.bold_font = QtGui.QFont()
        self.bold_font.setFamily('Consolas')
        self.bold_font.setFixedPitch(True)
        self.bold_font.setPointSize(9)
        self.bold_font.setBold(1)

        self.set_lexer(python, yaml)


    def build(self):

        self.setFont(self.font)
        self.setMarginsFont(self.font)

        self.setIndentationGuides(True)
        self.setIndentationGuidesForegroundColor(QtGui.QColor("#555569"))
        self.setIndentationGuidesBackgroundColor(QtGui.QColor("#555569"))

        self.setTabWidth(4)
        self.setAutoIndent(True)
        self.setWrapMode(QsciScintilla.WrapWord)
        self.setWrapIndentMode(QsciScintilla.WrapIndentIndented)
        self.setSelectionBackgroundColor(QtGui.QColor("#555569"))

        fontmetrics = QtGui.QFontMetrics(self.font)
        self.setMarginsFont(self.font)
        self.setMarginWidth(0, fontmetrics.width("00000"))
        self.setMarginLineNumbers(0, True)
        self.setMarginsBackgroundColor(QtGui.QColor("#14141b"))
        self.setMarginsForegroundColor(QtGui.QColor("#434359"))

        self.setMarginSensitivity(1, True)
        self.markerDefine(QsciScintilla.RightArrow,
            self.ARROW_MARKER_NUM)
        self.setMarkerBackgroundColor(QtGui.QColor("#ffffff"),
            self.ARROW_MARKER_NUM)

        self.setBraceMatching(QsciScintilla.SloppyBraceMatch)

        self.setCaretLineVisible(True)
        self.setCaretLineBackgroundColor(QtGui.QColor("#191921"))
        self.setCaretForegroundColor(QtGui.QColor("#ffffff"))
        self.setMatchedBraceBackgroundColor(QtGui.QColor("#555569"))
        self.setMatchedBraceForegroundColor(QtGui.QColor("#ffffff"))


        text = bytearray(str.encode("Consolas"))
        self.SendScintilla(QsciScintilla.SCI_STYLESETFONT, 1, text)
        self.SendScintilla(QsciScintilla.SCI_SETHSCROLLBAR, 0)

        self.setMinimumSize(600, 450)

    def set_lexer(self, python = 0, yaml = 1):
        if python:
            lexer = python_lexer.python_lexer(self)
        elif yaml:
            lexer = yaml_lexer.yaml_lexer(self)
        else:
            lexer = neutral_lexer.neutral_lexer(self)

        self.setLexer(lexer)
        self.setUtf8(1)
        self.build()

    def text(self):
            return str(super(SimplePythonEditor, self).text()).encode('UTF-8')

    def on_margin_clicked(self, nmargin, nline, modifiers):
        if self.markersAtLine(nline) != 0:
            self.markerDelete(nline, self.ARROW_MARKER_NUM)
        else:
            self.markerAdd(nline, self.ARROW_MARKER_NUM)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    editor = SimplePythonEditor()
    editor.show()
    #editor.setText(open(sys.argv[0]).read())
    app.exec_()
