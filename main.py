import requests
from datetime import datetime

USERNAME = 'telepuz'
TOKEN = 'y4s0sub1bu'
GRAPH_ID = 'kachalka'
pixela_endpoint = 'https://pixe.la/v1/users'

# https://pixe.la/v1/users/telepuz/graphs/kachalka.html

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}
# 1. Сперва создали

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)


# 2. Задали вид

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'
graph_config = {
    'id': GRAPH_ID,
    'name': 'Fights',
    'unit': 'Times',
    'type': 'int',
    'color': 'ajisai'
}
headers = {
    'X-USER-TOKEN': TOKEN
}
response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response)


# 3. Вводим данные

pixel_creation_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}'

today = datetime.now()
print(today.strftime('%Y%m%d'))

pixel_data = {
    'date': today.strftime('%Y%m%d'),
    'quantity': input("Skol`ko jal? "),
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)


update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    'quantity': '6'
}

response = requests.put(url=f'{pixel_creation_endpoint}/20210603', json=new_pixel_data, headers=headers)
print(response.text)