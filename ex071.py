'''Crie um programa que simule o funcionamento de um caixa eletrônico.
No ínicio, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues.
Obs.: Considere que o caixa possui cédulas de R$50, R$20, R$10, R$1.'''
valor_sacado = float(input('Digite o valor do saque: R$'))
valor_incial = valor_sacado
saque = int(valor_sacado * 100)
n100 = n50 = n20 = n10 = n5 = n2 = n1 = m50 = m25 = m10 = m5 = m1 = 0
while saque != 0:
    if saque >= 10000:
        saque -= 10000
        n100 += 1
    elif saque >= 5000:
        saque -= 5000
        n50 += 1
    elif saque >= 2000:
        saque -= 2000
        n20 += 1
    elif saque >= 1000:
        saque -= 1000
        n10 += 1
    elif saque >= 500:
        saque -= 500
        n5 += 1
    elif saque >= 200:
        saque -= 200
        n2 += 1
    elif saque >= 100:
        saque -= 100
        n1 += 1
    elif saque >= 50:
        saque -= 50
        m50 += 1
    elif saque >= 25:
        saque -= 25
        m25 += 1
    elif saque >= 10:
        saque -= 10
        m10 += 1
    elif saque >= 5:
        saque -= 5
        m5 += 1
    elif saque >= 1:
        saque -= 1
        m1 += 1
    else:
        break
print('Foram sacados R${:.2f}'.format(valor_incial))
if n100 > 0:
    print(f'{n100} notas de R$100')
if n50 > 0:
    print(f'{n50} notas de R$50')
if n20 > 0:
    print(f'{n20} notas de R$20')
if n10 > 0:
    print(f'{n10} notas de R$10')
if n5 > 0:
    print(f'{n5} notas de R$5')
if n2 > 0:
    print(f'{n2} notas de R$2')
if n1 > 0:
    print(f'{n1} moedas de R$1')
if m50 > 0:
    print(f'{m50} notas de 50¢')
if m25 > 0:
    print(f'{m25} notas de 25¢')
if m10 > 0:
    print(f'{m10} notas de 10¢')
if m5 > 0:
    print(f'{m5} notas de 5¢')
if m1 > 0:
    print(f'{m1} notas de 1¢')
print('Foram sacados R${:.2f}'.format(valor_incial))
