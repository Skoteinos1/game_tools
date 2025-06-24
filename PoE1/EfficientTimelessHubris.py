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
        data1 = ''
        save_pickle(fl_nm, data1)
    return data1


# Enter text from PoE trade:
trade_text = """
 Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 20740 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
10×chaosChaos Orb
HayImNew#9515 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 99240 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
10×chaosChaos Orb
HayImNew#9515 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 112700 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
10×chaosChaos Orb
HayImNew#9515 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 158440 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
10×chaosChaos Orb
HayImNew#9515 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 122820 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
10×chaosChaos Orb
HayImNew#9515 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 62160 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
10×chaosChaos Orb
HayImNew#9515 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 66380 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
10×chaosChaos Orb
HayImNew#9515 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 89300 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
10×chaosChaos Orb
HayImNew#9515 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 50600 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
10×chaosChaos Orb
HayImNew#9515 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 125660 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
10×chaosChaos Orb
HayImNew#9515 listed an hour ago
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
10×chaosChaos Orb
HayImNew#9515 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 71800 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
10×chaosChaos Orb
HayImNew#9515 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 86380 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
10×chaosChaos Orb
HayImNew#9515 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 130640 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
10×chaosChaos Orb
HayImNew#9515 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 103000 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
10×chaosChaos Orb
HayImNew#9515 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 31860 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
10×chaosChaos Orb
HayImNew#9515 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 29240 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
10×chaosChaos Orb
HayImNew#9515 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 27760 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
10×chaosChaos Orb
HayImNew#9515 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 40560 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
10×chaosChaos Orb
HayImNew#9515 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 2880 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
10×chaosChaos Orb
HayImNew#9515 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 83040 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
10×chaosChaos Orb
HayImNew#9515 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 93660 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
10×chaosChaos Orb
HayImNew#9515 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 104940 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
10×chaosChaos Orb
HayImNew#9515 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 64940 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
10×chaosChaos Orb
HayImNew#9515 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 140240 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
10×chaosChaos Orb
HayImNew#9515 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 120700 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
10×chaosChaos Orb
HayImNew#9515 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 131660 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
10×chaosChaos Orb
HayImNew#9515 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 81220 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
10×chaosChaos Orb
HayImNew#9515 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 28520 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
10×chaosChaos Orb
HayImNew#9515 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 59560 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
10×chaosChaos Orb
HayImNew#9515 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 54100 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
10×chaosChaos Orb
HayImNew#9515 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 146620 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
10×chaosChaos Orb
HayImNew#9515 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 57820 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
10×chaosChaos Orb
HayImNew#9515 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 84380 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
10×chaosChaos Orb
HayImNew#9515 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 56320 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
10×chaosChaos Orb
HayImNew#9515 listed an hour ago
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
10×chaosChaos Orb
HayImNew#9515 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 122360 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
10×chaosChaos Orb
HayImNew#9515 listed an hour ago
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
Asking Price:
10×chaosChaos Orb
HayImNew#9515 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 117340 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
10×chaosChaos Orb
HayImNew#9515 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 104820 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
10×chaosChaos Orb
HayImNew#9515 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 11380 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
10×chaosChaos Orb
HayImNew#9515 listed an hour ago
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
Asking Price:
10×chaosChaos Orb
HayImNew#9515 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 141100 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
10×chaosChaos Orb
HayImNew#9515 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 142080 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
10×chaosChaos Orb
HayImNew#9515 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 60520 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
10×chaosChaos Orb
HayImNew#9515 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 50640 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
10×chaosChaos Orb
HayImNew#9515 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 87140 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
10×chaosChaos Orb
HayImNew#9515 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 98000 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
10×chaosChaos Orb
HayImNew#9515 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 33540 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
10×chaosChaos Orb
HayImNew#9515 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 158480 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
10×chaosChaos Orb
HayImNew#9515 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 37940 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
10×chaosChaos Orb
HayImNew#9515 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 22000 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
10×chaosChaos Orb
HayImNew#9515 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 71140 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
10×chaosChaos Orb
HayImNew#9515 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 33320 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
10×chaosChaos Orb
HayImNew#9515 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 140760 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
10×chaosChaos Orb
HayImNew#9515 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 22760 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
10×chaosChaos Orb
HayImNew#9515 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 106920 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
10×chaosChaos Orb
HayImNew#9515 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 60000 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
10×chaosChaos Orb
HayImNew#9515 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 149860 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
10×chaosChaos Orb
HayImNew#9515 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 107700 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
10×chaosChaos Orb
HayImNew#9515 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 114620 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
10×chaosChaos Orb
HayImNew#9515 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 135120 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
10×chaosChaos Orb
HayImNew#9515 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 41120 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
10×chaosChaos Orb
HayImNew#9515 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 152060 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
10×chaosChaos Orb
HayImNew#9515 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 89440 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
10×chaosChaos Orb
HayImNew#9515 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 112900 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
10×chaosChaos Orb
HayImNew#9515 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 80
Commissioned 18900 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
12×chaosChaos Orb
Paul904#3370 listed 28 minutes ago
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
orlandoq1829#5913 listed 19 hours ago
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
13×chaosChaos Orb
AliaksandrKalkunou#6342 listed a day ago
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
13×chaosChaos Orb
AliaksandrKalkunou#6342 listed a day ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 83
Commissioned 67320 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
13×chaosChaos Orb
AliaksandrKalkunou#6342 listed a day ago
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
13×chaosChaos Orb
AliaksandrKalkunou#6342 listed a day ago
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
13×chaosChaos Orb
AliaksandrKalkunou#6342 listed a day ago
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
13×chaosChaos Orb
AliaksandrKalkunou#6342 listed a day ago
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
13×chaosChaos Orb
AliaksandrKalkunou#6342 listed a day ago
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
13×chaosChaos Orb
AliaksandrKalkunou#6342 listed a day ago
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
13×chaosChaos Orb
AliaksandrKalkunou#6342 listed a day ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 98260 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
13×chaosChaos Orb
AliaksandrKalkunou#6342 listed a day ago
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
13×chaosChaos Orb
AliaksandrKalkunou#6342 listed a day ago
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
13×chaosChaos Orb
AliaksandrKalkunou#6342 listed a day ago
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
13×chaosChaos Orb
AliaksandrKalkunou#6342 listed a day ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 99100 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
13×chaosChaos Orb
AliaksandrKalkunou#6342 listed a day ago
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
13×chaosChaos Orb
AliaksandrKalkunou#6342 listed a day ago
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
13×chaosChaos Orb
AliaksandrKalkunou#6342 listed a day ago
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
13×chaosChaos Orb
AliaksandrKalkunou#6342 listed a day ago
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
13×chaosChaos Orb
AliaksandrKalkunou#6342 listed a day ago
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
13×chaosChaos Orb
AliaksandrKalkunou#6342 listed a day ago
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
13×chaosChaos Orb
AliaksandrKalkunou#6342 listed a day ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 83
Commissioned 70840 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
13×chaosChaos Orb
AliaksandrKalkunou#6342 listed a day ago
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
13×chaosChaos Orb
AliaksandrKalkunou#6342 listed a day ago
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
13×chaosChaos Orb
AliaksandrKalkunou#6342 listed a day ago
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
13×chaosChaos Orb
AliaksandrKalkunou#6342 listed a day ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 141840 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
13×chaosChaos Orb
AliaksandrKalkunou#6342 listed a day ago
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
13×chaosChaos Orb
AliaksandrKalkunou#6342 listed a day ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 83
Commissioned 45560 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
13×chaosChaos Orb
AliaksandrKalkunou#6342 listed a day ago
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
13×chaosChaos Orb
AliaksandrKalkunou#6342 listed a day ago
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
13×chaosChaos Orb
AliaksandrKalkunou#6342 listed a day ago
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
13×chaosChaos Orb
AliaksandrKalkunou#6342 listed a day ago
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
13×chaosChaos Orb
AliaksandrKalkunou#6342 listed a day ago
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
"""

