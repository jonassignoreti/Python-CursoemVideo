'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo dastrês listas geradas.'''
lista = []
pares = []
impares = []

while True:
    lista.append(int(input('Digite um valor: ')))
    resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    while not (resp.__contains__('S') or resp.__contains__('N')):
        print('Código inválido, tente novamente:')
        resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if resp.__contains__('N'):
        break

for i, v in enumerate(lista):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)

lista.sort()
pares.sort()
impares.sort()

print(f'Todos os números {lista}')
print(f'Todos os números pares {pares}')
print(f'Todos os números ímpares {impares}')
