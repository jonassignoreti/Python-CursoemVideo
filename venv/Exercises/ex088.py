'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados
e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta.'''
from random import randint
from time import sleep
jogos = list()
jogo = list()
num = 0
print('$ ' * 10)
print('GERADOR DE NÚMEROS MEGA-SENA')
print('$ ' * 10)
njogos = int(input('Quantos jogos deseja gerar?: '))
for j in range(0, njogos):
    while len(jogo) != 6:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
    jogo.sort()
    jogos.append(jogo[:])
    jogo.clear()
for j in jogos:
    print(j)
    sleep(1)
print('$ BOA SORTE $')