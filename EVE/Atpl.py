'''
Copy Images from Img Folder to this folder.
Just set your route in game and run the code.
Difference between in-game autopilot and this code is that in game autopilot comes out of warp 10km from jump gate. And this code comes out exactly on gate. Then just jumps
through gate, waits a little bit there and then jumps to next one until it docks in desired station. Click positions and waiting times are not completely random to simulate more
human like behavior.
If they catch you, you will be banned from game.
'''

import cv2  # pip install opencv-python
import numpy as np
import pyautogui
import random
import time
import platform
import subprocess
from pynput.mouse import Button, Controller

mouse = Controller()

policka = 12
car_lvl = 11

is_retina = False
if platform.system() == "Darwin":
    is_retina = subprocess.call("system_profiler SPDisplaysDataType | grep 'retina'", shell=True)


def imagesearch(image, precision=0.8):
    '''
    Searchs for an image on the screen
    input :
    image : path to the image file (see opencv imread for supported types)
    precision : the higher, the lesser tolerant and fewer false positives are found default is 0.8
    im : a PIL image, usefull if you intend to search the same unchanging region for several elements
    returns :
    the top left corner coordinates of the element if found as an array [x,y] or [-1,-1] if not
    '''
    im = pyautogui.screenshot()
    if is_retina:
        im.thumbnail((round(im.size[0] * 0.5), round(im.size[1] * 0.5)))
    # im.save('testarea.png') useful for debugging purposes, this will save the captured region as "testarea.png"
    img_rgb = np.array(im)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(image, 0)
    template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val < precision:
        return [-1, -1]
    return max_loc


def autopilot():
    img_jump = "jump_img2.png"
    img_dock = "dock_img2.png"
    img_ingate = "EYE.png"  # "in_gate2.png"
    in_warp = False
    docked = False
    counter = 0
    while not docked:
        time.sleep(1)
        if not in_warp:
            pos = imagesearch(img_jump)
            if pos == [-1, -1]:
                pos = imagesearch(img_dock)
                if pos != [-1, -1]:
                    imp_sell_steps(img_dock, 5, 27, 5, 30, 'left', 0.9)
                    docked = True
                    pyautogui.moveTo(450 + random.randint(0, 800), 100 + random.randint(0, 450))
            else:
                imp_sell_steps(img_jump, 5, 30, 5, 30, 'left', 0.9)
                in_warp = True
                pyautogui.moveTo(450 + random.randint(0, 800), 100 + random.randint(0, 450))
        else:
            counter += 1
            if counter % 5 == 0:
                print(counter, end=' ', flush = True)
            pos = imagesearch(img_ingate)
            if pos == [-1, -1]:
                print("in gate")
                x = random.random() * 98.5
                x = 0.0000000000000001 * (x - 41) ** 10 + (x / 20) + 4
                print('sleeping:', x)
                time.sleep(x)
                in_warp = False
                counter = 0
            if counter > 90:
                counter = 0
                in_warp = False


def imp_sell_steps(img, x1, x2, y1, y2, btn, precision=0.9):
    done = False
    print(img)
    a = (x2 - x1)/2 + x1
    b = (y2 - y1)/2 + y1
    r_e = random.random() * 0.9 + 0.1
    # ((x-i)/a)**2 + (y-j)/b)**2 < 1
    v_kruhu = False
    while not v_kruhu:
        x = random.randint(x1, x2)-a
        y = random.randint(y1, y2)-b
        if (x/a)**2 + (y/b)**2 < r_e:
            v_kruhu = True
    print(x+a, y+b)

    error = 0
    while not done:
        pos = imagesearch(img, precision)
        if pos == [-1, -1]:
            if error >= 5:
                print('error 5')
                if img == 'impairor.png':
                    imp_sell_steps("item_hangar.png", 15, 70, 10, 15, 'left', 0.9)
                    pyautogui.moveTo(700+random.randint(0,100), 700+random.randint(0,100))
                    time.sleep(0.5 + random.random()*2)
                    imp_sell_steps("ship_hangar.png", 15, 70, 10, 15, 'left', 0.9)
                elif img == 'LeaveShip.png' or img == 'repackage.png' or img == 'sell_this.png':
                    pyautogui.moveTo(700 + random.randint(0, 100), 700 + random.randint(0, 100))
                    time.sleep(0.5 + random.random()*2)
                    imp_sell_steps("impairor.png", 5, 70, 5, 70, 'right', 0.9)
            error += 1
            time.sleep(1)
            continue
        pyautogui.moveTo(pos[0] + x + a, pos[1] + y +b)
        if btn == 'left':
            mouse.click(Button.left, 1)
        elif btn == 'right':
            mouse.click(Button.right, 1)
        done = True
    time.sleep(1 + random.random()*2)



autopilot()


