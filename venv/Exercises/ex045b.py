from time import sleep
from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] Pedra;
[ 1 ] Papel;
[ 2 ] Tesoura.''')
jogador = int(input('Qual é a sua Jogada?: '))
print('-=' * 20)
sleep(0.5)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PÔ!')
print('-=' * 20)
print('O Jogador escolheu {}'.format(itens[jogador]))
print('O Computador escolheu {}'.format(itens[computador]))

