import os
import cv2
import numpy as np

def make_video(images, file): 
    img_array = []
    for filename in images:
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        img_array.append(img)
    
    if img_array != []:
        out = cv2.VideoWriter(file, cv2.VideoWriter_fourcc(*'JPEG'), 24, size)
         
        for i in range(len(img_array)):
            out.write(img_array[i])
        out.release()