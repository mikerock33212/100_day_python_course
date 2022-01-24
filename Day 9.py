# Grading program - dictionary
# student_scores = {
#   "Harry": 81,
#   "Ron": 78,
#   "Hermione": 99,
#   "Draco": 74,
#   "Neville": 62,
# }
#
# for stu in student_scores:
#     if student_scores[stu] >= 91 and student_scores[stu] <= 100:
#         student_scores[stu] = 'Outstanding'
#     elif student_scores[stu] >= 81 and student_scores[stu] <= 90:
#         student_scores[stu] = 'Exceeds Expectations'
#     elif student_scores[stu] >= 71 and student_scores[stu] <= 80:
#         student_scores[stu] = 'Acceptable'
#     else:
#         student_scores[stu] = 'Fail'
# print(student_scores)

# travel_log = [
#     {
#         "country": "France",
#         "visits": 12,
#         "cities": ["Paris", "Lille", "Dijon"]
#     },
#     {
#         "country": "Germany",
#         "visits": 5,
#         "cities": ["Berlin", "Hamburg", "Stuttgart"]
#     },
# ]
#
#
# def add_new_country(country, visited_times, cities):
#     """add a new country, times, and city to the existing data"""
#     return travel_log.append({'country': country, 'visits': visited_times, 'cities': cities})
#
#
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)

# Auction bidder game
from art import logo

# print(logo)
# final_bidder_info = {}
# flag = True
# counter = 0
# final_name = ''

# def bidding(name, bid):
#     """store the bidding info"""
#     final_bidder_info[name] = bid
#     return final_bidder_info
#
#
# while flag:
#     start_auction = input('Do you want to start auction?\n')
#     if start_auction == 'yes' or start_auction == 'y':
#         name = input('Please enter your name.\n')
#         bid = int(input('What is your bid? $\n'))
#         bidding(name=name, bid=bid)
#         another_bidder = input('Is there any other bidder wants to join?\n')
#         while another_bidder == 'yes' or another_bidder == 'y':
#             name = input('Please enter your name.\n')
#             bid = int(input('What is your bid? $\n'))
#             bidding(name=name, bid=bid)
#             another_bidder = input('Is there any other bidder wants to join?\n')
#         for key in final_bidder_info:
#             if counter < final_bidder_info[key]:
#                 counter = final_bidder_info[key]
#                 final_name = key
#         print(f'{final_name} has won the auction for {counter}!')
#         flag = False

# solution 2

print(logo)

bids = {}
bidding_done = False


def find_highest_bidder(bidding_record):
    """find the highest bidder from dictionary given or list given"""
    highest = 0
    winner = ''
    for bidder in bidding_record:
        if highest < bidding_record[bidder]:
            highest = bidding_record[bidder]
            winner = bidder
    print(f'The winner is {winner} with a bid of ${highest}.')


while not bidding_done:
    name = input('What is your name? ')
    price = int(input('What is your bid? $'))
    bids[name] = price
    should_continue = input('Are there any other bidders? Type yes or y, no or n. ')
    if should_continue == 'no' or should_continue == 'n':
        bidding_done = True
        find_highest_bidder(bids)

