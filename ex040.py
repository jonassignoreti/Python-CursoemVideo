'''Crie um programa que leia duas notas de uma aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
-Média abaixo de 5.0: REPROVADO;
-Média entre 5.0 e 6.9: RECUPERAÇÃO;
-Média 7.0 ou superior: APROVADO'''
nome = str(input('Qual o nome do aluno?: ')).strip().capitalize()
na1 = float(input('Digite a nota da primeira avaliação: '))
na2 = float(input('Digite a nota da segunda avaliação: '))
na3 = float(input('Digite a nota da terceira avaliação: '))
na4 = float(input('Digite a nota da quarta avaliação: '))
np = float(input('Digite a nota da prova final: '))
mf = (np * 60/100) + (((na1 + na2 + na3 + na4) / 4) * 40/100)

if mf >= 7:
    print('Parabéns {}! você foi \033[34mAPROVADO\033[m com Média Final {:.1f}.'.format(nome, mf))
elif 5 <= mf and mf <= 6.9:
    print('{}, você está na \033[35mRECUPERAÇÃO\033[m com Média Final {:.1f}.'.format(nome, mf))
else:
    print('Que pena {}, você foi \033[31mREPROVADO\033[m com Média Final {:.1f}.'.format(nome, mf))
