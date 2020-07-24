'''Dentro do pacote que criamos no desafio 111,
temos um módulo chamado dado.
Crie uma função chamada leiamoeda()
que seja capaz de funcionar como função input(),
mas com uma validação de dados para aceitar apenas valores que sejam monetários
Ex: 856,00'''
from pacotes import moedas

p = moedas.leiamoeda('Digite um preço R$')
moedas.resumo(p, 10, 10)
