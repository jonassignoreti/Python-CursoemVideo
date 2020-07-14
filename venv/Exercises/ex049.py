'''Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher,
só que agora utilizando um laço for'''
print('x+' * 70)
for c in range(1, 11):
    print('{:2} x {} = {:2}'.format(c, 1, (c * 1)), '|',
          '{:2} x {} = {:2}'.format(c, 2, (c * 2)), '|',
          '{:2} x {} = {:2}'.format(c, 3, (c * 3)), '|',
          '{:2} x {} = {:2}'.format(c, 4, (c * 4)), '|',
          '{:2} x {} = {:2}'.format(c, 5, (c * 5)), '|',
          '{:2} x {} = {:2}'.format(c, 6, (c * 6)), '|',
          '{:2} x {} = {:2}'.format(c, 7, (c * 7)), '|',
          '{:2} x {} = {:2}'.format(c, 8, (c * 8)), '|',
          '{:2} x {} = {:2}'.format(c, 9, (c * 9)), '|',
          '{:2} x {} = {:2}'.format(c, 10, (c * 10)))
print('x+' * 70)
