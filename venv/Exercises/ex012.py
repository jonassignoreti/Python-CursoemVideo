# Faça um algoritmo que leia um preço de um produto,
# e mostre seu novo preço, com 5% de desconto.
p = float(input('Preço do produto(R$): '))
d = float(input('Desconto (%): '))
pcd = p-(p*(d/100))
print('O valor com {}% de desconto é R${:.2f}'.format(d, pcd))
