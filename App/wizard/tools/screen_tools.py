from PyQt5 import QtWidgets
import pyautogui

def get_current_screen():
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
	return (screen_1_h_bounds[0],screen_1_v_bounds[0], screen_1_h_bounds[1], screen_1_v_bounds[1])