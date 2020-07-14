'''ESTRUTURA DE REPETIÇÃO WHILE, LAÇOS DE REPETIÇÃO (PARTE 2)'''
print('*' * 40, '\nEquanto c < 10 faça:')
c = 0
while c < 10: #Enquanto c < 10 faça:
    print(c, end=' ')
    c += 1
print('END')

print('*' * 40, '\nEnquanto o valor digitado NÃO for 0 faça:')
n = 1
while n != 0: #condição de PARADA
    n = int(input('Digite um valor: '))
print('END')

print('*' * 40, '\n:Enquanto não for digitado ZERO(0), conte quantos números são pares e ímpares, e informe no final.')
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Foram digitados {} números pares, e {} números ímpares.'.format(par, impar))
