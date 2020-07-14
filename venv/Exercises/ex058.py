'''Melhore o jodo do Desafio 028 onde o computador vai "pensar" em um número entre o 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar , mostrando no final quantos palpites foram necessários para vencer.'''
'''Algumas melhorias: variáveis min/max para fácil mudança futura
dizer que o número digitado está fora da faixa
e dando dicas se o número é maior ou menor'''
from random import randint
max = 1000
min = 0
computador = randint(min, max)
tentativas = 0
jogador = -1
while computador != jogador:
    print('*' * 50)
    jogador = int(input('Digite um número entre {} e {}: '.format(min, max)))
    if jogador < min or jogador > max:
        print('você não digitou um número entre {} e {}, tente outra vez.'.format(min, max))
    elif computador != jogador:
        print('Você não acertou, tente outra vez.')
        if jogador > computador:
            print('É um número menor.')
        elif jogador < computador:
            print('É um número maior.')
    tentativas += 1
print('Parabéns, você acertou na {}ª tentativa, o número {}'.format(tentativas, computador))