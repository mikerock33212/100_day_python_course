# with open('weather_data.csv', mode='r') as f:
#     data = f.readlines()
#     clean_list = [line.strip() for line in data]
# print(clean_list)

# import csv
#
# with open('weather_data.csv', 'r') as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         temperature.append(row[1])
# temperature.pop(0)
# temperature = [int(i) for i in temperature]
# print(temperature)

import pandas as pd

# data = pd.read_csv('weather_data.csv')

# print(data['temp'].to_list())
# print(sum(data['temp']) / len(data['temp']))
# print(data['temp'].mean())
# print(data['temp'].max())
# print(data['temp'].min())
# print(data['temp'].quantile(.95))

# get data from columns
# print(data['condition'])
# print(data.condition)

# get data in a row
# print(data[data['day'] == 'Monday'])
# print(data[data.temp == data.temp.max()])
# monday = data[data.day == 'Monday']
# print(monday.temp * (9/5) + 32)

# create a dataframe from scratch
# data_dict = {
#     'students': ['Amy', 'James', 'Angela'],
#     'scores': [75, 86, 93]
# }
# convert from dic to data frame
# data_1 = pd.DataFrame(data_dict)

# convert data frame to csv and create a new csv file
# data_1.to_csv('new_csv.csv')
# print(data_1)

# data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
#
# new_data = data['Primary Fur Color']
#
# gray_squirrel_num = len(data[data['Primary Fur Color'] == 'Gray'])
#
# cinnamon_squirrel_num = len(data[data['Primary Fur Color'] == 'Cinnamon'])
#
# black_squirrel_num = len(data[data['Primary Fur Color'] == 'Black'])
#
# data_dict = {
#     'Fur Color': ['Gray', 'Cinnamon', 'Black'],
#     'Count': [gray_squirrel_num, cinnamon_squirrel_num, black_squirrel_num]
# }
#
# result = pd.DataFrame(data_dict)
#
# result.to_csv('squirrels_count.csv')




