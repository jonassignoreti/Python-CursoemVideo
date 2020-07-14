'''Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:
A) Apenas os 5 primeiros colocados;
B) Os últimos 4 colocados da tabela;
C) Uma lista com os times em ordem alfabética;
D) Em que posição na tabela está o time da Chapecoense'''
brasileirao = ('Corinthians', 'Palmeiras', 'São Paulo', 'Santos', 'Cruzeiro', 'Grêmio', 'Internacional',
               'Chapecoense', 'Vasco', 'Fluminense', 'Flamengo', 'Bahia', 'Sport', 'Fortaleza', 'Athelico-PR',
               'Bragantino', 'Ceará', 'Goiás', 'Bota-Fogo', 'Coritiba')
print('BRASILEIRÃO')
print('-=' * 15)
print(f'Os cinco primeiros colocados do Campeonato Brasileiro são: {brasileirao[0]}, {brasileirao[1]}, {brasileirao[2]}, {brasileirao[3]} e {brasileirao[4]}')
print('-=' * 15)
print(f'Os quatro últimos colocados na tabela são: {brasileirao[-4]}, {brasileirao[-3]}, {brasileirao[-2]} e {brasileirao[-1]}')
print('-=' * 15)
print(f'Em ordem alfabética: ', sorted(brasileirao))
print('-=' * 15)
print(f'A Posição do Chapecoense está na {brasileirao.index("Chapecoense") + 1}ª posição')
print('-=' * 15)