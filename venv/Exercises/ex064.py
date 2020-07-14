'''Crie um programa que leia vários números inteiro pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final mostre quantos números foram digitados e qual foi a soma entre eles
(desconsiderando o flag (999))'''
cont = 0
soma = 0
d = 0
while d != 999:
    d = int(input('Digite um número: '))
    if d != 999:
        soma += d
        cont += 1
print('Foram digitados {} números, e a soma entre eles é {}'.format(cont, soma))
print('PROGRAMA FINALIZADO')
