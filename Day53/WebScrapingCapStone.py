from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import requests
import lxml
import re

FORM_LINK = 'https://docs.google.com/' \
            'forms/d/e/1FAIpQLSfjQ0NK1DBiRAN5tkBKG1uH2cIBo4DS2XiCAcD98qpaYzfa1A/' \
            'viewform?usp=sf_link'

custom_headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/'
              'avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36'
}

# site_contents = requests.get('https://www.zillow.com/homes/for_rent/1-_beds/'
#                              '?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%'
#                              '3A%7B%22west%22%3A-122.71142043066406%2C%22east%22%'
#                              '3A-122.15523756933594%2C%22south%22%3A37.56930783911232%2C%'
#                              '22north%22%3A37.980702760442185%7D%2C%22mapZoom%22%3A11%2C%'
#                              '22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%'
#                              '22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%'
#                              '22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%'
#                              '22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%'
#                              '22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%'
#                              '3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%'
#                              '22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%'
#                              '3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D', headers=custom_headers).text

# with open('local_html.txt', 'w') as file:
#     file.write(site_contents)


# Important!
# Due to Zillow's updated page layout, BeautifulSoup is no longer suitable for scrapping all desired information.
# Further techniques maybe required, for example, regex or other text parsing techniques.
# All the information are live inside of script section
# However it's a giant json object, keys for same information maybe entirely different for each item.
# Other methods are required to generate a final complete solution.
# Therefore in this task we only go for partial solution(BS4 + Selenium) for demo purposes.

# -------

with open('local_html.txt', 'r') as file:
    content = file.read()
    html_file = content

soup = BeautifulSoup(html_file, 'lxml')

all_links = soup.select('li .list-card-info a')
# all_links = soup.find_all(name='a', class_='list-card-info')

links_list = []
for link in all_links:
    links_list.append(link.get('href'))

for i in range(len(links_list)):
    if links_list[i][0:5] != 'https':
        links_list[i] = 'https://www.zillow.com' + links_list[i]

prices = soup.find_all(name='div', class_='list-card-price')
all_prices = []
for pri in prices:
    string_to_be_matched = pri.text
    pattern = re.compile(r'[\d]*[.,][\d]*')
    all_prices.append(pattern.findall(string_to_be_matched))

final_prices = []
for i in all_prices:
    i[0] = int(i[0].replace(',', ''))
    final_prices.append(i[0])

address = soup.select('div .list-card-info .list-card-addr')
all_address = []
for add in address:
    all_address.append(add.text)

# print(all_address)
# print(final_prices)
# print(links_list)

# Below are the selenium for web automation

if len(all_address) == len(final_prices) == len(links_list):

    index_counter = 0
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(FORM_LINK)

    while index_counter < len(all_address):
        time.sleep(5)

        add_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')

        add_input.send_keys(all_address[index_counter])

        price_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')

        price_input.send_keys(final_prices[index_counter])

        link_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')

        link_input.send_keys(links_list[index_counter])

        index_counter += 1

        submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
        submit_button.click()

        another_one = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
        another_one.click()


# other_links = soup.find_all(name='script')
#
# for i in other_links:
#     print(i.getText)



