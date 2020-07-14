'''Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente
EX: Ana Maria de Souza
primeiro: Ana
segundo: Souza'''
name = input('Digite o seu nome completo: ')
names = name.split()
print('Primeiro nome: {}'.format(names[0]))
print('Último nome: {}'.format(names[len(names) - 1]))
