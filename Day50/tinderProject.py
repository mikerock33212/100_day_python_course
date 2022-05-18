from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import time

# project skipped because I have no overseas mobile phone to get verification message

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = 'mikezhaorunze@gmail.com'
TWITTER_PASS = 'Zrz1409197#'


class InternetSpeedTwitterBot:

    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.cn/')
        test_button = self.driver.find_element(By.CSS_SELECTOR, '#app > section > div.speed-home-warp > '
                                                  'div.speed-home-content > div.speedtest-warp > '
                                                  'div.start-circle > p')
        test_button.click()
        time.sleep(45)
        down_speed = self.driver.find_element(By.CSS_SELECTOR, '#app > section > div.speed-home-warp > '
                                                              'div.speed-home-content > '
                                                              'div.speedtest-warp.speedtest-end-warp > '
                                                              'div.speedtest-run.speed-end-wrap.add-speed-warp > '
                                                              'div.speed-run-warp.speed-run-warp-border > '
                                                              'div.transfer-warp > '
                                                              'div.transfer-item.transfer-item-down > '
                                                              'a > dl > dd').text
        self.down = float(down_speed)
        up_speed = self.driver.find_element(By.CSS_SELECTOR, '#app > section > div.speed-home-warp > '
                                                             'div.speed-home-content > '
                                                             'div.speedtest-warp.speedtest-end-warp > '
                                                             'div.speedtest-run.speed-end-wrap.add-speed-warp > '
                                                             'div.speed-run-warp.speed-run-warp-border > '
                                                             'div.transfer-warp > '
                                                             'div.transfer-item.transfer-item-up > a > dl > dd').text
        self.up = float(up_speed)

    def tweet(self):
        self.driver.get('https://twitter.com/i/flow/login')
        time.sleep(10)
        # wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div/div[5]/label/div/div[2]/div/input'))).click()
        email = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div/div[5]/label/div/div[2]/div/input')
        email.send_keys(TWITTER_EMAIL)


bot = InternetSpeedTwitterBot()
# bot.get_internet_speed()
bot.tweet()


