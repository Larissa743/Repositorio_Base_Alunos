import requests

print("==Menu de Ações ==")
print("1- GET(buscar post)")
print("2- POST(criar post)")
print("3- PATCH(atualizar título)")
print("4- DELETE(apagar post)")

opcao = input("Escolha uma opção(1-4): ")

if opcao == "1":
    post_id= input("Digite o ID do post: ")
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    r= requests.get(url)
    print("Resposta:", r.json())
elif opcao == "2":
    url="https://jsonplaceholder.typicode.com/posts"
    novo_post = {
        "title": input("Título: "),
        "body": input("Conteúdo: "),
        "userId":1
    }
    r= requests.post(url, json=novo_post)
    print("Post Criado:", r.json())
elif opcao == "3":
    post_id = input('Digite o ID do post a ser atualizado')
    novo_titulo = input("Novo Título: ")
    url =f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    r= requests.patch(url, json={"title":novo_titulo})
    print("Post atualizado:", r.json())
elif opcao == "4":
    post_id = input("Digite o ID do post a deletar: ")
    url=f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    r= requests.delete(url)
    print("Status:", r.status_code)
else:
    print("Opção inválida.")