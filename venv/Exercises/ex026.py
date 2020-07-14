'''Faça um programa que leia uma frase pelo teclado e mostre:
-Quantas vezes aparece a letra "A"
-Em que posição ela aparece a primera vez
-Em quem posição ela aparece a última vez'''
from unidecode import unidecode
frase = str(input('Digite uma frase: ')).strip()
letra = str(input('Qual letra deseja buscar: ')).strip()
letra = letra.lower()
frase0 = unidecode(frase.lower()) #tira todas as acentuações da String.
print('Na frase "{}" há {} letras "{}"'.format(frase, frase0.count(letra), letra.capitalize()))
print('O primeiro "{}" está na posição {}'.format(letra.capitalize(), frase0.find(letra)))
print('O último "{}" está na posição {}'.format(letra.capitalize(), frase0.rfind(letra)))
