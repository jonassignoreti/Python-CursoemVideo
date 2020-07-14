'''Faça um programa que leia um número de 0 à 9999 e mosre na tela cada um dos dígitos separados
Ex: Digite um número: 1834
unidade: 4
dezena: 3
centena: 8
milhar: 1'''
num = (input('Digite um número de 0 à 9999: '))
print('O número digitado foi {}, e nele há:'.format(num))
print('unidades: {}'.format(num[3]))
print('dezenas: {}'.format(num[2]))
print('centenas: {}'.format(num[1]))
print('milhares: {}'.format(num[0]))
