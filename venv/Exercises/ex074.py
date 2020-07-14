'''Crie um programa que vai gerar cinco programas aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor valor e o maior valor que estão na tupla.'''
from random import randint
tupla = (randint(1, 10), randint(1, 10),
         randint(1, 10), randint(1, 10), randint(1, 10))
print('-=' * 15)
print(f'Os Números gerados foram: {tupla}')
print('-=' * 15)
print(f'O maior número é: {max(tupla)}')
print('-=' * 15)
print(f'O menor número é: {min(tupla)}')
