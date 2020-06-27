'''Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá se o usuário quer ou não continuar.
No final, mostre:
a) Quantas pessoas tem mais de 18 anos de idade;
b) Quantos homens foram cadastrados;
c) Quantas mulheres tem menos de 20 anos de idade'''
from time import sleep
run = 1
maioridade = 0
homens = 0
mulheres20anos = 0

while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().capitalize()
    while not 'M' in sexo and not 'F' in sexo:
        sexo = str(input('Código Inválido. Digite o Sexo [M/F]: ')).strip().capitalize()
    if idade >= 18:
        maioridade += 1
    if 'M' in sexo:
        homens += 1
    if 'F' in sexo and idade <= 20:
        mulheres20anos += 1
    continuar = ''
    continuar = str(input('Deseja continuar? [S/N]: ')).upper().strip()
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Código inválido. Deseja continuar? [S/N]: ')).upper().strip()
    if 'N' in continuar:
        break
print('\33[31mColeta de dados finalizado.\33[m')
print('Calculando', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.')
print('Há {} pessoas com mais de 18 anos de idade;'.format(maioridade))
print('Há {} homens cadastrados;'.format(homens))
print('Há {} mulheres com menos de 20 anos de idade'.format(mulheres20anos))
print('FIM')
