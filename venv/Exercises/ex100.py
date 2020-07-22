'''Faça um programa que tenha uma lista chamada números
e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los em uma lista
e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior'''
from random import randint
from time import sleep


def sorteia(lst):
    print('SORTEANDO OS 5 VALORES DA LISTA: ', end='')
    sleep(1.5)
    for c in range(0, 5):
        lst.append(randint(1, 10))
        print(f'{lst[c]} ', end='')
        sleep(0.5)

    print('PRONTO!')


def somapar(lst):
    s = 0
    for v in lst:
        if v % 2 == 0:
            s += v
    print(f'SOMANDO OS VALORES PARES DE {lst}, temos {s}')


lista = []
sorteia(lista)
somapar(lista)
