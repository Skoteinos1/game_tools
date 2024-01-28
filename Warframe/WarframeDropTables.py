'''
get_data() - scraps website for reward list
find_locations('XXXX') - prints list of levels with highest chance of getting desired reward
mission_rewards('Jupiter/Callisto') - Prints list of rewards for selected mission
'''

# exec(open("WarframeDropTables.txt").read())
from urllib.request import urlopen as uReq
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as soup

main_path = '/PATH/TO/FOLDER/'

def get_data():
    driver = webdriver.Firefox()
    driver.get('https://n8k6e2y6.ssl.hwcdn.net/repos/hnfvc0o3jnfvc873njb03enrf56.html')
    driver.implicitly_wait(30)

    page_html = driver.page_source
    page_soup = soup(page_html, "html.parser")

    # f = open('skuska.html', 'w')
    # f.write(str(page_soup))

    containers = page_soup.findAll("table")

    data = ''
    i = 0
    for container in containers:
        if i > 1:
            continue
        i += 1
        n1 = False
        lines = container.findAll("tr")
        for line in lines:
            cells = line.findAll("td")
            headers = line.findAll("th")
            if len(cells) == 2:
                c0 = cells[0].text
                c0 = c0.replace(",", "0")
                data += nadpis1 + nadpis2 + c0 + ',' + cells[1].text + ',\n'
            elif len(cells) == 1:
                nadpis1 = ''
                nadpis2 = ','
                n1 = False
            elif len(headers) == 1:
                if not n1:
                    nadpis1 = headers[0].text + ','
                    n1 = True
                else:
                    nadpis2 = headers[0].text + ','

    f = open(main_path + 'WF D Tables.csv', 'w')
    f.write(data)
    f.close()


def find_locations(s=''):
    data = []
    data2 = []
    data3 = []
    with open(main_path + 'WF D Tables.csv', 'r') as file:
        data += file.readlines()

    for row in data:
        if 'Event:' in row:
            continue
        row2 = row.split(',')
        if s in row2[2]:
            num = row2[3].split(' (')[1]
            num = float(num[:-2])
            rel1 = row2[0].split(' (')[0]
            rel2 = row2[0].split(' (')[1][:-1]
            new_row = [row2[2], num, rel1, rel2]
            test = False
            try:
                if data2[-1][0] == new_row[0]:
                    if data2[-1][1] < new_row[1]:
                        data2[-1] = new_row
                else:
                    data2.append(new_row)
            except:
                data2.append(new_row)

    # relic_list = ['Axi', ]
    # relic_list = []
    for rw in data2:
        relic_list.extend([rw[2]])
    for rw in data2:
        print(rw)
    print('')

    for row in data:
        if 'Event:' in row:
            continue
        row2 = row.split(',')
        num = row2[3].split(' (')[1]
        num = float(num[:-2])
        row2[3] = num
        if any(rel in row2[2] for rel in relic_list):
            new_row = row2[:-1]
            data3.append(new_row)

    planet_list = []
    pla_list = []
    for row in data3:
        # pla_list.append(row[0])
        # if 'Rotation A' in row:
        pla_list.append(row[0])
        new_row = [row[0], 0, 0, 0, 0]
        if new_row not in planet_list:
            planet_list.append(new_row)

    for row in data3:
        if any(pla in row[0] for pla in pla_list):
            for i in range(len(planet_list)):
                pl = planet_list[i]
                if row[0] == pl[0]:
                    if 'Rotation A' in row:
                        pl[1] += row[3]
                        x = 4 * row[3]
                    elif 'Rotation B' in row:
                        pl[2] += row[3]
                        x = 0 * row[3]
                    elif 'Rotation C' in row:
                        pl[3] += row[3]
                        x = 0.5 * row[3]
                    else:
                        pl[1] += row[3]
                        x = 8 * row[3]
                    pl[4] += x

    pla_list = []
    planet_list = sorted(planet_list, key=lambda x2: x2[4])
    for i in range(1, 16):
        # print(planet_list[-i])
        try:
            pla_list.append(planet_list[-i][0])
        except:
            pass

    for pla in pla_list:
        for row in data3:
            if pla in row[0]:
                if any(rel in row[2] for rel in relic_list):
                    print(row)


def mission_rewards(s):
    data = []
    data2 = []
    data3 = []
    with open(main_path + 'WF D Tables.csv', 'r') as file:
        data += file.readlines()

    for row in data:
        if 'Event:' in row:
            continue
        row2 = row.split(',')
        if s in row2[0]:
            num = row2[3].split(' (')[1]
            num = float(num[:-2])
            rel1 = row2[0].split(' (')[0]
            rel2 = row2[0].split(' (')[1][:-1]
            new_row = [row2[1], row2[2], num, rel1, rel2]
            print(new_row)


relic_list = ['Axi W1 Relic', 'Meso I1 Relic',  # Inaros
              'Axi B4 Relic',  # Karyst
              ]
# get_data()
find_locations('aaa')
# mission_rewards('Jupiter/Callisto')
