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



 Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 80
Commissioned 133360 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
10×chaosChaos Orb
ViviAnGoldenLucky#1214 listed 3 hours ago
AFK
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
12×chaosChaos Orb
r0kudo#5246 listed 17 hours ago
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
r0kudo#5246 listed 17 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 149400 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
12×chaosChaos Orb
r0kudo#5246 listed 16 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 22840 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
kira_asashi#1418 listed 7 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 83
Commissioned 78460 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
15×chaosChaos Orb
Pleased12#1100 listed 18 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 35980 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
아르젠티노#2588 listed 14 hours ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 139500 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
아르젠티노#2588 listed 18 hours ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 83
Commissioned 52400 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
15×chaosChaos Orb
Horinger#4703 listed 10 minutes ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 72180 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
아르젠티노#2588 listed 18 hours ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 80
Commissioned 73180 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
melas__#2219 listed a day ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 83840 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
아르젠티노#2588 listed 18 hours ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 83
Commissioned 43340 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Bentosik#3618 listed 21 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 49740 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
PwnzMao#4389 listed 3 days ago
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
Cruden#7326 listed 13 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 83
Commissioned 43740 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Bentosik#3618 listed 21 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 66900 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Mamododarky#5995 listed 12 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 117420 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
15×chaosChaos Orb
zevah86#3144 listed a day ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 83
Commissioned 59620 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
15×chaosChaos Orb
Bentosik#3618 listed 20 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 112820 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
18×chaosChaos Orb
bggr21#7174 listed 13 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 83
Commissioned 130200 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
18×chaosChaos Orb
bggr21#7174 listed 13 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 46900 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
18×chaosChaos Orb
bggr21#7174 listed 13 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 60780 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
18×chaosChaos Orb
bggr21#7174 listed 13 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 82
Commissioned 152480 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
18×chaosChaos Orb
bggr21#7174 listed 13 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 29780 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
20×chaosChaos Orb
하아룽#7164 listed 3 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 80
Commissioned 117680 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
20×chaosChaos Orb
Snarky85#4985 listed an hour ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 97360 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
20×chaosChaos Orb
merfyk#0129 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 121120 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
DoubleXypMa#0542 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 90720 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
DoubleXypMa#0542 listed a day ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 38280 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
20×chaosChaos Orb
CtenawaReturn#6784 listed 2 days ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 118620 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
20×chaosChaos Orb
하아룽#7164 listed 3 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 35820 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
20×chaosChaos Orb
하아룽#7164 listed 3 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 124460 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
20×chaosChaos Orb
CtenawaReturn#6784 listed 2 days ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 43420 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
DoubleXypMa#0542 listed a day ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 76880 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
20×chaosChaos Orb
CtenawaReturn#6784 listed 2 days ago
AFK
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
DoubleXypMa#0542 listed 16 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 10440 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
DoubleXypMa#0542 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 45560 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
CxC332#1710 listed 14 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 31760 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
DoubleXypMa#0542 listed 16 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 2680 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
20×chaosChaos Orb
CtenawaReturn#6784 listed 2 days ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 80
Commissioned 42340 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
ton0149433601#1457 listed a day ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 145300 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
DoubleXypMa#0542 listed 3 days ago
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
lvjiale#7939 listed a day ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 103820 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
s778563#7674 listed a day ago
Online
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
LLcoolpelican#2149 listed a day ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 81860 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
20×chaosChaos Orb
CtenawaReturn#6784 listed 2 days ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 80
Commissioned 133540 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
steven25691837#0289 listed a day ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 90900 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
DoubleXypMa#0542 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 90860 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
20×chaosChaos Orb
CtenawaReturn#6784 listed 2 days ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 90360 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
20×chaosChaos Orb
CtenawaReturn#6784 listed 2 days ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 90720 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
20×chaosChaos Orb
CtenawaReturn#6784 listed 2 days ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 82
Commissioned 96960 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
Les_Larmes_du_Styx#1908 listed 18 minutes ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 136080 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
DoubleXypMa#0542 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 131940 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
DoubleXypMa#0542 listed a day ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 89620 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
20×chaosChaos Orb
CtenawaReturn#6784 listed 2 days ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 138740 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
DoubleXypMa#0542 listed a day ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 47720 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
20×chaosChaos Orb
하아룽#7164 listed 3 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 91840 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
20×chaosChaos Orb
NonExistance#0239 listed 10 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 30540 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
DoubleXypMa#0542 listed 3 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 28740 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
20×chaosChaos Orb
CtenawaReturn#6784 listed 2 days ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 147700 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
DoubleXypMa#0542 listed 3 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 90900 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
20×chaosChaos Orb
CtenawaReturn#6784 listed 2 days ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 124720 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
DoubleXypMa#0542 listed 3 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 42200 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
20×chaosChaos Orb
CtenawaReturn#6784 listed 2 days ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 92020 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
20×chaosChaos Orb
하아룽#7164 listed 3 days ago
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
MoistKoalaBalls#3504 listed a day ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 96380 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
20×chaosChaos Orb
하아룽#7164 listed 3 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 6460 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
DoubleXypMa#0542 listed 17 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 42640 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
20×chaosChaos Orb
하아룽#7164 listed 3 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 128320 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
DoubleXypMa#0542 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 118280 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
MegaJigitExploiter#2478 listed 17 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 70800 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
DoubleXypMa#0542 listed 2 days ago
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
lvjiale#7939 listed a day ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 29900 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
20×chaosChaos Orb
CtenawaReturn#6784 listed 2 days ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 138440 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
20×chaosChaos Orb
하아룽#7164 listed 3 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 33840 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
BaronChen#3795 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 152020 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
20×chaosChaos Orb
CtenawaReturn#6784 listed 2 days ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 80
Commissioned 8740 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
Morfs#4165 listed a day ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 15240 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
20×chaosChaos Orb
KonqweCrew#3836 listed a day ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 108820 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
BladSols#6362 listed 6 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 37240 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
20×chaosChaos Orb
CtenawaReturn#6784 listed 20 hours ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 93200 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
20×chaosChaos Orb
CtenawaReturn#6784 listed 2 days ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 136640 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
DoubleXypMa#0542 listed 4 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 157760 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
DoubleXypMa#0542 listed 17 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 31580 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
DoubleXypMa#0542 listed 19 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 26160 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
DoubleXypMa#0542 listed 2 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 95020 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
20×chaosChaos Orb
하아룽#7164 listed 3 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 45480 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
20×chaosChaos Orb
CtenawaReturn#6784 listed 2 days ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 39640 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
DoubleXypMa#0542 listed 16 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 73020 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
20×chaosChaos Orb
CtenawaReturn#6784 listed 2 days ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 138480 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
20×chaosChaos Orb
하아룽#7164 listed 3 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 133980 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
DoubleXypMa#0542 listed 4 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 14680 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
DoubleXypMa#0542 listed 16 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 154600 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
DoubleXypMa#0542 listed 17 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 98280 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
20×chaosChaos Orb
CtenawaReturn#6784 listed 2 days ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 58600 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
Môjoman85#7205 listed 16 hours ago
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
Falko#2616 listed 2 hours ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 117440 coins to commemorate Cadiro
Passives in radius are Conquered by the Eternal Empire
Historic
Exact Price:
20×chaosChaos Orb
asdasdasdasdf#2831 listed 4 days ago
Online
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 11060 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
20×chaosChaos Orb
CtenawaReturn#6784 listed 2 days ago
AFK
Verified
Elegant Hubris
Timeless Jewel
Limited to: 1 Historic
Radius: Large
Item Level: 84
Commissioned 10660 coins to commemorate Victario
Passives in radius are Conquered by the Eternal Empire
Historic
Asking Price:
20×chaosChaos Orb
하아룽#7164 listed 3 days ago
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
for i in range(2000, 160000, 20):
    entry = [str(i) + ' Victario','200 chaosChaos Orb']
    # trade_list.append(entry)
    

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


# sockets = 60735 61834 61419
socket = 60735
# socket = 61834
# socket = 61419

# page_url = 'https://vilsol.github.io/timeless-jewels/tree?jewel=5&conqueror=Victario&seed=10000&location=60735&mode=seed'
page_url = f'https://vilsol.github.io/timeless-jewels/tree?jewel=5&conqueror=Victario&seed=10000&location={socket}&mode=seed'

# start_browser = True
# start_browser = False
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

        # print(mods)
    # counter += 1
    # if counter > 2:
    #     break

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
    















