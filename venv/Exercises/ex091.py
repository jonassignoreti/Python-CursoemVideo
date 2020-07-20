'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário.
No final, coloque esse dicionário em ordem,
sabendo que o vencedor tirou o maior número no dado.'''
from random import randint
from time import sleep
from operator import itemgetter
jogo = dict()
ranking = list()
print('Valores Sorteados: ')
for c in range(1, 5):
    jogo[f'jogador{c}'] = randint(1, 6)
    sleep(0.5)
    print(f'Jogador {c} tirou {jogo[f"jogador{c}"]} no dado')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) #Pegando valores de um dicionário e ordenando dentro de uma lista de tuplas
print('-=' * 30)
print(f'  == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'    {i + 1}ºlugar: {v[0]} com {v[1]}')
    sleep(0.5)
