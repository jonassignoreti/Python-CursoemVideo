'''VARIÁVEIS COMPOSTAS, LISTAS (parte 1)'''

print('No Python, igualar duas listas significa ligar uma a outra, alterando a segunda, a primeira também se altera')
a = [1, 2, 3, 4]
b = a #igualando-as
b[2] = 9 #modificando-a para demonstração
print(f'Lista A: {a}')
print(f'Lista B: {b}')

print('\nMas é possível fazer uma cópia')
c = [1, 2, 3, 4]
d = c[:] #copiando os valores de outra lista sem ligar uma a outra
d[2] = 9 #modificando-a para demonstração
print(f'Lista C: {c}')
print(f'Lista D: {d}')