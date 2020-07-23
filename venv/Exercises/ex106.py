'''Faça um mini-sistema que utilize o INTERACTIVE HELP do Python.
Ousuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra 'FIM', O programa se encerrará.
Obs: Use cores.'''
c = ('\033[m',          # 0 sem cores
     '\033[0;30;41m',   # 1 vermelho
     '\033[0;30;42m',   # 2 verde
     '\033[0;30;43m',   # 3 amarelo
     '\033[0;30;44m',   # 4 azul
     '\033[0;30;45m',   # 5 roxo
     '\033[7;30m'       # 6 branco
     )

def line(n=30):
    """
    -> Mostra na tela uma linha tracejada
    :param n: o número de traços (tamanho da linha)
    :return: uma linha tracejada na tela
    """
    print('-' * n)


def title(txt, cor=0):
    """
    Exibe o texto em formato de título sobre duas linhas
    :param txt: o texto a ser mostrado
    :return: -
    """
    t = len(txt) + 6
    txt = txt.strip().upper()
    print(c[cor], end='')
    line(t)
    print(f'{txt:^{t}}')
    line(t)
    print(c[0], end='')


def int_help(f):
    from time import sleep
    title(f'acessando o manual do comando "{f}"', cor=4)
    sleep(1)
    print(c[6], end='')
    help(f)
    print(c[0], end='')


while True:
    title('SISTEMA DE AJUDA PyHELP', cor=2)
    resp = str(input(f'{c[5]}Função ou Biblioteca > {c[0]} ')).strip().lower()
    if resp == 'fim':
        title('PROGRAMA FINALIZADO', cor=1)
        break
    int_help(resp)
