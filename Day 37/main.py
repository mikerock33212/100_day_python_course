import requests
import datetime as dt

pixela_params = {
    'token': 'thatisasecretyayee',
    'username': 'runze',
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

pixela_endpoint = 'https://pixe.la/v1/users'

response = requests.post(url=pixela_endpoint, json=pixela_params)
# response.raise_for_status()
# print(response.text)

pixela_graph_params = {
    'id': 'test-graph',
    'name': 'runze',
    'unit': 'commit',
    'type': 'int',
    'color': 'ajisai',
    'timezone': 'Asia/Shanghai'
}

headers = {
    'X-USER-TOKEN': 'thatisasecretyayee'
}

create_graph_endpoint = 'https://pixe.la/v1/users/runze/graphs'

# res_2 = requests.post(url=create_graph_endpoint, json=pixela_graph_params, headers=headers)
# print(res_2.text)

now = dt.datetime.now()
today = now.strftime('%Y%m%d')

post_pixel = 'https://pixe.la/v1/users/runze/graphs/test-graph'
post_pixel_params = {
    'date': today,
    'quantity': '1',
}

# res_3 = requests.post(url=post_pixel, json=post_pixel_params, headers=headers)
# print(res_3.text)


update_pixel = 'https://pixe.la/v1/users/runze/graphs/test-graph/20220223'
update_pixel_params = {
    'quantity': '3',
}

res_4 = requests.put(url=update_pixel, json=update_pixel_params, headers=headers)
print(res_4.text)
