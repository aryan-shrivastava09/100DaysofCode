from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
currenttime = time.time()
timeout = currenttime + 5*60
chrome_webdriver_path = "C:/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_webdriver_path)
url = "https://orteil.dashnet.org/experiments/cookie/"
driver.get(url)
cookie = driver.find_element_by_css_selector("#cookie")

def numberformatter(n):
    num = ""
    for i in n:
        if i!=",":
            num+=i
    return int(num)


bs = ['//*[@id="buyCursor"]/b', '//*[@id="buyGrandma"]/b', '//*[@id="buyFactory"]/b', '//*[@id="buyMine"]/b', '//*[@id="buyShipment"]/b', '//*[@id="buyAlchemy lab"]/b', '//*[@id="buyPortal"]/b', '//*[@id="buyTime machine"]/b' ]

while time.time() < timeout:
    cookie.click()
    if (time.time() - currenttime) >= 5:
        m = driver.find_element_by_css_selector("#money").text
        money = numberformatter(m)
        maxitempos = -1
        amounts = [numberformatter(driver.find_element_by_xpath(b).text.split(" - ")[1]) for b in bs]
        for i in range(0, len(amounts)):
            mindiff = 1000000
            if money > amounts[i]:
                if money - amounts[i] < mindiff:
                    mindiff = money- amounts[i]
                    maxitempos= i
        ids = ['//*[@id="buyCursor"]', '//*[@id="buyGrandma"]', '//*[@id="buyFactory"]', '//*[@id="buyMine"]', '//*[@id="buyShipment"]', '//*[@id="buyAlchemy lab"]', '//*[@id="buyPortal"]', '//*[@id="buyTime machine"]']
        upgrades = [driver.find_element_by_xpath(id) for id in ids]
        item = upgrades[maxitempos]
        item.click()
        currenttime = time.time()
cps = driver.find_element_by_xpath('//*[@id="cps"]')
print(cps.text)
