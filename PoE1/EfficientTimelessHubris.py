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
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as soup
import time
import random


# Path to folder, because debug mode fails without this
pth = '/home/skoty/Peti/Projects/P39/git/game_tools/PoE1/'

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
        data1 = ''
        save_pickle(fl_nm, data1)
    return data1


# Enter text from PoE trade:
trade_text = """
Commissioned 57860 coins to commemorate Cadiro
Asking Price:
200×chaosChaos Orb
Commissioned 70200 coins to commemorate Cadiro
Asking Price:
200×chaosChaos Orb
Commissioned 103800 coins to commemorate Cadiro
Asking Price:
200×chaosChaos Orb
Commissioned 100000 coins to commemorate Cadiro
Asking Price:
200×chaosChaos Orb

Showing 100 results (10000 matched)
Verified
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
Gönner42069#5422 listed 12 minutes ago
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
AliaksandrKalkunou#6342 listed 2 days ago
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
AliaksandrKalkunou#6342 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 83
Commissioned 32700 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
10×chaosChaos Orb
AliaksandrKalkunou#6342 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 16520 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
10×chaosChaos Orb
AliaksandrKalkunou#6342 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 83
Commissioned 155360 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
10×chaosChaos Orb
AliaksandrKalkunou#6342 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 83
Commissioned 150680 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
10×chaosChaos Orb
AliaksandrKalkunou#6342 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 134280 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
10×chaosChaos Orb
AliaksandrKalkunou#6342 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 58800 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
10×chaosChaos Orb
AliaksandrKalkunou#6342 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 83
Commissioned 104020 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
10×chaosChaos Orb
AliaksandrKalkunou#6342 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 115360 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
10×chaosChaos Orb
AliaksandrKalkunou#6342 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 38960 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
10×chaosChaos Orb
AliaksandrKalkunou#6342 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 27280 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
10×chaosChaos Orb
liefe42#4814 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 83
Commissioned 113860 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
10×chaosChaos Orb
AliaksandrKalkunou#6342 listed 5 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 132100 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
10×chaosChaos Orb
AliaksandrKalkunou#6342 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 83
Commissioned 111700 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
10×chaosChaos Orb
AliaksandrKalkunou#6342 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 71920 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
10×chaosChaos Orb
AliaksandrKalkunou#6342 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 83
Commissioned 148560 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
10×chaosChaos Orb
AliaksandrKalkunou#6342 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 66400 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
10×chaosChaos Orb
AliaksandrKalkunou#6342 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 83
Commissioned 140880 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
10×chaosChaos Orb
AliaksandrKalkunou#6342 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 81920 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
10×chaosChaos Orb
AliaksandrKalkunou#6342 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 10540 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
10×chaosChaos Orb
AliaksandrKalkunou#6342 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 83
Commissioned 155120 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
10×chaosChaos Orb
AliaksandrKalkunou#6342 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 58660 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
10×chaosChaos Orb
AliaksandrKalkunou#6342 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 106620 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
10×chaosChaos Orb
AliaksandrKalkunou#6342 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 159620 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
10×chaosChaos Orb
AliaksandrKalkunou#6342 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 83
Commissioned 5340 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
10×chaosChaos Orb
AliaksandrKalkunou#6342 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 30300 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
10×chaosChaos Orb
AliaksandrKalkunou#6342 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 83
Commissioned 68000 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
10×chaosChaos Orb
AliaksandrKalkunou#6342 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 46740 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
10×chaosChaos Orb
AliaksandrKalkunou#6342 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 83
Commissioned 70840 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
10×chaosChaos Orb
AliaksandrKalkunou#6342 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 64260 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
10×chaosChaos Orb
Quentixo#1694 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 83
Commissioned 147640 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
10×chaosChaos Orb
AliaksandrKalkunou#6342 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 83
Commissioned 129400 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
10×chaosChaos Orb
AliaksandrKalkunou#6342 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 31900 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
10×chaosChaos Orb
AliaksandrKalkunou#6342 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 83
Commissioned 119540 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
10×chaosChaos Orb
AliaksandrKalkunou#6342 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 116220 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
10×chaosChaos Orb
AliaksandrKalkunou#6342 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 45280 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
10×chaosChaos Orb
Quentixo#1694 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 63860 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
10×chaosChaos Orb
AliaksandrKalkunou#6342 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 62540 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
10×chaosChaos Orb
Siiniix#1268 listed a minute ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 83
Commissioned 69540 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
10×chaosChaos Orb
AliaksandrKalkunou#6342 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 14460 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
10×chaosChaos Orb
AliaksandrKalkunou#6342 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 123220 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
10×chaosChaos Orb
AliaksandrKalkunou#6342 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 83
Commissioned 44200 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
10×chaosChaos Orb
AliaksandrKalkunou#6342 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 36160 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
10×chaosChaos Orb
AliaksandrKalkunou#6342 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 83
Commissioned 62860 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
10×chaosChaos Orb
AliaksandrKalkunou#6342 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 83
Commissioned 99740 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
10×chaosChaos Orb
AliaksandrKalkunou#6342 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 84340 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
10×chaosChaos Orb
AliaksandrKalkunou#6342 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 83
Commissioned 92100 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
10×chaosChaos Orb
AliaksandrKalkunou#6342 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 83
Commissioned 38420 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
10×chaosChaos Orb
AliaksandrKalkunou#6342 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 83
Commissioned 90660 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
10×chaosChaos Orb
AliaksandrKalkunou#6342 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 79900 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
12×chaosChaos Orb
orlandoq1829#5913 listed 3 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 89160 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
13×chaosChaos Orb
HayImNew#9515 listed 3 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 142200 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
13×chaosChaos Orb
HayImNew#9515 listed 3 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 155140 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
13×chaosChaos Orb
HayImNew#9515 listed 3 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 33480 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
13×chaosChaos Orb
HayImNew#9515 listed 3 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 38520 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
13×chaosChaos Orb
HayImNew#9515 listed 3 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 104060 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
13×chaosChaos Orb
HayImNew#9515 listed 3 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 159180 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
13×chaosChaos Orb
HayImNew#9515 listed 3 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 143080 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
13×chaosChaos Orb
HayImNew#9515 listed 3 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 113240 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
14×chaosChaos Orb
kotikikotikikotiki#0295 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 137880 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
14×chaosChaos Orb
kotikikotikikotiki#0295 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 71920 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 2 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 136700 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
XefeA1t#2582 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 16460 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 2 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 82
Commissioned 152180 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
BlBoswaggings#2882 listed 2 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 124140 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 2 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 64620 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Corrupted
Asking Price:
15×chaosChaos Orb
zzqkk#6868 listed 17 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 71980 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 2 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 150360 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 2 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 102360 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 2 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 54820 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 2 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 145500 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 2 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 87780 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 2 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 99760 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 2 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 104680 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 2 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 131940 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
15×chaosChaos Orb
kktkamkg80#3544 listed a day ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 151220 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
15×chaosChaos Orb
HayImNew#9515 listed 3 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 48780 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 2 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 47580 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 2 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 26020 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 2 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 97280 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 2 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 32900 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 2 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 79300 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
TRAFFIK2010#0523 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 22180 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 2 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 151820 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 2 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 88400 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 2 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 28520 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 2 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 125880 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 2 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 121200 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 2 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 80
Commissioned 10080 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Madzak#4730 listed 14 minutes ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 134940 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 2 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 127920 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 2 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 35800 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 2 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 103780 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 2 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 151240 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 2 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 154720 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 2 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 79600 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 2 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 54400 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 2 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 90420 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 2 hours ago
Online

Showing 100 results (10000 matched)
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 71960 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 3 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 88400 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 3 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 137140 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 3 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 71980 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 3 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 130300 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 3 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 150360 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 3 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 151820 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 3 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 102360 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 3 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 103880 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 3 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 32900 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 3 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 126460 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 3 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 99760 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 3 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 64620 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Corrupted
Asking Price:
15×chaosChaos Orb
zzqkk#6868 listed 17 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 124140 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 3 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 125880 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 3 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 83
Commissioned 64480 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Amiloctr#3774 listed 6 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 70380 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 3 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 54400 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 3 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 102280 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 3 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 87780 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 3 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 16460 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 3 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 82
Commissioned 152180 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
BlBoswaggings#2882 listed 3 hours ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 153420 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 3 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 121200 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 3 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 79600 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 3 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 90420 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 3 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 69160 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 3 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 127920 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 3 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 28520 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 3 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 3060 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 3 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 48780 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 3 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 154720 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 3 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 80
Commissioned 10080 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Madzak#4730 listed 31 minutes ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 47580 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 3 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 134940 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 3 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 104920 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 3 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 26020 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 3 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 145500 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 3 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 103780 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 3 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 20140 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 3 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 97280 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 3 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 151240 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 3 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 55620 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 3 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 104680 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 3 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 141860 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 3 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 35800 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 3 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 54820 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 3 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 22180 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 3 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 59580 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 3 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 152680 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 3 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 79300 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
TRAFFIK2010#0523 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 105520 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
XefeA1t#2582 listed 4 minutes ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 131940 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
15×chaosChaos Orb
kktkamkg80#3544 listed a day ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 137960 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 3 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 71920 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 3 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 46880 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 3 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 66120 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Sixpathofpain#5269 listed 3 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 154000 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
19×chaosChaos Orb
Astrom2014#2023 listed 2 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 120040 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
19×chaosChaos Orb
Astrom2014#2023 listed 2 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 22900 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
DarkaliaTM#5337 listed 14 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 79400 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
Dongter#1875 listed 4 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 3420 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
20×chaosChaos Orb
player3393#3314 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 68200 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
DarkaliaTM#5337 listed 14 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 83
Commissioned 11280 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
TerebonDolgunec#9074 listed 7 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 82
Commissioned 146480 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
niponiponi#9065 listed 2 days ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 107980 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Corrupted
Exact Price:
20×chaosChaos Orb
4FateUr6743#6909 listed 4 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 18380 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
Niktrons#1940 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 5280 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
DarkaliaTM#5337 listed 14 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 89440 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
20×chaosChaos Orb
BurtPeddar#2484 listed 10 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 22600 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
_NegaTiv_#7803 listed 7 hours ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 4780 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
DarkaliaTM#5337 listed 14 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 70520 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
DarkaliaTM#5337 listed 14 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 96420 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
DarkaliaTM#5337 listed 14 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 147020 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
DarkaliaTM#5337 listed 14 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 83
Commissioned 152400 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
20×chaosChaos Orb
MadnessOne#3334 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 44180 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
20×chaosChaos Orb
BurtPeddar#2484 listed 10 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 80
Commissioned 117540 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
807775002#8189 listed 16 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 134760 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
DarkaliaTM#5337 listed 14 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 6700 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
DarkaliaTM#5337 listed 14 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 124640 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
lvjiale#7939 listed 3 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 132120 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
k1reall#1965 listed 26 minutes ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 127460 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
20×chaosChaos Orb
BurtPeddar#2484 listed 10 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 80
Commissioned 90160 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
SssloW#1322 listed 6 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 60240 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
nidalee22444#6566 listed a day ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 83
Commissioned 114440 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
KioshiMun#6281 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 121820 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
lvjiale#7939 listed 4 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 157300 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
20×chaosChaos Orb
MadnessOne#3334 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 138540 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
DarkaliaTM#5337 listed 14 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 134900 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
DarkaliaTM#5337 listed 14 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 21320 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
20×chaosChaos Orb
MadnessOne#3334 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 44220 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
20×chaosChaos Orb
acman8090md#3463 listed 2 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 86
Commissioned 110860 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
_NegaTiv_#7803 listed 7 hours ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 134020 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
DarkaliaTM#5337 listed 14 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 112300 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
DarkaliaTM#5337 listed 14 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 56520 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
Dongter#1875 listed 4 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 64480 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
Frezer255#7533 listed 8 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 71400 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
DarkaliaTM#5337 listed 14 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 47640 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
DarkaliaTM#5337 listed 14 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 133100 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
lvjiale#7939 listed 3 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 11360 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
20×chaosChaos Orb
acman8090md#3463 listed 4 days ago
Online

Showing 100 results (10000 matched)
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 132120 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
k1reall#1965 listed 27 minutes ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 137260 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
DarkaliaTM#5337 listed 14 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 4780 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
DarkaliaTM#5337 listed 14 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 64480 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
Frezer255#7533 listed 8 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 42940 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
20×chaosChaos Orb
BurtPeddar#2484 listed 10 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 83
Commissioned 22080 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
Marfen#6347 listed 7 hours ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 127460 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
20×chaosChaos Orb
BurtPeddar#2484 listed 10 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 133100 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
lvjiale#7939 listed 3 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 137480 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
_NegaTiv_#7803 listed 7 hours ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 71400 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
DarkaliaTM#5337 listed 14 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 82
Commissioned 146480 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
niponiponi#9065 listed 2 days ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 145400 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
lvjiale#7939 listed 5 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 65120 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
DarkaliaTM#5337 listed 14 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 47960 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
DarkaliaTM#5337 listed 14 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 3420 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
20×chaosChaos Orb
player3393#3314 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 56520 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
Dongter#1875 listed 4 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 83
Commissioned 80360 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
20×chaosChaos Orb
RobloxOneLove#1548 listed 13 hours ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 96420 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
DarkaliaTM#5337 listed 14 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 60240 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
nidalee22444#6566 listed a day ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 137460 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
DarkaliaTM#5337 listed 14 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 44220 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
20×chaosChaos Orb
acman8090md#3463 listed 2 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 134020 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
DarkaliaTM#5337 listed 14 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 61980 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
Eugame#6371 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 63920 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
_NegaTiv_#7803 listed 7 hours ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 121820 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
lvjiale#7939 listed 4 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 38620 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
Dongter#1875 listed 4 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 95260 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
lvjiale#7939 listed 4 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 11360 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
20×chaosChaos Orb
acman8090md#3463 listed 4 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 135420 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
Defnotdrake#3704 listed a day ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 134900 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
DarkaliaTM#5337 listed 14 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 112300 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
DarkaliaTM#5337 listed 14 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 21320 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
20×chaosChaos Orb
MadnessOne#3334 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 83
Commissioned 114440 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
KioshiMun#6281 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 159400 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
BLFC#3853 listed 16 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 70520 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
DarkaliaTM#5337 listed 14 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 7260 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
Heatens#0787 listed 2 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 68200 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
DarkaliaTM#5337 listed 14 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 80
Commissioned 90160 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
SssloW#1322 listed 6 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 73160 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
DarkaliaTM#5337 listed 14 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 21820 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
20×chaosChaos Orb
acman8090md#3463 listed 4 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 5280 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
DarkaliaTM#5337 listed 14 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 74120 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
DarkaliaTM#5337 listed 14 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 83
Commissioned 132000 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
20×chaosChaos Orb
kuraharo#2246 listed 5 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 157300 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
20×chaosChaos Orb
MadnessOne#3334 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 80
Commissioned 115500 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
Valanour#6974 listed 3 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 134760 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
DarkaliaTM#5337 listed 14 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 138540 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
DarkaliaTM#5337 listed 14 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 82
Commissioned 144560 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
LapkaVklare#7656 listed 7 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 89440 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
20×chaosChaos Orb
BurtPeddar#2484 listed 10 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 80
Commissioned 117540 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
807775002#8189 listed 16 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 149540 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
Insanewolfy#6503 listed 2 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 76280 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
20×chaosChaos Orb
MadnessOne#3334 listed 19 minutes ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 18380 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
Niktrons#1940 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 78320 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
20×chaosChaos Orb
no_vhs#2624 listed 11 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 147020 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
DarkaliaTM#5337 listed 14 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 129200 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
20×chaosChaos Orb
acman8090md#3463 listed 2 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 107980 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Corrupted
Exact Price:
20×chaosChaos Orb
4FateUr6743#6909 listed 4 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 83
Commissioned 11280 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
TerebonDolgunec#9074 listed 7 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 79600 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
Insanewolfy#6503 listed 2 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 83
Commissioned 152400 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
20×chaosChaos Orb
MadnessOne#3334 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 130600 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
_NegaTiv_#7803 listed 7 hours ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 47640 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
DarkaliaTM#5337 listed 14 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 22900 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
DarkaliaTM#5337 listed 14 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 82160 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
nidalee22444#6566 listed a day ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 78620 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
lazk#1505 listed a day ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 86
Commissioned 110860 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
_NegaTiv_#7803 listed 7 hours ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 4540 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
DarkaliaTM#5337 listed 14 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 106160 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
im_mug#2357 listed a day ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 79400 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
Dongter#1875 listed 4 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 6700 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
DarkaliaTM#5337 listed 14 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 44180 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
20×chaosChaos Orb
BurtPeddar#2484 listed 10 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 124640 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
lvjiale#7939 listed 3 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 22600 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
_NegaTiv_#7803 listed 7 hours ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 82
Commissioned 134420 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
LLcoolpelican#2149 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 86
Commissioned 143360 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
21×chaosChaos Orb
Guardzor#0237 listed 19 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 83
Commissioned 56500 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
22×chaosChaos Orb
clever_xd#1926 listed a day ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 144380 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
24×chaosChaos Orb
KiFoR4Ik#5805 listed 18 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 155260 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
25×chaosChaos Orb
LoStGr00ver#3390 listed 4 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 10900 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
25×chaosChaos Orb
DirtySam2021#5235 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 80
Commissioned 65440 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
25×chaosChaos Orb
Abysmalblade#6564 listed 6 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 83
Commissioned 39120 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
25×chaosChaos Orb
iDarel#4185 listed a day ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 4280 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
25×chaosChaos Orb
TatudeJardim#7409 listed 10 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 17020 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
25×chaosChaos Orb
FoxSkill#6948 listed 6 days ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 31560 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
25×chaosChaos Orb
RewQew#6266 listed 4 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 80
Commissioned 159180 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
25×chaosChaos Orb
Puuchi#0954 listed 7 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 82
Commissioned 149980 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
25×chaosChaos Orb
NepperoniPipples#0963 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 67640 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
25×chaosChaos Orb
FoxSkill#6948 listed 6 days ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 21460 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
25×chaosChaos Orb
FoxSkill#6948 listed 6 days ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 80
Commissioned 32800 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
25×chaosChaos Orb
ayteebb#6710 listed 11 days ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 83
Commissioned 22080 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
25×chaosChaos Orb
ImParadoxx#6119 listed 20 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 25300 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
25×chaosChaos Orb
FoxSkill#6948 listed 6 days ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 93700 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
25×chaosChaos Orb
FoxSkill#6948 listed 6 days ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 130380 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
25×chaosChaos Orb
FoxSkill#6948 listed 6 days ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 156220 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
25×chaosChaos Orb
FoxSkill#6948 listed 6 days ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 113640 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
25×chaosChaos Orb
FoxSkill#6948 listed 6 days ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 108600 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
25×chaosChaos Orb
Aangst#4309 listed 3 days ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 110540 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
25×chaosChaos Orb
Lisien#4037 listed a day ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 150420 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
25×chaosChaos Orb
FoxSkill#6948 listed 6 days ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 78720 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
25×chaosChaos Orb
Hakkuren#8170 listed 3 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 82
Commissioned 29060 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
25×chaosChaos Orb
mercomancer222#4455  listed a day ago
Online


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

# To Download EE
for i in range(2000, 160020, 20): # 160020
    entry = [str(i) + ' Victario','200 chaosChaos Orb']
    trade_list.append(entry)

# Load pickle with previous data, so we don't have to scrap them again.
hubris_data = load_pickle('hubris_data')
if not hubris_data:
    hubris_data = {}

# open browser
def initiate_browser():
    global driver
    options = Options()
    
    # Set preferences directly on the profile via options
    # options.set_preference("privacy.donottrackheader.value", 1)
    # options.set_preference("media.peerconnection.enabled", False)
    options.set_preference("privacy.donottrackheader.enabled", True)  # DoNotTrack
    options.set_preference("privacy.donottrackheader.value", 1)
    options.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:61.0) Gecko/20100101 Firefox/106.0")
    #                        "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 selenium.py")
    options.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', False)  # You would also like to block flash
    options.set_preference("media.peerconnection.enabled", False)  # WebRTC

    # You can add headless mode if needed
    # options.headless = True  # Uncomment if you want to run in headless mode
    driver = webdriver.Firefox(options=options)
    return driver


# sockets = 60735 61834 61419
socket = 60735
socket = 61834
socket = 61419
socket = 54127
socket = 26196
socket = 26725

# page_url = 'https://vilsol.github.io/timeless-jewels/tree?jewel=5&conqueror=Victario&seed=10000&location=60735&mode=seed'
page_url = f'https://vilsol.github.io/timeless-jewels/tree?jewel=5&conqueror=Victario&seed=10000&location={socket}&mode=seed'

browser_started = False

socket = page_url.split('location=')
socket = socket[1].replace('&mode=seed', '')

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

        # GET DATA
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

        time.sleep(1 + (random.randint(1, 2000)/1000))

        seed.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)

        counter += 1
    if counter % 20 == 0:
        if new_data:
            print('saving')
            save_pickle('hubris_data', hubris_data)
            new_data = False
            # counter = 0
        # break

if new_data:
    save_pickle('hubris_data', hubris_data)

# print(hubris_data)
positive_mods = {'increased Damage per Power Charge': 1.3, 
                 'increased Energy Shield per Power Charge': 1.5,
                 'increased Damage per Frenzy Charge': 1, 
                 'increased Damage per Endurance Charge': 0.9,
                 'increased Melee Physical Damage': 0.4,  
                 'increased Spell Damage': 0.3, 
                 'chance to Avoid being Shocked': 0.1, 
                 'to Fire Resistance': 0,
                 'to Cold Resistance': 0,
                 'to Lightning Resistance': 0,
                  }
blue_mods = ['increased Energy Shield per Power Charge']
red_mods = ['increased Damage per Power Charge', 'increased Damage per Frenzy Charge', 'increased Damage per Endurance Charge',]
green_mods = ['chance to Avoid being Shocked', 'to Fire Resistance', 'to Cold Resistance', 'to Lightning Resistance']
yellow_mods = ['increased Melee Physical Damage', 'increased Spell Damage']
best_jewels_lst = []

counter = 0
for jewel in trade_list:
    # print(jewel)
    coins = jewel[0].split(' ')[0]
    for socket in hubris_data[coins]:
        # print(hubris_data[coins][socket].replace('(','\n'))
        score = 0
        mods = hubris_data[coins][socket].split('(')
        for mod in mods:
            mod = mod.split(')')
            # print(mod)
            try:
                # if any(x in mod[1] for x in positive_mods):
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
    # print('\n\n', best_jewels_lst[i], '\n', hubris_data[best_jewels_lst[i][1]][best_jewels_lst[i][2]].replace('(','\n'))
    if any(key in s1 for key in blue_mods) and 'increased Damage per Power Charge' in s1 and s1 not in s:
        s += s1

s = s.split('\n')

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
    
