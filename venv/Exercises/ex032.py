'''Faça um programa que leia um ano qualquer e mostre se ele é Bissexto.'''
from datetime import date
ano = int(input('Digite um ano qualquer (digite "0" se quiser analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0):
    print('O ano {} é um ano \033[7;30mBissexto\033[m'.format(ano))
else:
    print('O ano {} \033[30;41mNÃO\033[m é um ano Bissexto'.format(ano))
print('FIM')
