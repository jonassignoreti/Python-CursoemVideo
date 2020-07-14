'''Refaça o DESAFIO 51, lendo o primeiro termo PA e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura WHILE'''
print('{:=^100}'.format(' Os 10 PRIMEIROS TERMOS DE UMA PA '))
p = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
cont = 1
while cont != 11:
    termo = p + (cont - 1) * r
    print('{}'.format(termo), end=' > ')
    cont += 1
print('END')
