'''Faça um programa que tenha uma função chamada maior(),
que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e
dizer qual deles é o maior.'''
from time import sleep


def linha():
    print('-=' * 30)


def maior(* valores):
    linha()
    print('Analizando os valores... ', end=' ')
    sleep(1)
    p = 0
    for num in valores:
        print(num, end=' ')
        sleep(0.5)
        if p == 0:
            m = num
        else:
            if num > m:
                m = num
        p += 1
    print(f'\nForam informados {p} valores ao todo, o maior número é {m}')


maior(1, 2, 3, 4, 5)
maior()
