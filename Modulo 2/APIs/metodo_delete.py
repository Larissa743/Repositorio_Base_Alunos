# método DELETE (excluir)

import requests

url = "https://jsonplaceholder.typicode.com/posts/10"

response = requests.delete(url)

print("Status Code:", response.status_code)
print("Resposta da API:", response.text) # retorno deve ser vazio
