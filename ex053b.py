from unidecode import unidecode
frase0 = str(input('Digite uma frase: ')).strip().upper()
frase = unidecode(frase0)
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
'''inverso = junto[::-1]''' #Outra forma de fazer a inversão
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada NÃO é um Palíndromo.')
