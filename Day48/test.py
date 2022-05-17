id_ = 'buyCursor'
affordable_dict = {105: 'buyCursor', 100: 'buyGrandma',
                    500: 'buyFactory', 8000: 'buyMine',
                    7000: 'buyShipment', 50000: 'buyAlchemy lab',
                    1000000: 'buyPortal', 123456789: 'buyTime machine'
                   }

temp_dic = list(affordable_dict)
# for i in range(len(list(affordable_dict)) - 1):
#     if list(affordable_dict)[i] >= list(affordable_dict)[i + 1]:
#         temp_dic = affordable_dict
#         # list(affordable_dict).pop(list(affordable_dict)[i])
#         temp_dic.pop(105)

results = []
for i in range(len(temp_dic) - 1):
    print(temp_dic[i], temp_dic[i + 1])
    if temp_dic[i] >= temp_dic[i + 1]:
        results.append(temp_dic[i])
for y in results:
    affordable_dict.pop(y)
print(affordable_dict)


