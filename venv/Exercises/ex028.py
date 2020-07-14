'''Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador
O programa deverá escrever na tela se o usuário venceu ou perdeu'''
import random
from time import sleep
ne = random.randint(1, 5)
nu = int(input('Descubra o número que o computador pensou entre 1 e 5: '))
print('PROCESSANDO...')
sleep(3)
if ne == nu:
    print('PARABÉNS, VOCÊ ACERTOU!')
else:
    print('Desculpa, você não acertou, o número foi {}'.format(ne))
