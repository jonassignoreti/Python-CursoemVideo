'''Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços'''
from unidecode import unidecode
frase = str(input('Digite uma frase: ')).strip().split()
frase0 = (''.join(frase)).lower()
frase1 = unidecode(frase0)

lista1 = []
for c in range(0, len(frase1)):
    lista1.append(frase1[c])
print(lista1)

lista2 = []
for c in range(len(frase1), 0, -1):
    lista2.append(lista1[c-1])
print(lista2)

palindromo = (''.join(lista2))
print(frase1)
print(palindromo)

if palindromo == frase1:
    print('Essa frase é um Palíndromo')
else:
    print('Essa frase NÃO é um Palíndromo')