trade_text = trade_text.split('\n')
trade_list = []
entry = ['','']
for i in range(len(trade_text)):
    if "Commissioned" in trade_text[i]:
        entry[0] = trade_text[i].replace('Commissioned ', '').replace(' coins to commemorate', '')
    if "Asking Price:" in trade_text[i]:
        entry[1] = trade_text[i+1].replace('×', ' ')
        trade_list.append(entry)
        entry = ['','']

# print(trade_list)

# Load pickle with previous data, so we don't have to scrap them again.
hubris_data = load_pickle('hubris_data')
if not hubris_data:
    hubris_data = {}

# open browser
def initiate_browser():
    global driver
    # profile = webdriver.FirefoxProfile()
    # profile.set_preference("privacy.donottrackheader.enabled", True)  # DoNotTrack
    # profile.set_preference("privacy.donottrackheader.value", 1)
    # profile.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:61.0) Gecko/20100101 Firefox/106.0")
    #                        "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 selenium.py")
    # profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', False)  # You would also like to block flash
    # profile.set_preference("media.peerconnection.enabled", False)  # WebRTC
    # driver = webdriver.Firefox(firefox_profile=profile)
    # driver = webdriver.Firefox()
    # driver.set_window_size(1298, 1012)

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

# initiate_browser()
page_url = 'https://vilsol.github.io/timeless-jewels/tree?jewel=5&conqueror=Victario&seed=10000&location=60735&mode=seed'
# driver.get(page_url)

foo = input("Select Jewel socket and press Enter")

# socket = driver.current_url.split('location=')
socket = page_url.split('location=')
socket = socket[1].replace('&mode=seed', '')

seed = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div/div[5]/input")

# get the data:
for jewel in trade_list:
    coins = jewel[0].split(' ')[0]
    if coins not in hubris_data:
        hubris_data[coins] = {}
    if socket not in hubris_data[coins]:
        print(coins, socket)

        # GET DATA
        seed.send_keys(coins)
        
        # Wait
        time.sleep(500)
        
        # Get data
        page_html = driver.page_source
        page_soup = soup(page_html, "html.parser")
        notes = page_soup.find("ul", {"class": 'mt-1 svelte-9h6fz6 rainbow'}).text
        if notes:
            hubris_data[coins][socket] = notes

        time.sleep(1+ random.randint(1, 2000))

        seed.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)










