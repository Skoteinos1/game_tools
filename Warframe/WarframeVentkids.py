# To gain status with Ventkids guild you have to do tricks on hover board. If you are not fan of that, just run this code and it will jump arrround for 20 minutes.

# from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Controller
import time

# mouse = Controller()
keyboard = Controller()

b_press_dur = 0.05


def jump():
    keyboard.press(Key.space)
    time.sleep(b_press_dur)
    keyboard.release(Key.space)


def doublejump():
    jump()
    time.sleep(0.3)
    jump()


def triplejump():
    jump()
    time.sleep(0.3)
    jump()
    time.sleep(0.3)
    jump()


def flip():
    keyboard.press('/')
    time.sleep(b_press_dur)
    keyboard.release('/')


def combo():
    doublejump()
    time.sleep(0.3)
    flip()
    time.sleep(0.3)


def highjump():
    keyboard.press(Key.space)
    time.sleep(0.8)
    keyboard.release(Key.space)


def thepearl():
    keyboard.press('w')
    time.sleep(0.8)
    keyboard.press(Key.shift_l)
    time.sleep(1.4)  # 2

    for i in range(5):
        print(i+1)
        keyboard.release(Key.shift_l)
        time.sleep(b_press_dur)
        combo()
        keyboard.press(Key.shift_l)
        time.sleep(1.20)  # 1.75

    time.sleep(1)
    keyboard.release('w')
    keyboard.release(Key.shift_l)
    time.sleep(1.5)
    keyboard.press('s')
    time.sleep(0.5)
    keyboard.release('s')
    keyboard.press('w')
    time.sleep(0.5)
    jump()
    time.sleep(0.3)
    keyboard.release('w')


def auto_combo(s):
    bw_jumps = 0.34
    highjump()
    time.sleep(0.1)
    keyboard.press(s)
    time.sleep(0.15)
    jump()
    time.sleep(bw_jumps)
    flip()
    time.sleep(bw_jumps)
    jump()
    time.sleep(bw_jumps)
    flip()
    time.sleep(bw_jumps)
    jump()
    time.sleep(bw_jumps)
    flip()
    time.sleep(bw_jumps)
    jump()
    if s == 'd':
        # time.sleep(1.76)
        time.sleep(0.55)
    keyboard.release(s)
    time.sleep(1.3)


time.sleep(4)
"""
for j in range(3):
    time.sleep(1)
    thepearl()
"""

for j in range(50):  # 100
    print(j)
    auto_combo('a')
    auto_combo('d')
    auto_combo('d')

# mouse.move(20, -13)
# mouse.move(-5, 0)
# mouse.click(Button.right, 1)
# mouse.click(Button.left, 1)
# mouse.click(Button.right, 2)
# mouse.click(Button.left, 1)
# mouse.press(Button.right)
# mouse.release(Button.right)
# mouse.scroll(0, -100)
# print(mouse.position)
# mouse.position = (1500, 200)
