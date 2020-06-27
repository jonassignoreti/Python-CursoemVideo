# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2m².
h = float(input('Quantos metros a parede têm de altura?: '))
w = float(input('Quantos metros a parede têm de largura: '))
r = float(input('Quantos metros um litro de tinta faz?: '))
a = h*w
print('A área da parede é {:.2f}m²'.format(a))
print('e você precisa de {:.2f} litros de tinta para pintá-la.'.format(a/r))
