'''Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas;
B) A média de idade do grupo;
C) Uma lista com todas as mulheres.
D) Uma lista com todas as pessoas com idade acima da média.'''
from time import sleep
lista = list()
cadastro = dict()
tot = 0
print('-=' * 30)
print('     << CADASTRO DE PESSOAS >>')
print('-=' * 30)
while True:
    print('     - NOVO CADASTRO -')
    cadastro['nome'] = str(input('Nome: ')).strip().title()
    while True:
        cadastro['sexo'] = str(input('Sexo: ')).strip().upper()[0]
        if cadastro['sexo'] in 'MF': # Se houver 'M' ou 'F' na variável, faça:
            break
        else:
            print(f'\033[31mERRO: Código Inválido: Digite apenas M ou F.\033[m')
    cadastro['idade'] = int(input('Idade: '))
    tot += cadastro['idade']
    while True:
        resp = str(input('Quer Continuar? [S/N]: ')).strip().upper()
        if resp.__contains__('S') or resp.__contains__('N'):
            break
        else:
            print(f'\033[31mERRO: Código Inválido: Digite apenas S ou N.\033[m')
    lista.append(cadastro.copy())
    cadastro.clear()
    if 'N' in resp:
        print('FINALIZANDO...')
        sleep(1)
        break
print(lista)
print('-=' * 40)
print('     << RESULTADO DO CADASTRO >>')
print(f'A) Ao todo temos {len(lista)} pessoas cadastradas;')
media = tot / len(lista)
print(f'B) A idade média é de {media:5.2f} anos.')
print(f'C) As mulheres cadastradas foram:', end=' ')
for e in lista: # Para cada item da lista >>
    if e["sexo"] in 'F':
        print(f'{e["nome"]},', end=' ') #Mostra do item em questão o valor de 'nome'
print()
print(f'D) Lista de pessoas que estão acima da média: ')
for e in lista:
    for k, v in e.items():
        if k == 'idade':
            if v > media:
                print(f'    Nome: {e["nome"]}, sexo: {e["sexo"]}, idade: {e["idade"]} anos.')