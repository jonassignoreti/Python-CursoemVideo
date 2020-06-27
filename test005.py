from random import randint
import os

fileName = r'text.txt'
if not os.path.isfile(fileName):
    arquivo = open('text.txt', 'x+') #Cria o arquivo

while True:
    arquivo = open('text.txt', 'a+') #Abre o arquivo sem apagar o existente.
    linhas = int(input('Número de linhas: '))
    colunas = int(input('Número de colunas: '))
    max = int(input('Digite o valor máximo: '))

    for i in range(linhas):
        for c in range(colunas):
            arquivo.write(str(randint(0, max)) + '\t')
        arquivo.write('\n')

    arquivo = open('text.txt', 'r+') #Lê o arquivo
    print(arquivo.read())

    arquivo.close()

    escolha = str(input('CLEAN[C]/NEXT[N]/EXIT[E]: ')).strip().upper()
    if escolha in 'C':
        arquivo = open('text.txt', 'w+') #Abre para reescrever por cima posteriormente, ou limpa.
    if escolha in 'E':
        break
