'''Faça um programa que calcule a soma entre
todos os números ímpares que são múltiplos de 3
e que se encontram no intervalo de 1 até 500.'''
s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
        cont += 1
print('''A somatória entre todos os {} números ímpares que são múltiplos de 3 
e que se encontram no intervalo de 1 até 500 é: {}'''.format(cont, s))
print('')
