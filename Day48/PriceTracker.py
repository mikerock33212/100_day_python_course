import requests
from bs4 import BeautifulSoup
import lxml

url = 'https://www.walmart.com/ip/Beef-Choice-Angus-New-York-Strip-Steak-0-82-1-57-lb/39944456'
custom_headers = {'user-agent': 'Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
                  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                  'accept-language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
                  'dnt': '1',
                  'upgrade-insecure-requests': '1',
                  'sec-fetch-site': 'same-origin',
                  'sec-fetch-mode': 'navigate',
                  'sec-fetch-user': '?1',
                  'sec-fetch-dest': 'document',
                  'referer': 'https://www.amazon.com/'
                  }
content = requests.get(url, headers=custom_headers).content

soup = BeautifulSoup(content, 'lxml')

price = soup.find(name='span', itemprop='price')

final_price = []
for i in price:
    final_price.append(float(i.getText().split('$')[1]))
print(final_price)
