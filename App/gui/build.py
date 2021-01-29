import sys

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMenu, QAction

from wizard.prefs.user import user
from wizard.vars import defaults



def launch_stray(widget, app, title = 'Wizard'):

    main = widget
    main.setWindowTitle(title)
    main.setStyleSheet(load_stylesheet())


    tray_icon = QtWidgets.QSystemTrayIcon(main)
    tray_icon.setIcon(QtGui.QIcon(defaults._server_ico_))

    show_action = QAction("Open", main)
    quit_action = QAction("Exit", main)
    hide_action = QAction("Hide", main)

    show_action.triggered.connect(main.show)
    hide_action.triggered.connect(main.hide)
    quit_action.triggered.connect(app.quit)

    tray_menu = QMenu()

    tray_menu.addAction(show_action)
    tray_menu.addAction(hide_action)
    tray_menu.addAction(quit_action)
    tray_menu.setStyleSheet(load_stylesheet())
    tray_icon.setContextMenu(tray_menu)

    main.show()
    tray_icon.show()

    sys.exit(app.exec_())

def launch_normal(widget, title = 'Wizard'):

    app = QtWidgets.QApplication(sys.argv)
    main = widget
    main.setWindowTitle(title)
    main.setStyleSheet(load_stylesheet())


    main.show()
    sys.exit(app.exec_())

def launch_chat(widget, title = 'Chat room'):
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(defaults._wizard_ico_))
    main = widget()
    main.setWindowTitle(title)
    main.setStyleSheet(load_stylesheet())
    main.show()
    sys.exit(app.exec_())

def launch_position_frameless_ontop_as_child(widget, title = 'Wizard'):
    widget.setWindowTitle(title)
    widget.setStyleSheet(load_stylesheet())
    widget.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
    widget.setAttribute(QtCore.Qt.WA_TranslucentBackground)
    win_size = (widget.frameSize().width(), widget.frameSize().height())
    posx = QtGui.QCursor.pos().x() - 20
    posy = int(QtGui.QCursor.pos().y()) - win_size[1] + 20
    rect = QtWidgets.QDesktopWidget().screenGeometry()
    screen_1_h_bounds = [rect.x(), rect.x() + rect.width()]
    screen_1_v_bounds = [rect.y(), rect.y() + rect.height()]
    if posx + win_size[0] + 20 >= screen_1_h_bounds[-1]:
        posx = posx - win_size[0] + 40
    if posy - 20 <= screen_1_v_bounds[0]:
        posy = posy + win_size[1] - 40
    shadow = QtWidgets.QGraphicsDropShadowEffect()
    shadow.setBlurRadius(8)
    shadow.setColor(QtGui.QColor(0, 0, 0, 180))
    shadow.setXOffset(0)
    shadow.setYOffset(0)
    widget.setGraphicsEffect(shadow)

    widget.show()
    widget.move(posx, posy)

def launch_file_viewer(widget, title = 'File viewer'):

    app = QtWidgets.QApplication(sys.argv)
    main = widget
    main.setWindowTitle(title)
    main.setStyleSheet(load_stylesheet())

    main.show()
    sys.exit(app.exec_())

class launch_stray_server:
    def __init__(self, widget, app):

        self.main = widget
        self.main.setWindowTitle('Wizard - server')
        self.main.setStyleSheet(load_stylesheet())
        #self.main.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #self.main.setWindowFlags(QtCore.Qt.SplashScreen | QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)

        tray_icon = QtWidgets.QSystemTrayIcon(self.main)
        tray_icon.setIcon(QtGui.QIcon(defaults._server_ico_))
        tray_icon.activated.connect(self.systemIcon)

        show_action = QAction("Open", self.main)
        quit_action = QAction("Exit", self.main)
        hide_action = QAction("Hide", self.main)

        show_action.triggered.connect(self.main.show)
        hide_action.triggered.connect(self.main.hide)
        quit_action.triggered.connect(self.main.quit)

        tray_menu = QMenu()

        tray_menu.addAction(show_action)
        tray_menu.addAction(hide_action)
        tray_menu.addAction(quit_action)
        tray_icon.setContextMenu(tray_menu)
        tray_icon.show()
        #self.main.show()
        sys.exit(app.exec_())

    def systemIcon(self, reason):
        if reason == QtWidgets.QSystemTrayIcon.Trigger:
            if self.main.isVisible():
                self.main.hide()
            else:
                self.main.show()

