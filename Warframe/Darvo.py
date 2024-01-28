# Simple code. It goes to website, gets the data, stores it in file

from selenium import webdriver
import datetime

MainPath = "\PATH\TO\FOLDER"

driver = webdriver.Firefox()

driver.get("http://deathsnacks.com/wf/index.html")
driver.implicitly_wait(30)

s = ""
s += driver.find_element_by_class_name("deal-name").text + "|"
s += driver.find_element_by_class_name("deal-discount").text + "|"
s += driver.find_element_by_class_name("deal-amount").text + "plat|"
s += driver.find_element_by_class_name("deal-inventory").text + "|"
s += str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")) + '\n'

print(s)

with open(MainPath + '\Darvo.txt', 'a') as file:
    file.write(s)

driver.delete_all_cookies()
driver.quit()
