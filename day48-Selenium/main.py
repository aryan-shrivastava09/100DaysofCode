from selenium import webdriver

chrome_webdriver_path = "C:/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_webdriver_path)
# driver.get("https://www.flipkart.com/realme-buds-q-bluetooth-headset/p/itm2a9c125711e36?gclid=CjwKCAjwxuuCBhATEiwAIIIz0evRBh-aQFaG4rZauQoMyEDK0e7RruyJQFSH73s8b6sobJo3d6ZzJhoCJ4oQAvD_BwE&pid=ACCFVWN4PGNTEFGY&lid=LSTACCFVWN4PGNTEFGYNDRHV5&marketplace=FLIPKART&cmpid=content_headphone_840394530_g_8965229628_gmc_pla&tgi=sem,1,G,11214002,g,search,,472199938969,,,,c,,,,,,,&ef_id=CjwKCAjwxuuCBhATEiwAIIIz0evRBh-aQFaG4rZauQoMyEDK0e7RruyJQFSH73s8b6sobJo3d6ZzJhoCJ4oQAvD_BwE:G:s&s_kwcid=AL!739!3!472199938969!!!g!1039855654517!&gclsrc=aw.ds")
# price = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div[4]/div[1]/div/div[1]')
# print(price.text)
# # driver.close()
# # driver.quit()
driver.get(url = "https://www.python.org/")
Upcomin_events = driver.find_element_by_xpath('//*[@id="content"]/div/section/div[3]/div[2]/div/ul')
content = Upcomin_events.text
events = content.split("\n")
# print(events)
dates = [events[i] for i in range(0,len(events),2)]
# print(dates)
events = [events[i] for  i in range(1,len(events), 2)]
# print(events)
dic = {i : [f"time: {dates[i]}, event: {events[i]}"] for i in range(0,len(dates))}
print(dic)