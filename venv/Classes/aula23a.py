'''Aula 3, Tratamento de Erros'''

'''Exception'''
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b
    '''except Exception as erro:
    print(f'Problema encontrado foi {erro.__class__}')'''
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou')
except ZeroDivisionError:
    print('Não é possível dividir um número por Zero')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados')
else:
    print(f'O resultado da divisão é: {r}')
finally:
    print('Volte sempre! Muito Obrigado!')
