'''Faça um programa que leia um número de 0 à 9999 e mosre na tela cada um dos dígitos separados
Ex: Digite um número: 1834
unidade: 4
dezena: 3
centena: 8
milhar: 1'''
from math import trunc
num = int(input('Digite um número de 0 à 9999: '))
print('O número digitado foi {}, e nele há:'.format(num))
print('unidades: {}'.format((trunc(num)) - (trunc(num/10)) * 10))
print('dezenas: {}'.format((trunc(num/10)) - (trunc(num/100)) * 10))
print('centenas: {}'.format((trunc(num/100)) - (trunc(num/1000)) * 10))
print('milhares: {}'.format(trunc(num/1000)))
