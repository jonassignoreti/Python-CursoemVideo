'''VARIÁVEIS COMPOSTAS, DICIONÁRIOS'''
print('\n', '-=' * 30, '\nEntrando com dados em um dicionário:')
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy()) #copiando um dicionário dentro de uma lista
print(brasil)
print('\n', '-=' * 30, '\nExibindo dentro de um laço:')
for e in brasil:
    for k, v in e.items():
        print(f'{k} = {v}')
