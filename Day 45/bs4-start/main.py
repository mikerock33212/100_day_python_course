from bs4 import BeautifulSoup
import requests
import re

content = requests.get('https://news.ycombinator.com')
yc_webpage = content.text

soup = BeautifulSoup(yc_webpage, 'lxml')

title = soup.find_all(name='a', class_='titlelink')

title_list = []
title_link = []
for ti in title:
    title_list.append(ti.getText())
    title_link.append(ti.get('href'))

for item in title_link:
    if item[0:4] != 'http':
        title_link.remove(item)

final_score = [int(score.getText().split()[0]) for score in soup.find_all(name='span', class_='score')]

# print(title_list, title_link, final_score)

max_index = final_score.index(max(final_score))
print(title_list[max_index])
print(title_link[max_index])
print(final_score[max_index])

# stuff = soup.find_all(class_='athing')


# for s in stuff:
#     print(s)





# with open('website.html', 'r') as file:
#     contents = file.read()
# soup = BeautifulSoup(contents, 'lxml')

# print(soup.title)
# print(soup.title.string)

# print(soup.prettify())

# all_a_tag = soup.find_all(name='a')
#
# for tag in all_a_tag:
#     print(tag)
#     print(tag.getText())
#     print(tag.get('href'))

# heading = soup.find(name='h1', id='name')
# print(heading)

# section_heading = soup.find(name='h3', class_='heading')
# print(section_heading.getText())

# h3_heading = soup.find_all(name='h3')
# print(h3_heading)

# company_url = soup.select_one(selector='p a')
# print(company_url.get('href'))

# name = soup.select_one(selector='#name')
# print(name)

# heading = soup.select(selector='.heading')
# print(heading)