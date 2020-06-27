import math #importando a biblioteca math ou 'from math import sqrt' para importar uma única função de uma biblioteca
num = int(input('Digite um número: '))
raiz = math.sqrt(num) #caso importe uma única função, usar apenas o nome da função, exemplo: 'raiz = sqrt.(num)'
print('A raiz quadrada de {} é {:.2f}'.format(num, raiz))
