# file not found
#
# try:
#     file = open('a_file.txt')
#     dic = {'ddd': 'ggg'}
#     print(dic['ddd'])
# except FileNotFoundError:
#     file = open('a_file.txt', 'w')
#     file.write('something here')
# except KeyError as error_mes:
#     print(f'This is the error: {error_mes}')
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise KeyError
#     file.close()
#     print('File closed.')

# fruits = ["Apple", "Pear", "Orange"]
#
# #TODO: Catch the exception and make sure the code runs without crashing.
# def make_pie(index):
#     fruit = fruits[index]
#     print(fruit + " pie")
#
#
# try:
#     make_pie(3)
# except IndexError:
#     print('None')
# else:
#     print(fruit + " pie")
#

facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        # total_likes += 0
        pass


print(total_likes)