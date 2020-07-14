'''Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''
from datetime import date
idade = 0
maioridade = 0
menoridade = 0
cardinal = ('primeira',
            'segunda',
            'terceira',
            'quarta',
            'quinta',
            'sexta',
            'sétima')
for c in range(0, 7):
    idade = date.today().year - int(input('Digite o ano de nascimento da {} pessoa: '.format(cardinal[c])))
    if idade >= 18:
        maioridade += 1
    else:
        menoridade += 1
print('Há {} pessoas maiores de idade.'.format(maioridade))
print('Há {} pessoas menores de idade.'.format(menoridade))
