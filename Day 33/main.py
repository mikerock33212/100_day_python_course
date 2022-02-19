import requests
import datetime as dt
#
# response = requests.get('http://api.open-notify.org/iss-now.json')
# response.raise_for_status()
#
# data = response.json()['iss_position']
# longitude = response.json()['iss_position']['longitude']
# latitude = response.json()['iss_position']['latitude']
#
# print(longitude, latitude)

parameters = {
    'lat': 51.507351,
    'lng': -0.127758,
    'formatted': 0
}

response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
data = response.json()
sunrise = data['results']['sunrise'].split('T')[1].split(':')[0]
sunset = data['results']['sunset'].split('T')[1].split(':')[0]

time_now = dt.datetime.now()

print(time_now.hour, sunrise, sunset)