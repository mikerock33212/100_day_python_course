import requests
import datetime as dt

QUERY = input('Tell me what you have exercised today: ')
GENDER = 'male'
WEIGHT = 80.5
HEIGHT = 176
AGE = 34

nutrition_app_id = '56c2fcaf'
nutrition_app_keys = 'db4c2063077238703266e98ccb48b129'

headers = {
    'x-app-id': nutrition_app_id,
    'x-app-key': nutrition_app_keys,
    # 'x-remote-user-id': 0
}

params = {
    "query": QUERY,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
}

nutrition_exercise = 'https://trackapi.nutritionix.com/v2/natural/exercise'

res_1 = requests.post(nutrition_exercise, json=params, headers=headers)
exercise = res_1.json()['exercises'][0]
sports = exercise['user_input']
duration = exercise['duration_min']
calorie_burned = exercise['nf_calories']


date = dt.datetime.now().strftime('%d/%m/%Y')

hour = dt.datetime.now().hour
minute = dt.datetime.now().minute
time = (f'{hour}:{minute}:00')

USER_NAME = 'a1a6faefceb46d70799d83f6073350ce'
PROJECT = 'copyOfMyWorkouts'
SHEET = 'workouts'
sheety_endpoint = f'https://api.sheety.co/{USER_NAME}/{PROJECT}/{SHEET}'

# res_2 = requests.get(sheety_endpoint)

sheet_content = {'workout':
    {
    "date": date,
    "time": time,
    "exercise": sports.title(),
    "duration": duration,
    "calories": calorie_burned,
    }
}

auth_bearer_token = {'Authorization': 'Bearer 12312asfadfsadf'}

res_3 = requests.post(sheety_endpoint, json=sheet_content, headers=auth_bearer_token)
print(res_3.text)
