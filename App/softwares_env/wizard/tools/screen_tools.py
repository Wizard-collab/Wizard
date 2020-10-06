from PyQt5 import QtWidgets
import pyautogui
from desktopmagic.screengrab_win32 import (
getDisplayRects, saveScreenToBmp, saveRectToBmp, getScreenAsImage,
getRectAsImage, getDisplaysAsImages)

def screen_shot_current_screen(file):
    screens_list = list(range(QtWidgets.QDesktopWidget().screenCount()))
    for screen in screens_list:
        rect = QtWidgets.QDesktopWidget().screenGeometry(screen)
        screen_1_h_bounds = [rect.x(), rect.x() + rect.width()]
        screen_1_v_bounds = [rect.y(), rect.y() + rect.height()]
        point_x_y = pyautogui.position()
        point_x = point_x_y.x
        point_y = point_x_y.y
        h_condition = ( point_x in range(screen_1_h_bounds[0], screen_1_h_bounds[-1]))
        v_condition = ( point_y in range(screen_1_v_bounds[0], screen_1_v_bounds[-1]))
        if h_condition and v_condition:
            break
    rect256 = getRectAsImage((screen_1_h_bounds[0], screen_1_v_bounds[0], screen_1_h_bounds[1], screen_1_v_bounds[1]))
    rect256.save(file, format='png')