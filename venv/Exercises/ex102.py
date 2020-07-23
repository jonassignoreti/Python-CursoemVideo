'''Crie um programa que tenha uma função fatorial()
que receba dois parâmetros:
o primeiro que indique o número número a calcular
e o outro chamada show, que será um valor lógico(opcional)
indicando se será mostrado ou não na tela o processo de cálculo do fatorial.'''
def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número.
    :param num: O número a ser calculado
    :param show: Mostrar ou não a conta (opcional).
    :return: O valor do fatorial de um número n.
    """
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show == True:
            print(f'{c} ', end='')
            if c != 1:
                print('x ', end='')
    if show == True:
        print('= ', end='')
    return f


print(fatorial(5))
