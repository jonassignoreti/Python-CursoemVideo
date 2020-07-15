'''Faça um programa que leia o nome e o peso de várias pessoas, quardando tudo em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas
B) Uma listagem com as pessoas mais pesadas
C) Uma listagem com pessoas mais leves'''
#Variáveis
pessoas = list()
dados = list()
somapeso = 0
media = 0
pesado = list()
leve = list()

# Título do Programa
print('=-' * 30)
print('RELAÇÃO DE PESSOAS POR PESO')
print('=-' * 30)
# Entrada de dados
while True:
    dados.append(str(input('Digite o nome da pessoa: ')).strip().capitalize())
    dados.append(int(input(f'Digite a idade do(a) {dados[0]}: ')))
    dados.append(float(input(f'Digite o peso (Kg) do(a) {dados[0]}: ')))
    pessoas.append(dados[:])
    dados.clear()
    c = str(input('Deseja Continuar? [S/N]: ')).upper().strip()
    while not (c.__contains__('S') or c.__contains__('N')):
        print('Código Inválido, tente novamente.')
        c = str(input('Deseja Continuar? [S/N]: ')).upper().strip()
    if c == 'N':
        break
    print('-' * 60)

# Processamento dos dados
for i, v in enumerate(pessoas):
    somapeso += pessoas[i][2]
media = somapeso / len(pessoas)

for i, v in enumerate(pessoas):
    if pessoas[i][2] > media:
        pesado.append([pessoas[i][0], pessoas[i][1], pessoas[i][2]])
    if pessoas[i][2] <= media:
        leve.append([pessoas[i][0], pessoas[i][1], pessoas[i][2]])

#Visualização dos resultados
print('-=' * 30)
print(f'Foram cadastradas um total de {len(pessoas)} pessoas')
print(f'A média de peso de todas as pessoas é de {media:.2f}Kg')
print('-' * 20)
print('Pessoas mais leves:')
for i, v in enumerate(leve):
    print(f'Nome: {leve[i][0]}, Idade: {leve[i][1]} anos, Peso: {leve[i][2]}Kg')
print('-' * 20)
print('Pessoas mais pesadas:')
for i, v in enumerate(pesado):
    print(f'Nome: {pesado[i][0]}, Idade: {pesado[i][1]} anos, Peso: {pesado[i][2]}Kg')