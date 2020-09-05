'''Crie um pequeno sistema modularizado
que permita cadastrar pessoas pelo seu nome e idade
em um arquivo de texto simples.
O sistema só vai ter 2 opções: cadastrar uma nova pessoa
e listar todas as pessoas cadastradas.'''
import os
from pacotes import formatação
tam = 100

fileName = r'ex115.txt'
if not os.path.isfile(fileName):
    arquivo = open('ex115.txt', 'x+') #Cria o arquivo

while True:
    while True:
        formatação.title('Menu Principal', tam)
        print(f'\033[33m 1 - \033[34mVer Pessoas Cadastradas\033[m')
        print(f'\033[33m 2 - \033[34mCadastrar nova Pessoa\033[m')
        print(f'\033[33m 3 - \033[34mSair do Sistema\033[m')
        formatação.line(tam)

        op = str(input(f'\033[33mSua Opção: \033[m'))
        if op in '123':
            break
        else:
            print(f'\033[31mCódigo Inválido! escolha sua opção, 1, 2 ou 3.\033[m')

    if op == '1':
        formatação.title(f'\033[33mOpção 1 - \033[34mVer Pessoas Cadastradas\033[m', tam)
        arquivo = open('ex115.txt', 'r+') #Lê o arquivo
        print(arquivo.read())
        formatação.line(tam)

    if op == '2':
        formatação.title(f'\033[33mOpção 2 - \033[34mCadastrar nova Pessoa\033[m', tam)
        arquivo = open('ex115.txt', 'a+')  # Abre o arquivo sem apagar o existente.
        nome = str(input('Digite o nome da pessoa: ')).strip().title()
        idade = int(input(f'Digite a idade de {nome}: '))
        idade = str(idade)
        arquivo.write(nome + 2*'\t')
        arquivo.write(idade + ' anos' '\n')
        formatação.line(tam)

    if op == '3':
        formatação.title(f'\033[33mOpção 3 - \033[34mSair do Sistema\033[m', tam)
        print('PROGRAMA FINALIZADO')
        formatação.line(tam)
        break

