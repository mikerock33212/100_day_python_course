import requests
from bs4 import BeautifulSoup
import lxml
import re

Date = '2022-05-10'

website_content = requests.get(f'https://www.billboard.com/charts/hot-100/{Date}/').text

soup = BeautifulSoup(website_content, 'lxml')

current_week_ranking = soup.find_all(name='span', class_='c-label a-font-primary-bold-l u-font-size-32@tablet u-letter-spacing-0080@tablet')

rankings = []
for rank in current_week_ranking:
    rankings.append(int(rank.getText()))

song_title = soup.find_all(name='h3', class_='c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only', id='title-of-a-story')

title_of_song = []
for song in song_title:
    title_of_song.append(song.getText().strip("\t\n"))

first_song = soup.find_all(name='a', class_="c-title__link lrv-a-unstyle-link")
first_song_title = []
for i in first_song:
    first_song_title.append(i.getText().strip('\n\t'))

first_singer = soup.find_all(name='span', class_='c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only u-font-size-20@tablet')

champion = []
for i in first_singer:
    champion.append(i.getText().strip('\n\t'))

singers = soup.find_all(name='span', class_='c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only')

all_singers = []
for singer in singers:
    all_singers.append(singer.getText().strip('\n\t'))

all_singers.insert(0, champion[0])
title_of_song.insert(0, first_song_title[0])

final_playlist = {}
counter = 1
for i in range(100):
    final_playlist[counter] = [[title_of_song[i]], [all_singers[i]]]
    counter += 1
