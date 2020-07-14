'''Crie um programa que leia o nome completo de uma pessoa e mostre:
-O nome com todas as letras maiúsculas
-O nome com todas as letras minúsculas
-Quantas letras ao todo (sem considerar espaços)
-Quantas letras tem o primeiro nome'''
nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome com todas as letras maiúsculas fica:', nome.upper())
print('Seu nome com todas as letras minúsculas fica: {}'.format(nome.lower()))
letras = nome.split()
print(letras)
print('Ao todo há {} letras no seu nome'.format(len(''.join(letras))))
print('Seu primeiro nome é {} e ele tem {} letras'.format(letras[0], len(letras[0])))
