'''Crie um programa onde o usuário possa digitar vários valores numéricos, e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.
No final, será exibidos todos os valores únicos digitados, em ordem crescente.'''
lista = []
while True:
    num = int(input('Digite um valor: '))
    if num in lista:
        print('Valor duplicado')
    else:
        lista.append(num)
        print('Valor adicionado com sucesso...')

    while True:
        cond = str(input('Deseja continuar [S/N]: ')).strip().upper()
        if cond != 'S' and cond != 'N':
            print('Código inválido, tente novamente:')
        else:
            break
    if cond in 'N':
        break

print('=-' * 30)
lista.sort()
print(f'Você adicionou os valores {lista}')
