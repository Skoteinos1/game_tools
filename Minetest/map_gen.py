#!/usr/local/bin/python3
import numpy as np
from PIL import Image, ImageDraw
import pyautogui
import os

# 1. Make empty GAME_NAME_.png image with dimensions 2000x2000. It was designed for coords between -1000 - 1000
#   It can work fith larger maps, but you have to adjust few numbers down the line
# 2. Make sure you are facing North and find out your position
# 3. Make sure your map is not obstructed
# 4. Run the code
# 5. It will take screenshot
# Enjoy

cor_x = 255
cor_y = -377
game_name = 'GAME_NAME_'

# pyautogui.moveTo(pos[0] + pos[1], pos[2] + pos[3])
# print(pyautogui.position())

x1 = 1658
y1 = 48
x2 = 1900
y2 = 290

# Screenshot / Open the input image as numpy array, convert to RGB
img = pyautogui.screenshot()
img = img.crop((x1, y1, x2, y2))
