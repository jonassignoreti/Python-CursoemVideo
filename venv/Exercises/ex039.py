'''Faça um programa que leia o ano de nascimento de um jovem
e informe, de acordo com sua idade:
-Se ele ainda vai se alistar ao serviço militar
-Se é a hora dele se alistar
-Se já passou o tempo de alistamento

Seu programa também deverá mostrar o tempo que falta ou que passou o prazo.'''
from datetime import date

nome = str(input('Qual é o seu nome?: '))
ano_nascimento = int(input('Qual é o ano de seu nascimento?: '))
idade = date.today().year - ano_nascimento

if idade < 18:
    print('Você ainda vai se alistar, e faltam {} anos para seu alistamento.'.format(18 - idade))
elif idade == 18:
    print('Você está com 18 anos, e estamos no ano de seu alistamento.')
else:
    print('Já passou da hora de você se alistar, já se passaram {} anos do seu alistamento'.format(idade - 18))
