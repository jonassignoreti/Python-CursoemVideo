'''Aula 21, Funções part 2'''
print('--PARÂMETROS OPCIONAIS--')


def somar(a, b, c=0): #(c) é um parâmetro opcional, se caso não seja colocado nenhuma valor nele, será igual a 0
    s = a + b + c
    print(f'A soma vale {s}')


somar(3, 2, 5)
somar(8, 4)
