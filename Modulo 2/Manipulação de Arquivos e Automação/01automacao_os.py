# abrir e ler o arquivo

arquivo = open('hello.txt','r', encoding='utf-8') # abrindo o arquivo
conteudo = arquivo.read() # lendo o arquivo e armazenando a variável

print(conteudo) # apresentando a leitura feita
arquivo.close() # fechando o arquivo

#retorna o tamanho do arquivo em bytes
import os
print(os.path.getsize('hello.txt'), "bytes")

# listar todos os arquivos e pastas de um diretorio
# não iremos importar a biblioteca os porque já fizemos isso neste script (arquivo)
print(os.listdir(".")) # lista todo o conteúdo da pasta atual

# seprar diretórios e arquivos
# não iremos importar a biblioteca os porque já fizemos isso neste script (arquivo)
caminho = "/home/user/documentos/arquivo.txt"
print(os.path.dirname(caminho)) #/home/user/documentos
print(os.path.basename(caminho)) # arquivo.txt