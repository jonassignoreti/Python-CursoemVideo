'''Faça um programa que tenha uma função notas()
que pode receber várias notas de alunos
e vai retornar um dicionário com as seguintes informações:
- Quantidade de notas;
- A maior nota;
- A menor nota;
- A média da turma
- A situação (opcional)
Adicione também as docstrings da função.'''


def notas(*notas, sit=False):
    resultado = dict()
    resultado['total'] = len(notas)
    maior = menor = soma = 0
    for i, v in enumerate(notas):
        if i == 0:
            maior = menor = v
        else:
            if v > maior:
                maior = v
            if v < menor:
                menor = v
        soma += v
    resultado['maior'] = maior
    resultado['menor'] = menor
    resultado['média'] = soma / len(notas)
    if sit:
        if resultado['média'] < 5:
            resultado['situação'] = 'RUIM'
        elif resultado['média'] >= 7:
            resultado['situação'] = 'ÓTIMA'
        else:
            resultado['situação'] = 'BOA'
    return resultado


#Programa principal
resp = notas(9, 10, 6.5, sit=True)
print(resp)
