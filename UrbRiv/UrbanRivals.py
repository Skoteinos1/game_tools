'''
Move all images from Img folder to folder with this code to make it work.
Control this code in line 648

option = 1  -  Plays tutorial until your XP limit is reached. You have to fill your limit and XP amount you currently have.
option = 2  -  Plays the Rift. Put your 4 main cards to positions 2, 3, 4, 5. Code will heal you if you need it and will take rewards only if you don't need more power.
option = 3  -  Plays all game mods except Tutorial and Rift. Pick only offensive deck with no life and pillz manipulation. It plays 4 cards in random order
               with predefined pillz consumption on each card. Pillz consumption was picked based on games with highest win rate. 
               Because I didn't do image recognition for 2600 cards and strategies for each card, do not use defensive, life and pillz modifying cards. Of course code can
               play those, but if code bets lot of pillz on defensive cards, no pillz on offensive cards, poison in last turn, heal on full health... your opponent might get
               suspicious that you are using a bot. You don't have to worry about that if all cards are offensive, all cards are poisonous or all are heals.
option = 4  -  Similar to 3, plays until it detects Melody in deck.
option = 5  -  Use for Win rate analysis.
'''

import cv2  # pip install opencv-python
import numpy as np
import pyautogui
import random
import time
import platform
import subprocess
from pynput.mouse import Button, Controller
import os
import datetime

mouse = Controller()

policka = 12
car_lvl = 11

is_retina = False
if platform.system() == "Darwin":
    is_retina = subprocess.call("system_profiler SPDisplaysDataType | grep 'retina'", shell=True)

test_counter = 0

def region_grabber(region):
    '''
    grabs a region (topx, topy, bottomx, bottomy)
    to the tuple (topx, topy, width, height)
    input : a tuple containing the 4 coordinates of the region to capture
    output : a PIL image of the area selected.
    '''
    if is_retina:
        region = [n * 2 for n in region]
    x1 = region[0]
    y1 = region[1]
    width = region[2] - x1
    height = region[3] - y1

    return pyautogui.screenshot(region=(x1, y1, width, height))


