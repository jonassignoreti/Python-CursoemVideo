'''Crie um programa que tenha uma função chamada voto()
que vai receber como parÂmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto
NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.'''
from datetime import datetime


def line(n=30):
    """
    -> Mostra na tela uma linha tracejada
    :param n: o número de traços (tamanho da linha)
    :return: uma linha tracejada na tela
    """
    print('-' * n)


def title(txt):
    """
    Exibe o texto em formato de título sobre duas linhas
    :param txt: o texto a ser mostrado
    :return: -
    """
    t = len(txt) + 6
    txt = txt.strip().upper()
    line(t)
    print(f'{txt:^{t}}')
    line(t)


def voto(ano):
    """
    -> Informa se o voto é obrigatório, opcional ou negado em relação ao ano de nascimento
    :param ano: o ano de nascimento da pessoa
    :return: um valor literal (NEGADO, OPCIONAL OU OBRIGATÓRIO)
    """
    idade = datetime.now().year - ano
    if idade < 16:
        return 'NEGADO'
    elif 16 <= idade <= 17 or idade >= 65:
        return 'OPCIONAL'
    else:
        return 'OBRIGATÓRIO'


title('OBRIGATORIDADE DE VOTO')
nasc = int(input('Digite seu ano de nascimento: '))
line(28)
print(f'Para esse ano de {datetime.now().year}, seu voto é {voto(nasc)}')
