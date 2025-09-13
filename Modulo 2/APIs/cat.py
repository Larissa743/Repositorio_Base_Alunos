# api que apresenta curiosidades sobre os gatos

import requests

url ='https://catfact.ninja/fact'
response = requests.get(url)

print("Fatos sobre gatos:", response.json()['fact'])