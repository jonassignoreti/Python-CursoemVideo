'''Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em uma dicionário,
incluindo o total de gols feitos durante o compeonato.'''
jogador = {}
jogador['nome'] = str(input('Digite o nome do Jogador: ')).strip().title()
jogador['n_partidas'] = int(input(f'Digite quantas partidas {jogador["nome"]} jogou: '))
jogador['n_gols'] = []
jogador['total'] = 0
if jogador['n_partidas'] <= 0:
    print(f'O jogador {jogador["nome"]} não jogou nenhuma partida')
else:
    for n in range(0, jogador['n_partidas']):
        jogador['n_gols'].append(int(input(f'Número de Gols da {n + 1}ª partida: ')))
jogador['total'] = sum(jogador['n_gols']) #SOMANDO VALORES DE UMA LISTA. <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
print('-=' * 40)
print(jogador)
print('-=' * 40)
if jogador['n_partidas'] <= 0:
    print(f'O Jogador {jogador["nome"]} não jogou em nenhuma partida, portanto não fez nenhum gol.')
else:
    print(f'O Jogador {jogador["nome"]} jogou {jogador["n_partidas"]} partidas')
    for n in range(0, jogador['n_partidas']):
        print(f' => Na {n + 1}ª partida, Nº de Gols: {jogador["n_gols"][n]}')
    print(f'Número total de gols: {jogador["total"]}')