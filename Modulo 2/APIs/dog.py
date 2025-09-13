# api que apresenta imagens aleatórias de cachorros
import requests
url = 'https://dog.ceo/api/breeds/image/random'

response = requests.get(url)

print("Link da imagem: ", response.json()["message"])