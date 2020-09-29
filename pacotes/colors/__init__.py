'''CORES NO TERMINAL using the standard ANSI >>> Example "/033[0:30:40m"
STYLE:
    0 = None;
    1 = Bold;
    4 = Underline;
    7 = Negative.
TEXT COLOR:
    30 = White;
    31 = Red;
    32 = Green;
    33 = Yellow;
    34 = Blue;
    35 = Purple;
    36 = Agua;
    37 = Gray.
BACK COLOR:
    40 = White;
    41 = Red;
    42 = Green;
    43 = Yellow;
    44 = Blue;
    45 = Purple;
    46 = Agua;
    47 = Gray.
'''
def style_none(msg='', f=0):
    if f == 1:
        print(f'\033[m', end='')
    else:
        return f'\033[m{msg}\033[m'


def style_bold(msg='', f=0):
    if f == 1:
        print(f'\033[1m', end='')
    else:
        return f'\033[1m{msg}\033[m'


def style_underline(msg='', f=0):
    if f == 1:
        print(f'\033[4m', end='')
    else:
        return f'\033[4m{msg}\033[m'


def style_negative(msg='', f=0):
    if f == 1:
        print(f'\033[7m', end='')
    else:
        return f'\033[7m{msg}\033[m'


def txt_white(msg='', f=0):
    if f == 1:
        print(f'\033[30m', end='')
    else:
        return f'\033[30m{msg}\033[m'


def txt_red(msg='', f=0):
    if f == 1:
        print(f'\033[31m', end='')
    else:
        return f'\033[31m{msg}\033[m'


def txt_green(msg='', f=0):
    if f == 1:
        print(f'\033[32m', end='')
    else:
        return f'\033[32m{msg}\033[m'


def txt_yellow(msg='', f=0):
    if f == 1:
        print(f'\033[33m', end='')
    else:
        return f'\033[33m{msg}\033[m'


def txt_blue(msg='', f=0):
    if f == 1:
        print(f'\033[34m', end='')
    else:
        return f'\033[34m{msg}\033[m'


def txt_purple(msg='', f=0):
    if f == 1:
        print(f'\033[35m', end='')
    else:
        return f'\033[35m{msg}\033[m'


def txt_aqua(msg='', f=0):
    if f == 1:
        print(f'\033[36m', end='')
    else:
        return f'\033[36m{msg}\033[m'


def txt_gray(msg='', f=0):
    if f == 1:
        print(f'\033[37m', end='')
    else:
        return f'\033[37m{msg}\033[m'


def back_white(msg='', f=0):
    if f == 1:
        print(f'\033[40m', end='')
    else:
        return f'\033[40m {msg} \033[m'


def back_red(msg='', f=0):
    if f == 1:
        print(f'\033[41m', end='')
    else:
        return f'\033[41m {msg} \033[m'


def back_green(msg='', f=0):
    if f == 1:
        print(f'\033[42m', end='')
    else:
        return f'\033[42m {msg} \033[m'


def back_yellow(msg='', f=0):
    if f == 1:
        print(f'\033[43m', end='')
    else:
        return f'\033[43m {msg} \033[m'


def back_blue(msg='', f=0):
    if f == 1:
        print(f'\033[44m', end='')
    else:
        return f'\033[44m {msg} \033[m'


def back_purple(msg='', f=0):
    if f == 1:
        print(f'\033[45m', end='')
    else:
        return f'\033[45m {msg} \033[m'


def back_aqua(msg='', f=0):
    if f == 1:
        print(f'\033[46m', end='')
    else:
        return f'\033[46m {msg} \033[m'


def back_gray(msg='', f=0):
    if f == 1:
        print(f'\033[47m', end='')
    else:
        return f'\033[47m {msg} \033[m'
