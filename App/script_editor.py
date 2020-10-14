#-------------------------------------------------------------------------
# qsci_simple_pythoneditor.pyw
#
# QScintilla sample with PyQt
#
# Eli Bendersky (eliben@gmail.com)
# This code is in the public domain
#-------------------------------------------------------------------------
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.Qsci import QsciScintilla, QsciLexerPython
from PyQt5 import Qsci


class SimplePythonEditor(QsciScintilla):
    ARROW_MARKER_NUM = 8

    def __init__(self, parent=None):
        super(SimplePythonEditor, self).__init__(parent)

        # Set the default font
        font = QFont()
        font.setFamily('Courier New')
        font.setFixedPitch(True)
        font.setPointSize(10)
        self.setFont(font)
        self.setMarginsFont(font)
        self.setIndentationGuides(True)
        self.setTabWidth(4)
        self.setAutoIndent(True)
        self.setWrapMode(QsciScintilla.WrapWord)
        self.setWrapIndentMode(QsciScintilla.WrapIndentIndented)
        self.setSelectionBackgroundColor(QColor("#555569"))

        # Margin 0 is used for line numbers
        fontmetrics = QFontMetrics(font)
        self.setMarginsFont(font)
        self.setMarginWidth(0, fontmetrics.width("00000"))
        self.setMarginLineNumbers(0, True)
        self.setMarginsBackgroundColor(QColor("#191921"))
        self.setMarginsForegroundColor(QColor("#434359"))

        # Clickable margin 1 for showing markers
        self.setMarginSensitivity(1, True)
#        self.connect(self,
#            SIGNAL('marginClicked(int, int, Qt::KeyboardModifiers)'),
#            self.on_margin_clicked)
        self.markerDefine(QsciScintilla.RightArrow,
            self.ARROW_MARKER_NUM)
        self.setMarkerBackgroundColor(QColor("#ffffff"),
            self.ARROW_MARKER_NUM)

        # Brace matching: enable for a brace immediately before or after
        # the current position
        #
        self.setBraceMatching(QsciScintilla.SloppyBraceMatch)

        # Current line visible with special background color
        self.setCaretLineVisible(True)
        self.setCaretLineBackgroundColor(QColor("#191921"))
        self.setCaretForegroundColor(QColor("#ffffff"))
        self.setMatchedBraceBackgroundColor(QColor("#555569"))
        self.setMatchedBraceForegroundColor(QColor("#8ca0ff"))

        # Set Python lexer
        # Set style for Python comments (style number 1) to a fixed-width
        # courier.
        #

        lexer = QsciLexerPython()
        lexer.setDefaultFont(font)
        lexer.setDefaultPaper(QColor("#14141b"))
        lexer.setDefaultColor(QColor("#ffffff"))
        lexer.setColor(QColor("#555569"), lexer.Comment)
        lexer.setColor(QColor("#555569"), lexer.CommentBlock)
        lexer.setColor(QColor("#8ca0ff"), lexer.Number)
        lexer.setColor(QColor("#ff8787"), lexer.DoubleQuotedString)
        lexer.setColor(QColor("#ff8787"), lexer.SingleQuotedString)
        lexer.setColor(QColor("#b1ff7d"), lexer.Keyword)
        lexer.setColor(QColor("#ff8ce2"), lexer.ClassName)
        lexer.setColor(QColor("#ff8ce2"), lexer.FunctionMethodName)
        lexer.setColor(QColor("#b1ff7d"), lexer.Operator)
        self.setLexer(lexer)

        self.setUtf8(1)

        text = bytearray(str.encode("Arial"))
# 32, "Courier New"         
        self.SendScintilla(QsciScintilla.SCI_STYLESETFONT, 1, text)

        # Don't want to see the horizontal scrollbar at all
        # Use raw message to Scintilla here (all messages are documented
        # here: http://www.scintilla.org/ScintillaDoc.html)
        self.SendScintilla(QsciScintilla.SCI_SETHSCROLLBAR, 0)

        # not too small
        self.setMinimumSize(600, 450)

    def text(self):
            return str(super(SimplePythonEditor, self).text()).encode('UTF-8')

    def on_margin_clicked(self, nmargin, nline, modifiers):
        # Toggle marker for the line the margin was clicked on
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
