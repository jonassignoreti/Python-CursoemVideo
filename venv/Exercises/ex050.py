'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o.'''
s = 0
for c in range(1, 7):
    num = int(input('Digite o {}º valor: '.format(c)))
    if num % 2 == 0:
        s += num
print('A Somatória do números pares é: {}'.format(s))
