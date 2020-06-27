print('Somando vários valores com estrutura de repetição')
s = 0
for c in range(0, 10):
    n = float(input('Digite um número: '))
    s += n # é igual a 's = s + n'
print('A somatória de todos os valores foi {}'.format(s))
