# exercício 1.1: hello flask
# criar um app flask que exibe "olá, mundo!" na rota principal('/)

from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Olá, Mundo!"


if __name__ == '__main__':
    app.run(debug=True)

