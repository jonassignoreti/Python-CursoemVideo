# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.
#Ex: Digite um número: 6.127; O número 6.127 tem a parte inteira 6.
from math import trunc
num = float(input('Digite um número: '))
print('A Parte inteira do número {} é {:.0f}'.format(num, trunc(num)))

'''ou sem a necessidade de importar biblioteca, pode se usar int(num) dentro do format. para mostrar a porção inteira do número'''