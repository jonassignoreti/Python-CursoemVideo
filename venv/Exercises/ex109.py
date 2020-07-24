'''Modifique as funções que foram criadas no desafio 107 para que elas aceitem um um parâmetro a mais,
informando se o valor retornado por elas vai ser ou não formatado pela função moeda(),
desenvolvida no desafio 108.'''
from pacotes import moedas

p = float(input('Digite o preço R$: '))
print(f'A metade de {moedas.moeda(p)} é {moedas.metade(p, format=True)}')
print(f'O dobro de {moedas.moeda(p)} é {moedas.dobro(p, format=True)}')
print(f'Aumentando 10%, temos {moedas.aumentar(p, 10, format=True)}')
print(f'Reduzindo 13%, temos {moedas.diminuir(p, 13, format=True)}')
