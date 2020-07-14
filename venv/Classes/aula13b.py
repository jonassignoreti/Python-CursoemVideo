print('Contando quantas vezes for pedido no valor de entrada')
n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)
print('END')

from time import sleep
print('Aguardando um tempo')
n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)
    sleep(1)
print('END')

from time import sleep
print('entradando com mais variáveis')
i = int(input('Digite o valor de Ínicio: '))
f = int(input('Digite o valor Final: '))
p = int(input('Digite o valor de passo: '))
t = int(input('Digite o valor do tempo de cada passo em segundo: '))
for c in range(i, f, p):
    print(c)
    sleep(t)
print('END')
