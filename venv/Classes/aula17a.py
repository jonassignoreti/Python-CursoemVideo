'''VARIÁVEIS COMPOSTAS, LISTAS (parte 1)'''
print(f'Listas são representadas por colchetes []')
num = [5, 1, 9, 2]
print(num)

print(f'\nListas são mutáveis')
num[2] = 3
print(num)

print(f'\nAdicionando um item na lista')
num.append(7)
print(num)

print(f'\nColocando os itens em ordem crescente')
num.sort()
print(num)

print(f'\nColocando os itens em ordem decrescente')
num.sort(reverse=True)
print(num)

print(f'\nMostrando quantos elementos há na lista')
print(f'Essa lista possui {len(num)} elementos')

print(f'\nAdicionando elementos no meio da lista')
num.insert(2, 11)
print(num)

print(f'\nRemovendo um valor da lista (neste caso o último elemento)')
num.pop()
print(num)

print(f'\nRemovendo um valor no meio da lista')
num.pop(2)
print(num)

print(f'\nRemovendo um valor X da lista (3)')
num.remove(3)
print(num)

print(f'\nRemovendo itens usando uma condicional')
if 5 in num:
    num.remove(5)
print(num)
