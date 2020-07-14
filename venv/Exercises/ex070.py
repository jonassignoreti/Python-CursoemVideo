'''Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar.
No final, mostre:
a) Qual é o total gasto na compra
b) Quantos produtos custam mais de R$1000
c) Qual é o nome do produto mais barato.
'''
total = 0
cont = 0
prod_1000 = 0
valor_prod_barato = 0
nome_prod_barato = ''
produto = ''

while True:
    print('-=' * 20)
    produto = str(input('Digite o nome do Produto: ')).strip().capitalize()
    valor = float(input('Digite o valor do Produto: '))

    total += valor
    cont += 1

    if valor > 1000:
        prod_1000 += 1

    if cont == 1:
        valor_prod_barato = valor
        nome_prod_barato = produto
    elif cont > 1:
        if valor < valor_prod_barato:
            valor_prod_barato = valor
            nome_prod_barato = produto

    prog = str(input('Deseja continuar? [S/N]: ')).upper().strip()
    while prog not in 'SN':
        print('Código inválido!')
        prog = str(input('Deseja continuar? [S/N]: ')).upper().strip()
    if 'N' in prog:
        break

print('-=' * 20)
print('Valor total da compra R${:.2f}'.format(total))
print('Há {} produtos que custam mais de R$1000,00'.format(prod_1000))
print('O produto mais barato é {}'.format(nome_prod_barato))
