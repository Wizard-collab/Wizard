from PySide2 import QtWidgets, QtCore, QtGui
import substance_painter.ui

import os
import sys
path = os.path.abspath('softwares_env/')
sys.path.append(path)

for path in sys.path:
    print(path)

import plugin

from wizard.tools import log
logger = log.pipe_log(__name__)


plugin_widgets = []
"""Keep track of added ui elements for cleanup"""



def start_plugin():
    """This method is called when the plugin is started."""
    wizard_widget = wizard_toolbar()
    wizard_widget.setWindowTitle("Wizard")
    # Add this widget as a dock to the interface
    substance_painter.ui.add_dock_widget(wizard_widget)
    # Store added widget for proper cleanup when stopping the plugin
    plugin_widgets.append(wizard_widget)

def close_plugin():
    """This method is called when the plugin is stopped."""
    # We need to remove all added widgets from the UI.
    for widget in plugin_widgets:
        substance_painter.ui.delete_ui_element(widget)
    plugin_widgets.clear()

class wizard_toolbar(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)

        self.toolbar = QtWidgets.QToolBar()
        self.save_action = self.toolbar.addAction(QtGui.QIcon("C:/Users/conta/Documents/Allegorithmic/Substance Painter/python/plugins/save.png"), '')
        self.export_action = self.toolbar.addAction(QtGui.QIcon("C:/Users/conta/Documents/Allegorithmic/Substance Painter/python/plugins/export.png"), 'export')

        self.save_action.triggered.connect(plugin.save)

        self.layout = QtWidgets.QHBoxLayout()
        self.layout.addWidget(self.toolbar)
        self.setLayout(self.layout)
        self.setMinimumSize(100, 40)
        self.layout.setMargin(0)

if __name__ == "__main__":
    start_plugin()