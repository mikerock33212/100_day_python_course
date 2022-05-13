from bs4 import BeautifulSoup
import requests
import lxml

website = requests.get('https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/')
html_text = website.text

soup = BeautifulSoup(html_text, 'lxml')

movies = soup.find_all(name='h3', class_='title')

movie_list = []
for mov in movies[::-1]:
    movie_list.append(mov.getText())

with open('movie ranking.txt', 'w') as file:
    for movie in movie_list:
        file.write(movie + '\n')

