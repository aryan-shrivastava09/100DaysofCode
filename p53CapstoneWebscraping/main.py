from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import requests
import lxml
from pprint import pprint


zillow_url = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.69219435644531%2C%22east%22%3A-122.17446364355469%2C%22south%22%3A37.703343724016136%2C%22north%22%3A37.847169233586946%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
    "Accept-Language":"en-US,en;q=0.9",
}



content = requests.get(url = zillow_url, headers = headers).text
soup = BeautifulSoup(content, 'html.parser')
pprint(soup)
lists = soup.find("ul", class_ = "photo-cards photo-cards_wow photo-cards_short")
houses = lists.find_all("div", class_ = "list-card-info")
print(len(houses))
listings = {}

for i in range(0,len(houses)):
    house = houses[i]
    address = house.find("address", class_ = "list-card-addr").getText()
    link = house.find("a").get("href")
    if link[0] != 'h':
        link = "https://www.zillow.com" + link
    price = house.find("div", class_ = "list-card-price").getText()
    listings[i] = {"Address": address, "Link": link, "Price" : price}
    
forms_url = "https://forms.gle/aDn9j9QMeZrr6m7b7"
chromedriver = "c:/Development/chromedriver"
driver = webdriver.Chrome(executable_path= chromedriver)
driver.get(forms_url)
time.sleep(5)
for i in range(0,len(listings)):
    prop = listings[i]
    add = prop['Address']
    price = prop['Price']
    link = prop['Link']
    add_input = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    add_input.click()
    add_input.send_keys(add)
    price_input = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input.click()
    price_input.send_keys(price)
    link_input = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input.click()
    link_input.send_keys(link)
    submit = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div')
    submit.click()
    time.sleep(2)
    another_response = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    another_response.click()
    time.sleep(4)

