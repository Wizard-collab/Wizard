from addon_utils import enable
import sys
import os

# add softwares_env to path
sys.path.append(str(os.path.dirname(os.path.abspath(__file__))).rpartition('softwares')[0])
# add site_packages to path
sys.path.append(str(os.path.dirname(os.path.abspath(__file__))).rpartition('softwares_env')[0]+'\\ressources\\python37\\Lib\\site-packages')
# add blender_wizard to path
sys.path.append(str(os.path.dirname(os.path.abspath(__file__))))

# from wizard.tools import log
try:
    enable("shelf")
    # logger.info("Wizard installed")
except:
    # logger.warning("Wizard addon already installed")
    print("Wizard addon already installed.")
