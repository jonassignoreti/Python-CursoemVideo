'''Aula 21, Funções part 2'''
print('--RETORNANDO VALORES--')


def somar(a=0, b=0, c=0):
    """
    -> Soma os valores dentro dos parâmtros
    :param a: primeiro parâmetro, sendo opcional, por padrão é 0
    :param b: segundo parâmetro, sendo opcional, por padrão é 0
    :param c: terceiro parâmetro, sendo opcional, por padrão é 0
    :return: retorno o valor da soma dos parâmetros de entrada.
    """
    s = a + b + c
    return s


r1 = somar(3, 2, 5)
r2 = somar(8, 4)
r3 = somar(5)
print(f'Meus cálculos deram {r1}, {r2} e {r3}')