class launch_stray_as_child:
    def __init__(self,widget, app, title):

        self.widget = widget

        self.main = widget
        self.main.setStyleSheet(load_stylesheet())
        #QtWidgets.QApplication.setStyle('Windows')
        self.main.setWindowTitle(title)
        #widget.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        shutter = user().get_shutter()

        if shutter:
            widget.setWindowFlags(QtCore.Qt.FramelessWindowHint)# | QtCore.Qt.WindowStaysOnTopHint)

        tray_icon = QtWidgets.QSystemTrayIcon(self.main)
        tray_icon.setIcon(QtGui.QIcon(defaults._wizard_ico_))
        if shutter:
            tray_icon.activated.connect(self.systemIcon)

        show_action = QAction("Open", self.main)
        quit_action = QAction("Exit", self.main)
        hide_action = QAction("Hide", self.main)

        if shutter:
            show_action.triggered.connect(self.main.show_animation)
            hide_action.triggered.connect(self.main.hide_animation)
        quit_action.triggered.connect(self.main.close)

        tray_menu = QMenu()

        if shutter:
            tray_menu.addAction(show_action)
            tray_menu.addAction(hide_action)
        tray_menu.addAction(quit_action)
        tray_icon.setContextMenu(tray_menu)
        tray_menu.setStyleSheet(load_stylesheet())
        
        if not shutter:
            pass
            self.main.show()
            self.main.setWindowState(QtCore.Qt.WindowMaximized)
        else:
            self.main.show()

        if shutter:
            self.main.move_window()
            self.main.show_animation()

        tray_icon.show()
        sys.exit(app.exec_())

    def systemIcon(self, reason):
        if reason == QtWidgets.QSystemTrayIcon.Trigger:
            if self.main.isVisible():
                self.main.hide_animation()
            else:
                self.main.show_animation()

def launch_dialog_as_child(widget):
    widget.setWindowTitle('Wizard')
    widget.setStyleSheet(load_stylesheet())
    #widget.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    if widget.exec_() == QtWidgets.QDialog.Accepted:
        return 1
    else:
        return 0

def launch_dialog_comment(widget):
    widget.setWindowTitle('Wizard')
    widget.setStyleSheet(load_stylesheet())
    #widget.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
    if widget.exec_() == QtWidgets.QDialog.Accepted:
        return 1
    else:
        return 0

def launch_dialog_as_child_frameless(widget):
    widget.setWindowTitle('Wizard')
    widget.setStyleSheet(load_stylesheet())
    widget.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    if widget.exec_() == QtWidgets.QDialog.Accepted:
        return 1
    else:
        return 0

def launch_dialog_as_child_frameless_trans(widget):
    widget.setWindowTitle('Wizard')
    widget.setStyleSheet(load_stylesheet())
    widget.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    widget.setAttribute(QtCore.Qt.WA_TranslucentBackground)
    if widget.exec_() == QtWidgets.QDialog.Accepted:
        return 1
    else:
        return 0

def launch_normal_as_child(widget, minimized = 0):
    widget.setWindowTitle('Wizard')
    widget.setStyleSheet(load_stylesheet())
    if minimized:
        widget.showMinimized()
    else:
        widget.show()

def launch_normal_as_child_ontop(widget):
    widget.setWindowTitle('Wizard')
    widget.setStyleSheet(load_stylesheet())
    widget.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
    widget.show()

