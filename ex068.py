'''Faça um programa que jogue par ou ímpar com o computador.
O jogo só será imterrompido quando o jogador PERDER,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''
from random import randint
title = str(' PAR OU ÍMPAR ')
print('{:-^100}'.format(title))
jogada = 0
computador = 0
resultado = 0
vitorias = 0
while True:
    print('-=' * 50)
    escolha = ''
    while escolha != 'P' and escolha != 'I':
        escolha = str(input('PAR OU ÍMPAR [P/I]: ')).strip().capitalize()[0]

    jogada = int(input('NÚMERO DA SUA JOGADA: '))
    computador = randint(1, 10)
    resultado = jogada + computador
    print('O Computador escolheu {}'.format(computador))
    if (resultado % 2) == 0:
        print('DEU PAR')
        pi = 'P'
    else:
        print('DEU ÍMPAR')
        pi = 'I'
    if pi == escolha:
        print('Parabéns você Venceu!')
        print('Vamos Novamente.')
        vitorias += 1
    else:
        print('Você Perdeu')
        break
print('E Você teve {} vitórias'.format(vitorias))
print('-=' * 50)