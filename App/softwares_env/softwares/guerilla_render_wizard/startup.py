import sys
import os
#from wizard.vars import defaults

wizard_path = os.environ['abs_site_path']

sys.path.append(wizard_path+'/softwares_env/softwares')
sys.path.append(wizard_path+'/softwares_env')
sys.path.append(wizard_path+'/ressources/python27/Lib/site-packages/')

from softwares.guerilla_render_wizard import shelf
from softwares.guerilla_render_wizard import init_scene

shelf.shelf()
init_scene.create_main_node()