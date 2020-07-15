'''Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado
[  ][  ][  ]
[  ][  ][  ]
[  ][  ][  ]
No final, mostre a matriz na tela, com a formatação correta.'''
matriz = [[], [], []]
print('-=' * 30)
print('MATRIZ 3X3')
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l].append(int(input(f'Linha {l}, Coluna {c}: ')))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
