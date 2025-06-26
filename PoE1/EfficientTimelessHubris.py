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
Item Level: 83
Commissioned 92100 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
10×chaosChaos Orb
AliaksandrKalkunou#6342 listed 17 hours ago
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
AliaksandrKalkunou#6342 listed 17 hours ago
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
AliaksandrKalkunou#6342 listed 17 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 152920 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
10×chaosChaos Orb
AliaksandrKalkunou#6342 listed 17 hours ago
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
AliaksandrKalkunou#6342 listed 17 hours ago
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
AliaksandrKalkunou#6342 listed 17 hours ago
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
AliaksandrKalkunou#6342 listed 17 hours ago
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
AliaksandrKalkunou#6342 listed 17 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 83
Commissioned 50760 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
10×chaosChaos Orb
MaxMode#9882 listed 4 hours ago
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
AliaksandrKalkunou#6342 listed 17 hours ago
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
AliaksandrKalkunou#6342 listed 17 hours ago
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
AliaksandrKalkunou#6342 listed 17 hours ago
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
AliaksandrKalkunou#6342 listed 17 hours ago
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
AliaksandrKalkunou#6342 listed 17 hours ago
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
AliaksandrKalkunou#6342 listed 17 hours ago
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
AliaksandrKalkunou#6342 listed 17 hours ago
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
AliaksandrKalkunou#6342 listed 17 hours ago
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
AliaksandrKalkunou#6342 listed 17 hours ago
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
AliaksandrKalkunou#6342 listed 17 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 83880 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
10×chaosChaos Orb
AliaksandrKalkunou#6342 listed 17 hours ago
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
AliaksandrKalkunou#6342 listed 17 hours ago
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
AliaksandrKalkunou#6342 listed 17 hours ago
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
AliaksandrKalkunou#6342 listed 17 hours ago
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
AliaksandrKalkunou#6342 listed 17 hours ago
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
AliaksandrKalkunou#6342 listed 17 hours ago
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
AliaksandrKalkunou#6342 listed 17 hours ago
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
AliaksandrKalkunou#6342 listed 17 hours ago
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
AliaksandrKalkunou#6342 listed 17 hours ago
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
AliaksandrKalkunou#6342 listed 17 hours ago
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
AliaksandrKalkunou#6342 listed 17 hours ago
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
AliaksandrKalkunou#6342 listed 17 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 79240 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
10×chaosChaos Orb
AliaksandrKalkunou#6342 listed 17 hours ago
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
AliaksandrKalkunou#6342 listed 17 hours ago
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
AliaksandrKalkunou#6342 listed 17 hours ago
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
AliaksandrKalkunou#6342 listed 17 hours ago
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
AliaksandrKalkunou#6342 listed 17 hours ago
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
AliaksandrKalkunou#6342 listed 17 hours ago
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
AliaksandrKalkunou#6342 listed 17 hours ago
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
AliaksandrKalkunou#6342 listed 17 hours ago
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
AliaksandrKalkunou#6342 listed 17 hours ago
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
AliaksandrKalkunou#6342 listed 17 hours ago
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
AliaksandrKalkunou#6342 listed 17 hours ago
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
AliaksandrKalkunou#6342 listed 17 hours ago
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
AliaksandrKalkunou#6342 listed 17 hours ago
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
AliaksandrKalkunou#6342 listed 17 hours ago
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
AliaksandrKalkunou#6342 listed 17 hours ago
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
AliaksandrKalkunou#6342 listed 17 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 103400 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
10×chaosChaos Orb
Tallwind#1610 listed 22 minutes ago
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
AliaksandrKalkunou#6342 listed 17 hours ago
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
AliaksandrKalkunou#6342 listed 17 hours ago
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
AliaksandrKalkunou#6342 listed 17 hours ago
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
AliaksandrKalkunou#6342 listed 17 hours ago
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
AliaksandrKalkunou#6342 listed 17 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 138200 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
12×chaosChaos Orb
r0kudo#5246 listed 3 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 127700 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
12×chaosChaos Orb
r0kudo#5246 listed a day ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 68520 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
14×chaosChaos Orb
MagicAourun#5366 listed 2 hours ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 143580 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
ghs1994#7256 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 140380 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Cruden#7326 listed a day ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 80
Commissioned 34200 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
JokingJoker1106#3492 listed 33 minutes ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 64100 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Fspeed219#2657 listed 20 hours ago
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
kktkamkg80#3544 listed 4 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 109920 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
rawelgae#1958 listed 8 minutes ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 80
Commissioned 155000 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
20×chaosChaos Orb
wangyue013#6494 listed a day ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 12180 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
pathofexile_unsnap402#4891 listed 9 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 42340 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
Falko#2616 listed 14 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 2300 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
ManlyManatee#7538 listed 6 hours ago
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
niponiponi#9065 listed a day ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 83
Commissioned 138760 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
belufrench0#0594 listed 5 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 99060 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
blaxts#2815 listed 17 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 66580 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
MoistKoalaBalls#3504 listed 2 days ago
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
Eugame#6371 listed a day ago
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
lazk#1505 listed 12 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 110640 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
pathofexile_unsnap402#4891 listed 9 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 97520 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
D4NNYMUSIC#5120 listed 9 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 154980 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
20×chaosChaos Orb
Deeonex#2821 listed a day ago
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
nidalee22444#6566 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 21560 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
pathofexile_unsnap402#4891 listed 9 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 145320 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
Dingnasty#7165 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 48740 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
nidalee22444#6566 listed an hour ago
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
nidalee22444#6566 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 126980 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
21×chaosChaos Orb
ro0d#2399 listed 4 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 147340 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
22×chaosChaos Orb
kaiot312#5062 listed 15 hours ago
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
clever_xd#1926 listed 9 hours ago
Online
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
ayteebb#6710 listed 10 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 24440 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
25×chaosChaos Orb
mohito22#7766 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 120100 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
25×chaosChaos Orb
Lufix#7247 listed 4 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 85680 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
25×chaosChaos Orb
Lufix#7247 listed 4 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 37760 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
25×chaosChaos Orb
Lufix#7247 listed 4 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 83
Commissioned 87980 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
25×chaosChaos Orb
ImParadoxx#6119 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 141660 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
25×chaosChaos Orb
Meaticus#4308 listed 7 hours ago
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
mercomancer222#4455  listed 4 hours ago
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
25×chaosChaos Orb
ImParadoxx#6119 listed 10 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 25220 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
25×chaosChaos Orb
Lufix#7247 listed 4 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 145540 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
25×chaosChaos Orb
mohito22#7766 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 145380 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
25×chaosChaos Orb
SCHOCKY123#0413 listed 5 days ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 147860 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
25×chaosChaos Orb
mohito22#7766 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 42980 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
25×chaosChaos Orb
MercuryRageMultihack#4509 listed 7 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 130300 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
25×chaosChaos Orb
mohito22#7766 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 98440 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
25×chaosChaos Orb
Lufix#7247 listed 4 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 90460 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
25×chaosChaos Orb
mohito22#7766 listed 2 days ago
Online
© 2010 - 2025 Grinding Gear Games


