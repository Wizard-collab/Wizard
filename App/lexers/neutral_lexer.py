import sys
from PyQt5 import QtGui
from PyQt5.Qsci import QsciLexerCustom
import re
import copy

class neutral_lexer(QsciLexerCustom):
    def __init__(self, parent):
        super(neutral_lexer, self).__init__(parent)

        default_font = QtGui.QFont("Consolas", 9)
        italic_font = QtGui.QFont("Consolas", 9)
        italic_font.setItalic(1)

        self.setDefaultFont(default_font)
        self.setDefaultPaper(QtGui.QColor("#14141b"))
        self.setDefaultColor(QtGui.QColor("#c0c0d1"))

        self.setColor(QtGui.QColor("#ffffff"), 0)   # Style 0: default

    def language(self):
        return "Neutral"

    def description(self, style):
        if style == 0:
            return "myStyle_0"
        return ""

    def styleText(self, start, end):
        editor = self.editor()
        if editor is None:
            return
        self.setStyling(editor.length(), 0)
