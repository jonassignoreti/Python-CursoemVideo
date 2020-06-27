'''LAÇOS DE REPETIÇÃO (PARTE 3)'''
n = s = 0
while True: #REPETIÇÃO INFINITA
    n = int(input('Digite um número: '))
    if n == 999:
        break #INTERROMPENDO UMA REPETIÇÃO INFINITA
    s += n
print(f'A soma vale {s}') #Usando F STRINGS

nome = 'Jonas'
idade = 27
salário = 2508.9
print(f'O {nome:-^20} tem {idade} anos e ganha R${salário:.2f}') # <<< formanto uma string
