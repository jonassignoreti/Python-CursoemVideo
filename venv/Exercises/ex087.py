'''Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados;
B) A soma dos valores da terceira coluna;
C) O maior valor da segunda linha.'''
matriz = [[], [], []] #Declaração da lista
print('-=' * 30)
print('MATRIZ 3X3')
print('-=' * 30)

# Entradando com os dados:
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l].append(int(input(f'Linha {l + 1}, Coluna {c + 1}: ')))
print('-=' * 30)

# Visualizando a Matriz
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-=' * 30)

# Processando a soma dos números pares
pares = 0
for l in range(0, 3):
    for c in range(0, 3):
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]

# Processando a soma da terceira coluna
terceira_coluna = 0
for l in range(0, 3):
    terceira_coluna += matriz[l][2]

# Processando o maior valor da segunda linha
maior = 0
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]

print(f'A soma de todos os valores pares digitados é {pares}')
print(f'A soma dos valores da terceira coluna é {terceira_coluna}')
print(f'O maior valor da segunda linha é {maior}')
