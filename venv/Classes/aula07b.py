
name = input('Qual é o seu nome? ')

# Limitando o espaço de uma variável no String em 20 espaços
print('É um prazer em te Conhecer {:20}!'.format(name))

# Limitando o espaço de uma variável no String em 20 espaços e alinhando a direita
print('É um prazer em te Conhecer {:>20}!'.format(name))

# Limitando o espaço de uma variável no String em 20 espaços e alinhando a esquerda
print('É um prazer em te Conhecer {:<20}!'.format(name))

# Limitando o espaço de uma variável no String em 20 espaços e centralizando o alinhamento
print('É um prazer em te Conhecer {:^20}!'.format(name))

# Limitando o espaço de uma variável no String em 20 espaços e centralizando o alinhamento e preenchendo o restante com =
print('É um prazer em te Conhecer {:=^20}!'.format(name))

# Limitando o número de casas decimais depois da vírgula
print('O valor da divisão com 3 casas decimais flutuantes: {:.3f}'.format(100/3))

# \n para pular para a próxima linha
print('Teste de pular para a \n próxima linha')

# end=' ' no final do print para manter na mesma linha
print('Teste para manter na', end=' ')
print('mesma linha')