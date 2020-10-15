import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.Qsci import *
import re
import copy

class python_lexer(QsciLexerCustom):
    def __init__(self, parent):
        super(python_lexer, self).__init__(parent)
        # Default text settings
        # ----------------------

        default_font = QFont("Consolas", 10)
        italic_font = QFont("Consolas", 10)
        italic_font.setItalic(1)

        self.setDefaultFont(default_font)
        self.setDefaultPaper(QColor("#14141b"))
        self.setDefaultColor(QColor("#c0c0d1"))

        # Initialize colors per style
        # ----------------------------
        self.setColor(QColor("#ffffff"), 0)   # Style 0: default
        self.setColor(QColor("#ff80bb"), 1)   # Style 1: keyword
        self.setColor(QColor("#555569"), 2)   # Style 2: comment
        self.setColor(QColor("#caff80"), 3)   # Style 2: function
        self.setColor(QColor("#88c6fc"), 4)   # Style 2: function key
        self.setColor(QColor("#ffa061"), 5)   # Style 2: class key
        self.setColor(QColor("#88c6fc"), 6)   # Style 2: function call
        self.setColor(QColor("#ffe085"), 7)   # Style 2: string



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
        ###
        return ""
    '''
    def styleText(self, start, end):
        # 1. Initialize the styling procedure
        # ------------------------------------
        self.startStyling(start)

        # 2. Slice out a part from the text
        # ----------------------------------
        text = self.parent().text()[start:end]

        # 3. Tokenize the text
        # ---------------------
        p = re.compile(r"[*]\/|\/[*]|\s+|\w+|\W")

        # 'token_list' is a list of tuples: (token_name, token_len)
        token_list = [ (token, len(bytearray(token, "utf-8"))) for token in p.findall(text.decode('utf-8'))]

        # 4. Style the text
        # ------------------
        # 4.1 Check if multiline comment
        multiline_comm_flag = False
        editor = self.parent()
        if start > 0:
            previous_style_nr = editor.SendScintilla(editor.SCI_GETSTYLEAT, start - 1)
            if previous_style_nr == 3:
                multiline_comm_flag = True
        # 4.2 Style the text in a loop

        for line in text.decode('utf-8').splitlines():
            if line.startswith('#'):
                print(line+' comment')
            else:
                for token in line.split(' '):
                    print(token)
        '''

    def styleText(self, start, end):
        editor = self.editor()
        if editor is None:
            return

        source = ''
        if end > editor.length():
            end = editor.length()
        if end > start:
            source = bytearray(end - start)
            editor.SendScintilla(editor.SCI_GETTEXTRANGE, start, end, source)

        

        if not source:
            return

        # The line index will also be needed to implement folding
        index = editor.SendScintilla(editor.SCI_LINEFROMPOSITION, start)
        if index > 0:
            # The previous state may be needed for multi-line styling
            pos = editor.SendScintilla(editor.SCI_GETLINEENDPOSITION, index
                                       - 1)
            state = editor.SendScintilla(editor.SCI_GETSTYLEAT, pos)
        else:
            state = 0


        set_style = self.setStyling
        self.startStyling(start, 0x1f)

        # Scintilla always asks to style whole lines

        source = source.decode('utf-8')
        p = re.compile(r"[*]\/|\/[*]|\s+|\w+|\W")

        for line in source.splitlines(True):

            length = len(line)

            if line.startswith('#'):
                state = 2
                set_style(length, state)

            else:

                # 'token_list' is a list of tuples: (token_name, token_len)
                token_list = [ (token, len(bytearray(token, "utf-8"))) for token in p.findall(line)]

                next_is_fun_name = 0
                single_quote_started = 0

                for i, token in enumerate(token_list):

                    style = 0

                    print(token)

                    if not single_quote_started:
                        if (i+1) < len(token_list):
                            if token_list[i+1][0] == '(':
                                if next_is_fun_name:
                                    style = 3
                                    next_is_fun_name = 0
                                else:
                                    style = 6
                                    next_is_fun_name = 0
                        if token[0] in self.keyword_list:
                            style = 1
                            next_is_fun_name = 0
                        elif token[0] in self.function_key_list:
                            style = 4
                            next_is_fun_name = 1
                        elif token[0] in self.class_keys_list:
                            style = 5
                            next_is_fun_name = 0
                        elif token[0] == '"':
                            single_quote_started = 1
                            style = 7
                    else:
                        style = 7
                        if token[0] == '"':
                            single_quote_started = 0

                    self.setStyling(token[1], style)

        
        
