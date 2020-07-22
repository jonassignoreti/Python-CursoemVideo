'''Faça um programa que tenha uma função chamada área(),
que receba as dimensões de um terreno retangular (largura e comprimento)
e mostre a área do terreno.'''
def linha(n):
    print('-' * n)
def area(c, l):
    print(f'A área de um terreno {c:.1f} x {l:.1f} é de {c * l:.1f}m².')


linha(40)
print(f'{"CONTROLE DE TERRENOS":^40}')
linha(40)
c = float(input('COMPRIMENTO (M): '))
l = float(input('LARGURA (M): '))
area(c, l)
