from random import randint
# print(random.randint(0,3))
#
# a = [
#     {'1': 1},
#     {'2': 2}
# ]
#
# print(len(a))
#
# cardset = [{'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}]
# print((cardset[0]['A']))
card_set = []
# build the deck first


def create_cards():
    """create sets of cards"""
    points = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    pattern = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    cards = {}
    for index in range(len(points)):
        cards[pattern[index]] = points[index]
    return cards


def pop_key(dictionary_set):
    """pop remaining key from deck cardset"""
    tem_lst = []
    for key in dictionary_set:
        tem_lst.append(key)
    ram_index = randint(0, len(tem_lst) - 1)
    return tem_lst[ram_index]


def deal_cards():
    """deal cards from deck, remove cards afterwards"""
    random_set = randint(0, len(card_set)-1)
    temp_key = pop_key(card_set[random_set])
    temp_card_value = card_set[random_set][temp_key]
    card_set[random_set].pop(temp_key)
    return temp_key, temp_card_value


card_set_num = (input('Please select how many set of cards you want to play, default is 1: '))
while not card_set_num.isnumeric():
    card_set_num = (input('Please enter a valid number! '))
if int(card_set_num) > 0:
    for i in range(int(card_set_num)):
        card_set.append(create_cards())

aaa = []
aaa.append(deal_cards())
aaa.append(deal_cards())
print(card_set)
print(aaa)
print(aaa[0][1], aaa[1][1])