# Most desired Elegant Hubris Timeless Jewels are really expensive.
#
# But what is the price of second best?
# Or which is best for you from those cheapest 100?

# Simply explained what this tool does:
# 1. Get text from PoE trade site.
# 2. Run code, which will scrap data from Timeless Jewel calculator
# 3. We store data, so we don't have to scrap them again
# 4. Get list of jewels which are cheap and best for you from that trade list.

import pickle
from urllib.request import urlopen as uReq
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as soup
import time
import random


# Path to folder, because debug mode fails without this
pth = ''

def save_pickle(file, data1):
    if '.pkl' not in file:
        file += '.pkl'
    pkl_file = open(pth + file, 'wb')
    pickle.dump(data1, pkl_file)
    pkl_file.close()


def load_pickle(fl_nm):
    if '.pkl' not in fl_nm:
        fl_nm += '.pkl'
    try:
        pkl_file = open(pth + fl_nm, 'rb')
        data1 = pickle.load(pkl_file)
        pkl_file.close()
    except:
        print('Missing pickle table:', fl_nm)
        # pkl_file = open(file, 'wb')
        data1 = {}
        save_pickle(fl_nm, data1)
    return data1


# Select content on PoE trade website and copy-paste it here:
trade_text = """
Don't worry about it too much. Code only cares about lines with Comm.ssioned and lines after Exct.Price


Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 82
Commissioned 158740 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
8×chaosChaos Orb
XXXX#1111 listed 12 minutes ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 83
Commissioned 56280 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
10×chaosChaos Orb
XXXXX#2222 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 83
Commissioned 159480 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
10×chaosChaos Orb
XXXX#3333 listed 2 days ago
Online
Verified

"""

trade_text = trade_text.split('\n')
trade_list = []
entry = ['','']
for i in range(len(trade_text)):
    if "Commissioned" in trade_text[i]:
        entry[0] = trade_text[i].replace('Commissioned ', '').replace(' coins to commemorate', '')
    if "Asking Price:" in trade_text[i] or "Exact Price:" in trade_text[i]:
        entry[1] = trade_text[i+1].replace('×', ' ')
        trade_list.append(entry)
        entry = ['','']

# To Download Everything, set this to true
download_everything = False
if download_everything:
    for i in range(2000, 160020, 20): 
        entry = [str(i) + ' Victario','200 chaosChaos Orb']
        trade_list.append(entry)

# Load pickle with previous data, so we don't have to scrap them again.
# It is just one big dictionary: hubris_data[coins][socket] = 'text'
hubris_data = load_pickle('hubris_data')


# open browser
def initiate_browser():
    global driver
    options = Options()
    options.set_preference("privacy.donottrackheader.enabled", True)  # DoNotTrack
    options.set_preference("privacy.donottrackheader.value", 1)
    options.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:61.0) Gecko/20100101 Firefox/106.0")
    options.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', False)  # You would also like to block flash
    options.set_preference("media.peerconnection.enabled", False)  # WebRTC
    driver = webdriver.Firefox(options=options)
    return driver


# Just enter the socket, where you plan to insert jewel. Or download data for
# sockets = 60735 61834 61419 54127 26196 26725... There is image with socket numbers arround
socket = 26725
page_url = f'https://vilsol.github.io/timeless-jewels/tree?jewel=5&conqueror=Victario&seed=10000&location={socket}&mode=seed'

browser_started = False
new_data = False
# get the data:
counter = 0
for jewel in trade_list:
    coins = jewel[0].split(' ')[0]
    if coins not in hubris_data:
        hubris_data[coins] = {}
    if socket not in hubris_data[coins]:
        if not browser_started:
            initiate_browser()
            driver.get(page_url)
            browser_started = True
            foo = input("Select Jewel socket and press Enter")
            socket = driver.current_url.split('location=')
            socket = socket[1].replace('&mode=seed', '')
            seed = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div/div[5]/input")
            seed.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
            
        print(counter, coins, socket)
        seed.send_keys(coins)
        
        # Wait
        time.sleep(0.5)
        
        # Get data
        page_html = driver.page_source
        page_soup = soup(page_html, "html.parser")
        notes = page_soup.find("ul", {"class": 'mt-1 svelte-9h6fz6 rainbow'}).text
        if notes:
            hubris_data[coins][socket] = notes
            new_data = True

        # Don't set this too low, you'll get yourself banned
        time.sleep(1 + (random.randint(1, 2000)/1000))

        seed.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
        counter += 1

    if counter % 20 == 0:
        if new_data:
            print('saving')
            save_pickle('hubris_data', hubris_data)
            new_data = False

if new_data:
    print('saving')
    save_pickle('hubris_data', hubris_data)

# This is your filter
# Enter mods which are important for you and add number based on how important it is.
positive_mods = {'increased Global Physical Damage': 1.3, 
                 'increased maximum Life': 1.5,
                 'increased maximum Mana': 1.3, 
                 'to Global Critical Strike Multiplier': 1, 
                 'increased Global Critical Strike Chance': 0.9,
                 'increased Melee Physical Damage': 0.4,  
                 'increased Spell Damage': 0.3, 
                 'to Chaos Resistance': 0.1, 
                 'to Fire Resistance': 0,
                 'to Cold Resistance': 0,
                 'to Lightning Resistance': 0,
                  }
# This helps with color coding, it is easier to go through list if important stuff is highlighted
blue_mods = ['increased maximum Life', 'increased maximum Mana']
red_mods = ['to Global Critical Strike Multiplier', 'increased Global Critical Strike Chance', ]
green_mods = ['to Chaos Resistance', 'to Fire Resistance', 'to Cold Resistance', 'to Lightning Resistance']
yellow_mods = ['increased Melee Physical Damage', 'increased Spell Damage']
best_jewels_lst = []

# This gives score to jewel based on values in positive_mods
counter = 0
for jewel in trade_list:
    coins = jewel[0].split(' ')[0]
    for socket in hubris_data[coins]:
        score = 0
        mods = hubris_data[coins][socket].split('(')
        for mod in mods:
            mod = mod.split(')')
            try:
                for key in positive_mods:
                    if key in mod[1]:
                        score += int(mod[0]) * positive_mods[key]
            except:
                pass
        best_jewels_lst.append([score, coins, socket, jewel])
best_jewels_lst = sorted(best_jewels_lst, key=lambda x: x[0], reverse=True)

s = ""
for i in range(40):
    s1 = '\n\n' + str(best_jewels_lst[i]) + '\n' + hubris_data[best_jewels_lst[i][1]][best_jewels_lst[i][2]].replace('(','\n')
    # Second filter. This just make sure that important mods are present and are not overruled by multiple of not important ones
    # If
    # 'increased maximum Life': 1.5,
    # 'to Chaos Resistance': 0.1, 
    # Than
    # 16x Chaos res is better 1 Life
    # Also removes duplicates
    if all(key in s1 for key in blue_mods) and s1 not in s:
        s += s1

# Color coding
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Print result
s = s.split('\n')
for ln in s:
    if any(key in ln for key in blue_mods):
        print(bcolors.OKBLUE + ln + bcolors.ENDC)
    elif any(key in ln for key in red_mods):
        print(bcolors.FAIL + ln + bcolors.ENDC)
    elif any(key in ln for key in green_mods):
        print(bcolors.OKGREEN + ln + bcolors.ENDC)
    elif any(key in ln for key in yellow_mods):
        print(bcolors.WARNING + ln + bcolors.ENDC)
    else:
        print(ln)
    
