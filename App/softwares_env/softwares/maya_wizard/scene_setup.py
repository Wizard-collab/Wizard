import maya.cmds as cmds
from wizard.asset import main as asset_core
from wizard.prefs.main import prefs
import os
from wizard.vars import defaults

prefs = prefs()

def set_f_range(preroll=0):
    asset = asset_core.string_to_asset(os.environ[defaults._asset_var_])
    f_range = prefs.asset(asset).name.range
    
    if preroll:
        preroll = prefs.asset(asset).name.preroll
        postroll = prefs.asset(asset).name.postroll
        f_range[0] = f_range[0]-preroll
        f_range[1] = f_range[1]+postroll

    cmds.playbackOptions(animationStartTime=f_range[0], minTime=f_range[0], animationEndTime=f_range[1], maxTime=f_range[1])

def setFormatToMaya():
    imageFormat = prefs.format
    width=float(imageFormat[0])
    height=float(imageFormat[1])
    dar=width/height
    cmds.setAttr('defaultResolution.w', width)
    cmds.setAttr('defaultResolution.h', height)
    cmds.setAttr('defaultResolution.pa', 1)
    cmds.setAttr('defaultResolution.dar', dar)