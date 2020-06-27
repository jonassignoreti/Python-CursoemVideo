'''Escreva um programa que leia um número n inteiro qualquer
e mostre na tela os n primeiros elementos de um sequência de Fibonacci
Ex: 0 > 1 > 1 > 2 > 3 > 5 > 8 ...'''
num = int(input('Digite um número: '))
termos = int(input("Digite aqui o número de termos: "))
ant = prox = num
print('{} > {} > '.format(ant, prox), end='')
while termos != 0:
    prox = ant + prox
    ant = prox - ant
    termos -= 1
    print('{} > '.format(prox), end='')
print('FIM')