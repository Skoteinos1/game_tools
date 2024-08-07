#!/usr/local/bin/python3
import numpy as np
from PIL import Image, ImageDraw
import pyautogui
import os

# 1. Make empty GAME_NAME_.png image with desired dimensions... like 2000x2000.
#   It can work fith larger maps, but you have to adjust few numbers down the line
# 2. Make sure you are facing North and find out your position in game
# 3. Make sure your map is not obstructed by other window. We are doing screenshots here,
# 4. Enter your location in variables cor_x and cor_y
# 5. Run the code
# 6. It will take screenshot, crop the image, remove pointers, paste it into your GAME_NAME_x.png image and make GAME_NAME_x+1.png
# Enjoy

cor_x = 255
cor_y = -377
game_name = 'GAME_NAME_'  # In case you play multiple maps

# Length of side of map devided by 2.
# For example if you want your map to be for coordinates between -1000 and +1000, create empty image with size of 2000x2000 pixels
# and enter 1000 here
side_of_map = 1000

# pyautogui.moveTo(pos[0] + pos[1], pos[2] + pos[3])
# print(pyautogui.position())

# Location of minimap on your screen
x1 = 1658
y1 = 48
x2 = 1900
y2 = 290

# Screenshot / Open the input image as numpy array, convert to RGB
img = pyautogui.screenshot()
img = img.crop((x1, y1, x2, y2))
# img.show()  # Shows the image in image viewer

npImage = np.array(img)
h,w = img.size

# Create same size alpha layer with circle
alpha = Image.new('a', img.size,0)
draw = ImageDraw.Draw(alpha)
draw.pieslice([0,0,h,w],0,360,fill=255)

# Convert alpha Image to numpy array
npAlpha=np.array(alpha)

# Add alpha layer to RGB
npImage = np.dstack((npImage,npAlpha))

# Save with alpha
# Image.fromarray(npImage).save('result.png')
# img = Image.open('result.png').convert('RGBA') 
  
# Extracting the image data & creating an numpy array out of it 
img_arr = np.array(npImage)  # Somehow dstacked arrays ar not arrays

# Transparent rectangles. This removes your pointer on minimap as well as north pointer.
# If they are not removed correctly. Edit numbers in next 2 lines.
img_arr[108 : 134, 113 : 129] = (0, 0, 0, 0) 
img_arr[0 : 11, 114 : 129] = (0, 0, 0, 0)

# Open and convert to RGBA 
frontImage = Image.fromarray(img_arr).convert("RGBA") 

# Set Black-ish spots on screenshot as transparent
pixdata = frontImage.load()
for y in range(frontImage.size[1]):
    for x in range(frontImage.size[0]):
        if pixdata[x, y][0] < 35 and pixdata[x, y][1] < 35 and pixdata[x, y][2] < 35:
            # if pixdata[x, y] == (7, 10, 15, 255):
            pixdata[x, y] = (0, 0, 0, 0)

for i in range(100):
    if not os.path.exists(game_name+str(i)+'.png'):
        break
i-=1
background = Image.open(game_name+str(i)+'.png').convert("RGBA") 

x_fix = int((x2-x1)/2)
y_fix = int((y2-y1)/2)
# Paste the frontImage at coords
background.paste(frontImage, (cor_x+side_of_map-x_fix, (cor_y*-1)+side_of_map-y_fix), frontImage)   

# Save 
background.save(game_name+str(i+1)+'.png', format="png")