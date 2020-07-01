from wizard.vars import defaults
import pymel.core as pm
import maya.cmds as cmds
from wizard.prefs import project as porject_prefs
from maya_wizard import plugin

class menu():
	def __init__(self):
		self.createMenu()
	
	def createMenu(self):

			mainMayaWindow = pm.language.melGlobals['gMainWindow'] 
			
			mainMenu = pm.menu(l='Wizard', parent=mainMayaWindow, tearOff=1)
			
			cmds.menuItem(divider=True, label='Tools', parent=mainMenu)

			copy_paste_menu = pm.menuItem(l='Copy / Paste', subMenu=True, parent=mainMenu, i='')
			
			pm.menuItem(l='Copy ( selection )', c=self.copy_selection, i='')
			pm.setParent(copy_paste_menu, menu=True)
			pm.menuItem(l='Copy ( scene )', c=self.copy_scene, i='')
			pm.setParent(copy_paste_menu, menu=True)
			pm.menuItem(l='Paste', c=self.paste, i='')
			pm.setParent(copy_paste_menu, menu=True)

	def paste(self, *args):
		plugin.paste_team()

	def copy_selection(self, *args):
		plugin.copy_team()

	def copy_scene(self, *args):
		plugin.copy_team(False)