def rg_gb_to_cv(x1, y1, x2, y2):
    im = region_grabber(region=(x1, y1, x2, y2))
    if is_retina:
        im.thumbnail((round(im.size[0] * 0.5), round(im.size[1] * 0.5)))
    global test_counter
    # test_counter += 1
    # im.save('testarea' + str(test_counter) + '.png')  # useful for debugging purposes, this will save the captured region as "testarea.png"
    img_rgb = np.array(im)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    
    num = ''
    num_val = 0.05
    for imag in ['1.png', '2.png', '2b.png', '3.png', '3b.png', '4.png', ]:  # '5.png'
        res = cv2.matchTemplate(img_gray, priority_list[imag], cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        # print(max_val)
        if num_val < max_val:
            num_val = max_val
            num = imag

    return int(num[:1])


def is_pow_needed():
    # img_gray0 = rg_gb_to_cv(576,610,608,650)
    img_gray1 = rg_gb_to_cv(718,610,755,650)
    img_gray2 = rg_gb_to_cv(863,610,900,650)
    img_gray3 = rg_gb_to_cv(1005,610,1041,650)
    img_gray4 = rg_gb_to_cv(1149,610,1182,650)
    pow_n_lst = [img_gray1, img_gray2, img_gray3, img_gray4]
    print(pow_n_lst)
    return pow_n_lst


def imagesearch_priority(precision=0.8):
    # im = pyautogui.screenshot()
    im = region_grabber(region=(536, 408, 1548, 577))
    
    if is_retina:
        im.thumbnail((round(im.size[0] * 0.5), round(im.size[1] * 0.5)))
    im.save('testarea' + str(current_round) + '.png')  # useful for debugging purposes, this will save the captured region as "testarea.png"
    img_rgb = np.array(im)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

    print('Checking for match...')
    rew_mv = precision
    pow_mv = precision
    heal_mv = precision
    mheal_mv = precision
    shield_mv = precision
    lvl5 = precision
    best_rew = ''
    best_pow = ''
    best_heal = ''
    best_mheal = ''
    best_shield = ''
    for imag in priority_list:
        res = cv2.matchTemplate(img_gray, priority_list[imag], cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        if 'pow' in imag:
            if pow_mv < max_val:
                pow_mv = max_val
                best_pow = imag
        elif 'rew' in imag:
            if rew_mv < max_val:
                rew_mv = max_val
                best_rew = imag
        elif 'heal' in imag:
            if heal_mv < max_val:
                heal_mv = max_val
                best_heal = imag
        elif 'mhth' in imag:
            if mheal_mv < max_val:
                mheal_mv = max_val
                best_mheal = imag
        elif 'shield' in imag:
            if shield_mv < max_val:
                shield_mv = max_val
                best_shield = imag
        elif 'lvl' in imag:
            if lvl5 < max_val:
                lvl5 = max_val
        # print(imag, max_val)

    put_pow_here = float('nan')
    lowest_pow = 3
    if current_round > 2050:
       best_pow = ''
       best_heal = ''     
    if best_pow:
        pow = is_pow_needed()
        pow_needed = False
        for i in range(len(pow)):
            if pow[i] < lowest_pow:
                pow_needed = True
                lowest_pow = pow[i]
                put_pow_here = i
        if not pow_needed:
            best_pow = ''
            best_heal = ''
        else:
            if lowest_pow == 1 or pow.count(2) > 1:
                best_rew = ''
                best_heal = ''
            elif lowest_pow == 2:
                best_rew = ''

    items_lst = [best_rew, best_pow, best_heal, best_mheal, best_shield, put_pow_here]
    print(items_lst)
    return items_lst
    # return []


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
    # im.save('testarea.png')  # useful for debugging purposes, this will save the captured region as "testarea.png"
    img_rgb = np.array(im)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(image, 0)
    template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val < precision:
        return [-1, -1, 0, 0]
    
    x2 = template.shape[1]
    y2 = template.shape[0]
    a = (x2)/2
    b = (y2)/2
    r_e = random.random() * 0.45 + 0.4
    v_kruhu = False
    while not v_kruhu:
        x = random.randint(0, x2)-a
        y = random.randint(0, y2)-b
        if (x/a)**2 + (y/b)**2 < r_e:
            v_kruhu = True
    return [max_loc[0], x+a, max_loc[1], y+b]


def r(num, rand):
    return num + rand * random.random()


lst_pic = ''
lst_x = 0
lst_y = 0
lst_wait = 0
def imp_sell_steps(img, btn, extra_time, max_tries, precision=0.9):
    global lst_pic
    global lst_wait
    global lst_x
    global lst_y
    done = False
    all_good = False
    # print(img)
    
    error = 0
    while not done:
        pos = imagesearch(img, precision)
        if pos == [-1, -1, 0, 0]:
            if error % 5 == 0:
                print('error', error, img, '    Last:', lst_pic, lst_x, lst_y, 'wait', lst_wait)
            if error > max_tries:
                done = True
            error += 1
            time.sleep(1)
            continue
        pyautogui.moveTo(pos[0] + pos[1], pos[2] + pos[3])
        if btn == 'left':
            mouse.click(Button.left, 1)
            all_good = True
        elif btn == 'right':
            mouse.click(Button.right, 1)
            all_good = True
        else:
            all_good = True
        done = True
    my_wait = random.uniform(extra_time[0], extra_time[1])
    time.sleep(my_wait)

    lst_pic = img
    lst_x = pos[1]
    lst_y = pos[3]
    lst_wait = my_wait
    return all_good


def urban_fight(j=1):
    img_contin = "Continue.png"
    img_fight = "Fight.png"
    img_init = "Initialize.png"
    img_Lu = "Lucy.png"
    img_Va = "Vani.png"
    img_Re = "Rei.png"
    img_CC = "CrzCrl.png"
    img_caja = "Caja.png"
    img_time = 'TimeoutGirl.png'
    
    '''
    error 0 Fight.png 58.0 43.0 wait 11.973002185687038
    '''

    for i in range(j):
        print('run', i)
        pyautogui.moveTo(20, 20)

        imp_sell_steps(img_init, 'left', (4, 5), 20, 0.9)

        imp_sell_steps(img_caja, 'left', (0.3, 0.5), 20, 0.9)
        imp_sell_steps(img_caja, 'left', (0.3, 0.5), 20, 0.9)
        imp_sell_steps(img_caja, 'left', (0.3, 0.5), 20, 0.9)
        imp_sell_steps(img_caja, 'left', (0.3, 0.5), 20, 0.9)
        imp_sell_steps(img_caja, 'left', (0.3, 0.5), 20, 0.9)
        imp_sell_steps(img_caja, 'left', (0.3, 0.5), 20, 0.9)
        imp_sell_steps(img_caja, 'left', (1, 1.5), 20, 0.9)

        imp_sell_steps(img_Lu, 'left', (0.8, 1.5), 20, 0.9)
        imp_sell_steps(img_fight, 'left', (12, 14), 20, 0.9)
    
        imp_sell_steps(img_CC, 'left', (0.8, 1.5), 20, 0.9)
        imp_sell_steps(img_fight, 'left', (12, 14), 20, 0.9)
        
        imp_sell_steps(img_Va, 'left', (0.8, 1.5), 20, 0.9)
        imp_sell_steps(img_fight, 'left', (12, 14), 20, 0.9)
        
        imp_sell_steps(img_caja, 'left', (0.8, 1.5), 20, 0.9)
        
        imp_sell_steps(img_Re, 'left', (0.8, 1.5), 20, 0.9)
        imp_sell_steps(img_fight, 'left', (12, 14), 20, 0.9)

        if imp_sell_steps(img_time, 'leftt', (1, 2), 4, 0.9):
            imp_sell_steps('Timeout_ok.png', 'left', (4, 5), 4, 0.9)
        imp_sell_steps(img_contin, 'left', (6, 8), 20, 0.9)
    

def urban_rift():
    global current_round
    finished_station = False
    img_fight = 'Fight_rift.png'
    img_skip = 'Skip.png'
    pt = 2
    c = 0
    upg_seq = []
    # upg_seq = [2,2,2,]
    no_match_counter = 0
    skip_cards = False
    in_subway = False
    while no_match_counter < 5:
        img_lst = imagesearch_priority (0.8)

        img_name = 'No Matches'
        if current_round > 1950:
            pt = 5
        for imag in prior_table[pt]:
            if imag in img_lst:
                img_name = imag
                break
        
        print(img_name)

        if img_name != 'No Matches':
            no_match_counter = 0
            in_subway = False
            if any(x in img_name for x in ['heal', 'rewa', 'mhth', 'shield']):
                imp_sell_steps(img_name, 5, 100, 2, 100, 'left', (2, 5), 20, 0.8)
                my_wait = random.uniform(0.3, 0.6)
                time.sleep(my_wait)
            elif 'pow' in img_name:
                imp_sell_steps(img_name, 5, 100, 2, 100, 'left', (1.8, 3), 20, 0.8)
                try:
                    crd = img_lst[-1]
                    # crd = upg_seq[c]
                except:
                    crd = c
                x2 = random.randint(1, 50)
                # x2 = 50
                x = (crd % 4) * 149 + 149
                x += 560 + x2
                y = random.randint(720, 880)
                # y = 880
                pyautogui.moveTo(x+x2, y)
                my_wait = random.uniform(0.4, 0.6)
                time.sleep(my_wait)
                c += 1
                mouse.click(Button.left, 1)
                my_wait = random.uniform(0.8, 1.2)
                time.sleep(my_wait)
        else:
            skip_cards = True
            no_match_counter += 1
            print('There are no Matches')
            time.sleep(3)

        if no_match_counter > 1:
            in_subway = imp_sell_steps('Subway.png', 10, 131, 10, 30, 'lefttt', (2, 3), 3, 0.8)
            if in_subway:
                print('In Subway')
                in_subway = imp_sell_steps('tube_station.png', 13, 13, 48, 48, 'left', (12, 13), 30, 0.8)
                imp_sell_steps('Rest.png', 15, 130, 12, 30, 'left', (5, 8), 8, 0.8)
                
        if skip_cards:
            fight_done = imp_sell_steps(img_fight, 10, 131, 10, 30, 'left', (12, 13), 5, 0.8)
            skip_cards = imp_sell_steps(img_skip, 10, 131, 10, 30, 'left', (5, 6), 3, 0.8)
        else:
            fight_done = imp_sell_steps(img_fight, 10, 131, 10, 30, 'left', (13, 14), 5, 0.8)
        if fight_done:
            current_round += 1
        # no_match_counter = 100


def wait_for_my_turn(precision=0.8):
    print('waiting for turn')
    my_turn = False
    while not my_turn:
        time.sleep(0.89)

        im = pyautogui.screenshot()
        if is_retina:
            im.thumbnail((round(im.size[0] * 0.5), round(im.size[1] * 0.5)))
        # im.save('testarea.png')  # useful for debugging purposes, this will save the captured region as "testarea.png"
        img_rgb = np.array(im)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

        for key in ['yourturn1.png', 'yourturn2.png', 'yourturn3.png', 'TimeoutGirl.png', 'TimeoutGirl2.png', 'FightEnd.png']:
            res = cv2.matchTemplate(img_gray, your_turn_images[key], cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
            if max_val > precision:
                my_turn = True
                break
            # print(key, max_val)
        # print('wait_for_my_turn')
    if 'TimeoutGirl' in key:
        print('I see timeout girl')
        imp_sell_steps('Timeout_ok.png', 'left', (4, 5), 4, 0.9)
        return False
    elif key == 'FightEnd.png':
        return False
    # os.system('spd-say MyTurn')
    if not fast_game:
        my_wait = random.uniform(3, 6)
        print('wait before doing my stuff', my_wait)
        time.sleep(my_wait)
    return True


def check_for_result(precision=0.8):
    print('Checking for result')
    im = pyautogui.screenshot()
    if is_retina:
        im.thumbnail((round(im.size[0] * 0.5), round(im.size[1] * 0.5)))
    # im.save('testarea.png')  # useful for debugging purposes, this will save the captured region as "testarea.png"
    img_rgb = np.array(im)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

    rslt = ''
    for key in ['res_v.png', 'res_d.png', 'res_x.png']:
        res = cv2.matchTemplate(img_gray, your_turn_images[key], cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        # print(key, max_val)
        if max_val > precision:
            rslt = key[4:-4]
            f = open("strat_eff.txt", "a")
            f.write(rslt)
            f.close()
            '''if rslt == 'v':
                os.system('spd-say victory')
            elif rslt == 'x':
                os.system('spd-say draw')
            elif rslt == 'd':
                os.system('spd-say defeat')'''
            break
        # print('wait_for_my_turn')
    return rslt


def stat_anal():
    file1 = open("strat_eff.txt", "r")
    read_content = file1.read()
    file1.close()
    read_content = read_content.split('\n')

    result_dic = {}
    for line in read_content:
        line = line.split(';')
        strat = line[0]
        try:
            if strat not in result_dic:
                result_dic[strat] = {'v': 0, 'x': 0, 'd': 0}
            if 'v' in line[1]:
                result_dic[strat]['v'] += 1
            elif 'x' in line[1]:
                result_dic[strat]['x'] += 1
            elif 'd' in line[1]:
                result_dic[strat]['d'] += 1
        except:
            pass
    vysl_lst = []
    for strat in result_dic:
        try:
            uspesnost1 = round(result_dic[strat]['v']*100/(result_dic[strat]['x'] + result_dic[strat]['d']), 2)
            uspesnost2 = round((result_dic[strat]['v']+ result_dic[strat]['x'])*100/result_dic[strat]['d'], 2)
            s = str(strat) + ' ' + str(result_dic[strat])
            vysl_lst.append([uspesnost1, uspesnost2, s])
        except:
            pass
    vysl_lst.sort()
    for vys in vysl_lst:
        print(vys)


def click_on_random_card(c):
    x0 = 438
    x_lst = 1406
    x_len = int((x_lst - x0) / 4)
    
    y = random.randint(710, 800)
    x2 = random.randint(0, 135)
    # print(x0 + c*x_len + 90+ x2, y)
    pyautogui.moveTo(x0 + c*x_len + 90+ x2, y)
    mouse.click(Button.left, 1)
    my_wait = random.uniform(0.7, 1)
    time.sleep(my_wait)


def deck_change():
    imp_sell_steps('back_arrow.png', 'left', (3, 5), 9, 0.9)
    
    decks_clicked = imp_sell_steps('Decks_btn.png', 'left', (3, 5), 9, 0.9)
    if not decks_clicked:
        decks_clicked = imp_sell_steps('Decks_selected.png', 'left', (3, 5), 3, 0.9)

    if not decks_clicked:
        print('Niesom na deckoch')
    else:
        btn_used = imp_sell_steps('T1Deck.png', 'left', (3, 5), 5, 0.9)
        if not btn_used:
            imp_sell_steps('T2Deck.png', 'left', (3, 5), 5, 0.9)
        

def urban_one_char(i3=1):
    now = datetime.datetime.now()
    
    numbers = [0, 1, 2, 3]
    img_fight = "Fight.png"
    img_first_fight = 'FirstFight.png'
    img_plus = "Plus.png"
    img_end = 'FightEnd.png'
    img_newfight = 'NewFight.png'
    img_lose_char = ''
    img_win_char = 'Melody.png'
    img_win_char2 = ''

    strategy = [0,0,0,0]
    encounter = 0
    first_fight = True
    while encounter < i3:
        print('Starting next fight')
        
        if first_fight:
            btn_found = imp_sell_steps(img_first_fight, 'left', (11.6, 12.8), 4, 0.9)
            if not btn_found:
                btn_found = imp_sell_steps('Fight_btn.png', 'left', (11.6, 12.8), 4, 0.9)
        if not first_fight or not btn_found:
            imp_sell_steps(img_newfight, 'left', (11.6, 12.8), 4, 0.9)
        first_fight = False

        btn_found = imp_sell_steps(img_win_char, 'leftttt', (0.2, 0.3), 4, 0.75)
        if btn_found:
            os.system('spd-say Got_card')
            foo = input('Press key... ')
            encounter += 1
            continue

        for i in range(len(numbers)):
            pyautogui.moveTo(438, 710)
            if not wait_for_my_turn():
                break
            
            see_pillz = False
            while not see_pillz:
                click_on_random_card(numbers[i])
                time.sleep(0.5)
                see_pillz = imp_sell_steps(img_plus, 'lefttt', (0.12, 0.15), 3, 0.9)
                
            for j in range(strategy[i]):
                print('Pillz', strategy[i])
                imp_sell_steps(img_plus, 'left', (0.11, 0.13), 3, 0.9)
        
            my_wait = random.uniform(0.5, 1)
            time.sleep(my_wait)
            imp_sell_steps(img_fight, 'left', (11.6, 12.8), 20, 0.9)
        

def urban_tourney(i3=1):
    now = datetime.datetime.now()
    starting_hour = now.strftime("%H")

    numbers = [0, 1, 2, 3]
    img_fight = "Fight.png"
    img_first_fight = 'FirstFight.png'
    img_plus = "Plus.png"
    img_end = 'FightEnd.png'
    img_newfight = 'NewFight.png'

    strategies = [[5,0,4,3], [4,4,4,0], [6,0,6,0], [0,5,4,3], [1,4,4,3], ]
    # strategies = [[5,0,5,5], [4,4,4,3], [6,0,6,3], [0,5,5,5], [1,4,5,5], ]
    # strategies = [[5,4,4,5], [4,4,4,4], [6,4,6,2], [4,5,4,5], [4,4,4,5], ]
    #strategies = [[4,4,4,4]]
    if training:
        strategies = [[5,0,4,3], [4,4,4,0], [0,5,4,3], [1,4,4,3], ]
        # strategies = [[0,0,0,0]]
    # strategies = [[5,0,6,6], [4,4,7,2], [6,0,8,3], [0,5,6,6], [1,4,6,6],]
    # bad_strategies = [[4,0,4,4], [5,0,3,4]], [5,4,0,3], [6,0,0,6], [0,5,3,4],
    # strategies = [[6,0,0,10], [5,0,4,7], [4,4,4,4], [4,0,4,8], [6,0,6,4], [0,5,4,7], [1,4,4,7], [5,4,0,7], [0,5,4,7], [0,5,4,7]]

    i2 = 0
    while i2 < i3:
        last_fight = i2
        print('Starting next fight', i2)
        vys = check_for_result()
        if not vys:
            time.sleep(2)
            check_for_result()

        now = datetime.datetime.now()
        current_hour = now.strftime("%H")
        if not switch_decks:
            starting_hour = current_hour
        if current_hour != starting_hour:
            print('treba zmenit deck')
            deck_change()
            btn_found = imp_sell_steps(img_first_fight, 'left', (5, 7), 5, 0.9)
            starting_hour = current_hour
        
        if i2 == 0:
            btn_found = imp_sell_steps(img_first_fight, 'left', (11.6, 12.8), 4, 0.9)
        if i2 != 0 or not btn_found:
            imp_sell_steps(img_newfight, 'left', (11.6, 12.8), 4, 0.9)

        strategy = strategies[random.randint(0, len(strategies)-1)]
        random.shuffle(numbers)

        print('order:', numbers, 'strategy:', strategy)    
        for i in range(len(numbers)):
            if not wait_for_my_turn():
                break
            
            if i == 0:
                f = open("strat_eff.txt", "a")
                f.write('\n' + str(strategy) + ';')
                f.close()

            see_pillz = False
            see_pillz_counter = 0
            while not see_pillz and see_pillz_counter < 4:
                click_on_random_card(numbers[i])
                time.sleep(0.5)
                see_pillz = imp_sell_steps(img_plus, 'lefttt', (0.12, 0.15), 3, 0.9)
                see_pillz_counter += 1

            for j in range(strategy[i]):
                imp_sell_steps(img_plus, 'left', (0.11, 0.13), 3, 0.9)
        
            f = open("strat_eff.txt", "a")
            f.write(str(strategy[i]) + ',')
            f.close()
            
            if strategy[i] == 0 and not fast_game:
                time.sleep(2.78)
                
            my_wait = random.uniform(0.5, 1)
            if last_fight == i2:
                i2 += 1
            time.sleep(my_wait)
            was_fight = imp_sell_steps(img_fight, 'left', (0.1, 0.2), 20, 0.9)
            if was_fight:
                pyautogui.moveTo(438, 710)
                my_wait = random.uniform(11.6, 12.8)
                time.sleep(my_wait)
        # starting_hour = '100'


option = 3
switch_decks = True
switch_decks = False
fast_game = False
fast_game = True
training = True
# training = False
if option in [1, 3, 4]:
    your_turn_images = {'yourturn1.png': '', 'yourturn2.png': '', 'yourturn3.png': '', 'TimeoutGirl.png': '', 'TimeoutGirl2.png': '', 'res_v.png': '', 'res_d.png': '', 'res_x.png': '', 'FightEnd.png': '',}
    for key in your_turn_images:
        foo = ''
        foo = cv2.imread(key, 0)
        try:
            foo.shape[::-1]
        except:
            pass
        your_turn_images[key] = foo

if option == 1:
    time.sleep(4)
    current_xp = 0
    turns = (41000 - current_xp) / 1484
    urban_fight(int(turns))
elif option == 2:
    time.sleep(2)
    current_round = 1872
    priority_list = {'4rewardsb.png': '', '5lvl.png': '', 
                    '50pow1.png': '', '50pow2.png': '', '50pow3.png': '', '50pow4.png': '', '50pow5.png': '',
                    '40pow1.png': '', '40pow2.png': '', '40pow3.png': '', '40pow4.png': '', '40pow5.png': '',
                    '3rewards.png': '',
                    '30pow1.png': '', '30pow2.png': '', '30pow3.png': '', '30pow4.png': '', '30pow5.png': '',
                    '120heal1.png': '', '120heal2.png': '', '120heal4.png': '', '120heal5.png': '',
                    '180shield1.png': '', '180shield2.png': '', '180shield3.png': '', '180shield3b.png': '', '180shield4.png': '', '180shield5.png': '',
                    '90mhth1.png': '', '90mhth2.png': '', '90mhth3.png': '', '90mhth4.png': '', '90mhth5.png': '',
                    '75mhth1.png': '', '75mhth2.png': '', '75mhth3.png': '', '75mhth4.png': '', '75mhth5.png': '',
                    '100heal1.png': '', '100heal2.png': '', '100heal3.png': '', '100heal4.png': '', '100heal5.png': '',
                    '80heal1.png': '', '80heal2.png': '', '80heal3.png': '', '80heal4.png': '', '80heal5.png': '',
                    '2rewards.png': '', '2rewardsb.png': '', '2rewardsc.png': '',
                    '20pow1.png': '', '20pow2.png': '', '20pow3.png': '', '20pow4.png': '', '20pow5.png': '',
                    '60mhth1.png': '', '60mhth2.png': '', '60mhth3.png': '', '60mhth4.png': '', '60mhth5.png': '',
                    '60heal1.png': '', '60heal2.png': '', '60heal3.png': '', '60heal4.png': '', '60heal5.png': '',
                    '150shield1.png': '', '150shield2.png': '', '150shield3.png': '', '150shield4.png': '', '150shield5.png': '', 
                    '10pow1.png': '', '10pow2.png': '', '10pow3.png': '', '10pow4.png': '', '10pow5.png': '',
                    '1rewards.png': '',
                    '45mhth1.png': '', '45mhth2.png': '', '45mhth3.png': '', '45mhth4.png': '', '45mhth5.png': '',
                    '5.png': '', '4.png': '', '3.png': '', '3b.png': '', '2.png': '', '2b.png': '', '1.png': '', 'Subway.png': ''
                    }
    prior_table = {1: ['4rewardsb.png',
                    '50pow1.png', '50pow2.png', '50pow3.png', '50pow4.png', '50pow5.png',
                    '40pow1.png', '40pow2.png', '40pow3.png', '40pow4.png', '40pow5.png',
                    '3rewards.png',
                    '30pow1.png', '30pow2.png', '30pow3.png', '30pow4.png', '30pow5.png',
                    '120heal1.png', '120heal2.png', '120heal4.png', '120heal5.png',
                    '180shield1.png', '180shield2.png', '180shield3.png', '180shield3b.png', '180shield4.png', '180shield5.png',
                    '90mhth1.png', '90mhth2.png', '90mhth3.png', '90mhth4.png', '90mhth5.png',
                    '75mhth1.png', '75mhth2.png', '75mhth3.png', '75mhth4.png', '75mhth5.png',
                    '100heal1.png', '100heal2.png', '100heal3.png', '100heal4.png', '100heal5.png',
                    '80heal1.png', '80heal2.png', '80heal3.png', '80heal4.png', '80heal5.png',
                    '2rewards.png', '2rewardsb.png', '2rewardsc.png',
                    '20pow1.png', '20pow2.png', '20pow3.png', '20pow4.png', '20pow5.png',
                    '60mhth1.png', '60mhth2.png', '60mhth3.png', '60mhth4.png', '60mhth5.png',
                    '60heal1.png', '60heal2.png', '60heal3.png', '60heal4.png', '60heal5.png',
                    '150shield1.png', '150shield2.png', '150shield3.png', '150shield4.png', '150shield5.png', 
                    '10pow1.png', '10pow2.png', '10pow3.png', '10pow4.png', '10pow5.png',
                    '1rewards.png',
                    '45mhth1.png', '45mhth2.png', '45mhth3.png', '45mhth4.png', '45mhth5.png',],
                    2: [
                    '120heal1.png', '120heal2.png', '120heal4.png', '120heal5.png',
                    '100heal1.png', '100heal2.png', '100heal3.png', '100heal4.png', '100heal5.png',
                    '80heal1.png', '80heal2.png', '80heal3.png', '80heal4.png', '80heal5.png',
                    '60heal1.png', '60heal2.png', '60heal3.png', '60heal4.png', '60heal5.png',    
                    '4rewardsb.png',
                    '50pow1.png', '50pow2.png', '50pow3.png', '50pow4.png', '50pow5.png',
                    '40pow1.png', '40pow2.png', '40pow3.png', '40pow4.png', '40pow5.png',
                    '3rewards.png',
                    '30pow1.png', '30pow2.png', '30pow3.png', '30pow4.png', '30pow5.png',
                    '2rewards.png', '2rewardsb.png', '2rewardsc.png',
                    '20pow1.png', '20pow2.png', '20pow3.png', '20pow4.png', '20pow5.png',
                    '10pow1.png', '10pow2.png', '10pow3.png', '10pow4.png', '10pow5.png',
                    '1rewards.png',
                    ],
                    3: ['4rewardsb.png',
                    '50pow1.png', '50pow2.png', '50pow3.png', '50pow4.png', '50pow5.png',
                    '40pow1.png', '40pow2.png', '40pow3.png', '40pow4.png', '40pow5.png',
                    '3rewards.png',
                    '120heal1.png', '120heal2.png', '120heal4.png', '120heal5.png',
                    '100heal1.png', '100heal2.png', '100heal3.png', '100heal4.png', '100heal5.png',
                    '80heal1.png', '80heal2.png', '80heal3.png', '80heal4.png', '80heal5.png',
                    '30pow1.png', '30pow2.png', '30pow3.png', '30pow4.png', '30pow5.png',
                    '2rewards.png', '2rewardsb.png', '2rewardsc.png',
                    '60heal1.png', '60heal2.png', '60heal3.png', '60heal4.png', '60heal5.png',
                    '20pow1.png', '20pow2.png', '20pow3.png', '20pow4.png', '20pow5.png',
                    '10pow1.png', '10pow2.png', '10pow3.png', '10pow4.png', '10pow5.png',
                    '1rewards.png',
                    ],
                    4: ['4rewardsb.png',
                    '50pow1.png', '50pow2.png', '50pow3.png', '50pow4.png', '50pow5.png',
                    '40pow1.png', '40pow2.png', '40pow3.png', '40pow4.png', '40pow5.png',
                    '3rewards.png',
                    '30pow1.png', '30pow2.png', '30pow3.png', '30pow4.png', '30pow5.png',
                    '2rewards.png', '2rewardsb.png', '2rewardsc.png',
                    '20pow1.png', '20pow2.png', '20pow3.png', '20pow4.png', '20pow5.png',
                    '10pow1.png', '10pow2.png', '10pow3.png', '10pow4.png', '10pow5.png',
                    '1rewards.png',
                    ],
                    5: ['4rewardsb.png', '3rewards.png', '2rewards.png', '2rewardsb.png', '2rewardsc.png', '1rewards.png'],
    }

    for imag in priority_list:
        foo = ''
        # print(imag)
        foo = cv2.imread(imag, 0)
        foo.shape[::-1]
        priority_list[imag] = foo

    urban_rift()
elif option == 3:
    time.sleep(4)
    # urban_tourney(random.randint(500, 500))
    urban_tourney(5)
elif option == 4:
    time.sleep(4)
    urban_one_char(9)
elif option == 5:
    stat_anal()



os.system('spd-say Done')
