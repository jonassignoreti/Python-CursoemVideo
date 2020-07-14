#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import sin, cos, tan, radians
a = float(input('Digite um ângulo: '))
seno = sin(radians(a))
cosseno = cos(radians(a))
tangente = tan(radians(a))
print('O valor do seno é {:.2f} \nO valor do cosseno é {:.2f} \nO valor da tangente é {:.2f}'.format(seno, cosseno, tangente))
