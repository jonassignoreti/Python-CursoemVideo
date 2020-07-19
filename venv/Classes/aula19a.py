'''VARIÁVEIS COMPOSTAS, DICIONÁRIOS'''
print('-=' * 30, '\nCriando um Dicionário')
pessoas = {'nome': 'Jonas', 'sexo': 'M', 'idade': 27}
print(pessoas)
print(pessoas['nome'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print('\n', '-=' * 30, '\nComandos para exibição de chaves e valores de um dicionário')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print('\n', '-=' * 30, '\nComandos para exibição de chaves e valores de um dicionário dentro de um laço')
for k in pessoas.keys():
    print(k)
for v in pessoas.values():
    print(v)
for k, v in pessoas.items():
    print(f'{k} = {v}')
print('\n', '-=' * 30, '\nDeletando um item do dicionário')
del pessoas['sexo']
print(pessoas)
print('\n', '-=' * 30, '\nAlterando um item do dicionário')
pessoas['nome'] = 'Leandro'
print(pessoas)
print('\n', '-=' * 30, '\nAdicionando um item do dicionário')
pessoas['peso'] = 75.5
print(pessoas)