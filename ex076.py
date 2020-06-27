'''Crie um programa que tenha uma tupla única com nomes de produtos
e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços,
organizando os dados em forma tabular'''
tupla = (str(input('Digite o nome do produto: ')), float(input('Digite o valor desse produto: ')),
         str(input('Digite o nome do produto: ')), float(input('Digite o valor desse produto: ')),
         str(input('Digite o nome do produto: ')), float(input('Digite o valor desse produto: ')),
         str(input('Digite o nome do produto: ')), float(input('Digite o valor desse produto: ')))
print('-' * 40)
print(f'{"LISTA DE PRODUTOS":^40}')
print('-' * 40)
for pos in range(0, len(tupla)):
    if pos % 2 == 0:
        print(f'{tupla[pos]:.<30}', end='')
    else:
        print(f'R${tupla[pos]:>6.2f}')
print('-' * 40)
