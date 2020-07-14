'''Faça um programa que leia 5 valores númericos e guarde-os em um lista,
No final mostre qual foi o maior e menor valor digitado e as suas respectivas posições na lista'''

lista = list()
maior = menor = 0

while True:
    lista.append(int(input('Digite um valor: ')))
    while True:
        cond = str(input('Deseja continuar [S/N]: ')).upper().strip()
        if cond != 'S' and cond != 'N':
            print('Código Inválido, tente novamente: ', end='')
        else:
            break
    if cond in 'N':
        break

for c in range(0, len(lista)):
    if c == 0:
        menor = maior = lista[0]
    if lista[c] > maior:
        maior = lista[c]
    if lista[c] < menor:
        menor = lista[c]

print(f'Você digitou os valores {lista}')
print(f'O menor valor foi {menor} e está nas posições ', end='')
for i, v in enumerate(lista): # Verifica cada item da lista
    if v == menor:
        print(f'{i}...', end='')
print()
print(f'O maior valor foi {maior} e está nas posições ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}...', end='')
print()
