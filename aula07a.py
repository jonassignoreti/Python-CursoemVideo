# OPERADORES ARITMÉTICOS
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
# + Adição
print('Adição', n1+n2)
# - Subtração
print('Subtração', n1-n2)
# * Multiplicação
print('Multiplicação', n1*n2)
# / Divisão
print('Divisão', n1/n2)
# ** Potenciação
print('Potenciação', n1**n2)
print('Potenciação usando "pow(_,_)"', pow(n1,n2))
# Radiação ex: Raíz quadrada de 81: 81**(1/2)
print('Raíz', n1**(1/n2))
# // Divisão inteira
print('Divisão inteira', n1//n2)
# % Resto da Divisão
print('Resto da Divisão', n1%n2)
# == igualdade

#ORDEM DE PRECEDÊNCIA
#1. (), entre parênteses
#2. **, potenciação
#3. * / // %, multiplicação, divisão, divisão inteira e resto da divisão
#4. + -, adição e subtração

#Usando Operações com Strings
print('Oi'*5) #Imprime Oi 5 vezes
