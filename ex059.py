'''Crie um programa que leia dois valores e mostre um menu na tela:
[1]Somar
[2]Multiplicar
[3]Maior
[4]Novos números
[5]Sair do programa
Seu programa deverá realizar a operação solicitada em cada caso'''
menu = 0
while menu != 5:
    print('{:-^50}'.format('\033[36mNOVA OPERAÇÃO\033[m'))
    n1 = float(input('Digite o primeiro valor: '))
    n2 = float(input('Digite o segundo valor: '))
    print('{:-^50}'.format('\033[36mESCOLHA A OPERAÇÃO\033[m'))
    menu = int(input('[1]Somar\n[2]Multiplicar\n[3]Maior\n[4]Novos números\n[5]Sair do programa\nDigite uma operação: '))
    if menu != 5:
        if menu == 1:
            soma = n1 + n2
            print('\033[31mA soma entre {} e {} é {}.\033[m'.format(n1, n2, soma))
        if menu == 2:
            multiplicacao = n1 * n2
            print('\033[31mA multiplicação entre {} e {} é {}.\033[m'.format(n1, n2, multiplicacao))
        if menu == 3:
            if n1 > n2:
                maior = n1
                print('\033[31mO maior número digitado foi: {}.\033[m'.format(maior))
            elif n1 < n2:
                maior = n2
                print('\033[31mO maior número digitado foi: {}.\033[m'.format(maior))
            else:
                print('\033[31mImpossível, os dois números são iguais.\033[m')
print('\033[7;30mPROGRAMA FINALIZADO\033[m')
