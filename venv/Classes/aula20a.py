'''Funções (Parte 1)'''
def soma(a, b):
    print(a + b)

def contador(* num):
    print(num)

def somavários(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os números {valores} temos a soma {s}')


soma(5, 2)
soma(5, 6)
soma(b=9, a=10)

contador(5, 3, 9, 5, 7)
contador(1, 2, 3, 4)

somavários(1, 2, 3, 4, 5, 6)
