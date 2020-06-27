'''Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome'''
name = str(input('Digite seu nome: ')).lower().strip()
search = str(input('Sua busca: ')).lower()
print(search in name)
