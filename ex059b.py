from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do Programa''')
    opção = int(input('>>>>> Qual é a sua opção: '))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, soma))
        sleep(2)
    elif opção == 2:
        produto = n1 * n2
        print('O produto entre {} e {} é {}'.format(n1, n2, produto))
        sleep(2)
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior número é {}'.format(n1, n2, maior))
        sleep(2)
    elif opção == 4:
        print('Informe os números novamente')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
        sleep(1)
    else:
        print('Opção inválida. Tente novamente')
        sleep(1)
    print('=-=' * 20)
print('Fim do programa, volte sempre!')