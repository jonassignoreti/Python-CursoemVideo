'''Crie um programa que faça o computador jogar Jokenpô com você'''
from random import randint
from time import sleep

pc = randint(1, 3)
if pc == 1:
    computador = 'Pedra'
elif pc == 2:
    computador = 'Papel'
elif pc == 3:
    computador = 'Tesoura'

pl = str(input('''[ A ] Pedra;
[ B ] Papel;
[ C ] Tesoura.
ESCOLHA SUA JOGADA: ''')).strip().capitalize()
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)

if pl == 'A':
    jogador = 'Pedra'
    if computador == 'Pedra':
        print('O Computador escolheu Pedra também, jogo EMPATADO')
    elif computador == 'Papel':
        print('O Computador escolheu Papel, você PERDEU')
    elif computador == 'Tesoura':
        print('O Computador escolheu Tesoura, você GANHOU!')
elif pl == 'B':
    jogador = 'Papel'
    if computador == 'Pedra':
        print('O Computador escolheu Pedra, você GANHOU!')
    elif computador == 'Papel':
        print('O Computador escolheu Papel também, o jogo EMPATOU')
    elif computador == 'Tesoura':
        print('O Computador escolheu Tesoura, você PERDEU')
elif pl == 'C':
    jogador = 'Tesoura'
    if computador == 'Pedra':
        print('O Computador escolheu Pedra também, você PERDEU')
    elif computador == 'Papel':
        print('O Computador escolheu Papel, você GANHOU!')
    elif computador == 'Tesoura':
        print('O Computador escolheu Tesoura também, o jogo EMPATOU')
else:
    print('\033[31mCódigo Inválido\033[m')
