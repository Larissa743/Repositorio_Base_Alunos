# exercicio 1.2: rota personalizada
# adicione uma nova rota '/sobre' que retorna uma mensagem com seu nome
# e uma frase sobre você

from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Olá, Mundo!"

@app.route('/sobre')
def sobre():
    return 'Olá, meu nome é Larissa e sou uma escritora.'

if __name__ == '__main__':
    app.run(debug=True)
