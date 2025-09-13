import json
dados = {
    "nome":"Maria",
    "idade":30,
    "cursos":["Python", "Machine Learning"]
}

with open('dados.json', 'w', encoding='utf-8') as arquivo:
    json.dump(dados, arquivo, indent=4, ensure_ascii=False)