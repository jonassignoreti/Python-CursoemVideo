'''VARIÁVEIS COMPOSTAS, DICIONÁRIOS'''
print('\n', '-=' * 30, '\nCriando um dicionário dentro de uma lista')
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print('\n', '-=' * 30, '\nExibindo disferentes itens dos dicionários')
print(brasil[0]['uf'])
print(brasil[1]['sigla'])
