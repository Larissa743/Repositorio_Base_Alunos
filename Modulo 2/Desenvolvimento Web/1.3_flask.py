# exercício 1.3: parametros na url (rotas dinamicas)
# crie uma rota /saudacao/<nome> que retorne "Olá, <nome>! Seja bem-vindo!"

from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Olá, Mundo!"

@app.route('/sobre')
def sobre():
    return 'Olá, meu nome é Larissa e sou uma escritora.'

@app.route('/saudacao<nome>')
def saudacao(nome):
    return f'Olá {nome}! Seja bem-vindo(a)!'

if __name__ == '__main__':
    app.run(debug=True)