tempo = int(input('Quanto tempo tem seu carro: '))
print('Seu carro é novo' if tempo <= 3 else 'Seu carro é velho')
'''if tempo <= 3:
    print('Seu carro é novo')
else:
    print('Seu carro é velho')'''
print('------')

nome = str(input('Diga seu nome: ')).title().strip()
if 'Jonas' in nome:
    print('Que lindo nome você tem')
print('Prazer conhecer-lô {}'.format(nome))
print('------')

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1 + n2)/2
print('Sua nota Média é {:.1f}'.format(m))
if m >= 7:
    print('Parabéns, você foi aprovado!')
else:
    print('Que pena, você foi reprovado.')
print('------')
