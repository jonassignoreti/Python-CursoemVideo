'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre:
-A média de idade do grupo;
-Qual é o nome do homem mais velho;
-Quantas mulheres têm menos de 20 anos'''
cardinal = ('primeira', 'segunda', 'terceira', 'quarta')
idade_total = 0
idade_velho = 0
n_mulheres_menos20anos = 0
for c in range(0, 4):
    print('-=' * 70)
    nome = str(input('Digite o nome da {} pessoa: '.format(cardinal[c]))).strip().capitalize()
    idade = int(input('Digite a idade da {} pessoa: '.format(cardinal[c])))
    sexo = str(input('Digite o sexo da {} pessoa, [ F ] = Feminino, [ M ] = masculino: '.format(cardinal[c]))).strip().capitalize()
    idade_total += idade

    if sexo[0] == 'M' and idade > idade_velho:
        idade_velho = idade
        velho = nome

    if sexo[0] == 'F' and idade < 20:
        n_mulheres_menos20anos += 1
print('-=' * 20, ' RESULTADO ', '-=' * 20)
media = idade_total / 4
print('A média de idade do grupo é {:.0f} anos;'. format(media))

print('O nome do homem mais velho é {};'.format(velho))
print('Há {} mulheres com menos de 20 anos de idade no grupo.'.format(n_mulheres_menos20anos))