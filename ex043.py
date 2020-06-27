'''Desenvolva uma lógica que leia o peso uma altura de uma pessoa,
calcule seu IMC e mostre seu status, de acordo com a tabela abaixo.
-Abaixo de 18.5: Abaixo do peso;
-Entre 18.5 e 25: Peso ideal;
-Entre 25 até 30: Sobrepeso;
-Entre 30 até 40: Obesidade;
-Acima de 40: Obesidade Mórbida'''
peso = float(input('Digite o peso da pessoa em Kg: '))
altura = float(input('Digite a altura da pessoa em Metros: '))
imc = peso / altura ** 2

if imc < 18.5:
    print('Seu IMC é {:.2f}, que se classifica como ABAIXO DO PESO.'.format(imc))
elif imc <= 25:
    print('Seu IMC é {:.2f}, que se classifica como PESO IDEAL.'.format(imc))
elif imc <= 30:
    print('Seu IMC é {:.2f}, que se classifica como SOBREPESO.'.format(imc))
elif imc <= 40:
    print('Seu IMC é {:.2f}, que se classifica como OBESIDADE.'.format(imc))
else:
    print('Seu IMC é {:.2f}, que se classifica como OBESIDADE MÓRBIDA'.format(imc))
