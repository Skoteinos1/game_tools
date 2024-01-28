import glob
import os
from selenium import webdriver
from bs4 import BeautifulSoup as soup


def read_logs():
    """
    This code reads all .txt files in folder.
    Always copy files which you want to read to different location.
    You don't want python to accidentally delete or owerwrite original files.
    :return: list of gamelogs
    """
    path = 'Logs/'
    db = []
    usr = ''
    # Read All .txt files
    for filename in glob.glob(os.path.join(path, '*.txt')):
        with open(filename) as f:
            db += f.readlines()
    # Delete unwanted lines - everything what don't has '(combat)' in it
    # When you are going to delete items in list, always go through list from back. It will save you lot of headaches
    for i in range(len(db)-1, -1, -1):
        if '(combat)' not in db[i]:
            if 'Listener:' in db[i]:
                usr = db[i]
                # Ways to manipulate string
                usr = usr.replace('Listener:', '')  # This removes substring 'Listener:'
                usr = usr[:-1]  # This removes last character '\n' # new line
                usr = usr.strip()  # This removes spaces at front and back. It would also remove \n
            del db[i]
        else:
            # Probably there is way to edit string as xml...
            # In this code there is not much to do, so we fix it with few extra steps
            db[i] = db[i].replace('\n', '')
            db[i] = db[i].replace('[ ', '')
            db[i] = db[i].replace(' ]', '')
            db[i] = db[i].replace(' (combat) ', '|')  # I will use | as list separator later
            db[i] = db[i].replace('<b>', '')
            db[i] = db[i].replace('</b>', '')
            db[i] = db[i].replace('<u>', '')
            db[i] = db[i].replace('</u>', '')
            # these color codes probably mean something. Like Dmg to you, from you, warp scramble...
            # just put # in front of line and they will show up. If you want to play with it
            db[i] = db[i].replace('<color=0xffcc0000>', '')
            db[i] = db[i].replace('<color=0xffffffff>', '')
            db[i] = db[i].replace('<color=0xff00ffff>', '')
            db[i] = db[i].replace(' <color=0x77ffffff><font size=10>to</font> ', '|to|')
            db[i] = db[i].replace(' <color=0x77ffffff><font size=10>from</font> ', '|from|')
            db[i] = db[i].replace('<font size=10><color=0x77ffffff>', '')
            db[i] = db[i].replace(' <color=0x77ffffff><font size=10>to </font>', '|to|')
            db[i] = db[i].replace('<font size=12><color=0xFFFFB900> ', '')
            db[i] = db[i].replace('</color></font>', '|')
            db[i] = db[i].replace('<color=0xFFFFFFFF> -', '')
            db[i] = db[i].replace('<font size=12><color=0xFFFEFF6F>', '')
            db[i] = db[i].replace(' - ', '|')
            db[i] = db[i].split('|')
            try:
                # this tries to convert dmg 'string' to integer
                db[i][1] = int(db[i][1])
            except:
                # if there is error, like field is not number but text 'Angel Impaler misses...'
                # code ignores it and leaves is as it is
                pass
            # So there is one big problem.
            # db[i][0] is always time
            # db[i][1] is sometimes dmg, sometimes attack type, sometimes npc name
            # rows also have different length which will cause trouble later
    return db, usr


def read_website(page):
    # you will need selenium and chromedriver and chrome for this code to work
    # Most websites hate when you scrap them (against T&C). Problem is mostly because if you send to many commands
    # you can take down whole server. If you do your scraping at human speed, you should be fine, without them noticing.
    # Scrap at your own risk. And yes websites can detect if you are human or bot. And yes there are ways to hide that
    # bot is reading page.
    # There are lots of usefull videos on how to scrap websites. You can't test your code as usual. Use command-line
    driver = webdriver.Chrome()  # Use chrome
    driver.get(page)  # go to page
    driver.implicitly_wait(30)  # wait until page loads, max 30 seconds

    page_html = driver.page_source  # read html code
    page_soup = soup(page_html, "html.parser")  # transforms page_source to BeautifulSoup format

    # These guys really hate getting their data scraped, they rarely add class names, which will make your job harder
    body = page_soup.find("tbody")
    tables = body.findAll("table", {"class": "table-condensed"})
    player = tables[0].text
    player = player.strip()
    player = player.replace('\n\n', ' - ')
    print('Player:', player)
    trs = tables[1].findAll("tr")
    ship = trs[0].text
    ship = ship.replace('\n', '')
    print(ship)
    sys = trs[2].text
    sys = sys.replace('\n', '')
    print(sys)
    dmg = trs[6].text
    dmg = dmg.replace('\n', '')
    dmg = dmg.replace('Damage:', '')
    dmg = dmg.replace(',', '')
    dmg = int(dmg)
    print('Damage:', dmg)


def salvage_counter():
    path = 'Logs/'
    db = []
    usr = ''
    # Read All .txt files
    for filename in glob.glob(os.path.join(path, '*.txt')):
        with open(filename) as f:
            db += f.readlines()
        db.append('*******************')
    for i in range(len(db) - 1, -1, -1):
        foo = db[i]
        if '(notify)' not in db[i] and '***' not in db[i]:
            del db[i]
        elif 'successfully' not in db[i] and '***' not in db[i]:
            del db[i]
        elif 'successfully access' in db[i]:
            del db[i]
        else:
            # Probably there is way to edit string as xml...
            # In this code there is not much to do, so we fix it with few extra steps
            db[i] = db[i].replace('\n', '')
    count = 0
    for entry in db:
        if '***' in entry:
            print(count)
            count = 0
        else:
            count += 1
        print(entry)
    print(len(db))


opt = 2
if opt == 0:
    logs, user = read_logs()
    print(user)
    for log in logs:
        print(log)
elif opt == 1:
    read_website('https://zkillboard.com/kill/88268333/')
elif opt == 2:
    salvage_counter()
foo = input('press key')
