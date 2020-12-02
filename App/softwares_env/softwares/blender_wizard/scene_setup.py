from wizard.asset import main as asset_core
from wizard.prefs.main import prefs
import os
from wizard.vars import defaults

import bpy

prefs = prefs()


def match_frame_range(preroll=0):
    asset = asset_core.string_to_asset(os.environ[defaults._asset_var_])
    f_range = prefs.asset(asset).name.range
    print(f_range)
    # set timeline settings for all file scenes
    for s in  list(bpy.data.scenes):
        if preroll:
            preroll = prefs.asset(asset).name.preroll
            postroll = prefs.asset(asset).name.postroll
            f_range[0] = f_range[0] - preroll
            f_range[1] = f_range[1] + postroll
        bpy.data.scenes[s.name].frame_start = f_range[0]
        bpy.data.scenes[s.name].frame_end = f_range[1]


def match_project_format():
    imageFormat = prefs.format
    width=float(imageFormat[0])
    height=float(imageFormat[1])
    frame_rate = prefs.frame_rate

    # set project settings for all file scenes
    for s in list(bpy.data.scenes):
        bpy.data.scenes[s.name].render.resolution_x = width
        bpy.data.scenes[s.name].render.resolution_y = height
        bpy.data.scenes[s.name].render.pixel_aspect_x = 1
        bpy.data.scenes[s.name].render.pixel_aspect_y = 1
        bpy.data.scenes[s.name].render.fps = frame_rate
