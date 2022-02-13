import pandas as pd

student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
# for (key, value) in student_dict.items():
#     print(key, value)

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    pass


# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
data = pd.read_csv('nato_phonetic_alphabet.csv')

data_dict = {code.letter: code.code for (letter, code) in data.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_input = input('Type your words: ').upper()
result = [data_dict[x] for x in user_input]
# for let in user_input:
#     result.append(data_dict[let])
print(result)
