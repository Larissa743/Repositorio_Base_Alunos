# exercício 1.4: rota com número (tipagem de rota)

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

@app.route('/dobro/<int:numero>')
def dobro(numero):
    return f'O dobro do {numero} é {2*numero}.'

if __name__ == '__main__':
    app.run(debug=True)