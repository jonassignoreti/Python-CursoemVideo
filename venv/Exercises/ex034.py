'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento
Para salários superiores a R$1250.00, calcule um aumento de 10%
Para salários inferiores ou iguais, o aumento é de 15%'''
s = float(input('Digite o valor do salário: '))
if s > 1250:
    print('O valor do salário com o aumento de 10% é de R${:.2f}'.format(s + (s*10/100)))
else:
    print('O valor do salário com o aumento de 15% é de R${:.2f}'.format(s + (s*15/100)))
print('FIM')
