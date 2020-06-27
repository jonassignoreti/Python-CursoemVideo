'''A confederação Nacional de Natação precisa de um programa que leia
o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
-Até 9 anos: MIRIM;
-Até 14 anos: INFANTIL;
-Até 19 anos: JUNIOR;
-Até 20 Anos: SÊNIOR;
-Acima: MASTER.'''
from datetime import date
nome = str(input('Digite o nome do atleta: ')).strip().capitalize()
ano_nascimento = int(input('Digite o ano de nascimento do atleta: '))
idade = date.today().year - ano_nascimento

if idade <= 9:
    print('O Atleta {} tem {} anos de idade, portanto é da categoria \033[36mMIRIM\033[m'.format(nome, idade))
elif idade <= 14:
    print('O Atleta {} tem {} anos de idade, portanto é da categoria \033[36mINFANTIL\033[m'.format(nome, idade))
elif idade <= 19:
    print('O Atleta {} tem {} anos de idade, portanto é da categoria \033[36mJUNIOR\033[m'.format(nome, idade))
elif idade <= 25:
    print('O Atleta {} tem {} anos de idade, portanto é da categoria \033[36mSÊNIOR\033[m'.format(nome, idade))
else:
    print('O Atleta {} tem {} anos de idade, portanto é da categoria \033[36mMASTER\033[m'.format(nome, idade))
