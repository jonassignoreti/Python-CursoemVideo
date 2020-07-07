'''Crie um programa  que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados;
B) A lista de valores, ordenada de forma decrescente;
C) Se o valor 5 foi digitado e está ou não na lista'''

lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    cond = str(input('Deseja continuar? [S/N]: ')).strip()
    while 'SsNn' in cond:
        print('Código Inválido, tente novamente:')
        cond = str(input('Deseja continuar? [S/N]: '))

    if 'Nn' in cond:
        break
print('-=' * 30)

print(f'foram digitados {len(lista)} itens na lista')
lista.sort(reverse=True)
print(f'Os valores da lista ordenados de forma decrescente: {lista}')
pos = 0
while pos < len(lista):
    if lista[pos] == 5:
        print('O valor 5 foi digitado, e está na lista')
        break
    elif pos == len(lista) - 1:
        print('O número 5 não foi digitado, portanto não está na lista')
        break
    else:
        pos += 1
