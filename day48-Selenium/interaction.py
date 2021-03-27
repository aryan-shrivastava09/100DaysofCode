from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

chrome_webdriver_path = "C:/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_webdriver_path)

driver.get("http://www.createafreewebsite.net/html_forms.html")
fname = driver.find_element_by_name("firstname")
fname.send_keys("Aryan")
lname = driver.find_element_by_name("lastname")
lname.send_keys("Srivastava")
street = driver.find_element_by_name("street")
street.send_keys("djkfhkshfash")
city = driver.find_element_by_name("city")
street.send_keys("agra")
zip = driver.find_element_by_name("zip")
zip.send_keys("12345")
state = Select(driver.find_element_by_name("state"))
state.select_by_visible_text("FL")
button = driver.find_element_by_xpath('/html/body/div/form/pre/input[8]')
button.send_keys(Keys.ENTER)

