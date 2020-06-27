# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
n = float(input('Digite um número: '))
print('-' * 10)
print('{} x {:2} = {:.3f}'.format(n, 1, n*1))
print('{} x {:2} = {:.3f}'.format(n, 2, n*2))
print('{} x {:2} = {:.3f}'.format(n, 3, n*3))
print('{} x {:2} = {:.3f}'.format(n, 4, n*4))
print('{} x {:2} = {:.3f}'.format(n, 5, n*5))
print('{} x {:2} = {:.3f}'.format(n, 6, n*6))
print('{} x {:2} = {:.3f}'.format(n, 7, n*7))
print('{} x {:2} = {:.3f}'.format(n, 8, n*8))
print('{} x {:2} = {:.3f}'.format(n, 9, n*9))
print('{} x {:2} = {:.3f}'.format(n, 10, n*10))
print('-' * 10)
# limitando o número de dígitos dentro das máscaras de formatação usando por exemplo {:2} para limitar para 2
# repetindo o texto usando a multiplicação ['texto' * número de vezes]
