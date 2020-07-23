'''Crie um programa que tenha a função leiaInt(),
que vai funcionar de forma semelhante à função input do Python,
só que fazendo a validação para aceitar apenas um valor numérico.
Ex:
n = leiaInt('Digite um n')'''
def leiaInt(show):
    global n
    while True:
        print(show, end='')
        resp = str(input('')).strip()
        if resp.isnumeric():
            return resp
        else:
            print(f'\033[31mERRO! Digite um número inteiro válido.\033[m')


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')