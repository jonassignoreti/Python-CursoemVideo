'''Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo"'''
cidade = input('Digite o nome da cidade: ').lower().strip()

print('santo ' in cidade[:6])

city = cidade.split()
print('santo' in city[0])
