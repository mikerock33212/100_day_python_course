from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('https://www.linkedin.com/login')

email = driver.find_element(By.CSS_SELECTOR, '#username')
email.send_keys('mikezhaorunze@gmail.com')

password = driver.find_element(By.CSS_SELECTOR, '#password')
password.send_keys('zrz1409197')

agree = driver.find_element(By.CSS_SELECTOR, '#organic-div > form > div.login__form_action_container > button')
agree.click()

time.sleep(1)

job = driver.find_element(By.CSS_SELECTOR, '#ember19')
job.click()

time.sleep(1)
driver_2 = driver.get('https://www.linkedin.com/jobs/shenzhen-jobs-worldwide/?geoId=92000000')

job_found = driver.find_element(By.CSS_SELECTOR, '#ember877')
job_found.click()


# first_name = driver.find_element(By.CSS_SELECTOR, '#first-name')
# first_name.send_keys('Runze')
# last_name = driver.find_element(By.CSS_SELECTOR, '#last-name')
# last_name.send_keys('Zhao')
#
# continue_ = driver.find_element(By.CSS_SELECTOR, '#join-form-submit')
# continue_.click()
#
# time.sleep(3)