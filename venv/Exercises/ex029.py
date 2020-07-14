'''Escreva um programa que leia a velocidade de um carro
Se ele ultrapassar 80Km/h, mostre um mensagem dizendo que ele foi multado
A multa vai custar R$7,00 por cada Km acima do limite'''
v = int(input('Qual a velocidade do carro em Km/h?: '))
if v > 80:
    print('Você está acima da velocidade permitida e foi multado')
    print('O valor da multa é de R${:.2f}'.format((v-80)*7))
else:
    print('Você não está acima da velocidade permitida')
print('Tenha um bom dia, dirija com segurança')
print('FIM')
