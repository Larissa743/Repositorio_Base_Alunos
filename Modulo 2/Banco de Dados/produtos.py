import sqlite3

produto = 'produtos.db'

script_produtos = '''CREATE TABLE IF NOT EXISTS Produtos(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    preco REAL NOT NULL,
                    categoria TEXT NOT NULL,
                    estoque INTEGER NOT NULL
                    );'''
try:
    with sqlite3.connect(produto) as con:
        cur = con.cursor()

        cur.execute(script_produtos)

        con.commit()
        print('Tabela criada com sucesso!')
except sqlite3.OperationalError as e:
    print('Erro:', e)

res= cur.execute('SELECT name FROM sqlite_master')
print(res.fetchall())