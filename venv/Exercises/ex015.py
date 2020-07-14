d = int(input('Quantos dias alugados?: '))
km = float(input('Quantos Km rodados?: '))
a = (60 * d) + (0.15 * km)
print('O valor do aluguel por {} dias e {}Km rodados é de R${:.2f}'.format(d, km, a))
