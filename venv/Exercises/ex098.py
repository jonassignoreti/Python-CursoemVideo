'''Faça um programa que tenha uma função chamada contador(),
que receba três parâmetros: início, fim e passo e realize a contagem.
Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) contagem personalizada'''
from time import sleep

def linha(n):
    print('-=' * n)

def contador(ini, fim, passo):
    if passo == 0:
        passo = 1
    if passo < 0:
        passo *= -1
    print(f'Contagem de {ini} até {fim} de {passo} em {passo}')
    sleep(2.5)
    if ini < fim:
        for c in range(ini, fim+1, passo):
            sleep(0.5)
            print(c, end=' ')
        print()
    elif ini > fim:
        passo = passo * -1
        for c in range(ini, fim-1, passo):
            sleep(0.5)
            print(c, end=' ')
        print()

linha(20)
print(f'{"<< CONTADOR >>":^40}')
linha(20)
sleep(3)
contador(1, 10, 1)
linha(20)
contador(10, 0, 2)
linha(20)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
