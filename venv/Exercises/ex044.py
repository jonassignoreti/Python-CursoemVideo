'''Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço nominal e condição de pagamento:
-à vista dinheiro/cheque: 10% de desconto;
-à vista no cartão: 5% de desconto;
-em até 2x no cartão: preço normal;
-3x ou mais no cartão: 20% de juros.'''
print('{:=^40}'.format('LOJAS MAGAZINE'))
preco = float(input('Digite o valor nominal do produto: R$'))
forma_pagamento = str(input('''[ A ] à vista dinheiro/cheque: 10% de desconto;
[ B ] à vista no cartão: 5% de desconto; 
[ C ] em até 2x no cartão: preço normal; 
[ D ] 3x ou mais no cartão: 20% de juros.
ESCOLHA A FORMA DE PAGAMENTO: ''')).strip().capitalize()

if forma_pagamento == 'A' or forma_pagamento == 'B' or forma_pagamento == 'C' or forma_pagamento == 'D':
    if forma_pagamento == 'A':
        print('Pagando à vista no dinheiro/cheque: R${:.2f}'.format(preco - (preco * 10/100)))
    elif forma_pagamento == 'B':
        print('Pagando à vista no cartão: R${:.2f}'.format(preco - (preco * 5/100)))
    elif forma_pagamento == 'C':
        print('Pagando em até 2x no cartão: R${:.2f}'.format(preco))
    elif forma_pagamento == 'D':
        prestacoes = int(input('Em quantas prestações?: '))
        print("Pagando no cartão, sai por {:.2f} em {} prestações de {:.2f}".format(preco + (preco * 20/100), prestacoes, (preco + (preco * 20/100)) / prestacoes))
else:
    print('\033[31mCódigo inválido!\033[m')