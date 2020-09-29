lista = []
while True:
    while True:
        try:
            n = float(input('Digite um número inteiro: '))
            lista.append(n)
            break
        except:
            print('ERRO! Digite um número real')
    print(lista)
    print(f'O maior número é {max(lista)}')
    print(f'O menor número é {min(lista)}')
    print('-' * 50)
