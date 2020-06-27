'''Refaça o DESAFIO 035 dos triângulos,
acrescentando o recurso de mostrar que tipo de triângulo será formado:
-EQUILÁTERO: todos os lados iguais
-ISÓSCELES: dois lados iguais
-ESCALENO: todos os lados diferentes'''
r1 = float(input('Primeira reta do triângulo: '))
r2 = float(input('Segunda reta do triângulo: '))
r3 = float(input('Terceira reta do triângulo: '))
if ((r1 + r2) > r3) and ((r1 + r3) > r2) and ((r2 + r3) > r1):
    print('Essas retas podem formar um triângulo')
    if r1 == r2 == r3:
        print('Esse triângulo é Equilátero.')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Esse triângulo é Isósceles.')
    elif r1 != r2 != r3 != r1:
        print('Esse triângulo é Escaleno.')
else:
    print('Essas retas NÃO podem formar um triângulo')
print('FIM')
