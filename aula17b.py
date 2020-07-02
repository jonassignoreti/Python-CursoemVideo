'''VARIÁVEIS COMPOSTAS, LISTAS (parte 1)'''

#Declarando uma lista
valores = list() # or just: []

valores.append(5)
valores.append(8)
valores.append(4)
valores.append(5)

print('mostando de outra maneira')
for v in valores:
    print(f'{v}... ', end='')

print('\nOutra maneira, enumerada')
for c, v in enumerate(valores):
    print(f'Na posição {c}ª está o valor {v}!')

print('\nAdicionando itens na lista pelo teclado')
valores2 = list()
for cont in range(0, 5):
    valores2.append(int(input('Digite um valor: ')))
print(valores2)
