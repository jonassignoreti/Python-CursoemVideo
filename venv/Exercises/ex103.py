'''Faça um programa que tenha uma função chamada ficha(),
que receba dois parâmetros opcionais:
o nome de um jogador
e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador,
mesmo que algum dado não tenha sido informado corretamente.'''


def ficha(nome='<desconhecido>', gols=0):
    print(f'O Jogador {nome} fez {gols} gol(s) no campeonato.')


nome_jogador = str(input('Nome do Jogador: ')).strip().title()
n_gols = str(input('Número de gols: ')).strip()
if n_gols.isnumeric():
    n_gols = int(n_gols)
else:
    n_gols = 0
if nome_jogador.strip() == '':
    ficha(gols=n_gols)
else:
    ficha(nome_jogador, n_gols)
