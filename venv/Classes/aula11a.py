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
print('\33[31mOlá Mundo!') #letra vermelha
print('\33[31;43mOlá Mundo!') #letra vermelha, fundo amarelo
print('\33[1;31;43mOlá Mundo!') #Negrito, letra vermelho, fundo amarelo
print('\33[1;31;43mOlá Mundo!\033[m') #finalizando a formatação
print('\33[4;30;45mOlá Mundo!\033[m') #Sublinhado, letra branca, fundo lilás
print('\33[30mOlá Mundo!\033[m') #Letra branca
print('\33[7;30mOlá Mundo!\033[m') #invertendo as cores, letra branca, fundo padrão preto, fica letra preta, fundo branco
print('\33[7;33;44mOlá Mundo!\033[m') #letra amarela, fundo azul invertendo fica >>>

'''Há outras formas de colorir as letras com a biblioteca "colorize"'''

a = 2
b = 3
print('Os valores são \033[36m{}\033[m e \033[31m{}\033[m!!!'.format(a, b)) #Usando dentro dos prints

nome = 'Jonas'
print('Olá, muito prazer em te conhecer, {}{}{}!'.format('\033[4;34m', nome, '\033[m')) #Usando dentro do .format

# Usando Dicionários
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;30m'}
print('Olá, muito prazer em te conhecer, {}{}{}!'.format(cores['pretoebranco'], nome, cores['limpa']))
