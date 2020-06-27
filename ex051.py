'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.'''
print('=' * 40)
print('10 TERMOS DE UMA PA')
print('=' * 40)
p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
decimo = p + (10 - 1) * r
for c in range(p, decimo + r, r):
    print('{}'.format(c), end=' > ')
print('ACABOU')