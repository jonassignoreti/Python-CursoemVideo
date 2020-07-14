'''Faça um programa que leia o peso de cinco pessoas,
No final, mostre qual foi o maior e o menor peso lidos.'''
cardinal = ('primeira',
            'segunda',
            'terceira',
            'quarta',
            'quinta')
maior = 0
menor = 1000
peso = 0
for c in range(0, 5):
    peso = float(input('Digite o pessoa da {} pessoa: '. format(cardinal[c])))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print('O menor peso registrado foi {}'.format(menor))
print('O maior peso registrado foi {}'.format(maior))
