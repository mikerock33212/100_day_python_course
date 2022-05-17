from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# driver.get('https://en.wikipedia.org/wiki/Main_Page')

# article_num = driver.find_element(By.CSS_SELECTOR, '#articlecount > a:nth-child(1)')
# driver.implicitly_wait(2)
# print(article_num.text)
# article_num.click()

# community_portal = driver.find_element(By.LINK_TEXT, 'Community portal')
# community_portal.click()

# search_box = driver.find_element(By.NAME, 'search')
# search_box.send_keys('Python')
# search_box.send_keys(Keys.ENTER)



# driver.quit()

driver.get('http://secure-retreat-92358.herokuapp.com/')

first_name = driver.find_element(By.NAME, 'fName')
first_name.send_keys('Runze')

last_name = driver.find_element(By.NAME, 'lName')
last_name.send_keys('Zhao')

email_add = driver.find_element(By.NAME, 'email')
email_add.send_keys('mikezhaorunze@gmail.com')

time.sleep(2)

sign_up_button = driver.find_element(By.CSS_SELECTOR, 'body > form > button')
sign_up_button.click()

time.sleep(3)

driver.quit()
