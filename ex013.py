# Faça uma algoritmo que leia o salário de um funcionário
# e mostre seu novo salário , com % de aumento
s = float(input('Digite o valor do salário: '))
a = float(input('Quantos % de aumento?: '))
ns = s+(s*(a/100))
print('O novo valor do salário com {}% de aumento é de {:.2f}'. format(a, ns))
