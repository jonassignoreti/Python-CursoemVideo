'''Escreva um programa que leia um número inteiro qualquer
e peça para o usuário escolher qual será a base de conversão
-1 para binário
-2 para octal
-3 para hexadecimal'''

num = int(input('Digite um número inteiro: '))
base = str(input('''ESCOLHA
"1" para converter para binário, 
"2" para converter para octal, 
"3" para converter para hexadecimal 
Escolha uma conversão: ''')).strip()

if base == '1':
    binario = bin(num)
    print('O número {} em Binário é \033[7m{}\033[m'.format(num, binario))
elif base == '2':
    octal = oct(num)
    print('O número {} em Octal é \033[7m{}\033[m'.format(num, octal))
elif base == '3':
    hexa = hex(num)
    print('O número {} em Hexadecimal é \033[7m{}\033[m'.format(num, hexa))
else:
    print('Código inválido')
