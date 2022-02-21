import requests
import os
from twilio.rest import Client

account_sid = 'AC1abf4f7653fa276be9e7597c78e22729'
auth_token = '925b16213e9f8c35e8b860f2faffa93e'
# os.environ.get('')
# use export to set up environment variable

api_keys = '9f20ee19d0cf5bc4134bda97e71b8264'
LAT = 22.56087085
LON = 113.94490240560009

weather_params = {
    'lat': LAT,
    'lon': LON,
    'appid': api_keys,
    'exclude': 'current,minutely,daily'
}

# response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={api_keys}')
# response_1 = requests.get(f'https://api.openweathermap.org/data/2.5/forecast/daily?lat
# ={LAT}&lon={LON}&cnt={2}&appid={api_keys}')

response_2 = requests.get('https://api.openweathermap.org/data/2.5/onecall?', weather_params)
response_2.raise_for_status()
data = response_2.json()
hourly_forecast = data['hourly'][0:12]

will_rain = False
for item in hourly_forecast:
    condition_code = int(item['weather'][0]['id'])
    if condition_code < 700:
        will_rain = True
if will_rain:
    print('Raining, bring an umbrella!')
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body=f'Raining, bring an umbrella!',
        from_='+19107084518',
        to='+8618516982583')
    print(message.status)


# Download the helper library from https://www.twilio.com/docs/python/install
# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
