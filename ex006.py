n = int(input('Digite um número: '))
print('O número o que digitou foi o {} \nseu dobro é {}, \nseu triplo é {}, \ne sua raiz quadrada é {:.2f}'.format(n, n*2, n*3, n**(1/2)))
# fazendo raiz usando exponenciação**: n**(1/2), onde n é o Radicando da Raíz, o número no denominador da potenciação é o índice da Radiação
# formatando o número de casa decimais depois da vírgula usando dentro da máscara de formatação {:.2f} para duas casas depois da vírgula
print('A raiz cúbica é {:.2f}'.format(pow(n, (1/3))))
# Usando Raiz usando a função pow(), onde pow(radicando, (1/índice do radical))
