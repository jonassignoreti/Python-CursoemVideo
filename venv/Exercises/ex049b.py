'''Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher,
só que agora utilizando um laço for'''
print('x+' * 80)
for c in range(1, 11):
    for m in range(1, 11):
        print('{:2} x {:2} = {:3}'.format(m, c, (c * m)), '|', end='')
        if m == 10:
            print('')
print('x+' * 80)
