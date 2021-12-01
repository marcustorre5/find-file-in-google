from googlesearch import search
from time import sleep

print('=-='*30)
print('achar arquivos no google')
print('com este algoritimo podemos achar qualquer tipo de arquivo com uma ajuda do google')
print('=-='*30)
sleep(1)

while True:
    tipo = int(input('''qual o tipo de arquivo que deseja encontrar ?
    [0] documentos Pdf
    [1] documentos doc
    [2] documentos txt'''))

    if tipo == 0:
        busca = str(input('Digite sua busca: \n'))
        quantidade = int(input('Qual a quantidade de buscas ? \n'))
        for c in search(busca+'filetype:pdf',stop=quantidade):
            print(c)

    if tipo == 1:
        busca2 = str(input('Digite sua busca: \n'))
        quantidade2 = int(input('Qual a quantidade de buscas ? \n'))
        for c in search(busca2+'filetype:doc',stop=quantidade2):
            print(c)

    if tipo == 2:
        busca3 = str(input('Digite sua busca: \n'))
        quantidade3 = int(input('Qual a quantidade de buscas ? \n'))
        for c in search(busca3+'filetype:txt',stop=quantidade3):
            print(c)

