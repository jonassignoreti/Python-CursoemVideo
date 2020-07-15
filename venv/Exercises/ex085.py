'''Crie um programa onde o usuário possa digitar sete valores numéricos
e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
No final, mostre os valores pares e ímpares em ordem crescente'''
lista = list()
par = list()
impar = list()

for c in range(0, 7):
    entrada = int(input(f'Digite o {c + 1}º número: '))
    if entrada % 2 == 0:
        par.append(entrada)
    else:
        impar.append(entrada)
par.sort()
impar.sort()
lista.append(par)
lista.append(impar)

if len(lista[0]) == 0:
    print('Não foi digitado nenhum número par')
elif len(lista[0]) == 1:
    print(f'O número par digitado foi: {lista[0]}')
else:
    print(f'Os números pares digitados foram: {lista[0]}')

if len(lista[1]) == 0:
    print('Não foi digitado nenhum número ímpar')
elif len(lista[1]) == 1:
    print(f'O número ímpar digitado foi {lista[1]}')
else:
    print(f'Os números ímpares digitados foram: {lista[1]}')
