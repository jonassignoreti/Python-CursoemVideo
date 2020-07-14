'''Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''
tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = -1
    while True:
        num = int(input('Digite um número entre 0 e 20: '))
        if 0 <= num <= 20:
            break
        print('Tente Novamente')
    print(f'Você digitou o número {tupla[num]}.')
    cntn = ' '
    while cntn not in 'SN':
        cntn = str(input('Deseja continuar [S/N]:')).strip().upper()
    if cntn[0] == 'N':
        break
print('PROGRAMA FINALIZADO')