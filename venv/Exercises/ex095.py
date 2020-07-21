'''Aprimore o DESAFIO 093 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.'''
from time import sleep
lista = list()
jogador = dict()
print('-=' * 35, f'\n{"<<CADASTRO DE JOGADORES>>":^70}\n', '-=' * 35)
while True:
    jogador.clear()
    jogador['nome'] = str(input('Digite o nome do Jogador: ')).strip().title()
    jogador['n_partidas'] = int(input(f'Digite quantas partidas {jogador["nome"]} jogou: '))
    jogador['n_gols'] = []
    jogador['total'] = 0
    if jogador['n_partidas'] <= 0:
        print(f'O jogador {jogador["nome"]} não jogou nenhuma partida')
    else:
        for n in range(0, jogador['n_partidas']):
            jogador['n_gols'].append(int(input(f'   Número de Gols da {n + 1}ª partida: ')))
    jogador['total'] = sum(jogador['n_gols']) #SOMANDO VALORES DE UMA LISTA. <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    lista.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if resp in 'SN':
            break
        else:
            print(f'\033[31mERRO!: Código Inválido, digite somente S ou N\033[m')
    if resp in 'N':
        print('Finalizando...')
        sleep(1)
        break
    print('-' * 20)

print('-=' * 35)
print(f'{"ANÁLISE DOS DADOS":^70}')
print(f'|{"cod":^5}|{"NOME":^30}|{"Gols":^22}|{"TOTAL":^7}|')
print('-' * 70)
for i, v in enumerate(lista):
    print(f'|{i + 1:^5}| {v["nome"]:<29}| {str(v["n_gols"]):<21}|{v["total"]:^7}|')
print('-=' * 35)
while True:
    ans = int(input('Mostrar dados de qual jogador?: [ZERO para parar o programa]'))
    if ans == 0:
        break
    elif ans > len(lista) or ans < 0:
        print(f'\033[31mErro, Código Inválido, digite um número entre 1 e {len(lista)}\033[m')
    else:
        print(' -- LEVANTAMENTO DO JOGADOR --')
        print(f'Nome do Jogador: {lista[ans - 1]["nome"]}')
        for i, v in enumerate(lista[ans - 1]["n_gols"]):
            print(f'No {i + 1}º jogo fez {v} gols')
        print('-' * 20)

