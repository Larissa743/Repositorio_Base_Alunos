# criar código que consuma uma api de clima e informe
# a temperatura e a descição do clima em um lugar específico

# 1. definir chave da API e o link da requisição
import requests

cidade = input("Digite o nome da cidade: ").strip()
api_key = '2a1ac38a32354cb7b19133643251408'
url = f'https://api.weatherapi.com/v1/current.json'

# 2. parâmetros da requisição
parametros = {
    'key': api_key,
    'q':cidade,
    'lang':'pt' # define a lingua da resposta como português do Brasil
}

# 3. fazer a requisição
resposta = requests.get(url, params=parametros)

# 4. verificar se a requisição foi bem sucedida
if resposta.status_code == 200:
    dados = resposta.json()
    temperatura = dados['current']['temp_c']
    descricao = dados['current']['condition']['text']
    print(f'Temperatura na cidade {cidade} é {temperatura}°C.')
    print(f'Descrição: {descricao}')
else:
    print(f'Erro na requisição: {resposta.status_code}')
    print(resposta.content)