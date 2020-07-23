'''Aula 21, Funções part 2'''
print('--ESCOPO DE VARIÁVEIS--')


def teste(b):
    global a # obriga o programa a não criar outra variável dentro da função, e usa a variável global especificada.
    a = 8 # (a) uma variável local, pois está dentro de uma função (caso não tenha sido declarada como global no início)
    b += 4  # (b) é uma variável local, pois está dentro de uma função
    c = 2  # (c) é uma variável local, pois está dentro de uma função
    print(f'A dentro vale {a}') # << funciona pegando a variável (a) local, caso não exista, ele pega (a) global
    print(f'B dentro vale {b}') # << funciona normalmente
    print(f'C dentro vale {c}') # << funciona normalmente


a=5 # (a) é uma variável global, pois está dentro do programa principal
teste(a)
print(f'A fora vale {a}') # << funciona normalmente
print(f'B fora vale {b}') # << impossível, pois a variável (b) não é global
print(f'C fora vale {c}') # << impossível, pois a variável (c) não é global
