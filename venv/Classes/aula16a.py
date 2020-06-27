'''VÁRIAS COMPOSTAS (TUPLAS)
As Tuplas são imutáveis'''
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)
print(lanche[1])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-3])
print(lanche[-3:])
print(len(lanche))
print(' ')
print('Usando o for')
for comida in lanche:
    print(f'{comida}')
print(' ')
print('Usando o for c in range')
for cont in range(0, len(lanche)):
    print(f'{lanche[cont]}')
print(' ')
print('Usando o for c in enumerate')
for pos, comida in enumerate(lanche):
    print(f'{comida} na posição {pos}')
print(' ')
print('Em ordem alfabética')
print(sorted(lanche))
print(' ')
print('Somando tuplas')
a = (2, 5, 1)
b = (9, 6, 7 , 1)
c = a + b
d = b + a
print(c)
print(d)
print(' ')
print('Contando itens em uma tupla')
print(f'Há {c.count(1)} número 1 na tupla d')
print(' ')
print('Mostrando a posição de um item em uma tupla')
print(f'O número 7 está na posição {c.index(7)} na tupla c')
print(' ')
print('As tuplas podem ter variáveis de diferentes tipos:')
pessoa = ('Jonas', 27, 'M', 75.3)
print(pessoa)
del(pessoa) #excluindo uma tupla.

# Testando o GitHub
