'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O Programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado'''
valor = float(input('Qual é o valor do imóvel?: R$'))
salario = float(input('Quanto é o salário do comprador?: R$'))
anos = int(input('Em quantos anos será pago?: '))
meses = anos * 12
prestacao = valor / meses

if prestacao <= (salario * 30/100):
    print('\033[34mEmpréstimo Aprovado!\033[m')
    print('Será pago em {} prestações de R${:.2f}'.format(meses, prestacao))
else:
    print('\033[31mEmpréstimo não Aprovado\033[m')
