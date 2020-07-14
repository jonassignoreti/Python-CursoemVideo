'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre:
A) Quantas vezes apareceu o valor 9;
B) Em que posição foi digitado o valor 3;
C) Quais foram os números pares;'''
tupla = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')))
print('-=' * 15)
print(f'O número 9 apareceu {tupla.count(9)} vezes')
print('-=' * 15)
if 3 in tupla:
    print(f'O número 3 foi digitado na {tupla.index(3) + 1}ª posição')
else:
    print('O número 3 não foi digitado em nenhuma posição.')
print('-=' * 15)
v = 0
for n in tupla:
    if n % 2 == 0:
        v += 1
if v == 0:
    print('Não foi digitado nenhum valor par.')
else:
    print(f'Os número pares são ', end='')
    for n in tupla:
        if n % 2 == 0:
            print(n, end=' ')
