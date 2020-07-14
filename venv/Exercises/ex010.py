# Crie um programa que leia quanto uma pessoa tem na carteira em R$ e mostre em quantos dólares (USD) ela pode comprar. Considere 1USD = R$3,27
reais = float(input('Quantos reais você têm?: '))
usd = 3.27
print('Você pode comprar {:.2f} dólares'. format(reais/usd))
