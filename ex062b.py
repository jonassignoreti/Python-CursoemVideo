q = -1
while q != 0:
    print('{:=^100}'.format(' TERMOS DE UMA PA '))
    q = int(input('Nº de Termos ou [0] para terminar: '))
    if q != 0:
        p = int(input('Primeiro Termo: '))
        r = int(input('Razão: '))
        cont = 1
        while cont != (q + 1):
            termo = p + (cont - 1) * r
            print('{}'.format(termo), end=' > ')
            cont += 1
        if cont == (q + 1):
            print('FIM')
print('END')