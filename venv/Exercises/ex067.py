'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo'''
while True:
    valor = int(input('Digite um valor: '))
    print('-' * 30)
    if valor < 0:
        break
    for c in range (1, 11):
        print(f'{valor} x {c} = {valor * c}')
    print('-' * 30)
print('PROGRAMA FINALIZADO')