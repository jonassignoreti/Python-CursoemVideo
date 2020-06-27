frase = 'Curso em Vídeo Python'
frase2 = '   Aprenda Python  '
print(frase) #imprime a variável "frase"
print(frase[3]) #mostra o caractere 3
print(frase[3:13]) #mostra do caractere 3 até o 13
print(frase[:14]) #mostra do ínicio até o 14
print(frase[9:]) #mostra do 9 até o final
print(frase[1:14:2]) #mostra do 1 ao 14 pulando de 2 em 2 "urso em Video" > us mVdo
print("""Welcome! Are you completely new to programming?
If not then we presume you will be looking for information 
about why and how to get started with Python. 
Fortunately an experienced programmer in any 
programming language (whatever it may be) 
can pick up Python very quickly. 
It's also easy for beginners to use and learn, s
o jump in!""") #imprime pulando as linhas

print(frase.count('o')) #conta quantas vezes aparece a letra 'o'
print(frase.upper().count('o')) #combinando: passando tudo para maiúsculas e contando quantas vezes aparece 'o'
print('Curso' in frase) #mostra True or False se 'Curso' está na string frase
print(frase.find('Curso')) #procura 'Curso' e mostra em qual caractere inicia
print(frase.find('Python')) #procura 'Python' e mostra em qual caractere inicia
print(len(frase)) #conta quantos caracteres há na string

print(frase.upper()) #Substitui todas as letras para MAIÚSCULAS
print(frase.lower()) #Substitui todas as letras para minúsculas
print(frase.capitalize()) #Inicia a frase com Maiúsculas e todas as outras em minúsculas
print(frase.title()) #Começa Cada Palavra Em Maiúsculas <<<

print(frase.split()) #Divide a frase em uma lista nos espaços, palavra por palavra
dividido = frase.split() #Jogando a variável dividida em uma lista em outra variável
print(dividido) #imprime a lista
print(dividido[0]) #imprime o item 0 da lista
print(dividido[2][3]) #imprime a letra 3 do segundo item da lista (Vídeo)
print('-'.join(dividido)) #junta todos os itens da lista com '-' (por exemplo) e manda imprimir

print(frase2.strip()) #remove os espaços no começo e final da frase
print(frase2.rstrip()) #remove os espaços a direita da frase (final)
print(frase2.lstrip()) #remove os espaços a esquerda da frase (começo)

print(frase.replace('Python', 'Android')) #procura 'Python' e substitui por 'Android', Mas não altera a variável, apenas mostra sustituido

frase = frase.replace('Python', 'Java') #Altera a variável !!!
print(frase)