Showing 100 results (10000 matched)
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 141660 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
25×chaosChaos Orb
Meaticus#4308 listed 8 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 150480 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
25×chaosChaos Orb
Befox22#7990 listed 9 hours ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 83
Commissioned 78820 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
25×chaosChaos Orb
Wildwilie#5611 listed 2 days ago
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
mercomancer222#4455  listed 4 hours ago
Online
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
Aangst#4309 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 145380 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
25×chaosChaos Orb
SCHOCKY123#0413 listed 5 days ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 147860 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
25×chaosChaos Orb
mohito22#7766 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 42980 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
25×chaosChaos Orb
MercuryRageMultihack#4509 listed 7 days ago
Online
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
Hakkuren#8170 listed 2 days ago
Online
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
ayteebb#6710 listed 10 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 85
Commissioned 22780 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
25×chaosChaos Orb
KitcuneMia#4048 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 83
Commissioned 149300 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
25×chaosChaos Orb
kingnyansen#5143 listed 24 minutes ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 83
Commissioned 87980 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
25×chaosChaos Orb
ImParadoxx#6119 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 24440 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
25×chaosChaos Orb
mohito22#7766 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 125340 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
25×chaosChaos Orb
kingnyansen#5143 listed 24 minutes ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 145540 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
25×chaosChaos Orb
mohito22#7766 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 85
Commissioned 22020 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
25×chaosChaos Orb
KitcuneMia#4048 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 80
Commissioned 118980 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
25×chaosChaos Orb
Derocchio#4092 listed 4 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 39160 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
25×chaosChaos Orb
isaacthegod#6108 listed a minute ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 47600 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
25×chaosChaos Orb
mohito22#7766 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 130300 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
25×chaosChaos Orb
mohito22#7766 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 90460 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
25×chaosChaos Orb
mohito22#7766 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 82
Commissioned 111480 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
25×chaosChaos Orb
jimmyjams86#1868 listed a day ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 108140 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
25×chaosChaos Orb
mohito22#7766 listed 2 days ago
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
25×chaosChaos Orb
ImParadoxx#6119 listed 10 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 105100 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
25×chaosChaos Orb
kurtsaidwhat#6388 listed 5 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 66000 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
25×chaosChaos Orb
mohito22#7766 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 62440 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
29×chaosChaos Orb
KraitLive#6331 listed 5 hours ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 19940 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
29×chaosChaos Orb
KraitLive#6331 listed 5 hours ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 107480 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
29×chaosChaos Orb
qorms1#6736 listed 10 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 110660 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
29×chaosChaos Orb
KraitLive#6331 listed 5 hours ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 8520 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
29×chaosChaos Orb
KraitLive#6331 listed 5 hours ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 21380 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
29×chaosChaos Orb
KraitLive#6331 listed 5 hours ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 147080 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
29×chaosChaos Orb
qorms1#6736 listed 10 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 95760 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
29×chaosChaos Orb
KraitLive#6331 listed 5 hours ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 61800 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
29×chaosChaos Orb
KraitLive#6331 listed 5 hours ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Damage Penetrates 1% Lightning Resistance
Commissioned 65600 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Corrupted
Asking Price:
29×chaosChaos Orb
dungvbhp11#2980 listed 3 days ago
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
Asking Price:
29×chaosChaos Orb
KraitLive#6331 listed 5 hours ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 145860 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
29×chaosChaos Orb
KraitLive#6331 listed 5 hours ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 51440 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
29×chaosChaos Orb
KraitLive#6331 listed 5 hours ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 56580 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
29×chaosChaos Orb
KraitLive#6331 listed 5 hours ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 156780 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
29×chaosChaos Orb
KraitLive#6331 listed 5 hours ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 118380 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
29×chaosChaos Orb
KraitLive#6331 listed 5 hours ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 116140 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
29×chaosChaos Orb
qorms1#6736 listed 10 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 96160 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
29×chaosChaos Orb
KraitLive#6331 listed 5 hours ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 27480 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
29×chaosChaos Orb
KraitLive#6331 listed 5 hours ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 112820 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
29×chaosChaos Orb
KraitLive#6331 listed 5 hours ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 77800 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
29×chaosChaos Orb
KraitLive#6331 listed 5 hours ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 7140 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
29×chaosChaos Orb
KraitLive#6331 listed 5 hours ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 94720 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
30×chaosChaos Orb
ilyakoo#4413 listed 6 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 36380 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
30×chaosChaos Orb
lordofthings1#4656 listed a day ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 80
Commissioned 107840 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
30×chaosChaos Orb
Guplo#4961 listed 13 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 63080 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
30×chaosChaos Orb
CXwnitsu#0230 listed a day ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 87420 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
30×chaosChaos Orb
SESAK#2901 listed 6 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 87360 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
30×chaosChaos Orb
kaneki62#3459 listed 3 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 38300 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
30×chaosChaos Orb
Xeon1979#1444 listed 15 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 156560 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
30×chaosChaos Orb
NaDa__#3042 listed 2 days ago
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
30×chaosChaos Orb
Insanewolfy#6503 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 83
Commissioned 158060 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
30×chaosChaos Orb
Guess_whoo#7968 listed a day ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 82
Commissioned 115780 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
30×chaosChaos Orb
Cruden#7326 listed a day ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 83620 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
30×chaosChaos Orb
ImParadoxx#6119 listed 10 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 138900 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
30×chaosChaos Orb
ImParadoxx#6119 listed 10 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 83
Commissioned 151320 coins to commemorate Caspiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
30×chaosChaos Orb
tookiplaty#5841 listed 17 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 111400 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
30×chaosChaos Orb
loguedog#0679 listed 8 hours ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 6600 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
30×chaosChaos Orb
ManaPong#1118 listed a day ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 107940 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
30×chaosChaos Orb
SESAK#2901 listed 6 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 83
Commissioned 141500 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
30×chaosChaos Orb
TicoXz#1094 listed 2 days ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 29900 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
30×chaosChaos Orb
Falko#2616 listed 12 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 9160 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
30×chaosChaos Orb
SESAK#2901 listed 8 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 24240 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
30×chaosChaos Orb
SESAK#2901 listed 6 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 156600 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
30×chaosChaos Orb
ImParadoxx#6119 listed 10 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 132960 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
30×chaosChaos Orb
SESAK#2901 listed 8 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 89300 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
30×chaosChaos Orb
Flowski12#4992 listed 3 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 123600 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Corrupted
Exact Price:
30×chaosChaos Orb
PaudoFalcão#4296 listed 4 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 23920 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
30×chaosChaos Orb
SESAK#2901 listed 6 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 83
Commissioned 144380 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
30×chaosChaos Orb
ImParadoxx#6119 listed 10 hours ago
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
30×chaosChaos Orb
SESAK#2901 listed 8 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 80
Commissioned 89080 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
30×chaosChaos Orb
해달오름#1118 listed 7 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 86
Commissioned 64700 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
30×chaosChaos Orb
SESAK#2901 listed 6 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 122240 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
30×chaosChaos Orb
Khazadan#2427 listed a day ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 109080 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
30×chaosChaos Orb
Flowski12#4992 listed 3 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 19680 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
30×chaosChaos Orb
lairaguiar#1180 listed 3 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 109120 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
30×chaosChaos Orb
Lecter12#5289 listed a day ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 145680 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
30×chaosChaos Orb
Flowski12#4992 listed 3 days ago
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
30×chaosChaos Orb
NooBXan02#0732 listed 3 hours ago
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
30×chaosChaos Orb
Insanewolfy#6503 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 75300 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
30×chaosChaos Orb
odaric#6039 listed a day ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 24880 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
30×chaosChaos Orb
vunderkind228#3087 listed 16 minutes ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 102940 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
30×chaosChaos Orb
hanzzang_NEW#7182 listed 13 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 83
Commissioned 16820 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
30×chaosChaos Orb
Flowski12#4992 listed 3 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 116660 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
30×chaosChaos Orb
SESAK#2901 listed 8 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 65840 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
30×chaosChaos Orb
SESAK#2901 listed 6 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 134920 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
30×chaosChaos Orb
SESAK#2901 listed 8 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 6520 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
30×chaosChaos Orb
ImParadoxx#6119 listed 10 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 58980 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
30×chaosChaos Orb
aa8537527#1742 listed 3 days ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 109540 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
30×chaosChaos Orb
gorecrak#2099 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 57700 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
30×chaosChaos Orb
SESAK#2901 listed 6 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 53940 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
30×chaosChaos Orb
Pl0uch#1791 listed 3 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 147940 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
30×chaosChaos Orb
SESAK#2901 listed 8 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 80
Commissioned 43600 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
30×chaosChaos Orb
littlendt131#6782 listed 9 hours ago
Online
© 2010 - 2025 Grinding Gear Games
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
for i in range(2000, 97880, 20): # 160020
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
positive_mods = {'increased Damage per Power Charge': 1, 
                 'increased Energy Shield per Power Charge': 1.2,
                 'increased Damage per Frenzy Charge': 1.2, 
                 'increased Damage per Endurance Charge': 0.9,
                 'increased Melee Physical Damage': 0.6,  
                 'increased Spell Damage': 0.5, 
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
for i in range(30):
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
    
