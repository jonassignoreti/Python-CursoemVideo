'''Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos'''
print('{:=^100}'.format(' Os 10 PRIMEIROS TERMOS DE UMA PA '))
p = int(input('Primeiro Termo: '))
r = int(input('Razão: '))
cont = 1
meta = 10
while cont != (meta + 1):
    termo = p + (cont - 1) * r
    print('{}'.format(termo), end=' > ')
    cont += 1
    if cont == (meta + 1):
        meta = int(input('\nQuantos termos você deseja mais ver: ')) + meta

print('END')