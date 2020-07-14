'''Crie um programa que leia vários números inteiro pelo teclado.
No final da execução mostre a média entre todos os valores
e qual foi o maior e o menor valores lidos.
O Programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''
cont = 0
soma = 0
maior = 0
menor = 0
valor = 1
continuar = ''
while valor != 0:
    print('*' * 50)
    valor = int(input('Digite um valor: '))
    soma += valor
    if cont == 0:
        maior = menor = valor
    if maior < valor:
        maior = valor
    if menor > valor:
        menor = valor
    cont += 1
    continuar = ''
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('Deseja Continuar? [S/N]: ')).strip().upper()
        if continuar != 'S' and continuar != 'N':
            print('Código inválido.')
    if continuar == 'N':
        valor = 0
    elif continuar == 'S':
        valor = 1
media = soma / cont
print('*' * 50)
print('A média dos {} valores é igual a {:.3f}'.format(cont, media))
print('Maior número: {}, Menor número: {}'.format(maior, menor))
print('PROGRAMA FINALIZADO')
