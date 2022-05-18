from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

USERNAME = '383218438@qq.com'
PASS = 'Zrz1988412'
TARGET_ACCOUNT = ''


class InstaFollower:

    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def login(self):
        self.driver.get('https://www.instagram.com')
        time.sleep(3)
        user_name = self.driver.find_element(By.CSS_SELECTOR, '#loginForm > div > div:nth-child(1) > div > label > input')
        user_name.send_keys(USERNAME)
        pass_word = self.driver.find_element(By.CSS_SELECTOR, '#loginForm > div > div:nth-child(2) > div > label > input')
        pass_word.send_keys(PASS)
        log_in_button = self.driver.find_element(By.CSS_SELECTOR, '#loginForm > div > div:nth-child(3) > button > div')
        log_in_button.click()
        time.sleep(3)
        not_now_button = self.driver.find_element(By.CSS_SELECTOR,
                                             '#react-root > section > main > div > div > div > div > button')
        not_now_button.click()
        time.sleep(3)
        not_now_button_2 = self.driver.find_element(By.CSS_SELECTOR,
                                               'body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm')
        not_now_button_2.click()
        time.sleep(3)

    def find_followers(self):
        pass

    def follow(self):
        pass


# Instagram detected my unusual login attempt, mission abort.
