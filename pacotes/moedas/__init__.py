from pacotes import formatação


def moeda(valor=0, moeda='R$'):
    r = f'{moeda}{valor:.2f}'.replace('.', ',')
    return r


def aumentar(v=0, por=0, format=False):
    r = v + (v * (por / 100))
    if format:
        r = moeda(r)
    return r


def diminuir(v=0, por=0, format=False):
    r = v - (v * (por / 100))
    if format:
        r = moeda(r)
    return r


def dobro(n=0, format=False):
    r = n * 2
    if format:
        r = moeda(r)
    return r


def metade(n=0, format=False):
    r = n / 2
    if format:
        r = moeda(r)
    return r


def leiamoeda(show):
    while True:
        print(show, end='')
        resp = str(input('')).strip().replace(',', '.')
        if resp.isalpha() or resp == '':
            print(f'\033[31mERRO! "{resp}" é um preço inválido.\033[m')
        else:
            resp = float(resp)
            return resp



def resumo(v=0, increase=0, reduction=0):
    tam = 30
    formatação.title('RESUMO DO VALOR', tam)
    print(f'{"Preço analisado:":<20}{moeda(v):>10}')
    print(f'{"Dobro do preço:":<20}{dobro(v, format=True):>10}')
    print(f'{"Metade do preço:":<20}{metade(v, format=True):>10}')
    print(f'{increase}% {"de aumento:":<16}{aumentar(v, increase, format=True):>10}')
    print(f'{reduction}% {"de redução:":<16}{diminuir(v, reduction, format=True):>10}')
    formatação.line(tam)
