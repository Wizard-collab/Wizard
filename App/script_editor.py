import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.Qsci import QsciScintilla, QsciLexerPython
from PyQt5 import Qsci
from wizard.vars import python_lexer

#Bonsoir

class SimplePythonEditor(QsciScintilla):
    ARROW_MARKER_NUM = 8

    def __init__(self, parent=None):
        super(SimplePythonEditor, self).__init__(parent)

        font = QFont()
        font.setFamily('Consolas')
        font.setFixedPitch(True)
        font.setPointSize(10)

        bold_font = QFont()
        bold_font.setFamily('Consolas')
        bold_font.setFixedPitch(True)
        bold_font.setPointSize(10)
        bold_font.setBold(1)


        self.setFont(font)
        self.setMarginsFont(font)

        self.setIndentationGuides(True)
        self.setIndentationGuidesForegroundColor(QColor("#555569"))
        self.setIndentationGuidesBackgroundColor(QColor("#555569"))

        self.setTabWidth(4)
        self.setAutoIndent(True)
        self.setWrapMode(QsciScintilla.WrapWord)
        self.setWrapIndentMode(QsciScintilla.WrapIndentIndented)
        self.setSelectionBackgroundColor(QColor("#555569"))

        fontmetrics = QFontMetrics(font)
        self.setMarginsFont(font)
        self.setMarginWidth(0, fontmetrics.width("00000"))
        self.setMarginLineNumbers(0, True)
        self.setMarginsBackgroundColor(QColor("#14141b"))
        self.setMarginsForegroundColor(QColor("#434359"))

        self.setMarginSensitivity(1, True)
        self.markerDefine(QsciScintilla.RightArrow,
            self.ARROW_MARKER_NUM)
        self.setMarkerBackgroundColor(QColor("#ffffff"),
            self.ARROW_MARKER_NUM)

        self.setBraceMatching(QsciScintilla.SloppyBraceMatch)

        self.setCaretLineVisible(True)
        self.setCaretLineBackgroundColor(QColor("#191921"))
        self.setCaretForegroundColor(QColor("#ffffff"))
        self.setMatchedBraceBackgroundColor(QColor("#555569"))
        self.setMatchedBraceForegroundColor(QColor("#ffffff"))


        lexer = python_lexer.python_lexer(self)
        '''
        lexer.setDefaultFont(font)
        lexer.setDefaultPaper(QColor("#14141b"))
        lexer.setDefaultColor(QColor("#c0c0d1"))

        lexer.setColor(QColor("#555569"), lexer.Comment)
        lexer.setColor(QColor("#555569"), lexer.CommentBlock)
        lexer.setColor(QColor("#8ca0ff"), lexer.Number)
        lexer.setColor(QColor("#ff8787"), lexer.DoubleQuotedString)
        lexer.setColor(QColor("#ff8787"), lexer.SingleQuotedString)
        lexer.setColor(QColor("#ff8ce2"), lexer.Keyword)
        lexer.setColor(QColor("#b1ff7d"), lexer.ClassName)
        lexer.setColor(QColor("#b1ff7d"), lexer.FunctionMethodName)
        lexer.setColor(QColor("#b1ff7d"), lexer.Operator)

        lexer.setFont(font, lexer.Comment)
        lexer.setFont(font, lexer.CommentBlock)
        lexer.setFont(bold_font, lexer.Number)
        lexer.setFont(bold_font, lexer.DoubleQuotedString)
        lexer.setFont(bold_font, lexer.SingleQuotedString)
        lexer.setFont(bold_font, lexer.Keyword)
        lexer.setFont(bold_font, lexer.ClassName)
        lexer.setFont(bold_font, lexer.FunctionMethodName)
        lexer.setFont(bold_font, lexer.Operator)
        '''
        self.setLexer(lexer)

        self.setUtf8(1)

        text = bytearray(str.encode("Consolas"))
        self.SendScintilla(QsciScintilla.SCI_STYLESETFONT, 1, text)
        self.SendScintilla(QsciScintilla.SCI_SETHSCROLLBAR, 0)

        self.setMinimumSize(600, 450)

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
    editor.setText(open(sys.argv[0]).read())
    app.exec_()
