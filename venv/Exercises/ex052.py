'''Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''
num = int(input('Digite um número inteiro: '))
tot = 0
for c in range(1, num+1):
    if num % c == 0:
        print('\033[7:33m', end='')
        tot += 1
    else:
        print('\033[0:33m', end='')
    print(' {:2}'.format(c), end=' \033[m')
print('\n\033[mO número {} foi divisível {} vezes,'.format(num, tot))
if tot == 2:
    print('Portanto ele É PRIMO.')
else:
    print('Portanto ele NÃO É PRIMO.')