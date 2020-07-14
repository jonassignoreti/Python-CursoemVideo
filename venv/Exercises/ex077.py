'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são suas vogais.'''
palavra = ''
tupla = ('APRENDER',
         'PROGRAMAR',
         'LINGUAGEM',
         'PYTHON',
         'CURSO',
         'GRATIS',
         'ESTUDAR',
         'PRATICAR',
         'TRABALHAR',
         'MERCADO',
         'PROGRAMADOR',
         'FUTURO')
for pos in tupla:
    print(f'\nNa palavra {pos} temos ', end='')
    for letra in pos:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')




'''for pos in range(0, len(tupla)):
    palavra = tupla[pos]
    print(f'\nNa palavra {tupla[pos]} temos as vogais ', end='')
    for c in range(0, len(palavra)):
        if palavra[c] == 'A':
            print('a', end=' ')
        if palavra[c] == 'E':
            print('e', end=' ')
        if palavra[c] == 'I':
            print('i', end=' ')
        if palavra[c] == 'O':
            print('o', end=' ')
        if palavra[c] == 'U':
            print('u', end=' ')'''
