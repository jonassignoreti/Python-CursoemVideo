'''Crie um programa que leia o nome de duas notas de vários alunos
guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um
e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''
from time import sleep
aluno = list()
notas = list()
lista = list()
media = a = 0
while True:
    nome = str(input('Digite o nome do aluno: ')).strip().capitalize()
    aluno.append(nome)
    n1 = float(input('   Nota 1: '))
    notas.append(n1)
    n2 = float(input('   Nota 2: '))
    notas.append(n2)
    media = (notas[0] + notas[1]) / 2
    aluno.append(notas[:])
    aluno.append(media)
    lista.append(aluno[:])
    notas.clear()
    aluno.clear()
    r = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    while not (r.__contains__('N') or r.__contains__('S')):
        print('Código inválido, tente novamente')
        r = str(input('Deseja continuar? [S para SIM, e N para NÃO]:'))
    if r == 'N':
        break
    print('-' * 30)
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
for i, v in enumerate(lista):
    print(f'{i:<4}{v[0]:<10}{v[2]:>8.1f}')
print('-=' * 30)
while True:
    a = int(input('Qual aluno você deseja ver as notas? [999 interrompe programa]: '))
    if a == 999:
        break
    if a <= len(lista) - 1:
        print(f'Notas de {lista[a][0]} são {lista[a][1]}, média final {lista[a][2]}')
    print('-' * 30)
print('-=' * 30)
print('-=' * 3, ' < PROGRAMA FINALIZADO > ', '=-' * 3)