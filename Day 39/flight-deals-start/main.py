#This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.

import requests

res = requests.get('https://api.sheety.co/a1a6faefceb46d70799d83f6073350ce/copyOfFlightDeals/prices')
price = res.json()['prices']

places = []
for place in price:
    places.append(place['city'])

# -----

kiwi_apikey = 'gfcfU816CK58kRWzHyYikMt4pt2srIsR'
kiwi_endpoint = 'https://tequila-api.kiwi.com/locations/query'
IATA_list = []
for item in places:
    kiwi_param = {
        'term': item,
        'locale': 'en-US',
        'location_types': 'airport',
        'limit': 10,
        'active_only': True,
    }
    header = {
        'Accept': 'application/json',
        'apikey': kiwi_apikey
    }

    kiwi_res = requests.get(kiwi_endpoint, kiwi_param, headers=header).json()['locations']
    iata_code = kiwi_res[0]['code']
    IATA_list.append(iata_code)

id_num = 2
for code in IATA_list:
    sheety_post_endpoint = f'https://api.sheety.co/a1a6faefceb46d70799d83f6073350ce/' \
                           f'copyOfFlightDeals/prices/{str(id_num)}'
    sheet_content = {'price':
        {
        "iataCode": code,
        }
    }
    res_3 = requests.put(sheety_post_endpoint, json=sheet_content)
    id_num += 1

