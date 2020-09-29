from pacotes.colors import *

def line(size=0):
    print('-' * size)


def double_line(size=0):
    print('=' * size)


def title(txt, size=0):
    """
    --------------------------------------------------
                            'txt'
    --------------------------------------------------
    :param txt: the text in the center
    :param size: size of the lines
    :return: a title like the one above
    """
    if size == 0:
        size = len(txt) + 10
        double_line(size)
        print(f'{txt:^{size}}')
        double_line(size)
    else:
        double_line(size)
        print(f'{txt:^{size}}')
        double_line(size)


def error(msg):
    """
    :param msg: enter a message of error
    :return: return a message with letters in red color
    """
    print(f'{txt_white(back_red(msg))}')


def readInt(msg, errormsg):
    while True:
        print(msg, end='')
        ans = str(input('')).strip()
        if ans.isnumeric():
            ans = int(ans)
            return ans
        else:
            error(errormsg)


def menu(list, size):
    title('MAIN MENU', size)
    c = 1
    back_blue(f=1)
    for i in list:
        print(f'{txt_yellow(back_aqua(c))}', end='')
        back_blue(f=1)
        txt_white(f=1)
        print(f' - {i}')
        c += 1
        back_red(f=1)
    double_line(size)
    style_none(f=1)
    while True:
        opt = readInt('your option: ', 'ERROR!, is not a integer number.')
        if 0 < opt <= len(list):
            break
        else:
            error('ERROR!, select a valid option.')
            continue
    return opt
