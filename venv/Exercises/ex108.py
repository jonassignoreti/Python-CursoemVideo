'''Adapte o código do desafio 107,
criando uma função adicional chamada moeda()
que consiga mostrar os valores como um valor monetário formatado'''

from pacotes import moedas

p = float(input('Digite o preço R$: '))
print(f'A metade de {moedas.moeda(p)} é {moedas.moeda(moedas.metade(p))}')
print(f'O dobro de {moedas.moeda(p)} é {moedas.moeda(moedas.dobro(p))}')
print(f'Aumentando 10%, temos {moedas.moeda(moedas.aumentar(p, 10))}')
print(f'Reduzindo 13%, temos {moedas.moeda(moedas.diminuir(p, 13))}')
