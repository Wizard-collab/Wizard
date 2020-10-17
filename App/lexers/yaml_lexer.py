import sys
from PyQt5 import QtGui
from PyQt5.Qsci import QsciLexerCustom
import re
import copy

class yaml_lexer(QsciLexerCustom):
    def __init__(self, parent):
        super(yaml_lexer, self).__init__(parent)

        default_font = QtGui.QFont("Consolas", 9)
        italic_font = QtGui.QFont("Consolas", 9)
        italic_font.setItalic(1)

        self.setDefaultFont(default_font)
        self.setDefaultPaper(QtGui.QColor("#14141b"))
        self.setDefaultColor(QtGui.QColor("#c0c0d1"))

        self.setColor(QtGui.QColor("#ffffff"), 0)   # Style 0: default
        self.setColor(QtGui.QColor("#ff80bb"), 1)   # Style 1: keyword
        
        self.setFont(italic_font, 1)

    def language(self):
        return "Yaml"

    def description(self, style):
        if style == 0:
            return "myStyle_0"
        elif style == 1:
            return "myStyle_1"
        return ""

    def styleText(self, start, end):
        editor = self.editor()
        if editor is None:
            return

        source = ''
        end = editor.length()
        start = 0
        if end > start:
            source = bytearray(end - start)
            editor.SendScintilla(editor.SCI_GETTEXTRANGE, start, end, source)

        if not source:
            return

        index = editor.SendScintilla(editor.SCI_LINEFROMPOSITION, start)
        if index > 0:
            pos = editor.SendScintilla(editor.SCI_GETLINEENDPOSITION, index
                                       - 1)
            state = editor.SendScintilla(editor.SCI_GETSTYLEAT, pos)
        else:
            state = 0

        set_style = self.setStyling
        self.startStyling(start, 0x1f)

        source = source.decode('utf-8')
        p = re.compile(r"[*]\/|\/[*]|\s+|\w+|\W")

        token_list = [ (token, len(bytearray(token, "utf-8"))) for token in p.findall(source)]

        for i, token in enumerate(token_list):

            if i+1 < len(token_list):
                if token_list[i+1][0] == ':':
                    style = 1
                else:
                    style = 0
            else:
                style = 0

            self.setStyling(token[1], style)
