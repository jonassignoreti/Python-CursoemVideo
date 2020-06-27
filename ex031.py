'''Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens até 200Km
e R$0,45 para viagens mais longas'''
d = float(input('Qual a distância a ser percorrida?: '))
if d <= 200:
    print('Será cobrado R${:.2f}'.format(d*0.5))
else:
    print('Será cobrado R${:.2f}'.format(d*0.45))
print('FIM')
