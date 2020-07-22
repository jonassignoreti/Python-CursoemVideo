'''Faça um programa que tenha uma função chamada escreva(),
que receba um texto qualquer como parâmetro
e mostre uma mensagem com tamanho adaptável
Ex:
escreva('Olá, Mundo!')
Saída:
-----------------
   Olá, Mundo!
-----------------'''
def escreva(txt):
    t = len(txt) + 6
    print('-' * (t))
    print(f'{txt:^{t}}')
    print('-' * (t))


texto = str(input('Digite o Título: ')).strip().title()
escreva(texto)
