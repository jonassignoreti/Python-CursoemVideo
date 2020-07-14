'''Desenvolva um programa que leia o comprimento de três retas
e diga ao seu usuário se elas podem ou não formar um triângulo'''
r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))
if ((r1 + r2) > r3) and ((r1 + r3) > r2) and ((r2 + r3) > r1):
    print('Essas retas podem formar um triângulo')
else:
    print('Essa retas NÃO podem formar um triângulo')
print('FIM')
