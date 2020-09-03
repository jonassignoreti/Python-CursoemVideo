'''Reescreva a função leiaInt() que fizemos no desafio 104,
incluindo agora a possibilidade da digitação de um número de tipo inválido.
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade'''


def leiaInt():
    while True:
        try:
            r = int(input('Digite um Número Inteiro: '))
            return r
        except:
            print(f'\033[31mERRO: por favor, digite um número inteiro válido\033[m')
            continue


def leiaFloat():
    while True:
        try:
            r = float(input('Digite um Número Real: '))
            return r
        except:
            print(f'\033[31mERRO: por favor, digite um número real válido\033[m')
            continue


n_int = leiaInt()
n_float = leiaFloat()
print(f'O valor inteiro digitado foi {n_int} e o real foi {n_float}')
