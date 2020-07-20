'''Crie um programa que leia o nome, ano de nascimento e carteira de trabalho
e cadastre-os (com idade) em um dicionário e se por acaso a CTPS for diferente de ZERO,
o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoas vai se aposentar.'''
from datetime import datetime
cadastro = dict()
print('<< CADASTRO DO TRABALHADOR >>')
cadastro['nome'] = str(input('Nome do trabalhador: ')).strip().title()
cadastro['idade'] = datetime.now().year - int(input('Ano de Nascimento do trabalhador: '))
cadastro['ctps'] = int(input('Número da Carteira de Trabalho se houver (caso não tenha, digite 0 (ZERO)): '))
if cadastro['ctps'] != 0:
    cadastro['a_contribuição'] = datetime.now().year - int(input('Ano de Contratação: '))
    cadastro['salario'] = float(input('Salário (R$): '))
cadastro['aposentar'] = (55 - (cadastro['a_contribuição'])) + cadastro['idade']
print('\n == CADASTRO TRABALHADOR ==')
print(f'Nome do Trabalhador: {cadastro["nome"]}')
print(f'Idade atual do Trabalhador: {cadastro["idade"]}')
print(f'Número da CTPS do Trabalhador: {cadastro["ctps"]}')
print(f'Anos de contribuição: {cadastro["a_contribuição"]}')
print(f'Salário do Trabalhador: R${cadastro["salario"]}')
print(f'Irá se aposentar com {cadastro["aposentar"]} anos de idade.')
