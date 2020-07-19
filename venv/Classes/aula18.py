'''VARIÁVEIS COMPOSTAS, LISTAS (parte 2)'''
print('Adicionando listas dentro de outra lista')
teste = list()
teste.append('João')
teste.append(19)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:]) #Faz a cópia da lista teste dentro da lista galera
print(galera)
print('-=' * 30)

print('Declarando um lista composta com mais listas dentro')
turminha = [['Jonas', 27], ['José', 50], ['Jean', 24], ['Geni', 47]]
print(turminha)
print('-=' * 30)

print('Mostrando apenas um item da lista geral')
print(turminha[0])
print('-=' * 30)

print('')
print('Mostrando apenas um item de uma lista dentro da lista geral')
print(turminha[3][1])
print('-=' * 30)

print('Usando um "for"')
for p in turminha:
    print(f'Nome: {p[0]}, Idade: {p[1]} anos')
print('-=' * 30)

print('Inserindo dados')
lista = list()
dado = list()
for c in range(0, 4):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    lista.append(dado[:])
    dado.clear()
print(lista)
print('-=' * 30)

print('')

print('-=' * 30)