def launch_normal_as_child_frameless(widget):
    widget.setWindowTitle('Wizard')
    widget.setStyleSheet(load_stylesheet())
    widget.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    widget.setAttribute(QtCore.Qt.WA_TranslucentBackground)
    widget.show()

def launch_normal_as_child_frameless_no_transparent(widget):
    widget.setWindowTitle('Wizard')
    widget.setStyleSheet(load_stylesheet())
    widget.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    widget.setAttribute(QtCore.Qt.WA_TranslucentBackground)
    widget.show()

def launch_normal_as_child_frameless_ontop(widget):
    widget.setWindowTitle('Wizard')
    widget.setStyleSheet(load_stylesheet())
    widget.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
    widget.setAttribute(QtCore.Qt.WA_TranslucentBackground)
    widget.show()

def launch_options(widget):
    widget.setWindowTitle('Wizard')
    widget.setStyleSheet(load_stylesheet())
    widget.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    widget.setAttribute(QtCore.Qt.WA_TranslucentBackground)
    if len(widget.items) > 1:
        widget.items[0].setStyleSheet('border-top-left-radius:10px;border-top-right-radius:10px')
        widget.items[-1].setStyleSheet('border-bottom-right-radius:10px')
    else:
        widget.items[0].setStyleSheet('border-top-left-radius:10px;border-top-right-radius:10px;border-bottom-right-radius:10px')
    widget.show()
    widget.move_ui()

def launch_running(widget):
    widget.setWindowTitle('Wizard')
    widget.setStyleSheet(load_stylesheet())
    widget.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
    widget.setAttribute(QtCore.Qt.WA_TranslucentBackground)
    widget.show()
    widget.move_ui()

def launch_running_dialog(widget):
    widget.setWindowTitle('Wizard')
    widget.setStyleSheet(load_stylesheet())
    widget.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
    widget.setAttribute(QtCore.Qt.WA_TranslucentBackground)
    widget.move_ui()
    if widget.exec_() == QtWidgets.QDialog.Accepted:
        return 1
    else:
        return 0

def launch_imported_asset_dialog(widget):
    widget.setWindowTitle('Wizard')
    widget.setStyleSheet(load_stylesheet())
    widget.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    widget.setAttribute(QtCore.Qt.WA_TranslucentBackground)
    widget.move_ui()
    if widget.exec_() == QtWidgets.QDialog.Accepted:
        return 1
    else:
        return 0

def launch_popup(widget):
    widget.setWindowTitle('Wizard')
    widget.setStyleSheet(load_stylesheet())
    widget.setAttribute(QtCore.Qt.WA_TranslucentBackground)
    widget.setAttribute(QtCore.Qt.WA_ShowWithoutActivating)
    widget.move2ScreenBottom()
    widget.show()

def launch_wizard_desktop(widget):
    widget.setWindowTitle('Wizard')
    widget.setStyleSheet(load_stylesheet())
    widget.setAttribute(QtCore.Qt.WA_TranslucentBackground)
    widget.setWindowFlags(QtCore.Qt.SplashScreen | QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
    widget.move2ScreenTop()
    widget.show()

def load_stylesheet(theme = None, chat_theme = None):

    user_prefs = user()

    with open(defaults._stylesheet_template_, 'r') as f:
        stylesheet = f.read()

    if theme == None:
        theme = user_prefs.get_theme()

    if chat_theme == None:
        chat_theme = user_prefs.get_chat_theme()
        
    stylesheet = conform_stylesheet(stylesheet, theme, chat_theme)

    return stylesheet

def conform_stylesheet(stylesheet, theme, chat_theme):

    for string, value in defaults._themes_dic_[defaults._dark_theme_key_].items():
        stylesheet = stylesheet.replace(string, value)

    stylesheet = stylesheet.replace(defaults._message_color_replace_key_, defaults._message_colors_dic_[chat_theme])

    return stylesheet