import sd
from PySide2 import QtWidgets, QtGui
import plugin
import importlib
importlib.reload(plugin)
import os

app = sd.getContext().getSDApplication()
uiMgr = app.getQtForPythonUIMgr()

# Plugin entry point. Called by Designer when loading a plugin.
def initializeSDPlugin():

	# Create a new menu.
	menu = uiMgr.newMenu(menuTitle="Wizard", objectName="wizard_menu")
	# Create a new action.

	currentDir = os.path.dirname(__file__)

	save_action = QtWidgets.QAction('Save', menu)
	save_action.triggered.connect(plugin.save)
	save_action.setIcon(QtGui.QIcon(os.path.join(currentDir, 'save.png')))

	export_action = QtWidgets.QAction('Export ( sbsar )', menu)
	export_action.triggered.connect(plugin.export_sbsar)
	export_action.setIcon(QtGui.QIcon(os.path.join(currentDir, 'export.png')))

	# Add the action to the menu.
	menu.addAction(save_action)
	menu.addAction(export_action)

# If this function is present in your plugin,
# it will be called by Designer when unloading the plugin.
def uninitializeSDPlugin():
	uiMgr.deleteMenu("wizard_menu")
