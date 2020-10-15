import sys
from PyQt5 import QtGui
from PyQt5.Qsci import QsciLexerCustom
import re
import copy

class python_lexer(QsciLexerCustom):
    def __init__(self, parent):
        super(python_lexer, self).__init__(parent)

        default_font = QtGui.QFont("Consolas", 9)
        italic_font = QtGui.QFont("Consolas", 9)
        italic_font.setItalic(1)

        self.setDefaultFont(default_font)
        self.setDefaultPaper(QtGui.QColor("#14141b"))
        self.setDefaultColor(QtGui.QColor("#c0c0d1"))

        self.setColor(QtGui.QColor("#ffffff"), 0)   # Style 0: default
        self.setColor(QtGui.QColor("#ff80bb"), 1)   # Style 1: keyword
        self.setColor(QtGui.QColor("#555569"), 2)   # Style 2: comment
        self.setColor(QtGui.QColor("#caff80"), 3)   # Style 2: function
        self.setColor(QtGui.QColor("#88c6fc"), 4)   # Style 2: function key
        self.setColor(QtGui.QColor("#ffa061"), 5)   # Style 2: class key
        self.setColor(QtGui.QColor("#88c6fc"), 6)   # Style 2: function call
        self.setColor(QtGui.QColor("#ffe085"), 7)   # Style 2: string
        self.setColor(QtGui.QColor("#d270ff"), 8)   # Style 2: string

        self.setFont(italic_font, 4)
        self.setFont(italic_font, 5)

        self.keyword_list = ["from",
                            "import",
                            "if",
                            "elif",
                            "else",
                            "finally",
                            "try",
                            "except",
                            "for",
                            "while",
                            "return",
                            "=",
                            "+",
                            "*"
                            "-",
                            "/",
                            "*",
                            "!",
                            "<",
                            ">",
                            "@",
                            '__name__']

        self.function_key_list = ['def', 'class']
        self.class_keys_list = ['self', 'parent']
        self.string_quotes = ['"', "'"]
        self.comment_quotes = ["#"]
        self.boolean_list = ['True', 'False', 'None']
        self.return_list = ['\n', '\r', '\r\n', '\\r', '\\n', '\\r\\n', '\n\n', '\\n\\n']

    def language(self):
        return "Python"

    def description(self, style):
        if style == 0:
            return "myStyle_0"
        elif style == 1:
            return "myStyle_1"
        elif style == 2:
            return "myStyle_2"
        elif style == 3:
            return "myStyle_3"
        elif style == 4:
            return "myStyle_4"
        elif style == 5:
            return "myStyle_5"
        elif style == 6:
            return "myStyle_6"
        elif style == 7:
            return "myStyle_7"
        elif style == 8:
            return "myStyle_8"
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

        token_list = [(token, len(bytearray(token, "utf-8"))) for token in p.findall(source)]

        next_is_fun_name = 0
        string_started = None
        comment_started = None

        for i, token in enumerate(token_list):

            try:
                float(token[0])
                is_number = 1
            except:
                is_number = 0

            if not string_started and not comment_started:

                if token[0] in self.keyword_list:
                    style = 1
                    next_is_fun_name = 0
                elif token[0] in self.function_key_list:
                    style = 4
                    next_is_fun_name = 1
                elif token[0] in self.class_keys_list:
                    style = 5
                    next_is_fun_name = 0
                elif token[0] in self.string_quotes:
                    string_started = token[0]
                    style = 7
                elif token[0] in self.comment_quotes:
                    comment_started = token[0]
                    style = 2
                elif is_number or token[0] in self.boolean_list:
                    style = 8
                    is_number = 0
                else:
                    
                    style = 0

                    if (i+1) < len(token_list):
                        if token_list[i+1][0] == '(':
                            if next_is_fun_name:
                                style = 3
                                next_is_fun_name = 0
                            else:
                                style = 6
                                next_is_fun_name = 0

            elif string_started:
                style = 7
                if token[0] == string_started:
                    string_started = None

            elif comment_started:
                style = 2
                for item in self.return_list:
                	if item in token[0]:
                		comment_started = None
                		break

            self.setStyling(token[1], style)
