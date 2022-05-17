from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# driver.get('https://www.walmart.com/ip/Beef-Choice-Angus-New-York-Strip-Steak-0-82-1-57-lb/39944456')
#
# price = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div/div/div/div/section/main/div/div[2]/div/div[1]/div/div/div[1]/div/div/div[2]/div/div/div[1]/span[1]/span[2]')
# print(price.text)
#

driver.get('https://www.python.org/')
date_ = driver.find_elements(By.CSS_SELECTOR, '#content > div > section > div.list-widgets.row > div.medium-widget.event-widget.last > div > ul > li > time')
time_ = []
for i in date_:
    time_.append(i.get_attribute('datetime').split('T')[0])

events = driver.find_elements(By.CSS_SELECTOR, '#content > div > section > div.list-widgets.row > div.medium-widget.event-widget.last > div > ul > li > a')
events_ = []
for y in events:
    events_.append(y.text)

Events_on_python_org = {}
if len(time_) == len(events_):
    for i in range(len(events_)):
        Events_on_python_org[i] = {time_[i]: events_[i]}
print(Events_on_python_org)

# price.get_attribute()

# driver.close() # close tab
driver.quit()



# driver_path = '/Users/zhaorunze/Desktop/pythonProject/chromedriver'
# driver = webdriver.Chrome(service=)


