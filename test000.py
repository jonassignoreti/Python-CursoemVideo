'''Faça um programa que leia uma número de CPF
e mostre na tela o CPF digitado'''
cpf = str(input('Digite seu C.P.F.: ')).strip()
cpf = cpf.replace('.', '')
cpf = cpf.replace('-', '')
cpf = cpf.replace(',', '')
cpf = cpf[:11]
cpf = str(cpf[:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:])
print('Seu C.P.F. é o: {}'.format(cpf))
