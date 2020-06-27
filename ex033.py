'''Faça um programa que leia três números
e mostre qual é o maior e qual é o menor'''
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))
if n1 > n2:
    if n1 > n3:
        print('O maior número é: {}'.format(n1))
if n2 > n1:
    if n2 > n3:
        print('O maior número é: {}'.format(n2))
if n3 > n1:
    if n3 > n2:
        print('O maior número é: {}'.format(n3))
if n1 < n2:
    if n1 < n3:
        print('O menor número é: {}'.format(n1))
if n2 < n1:
    if n2 < n3:
        print('O menor número é: {}'.format(n2))
if n3 < n1:
    if n3 < n2:
        print('O menor número é: {}'.format(n3))
print('FIM')
