import urllib.request
import json

question_data = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
    {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
    {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home "
             "to eat.", "answer": "True"},
    {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state "
             "funeral.", "answer": "False"},
    {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
    {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
    {"text": "Google was originally called 'Backrub'.", "answer": "True"},
    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
    {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
    {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]



def generate_new_questions(existing_question_list, user_given_url):
    """append new questions into existing question list"""
    req = urllib.request.urlopen(user_given_url)
    res = json.loads(req.read().decode('utf-8'))
    temp_lst = []
    for i in res['results']:
        temp_dic = {'text': i['question'], 'answer': i['correct_answer']}
        temp_lst.append(temp_dic)
    for y in temp_lst:
        existing_question_list.append(y)
    return existing_question_list



print(generate_new_questions(question_data, 'https://opentdb.com/api.php?amount=45&type=boolean'))
