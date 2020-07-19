'''Faça um programa que leia nome e média de um aluno,
guardando também sua situação em uma dicionário.
No final, mostre o conteúdo da estrutura na tela.'''
aluno = dict()
aluno['nome'] = str(input('Digite o nome do aluno: ')).title().strip()
aluno['media'] = float(input(f'Digite a média de {aluno["nome"]}: '))
while aluno['media'] < 0 or aluno['media'] > 10:
    print('VALOR INVÁLIDO. Digite um valor entre 0 e 10.')
    aluno['media'] = float(input(f'Digite a média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situação'] = 'APROVADO(A)'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'RECUPERAÇÃO'
else:
    aluno['situação'] = 'REPROVADO(A)'
print('-=' * 30)
print(f'-Nome do aluno(a): {aluno["nome"]}')
print(f'-Média é igual a: {aluno["media"]}')
print(f'-Situação de {aluno["nome"]} é {aluno["situação"]}')
