from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('http://orteil.dashnet.org/experiments/cookie/')

cookie = driver.find_element(By.ID, 'cookie')

# money = (driver.find_element(By.ID, 'money'))


items = driver.find_elements(By.CSS_SELECTOR, '#store div')
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 2
five_min = time.time() + 60 * 5

while True:
    cookie.click()

    if time.time() > timeout:
        # update items spending part
        all_prices = driver.find_elements(By.CSS_SELECTOR, '#store b')
        item_prices = []
        for price in all_prices:
            temp_text = price.text
            if temp_text != '':
                cost = int(temp_text.split('-')[1].strip().replace(',', ''))
                item_prices.append(cost)

        # create a dictionary to store items and prices
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        # update money part
        money_element = driver.find_element(By.ID, "money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        # check upgrades that we can currently afford
        affordable_upgrades = {}
        for cost, id_ in cookie_upgrades.items():
            if cookie_count >= cost:
                affordable_upgrades[cost] = id_

        # Keep track of amount of any single item not to go above 20
        item_to_remove_id = []
        temporary_item_above_20 = []
        single_item_numbers = driver.find_elements(By.CSS_SELECTOR, '#store .amount')
        single_item_numbers_to_integer = [int(i.text) for i in single_item_numbers]
        for item_count in single_item_numbers_to_integer:
            if item_count >= 15:
                temporary_item_above_20.append(item_count)
        for t in range(len(temporary_item_above_20)):
            item_to_remove_id.append(item_ids[t])
        # we have a problem here because we cannot locate correct index for item go above 20
        # print(single_item_numbers_to_integer)
        # print(temporary_item_above_20)
        # print(item_to_remove_id)
        # check if any item price is greater than the following item, if it is, pop it
        item_to_be_popped = []
        for i in range(len(list(cookie_upgrades)) - 1):
            if list(cookie_upgrades)[i] >= list(cookie_upgrades)[i + 1]:
                item_to_be_popped.append(list(cookie_upgrades)[i])
        if item_to_be_popped:
            for ite in affordable_upgrades.copy():
                if affordable_upgrades[ite] in item_to_be_popped:
                    try:
                        affordable_upgrades.pop(ite)
                    except KeyError:
                        pass

        # remove item greater than 20 in affordable upgrades dictionary
        if item_to_remove_id:
            for keys in affordable_upgrades.copy():
                if affordable_upgrades[keys] in item_to_remove_id:
                    affordable_upgrades.pop(keys)

        # check if we can upgrade
        if affordable_upgrades:
            highest_affordable_upgrades = max(affordable_upgrades)
            to_purcahse_id = affordable_upgrades[highest_affordable_upgrades]
            driver.find_element(By.ID, to_purcahse_id).click()

        timeout = time.time() + 1
    # after 5 minutes we can stop and check our final results, cookie per second
    if time.time() > five_min:
        cookie_per_s = driver.find_element(By.ID, 'cps').text
        print(cookie_per_s)
        break


# def countdown():
#     time_sec = 300
#     while time_sec:
#         mins, secs = divmod(time_sec, 60)
#         time.sleep(1)
#         time_sec -= 1
#     return False


